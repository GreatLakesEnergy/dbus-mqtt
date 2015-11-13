#!/usr/bin/python -u
# -*- coding: utf-8 -*-

# Code is a quite raw copy from the pubnub code, but then with mqtt,

import os
import sys
import signal
import gobject
import argparse
import threading
import time
import json
import logging
from time import sleep

logger = logging.getLogger(__name__)

from dbus.mainloop.glib import DBusGMainLoop

# Victron imports
sys.path.insert(1, os.path.join(os.path.dirname(__file__), './ext/velib_python'))
sys.path.insert(1, os.path.join(os.path.dirname(__file__), './ext/paho-mqtt-client'))
from dbusmonitor import DbusMonitor
import datalist
from ve_utils import get_vrm_portal_id, exit_on_error

import client as mqtt

softwareversion = '0.01'

# The DataUpdateSender class receives all the dbus-dataupdate-events, and forwards them to mqtt
# if and when necessary.
class DbusMqtt:
	def __init__(self,mqqthost,nodeid,service,base_topic='emonhub'):
		self.d = DbusMonitor(datalist.vrmtree, self._value_changed_on_dbus)

		"""
		self.ttl = 300    # seconds to keep sending the updates.  If no keepAlive received in this
						  # time - stop sending

		self.lastKeepAliveRcd = int(time.time()) - self.ttl   # initialised to when this code launches
		"""

		self.ttm = 0      # seconds to gather data before sending, 0 - send immediate, NN - gather
						  # for NN seconds
		self._last_publish = int(time.time() - 60)  # Just an initialisation value, so the first
											   # ttm timeout is _now_
		self._gathered_data_timer = None
		self._gathered_data = {}

		self._mqtt = mqtt.Client(client_id=get_vrm_portal_id(), clean_session=True, userdata=None)
		self._mqtt.loop_start()  # creates new thread and runs Mqtt.loop_forever() in it.
		self._mqtt.on_connect = self._on_connect
		self._mqtt.on_message = self._on_message
		self._mqtt.connect_async(mqqthost, port=1883, keepalive=60, bind_address="")


		self._service_name = service

		self._nodeid = nodeid #node ide expected by emonhub . need to modigy emonhub.conf accordingly
		self._topic = base_topic
		message = '{basetopic}/tx/{nodeid}/values'
		self._publishPath = message.format(basetopic=self._topic,nodeid=self._nodeid)




	def get_service_values(self):
	 	 """
		 Hackish way to send BMV data on dbus to MQTT for EMON
	 	 """
  		 current_vals = self.d.get_values_for_service(['onIntervalAlways'],self._service_name)
		 payload = []
		 #Create String that Emon will like
		 for val in current_vals:
			payload.append(str(current_vals[val]))

		 #Emon Expects , between data point objects
		 payload_str = ", ".join(payload)
		 logger.debug('Sending payload data  %s  ' % (payload_str))
		 #publish away
		 self._publish(payload_str,self._topic)


	#   servicename: for example com.victronenergy.dbus.ttyO1
	#   path: for example /Ac/ActiveIn/L1/V
	#   props: the dictionary containing the properties from the vrmTree
	#   changes: the changes, a tuple with GetText() and GetValue()
	#   instance: the deviceInstance
	def _value_changed_on_dbus(self, servicename, path, props, changes, instance):
		# if not self.someone_watching():
		# 	return

		self._gathered_data[props["code"] + str(instance)] = {
			'code': props["code"], 'instance': instance, 'value': str(changes['Value'])}

		if self.ttm:     # != 0, ie. gather before sending

			logger.debug('Got data from DBUS checking ttm')
			if self._marshall_says_go():
				self._publish(str(self._gathered_data),self._topic)
			elif self._gathered_data_timer is None:
				# Set timer, to make sure that this data will not reside in this queue for longer
				# than ttm-time
				self._gathered_data_timer = gobject.timeout_add(
					self.ttm * 1000,
					exit_on_error, self._publish)

		else:       # send immediate
			logger.debug('collected data : %s'%self._gathered_data)
			logger.debug('sending data')
			self._publish(str(self._gathered_data),self._topic)

	def _on_message(self, client, userdata, msg):
		logger.debug('message! userdata: %s, message %s' % (userdata, msg.topic+" "+str(msg.payload)))

	def _on_connect(self, client, userdata, flags, rc):
		"""
		RC definition:
		0: Connection successful
		1: Connection refused - incorrect protocol version
		2: Connection refused - invalid client identifier
		3: Connection refused - server unavailable
		4: Connection refused - bad username or password
		5: Connection refused - not authorised
		6-255: Currently unused.
		"""
		logger.debug('connected! client=%s, userdata=%s, flags=%s, rc=%s' % (client, userdata, flags, rc))

		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
		# client.subscribe("$SYS/#")

	def _someone_watching(self):
		return True  # (self.lastKeepAliveRcd + self.ttl) > int(time.time())

	def _marshall_says_go(self):
		return (self._last_publish + self.ttm) < int(time.time())

	def _publish(self,payload,topic):
		self._last_publish = int(time.time())

		"""
		message = {'dataUpdate': self.gatheredData.values()}
		self.gatheredData = {}


		if self.gatheredDataTimer is not None:
			gobject.source_remove(self.gatheredDataTimer)
			self.gatheredDataTimer = None

		logger.debug("Sending dataUpdate, fired by timer is %s" % firedbytimer)

		send_to_pubnub('livefeed', message)
		return False    # let gobject know that it is not necessary to fire us again.
		"""
		topic = self._publishPath
		logger.debug('publishing on topic "%s", data "%s"' % (topic, payload))
		self._mqtt.publish(topic, payload=payload, qos=0, retain=False)

def main():
	# Argument parsing
	parser = argparse.ArgumentParser(
		description=' Get data from Victron device in DBUS and relay to MQTT for EMON to pickup V %s' % softwareversion
	)

	parser.add_argument("-d", "--debug", help="set logging level to debug",
						action="store_true")

	parser.add_argument("nodeid", help="nodeid defined in emonhub.conf",
						type=int)

	parser.add_argument("mqtt", help="ip address for mqtt server",
						)

	parser.add_argument("-t", "--topic", help="base topic for emonhub, default is emonhub",
						default="emonhub")

	parser.add_argument("service", help="serivce name to look for on dbus sample  example: com.victronenergy.battery.ttyUSB0",
						action="store")

	parser.add_argument("-c", "--ctime", help="cycle time for service , numeric value to specify how often data should be sent default 1s",
						default=1,
						action="store")
	#TODO doing fast and ugly way for now
	args = parser.parse_args()
	# (self,mqqthost,nodeid,service,base_topic)
	# Init logging
	logging.basicConfig(level=(logging.DEBUG if True or args.debug else logging.INFO))

	ctime = args.ctime
	nodeid = int(args.nodeid)
	mqqt_host = args.mqtt
	topic =args.topic
	service = args.service



	logger.info("%s v%s is starting up" % (__file__, softwareversion))
	logLevel = {0: 'NOTSET', 10: 'DEBUG', 20: 'INFO', 30: 'WARNING', 40: 'ERROR'}
	logger.info('Loglevel set to ' + logLevel[logging.getLogger().getEffectiveLevel()])

	# Have a mainloop, so we can send/receive asynchronous calls to and from dbus
	DBusGMainLoop(set_as_default=True)

	# Without this, the threads on wich the Pubnub.subscribe() functions only
	# work when there is activity on the dbus.
	# gobject.threads_init()
	dbusmqtt = DbusMqtt(mqqt_host,nodeid,service,topic)

	while 1:
		dbusmqtt.get_service_values()
		sleep(ctime)
	# Start and run the mainloop
	logger.info("Starting mainloop, responding on only events")
	#mainloop = gobject.MainLoop()
	#mainloop.run()


if __name__ == "__main__":
	main()
