# Exported from dataAttributes and deviceTypes on 2015-09-17 14:32:55
vrmtree = {
'com.victronenergy.gps': {
	'/Position/Latitude': {'code': 'lt', 'whenToLog': 'onIntervalAlways', 'precision': 5},
	'/Position/Longitude': {'code': 'lg', 'whenToLog': 'onIntervalAlways', 'precision': 5},
	'/Course': {'code': 'lc', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Speed': {'code': 'ls', 'whenToLog': 'onIntervalAlways', 'precision': 2}
},
'com.victronenergy.settings': {
	'/Settings/Vrmlogger/LogInterval': {'code': 'sl', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/Vrmlogger/Logmode': {'code': 'vl', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/System/AccessLevel': {'code': 'al', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/System/AutoUpdate': {'code': 'au', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/System/ReleaseType': {'code': 'ut', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/Services/Vrmpubnub': {'code': 'tw', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/Services/Modbus': {'code': 'mb', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/Services/OceanvoltMotorDrive': {'code': 'od', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/Services/OceanvoltValence': {'code': 'ov', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/System/RemoteSupportPort': {'code': 'rs', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/System/RemoteSupport': {'code': 'rss', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/System/TimeZone': {'code': 'tz', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/SystemSetup/AcInput1': {'code': 'si1', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/SystemSetup/AcInput2': {'code': 'si2', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/SystemSetup/BatteryService': {'code': 'sb', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/SystemSetup/HasDcSystem': {'code': 'shd', 'whenToLog': 'configChange', 'accessLevel': 'owner'},
	'/Settings/Gui/DemoMode': {'code': 'dm', 'whenToLog': 'configChange', 'accessLevel': 'owner'}
},
'com.victronenergy.vebus': {
	'/Interfaces/Mk2/Version': {'code': 'vmk2', 'whenToLog': 'configChange'},
	'/FirmwareVersion': {'code': 'vvv', 'whenToLog': 'configChange'},
	'/ProductId': {'code': 'vvp', 'whenToLog': 'configChange'},
	'/Ac/ActiveIn/L1/V': {'code': 'IV1', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/ActiveIn/L2/V': {'code': 'IV2', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/ActiveIn/L3/V': {'code': 'IV3', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/ActiveIn/L1/I': {'code': 'II1', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/ActiveIn/L2/I': {'code': 'II2', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/ActiveIn/L3/I': {'code': 'II3', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/ActiveIn/L1/F': {'code': 'IF1', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/ActiveIn/L2/F': {'code': 'IF2', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/ActiveIn/L3/F': {'code': 'IF3', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/ActiveIn/L1/P': {'code': 'IP1', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/ActiveIn/L2/P': {'code': 'IP2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/ActiveIn/L3/P': {'code': 'IP3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Out/L1/V': {'code': 'OV1', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/Out/L2/V': {'code': 'OV2', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/Out/L3/V': {'code': 'OV3', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/Out/L1/I': {'code': 'OI1', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/Out/L2/I': {'code': 'OI2', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/Out/L3/I': {'code': 'OI3', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/Out/L1/F': {'code': 'OF', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/ActiveIn/CurrentLimit': {'code': 'AILIM', 'whenToLog': 'onIntervalAlways', 'accessLevel': 'operator', 'precision': 2},
	'/Ac/Out/L1/P': {'code': 'OP1', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Out/L2/P': {'code': 'OP2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Out/L3/P': {'code': 'OP3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/0/Voltage': {'code': 'CV', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/0/Current': {'code': 'CI', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/NumberOfPhases': {'code': 'PC', 'whenToLog': 'onIntervalAlways'},
	'/Ac/ActiveIn/ActiveInput': {'code': 'AI', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Soc': {'code': 'VSOC', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/State': {'code': 'S', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/VebusError': {'code': 'ERR', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Mode': {'code': 's', 'whenToLog': 'onIntervalAlwaysAndOnEvent', 'accessLevel': 'operator'},
	'/Alarms/HighTemperature': {'code': 'eT', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowBattery': {'code': 'eL', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/Overload': {'code': 'eO', 'whenToLog': 'onIntervalAlwaysAndOnEvent'}
},
'com.victronenergy.battery': {
	'/ProductId': {'code': 'BM', 'whenToLog': 'configChange'},
	'/FirmwareVersion': {'code': 'BV', 'whenToLog': 'configChange'},
	'/Serial': {'code': 'BSN', 'whenToLog': 'configChange'},
	'/Dc/0/Voltage': {'code': 'V', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/1/Voltage': {'code': 'VS', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/0/Current': {'code': 'I', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/0/Temperature': {'code': 'BT', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/0/MidVoltage': {'code': 'VM', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/0/MidVoltageDeviation': {'code': 'VMD', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/ConsumedAmphours': {'code': 'CE', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Soc': {'code': 'SOC', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/TimeToGo': {'code': 'TTG', 'whenToLog': 'onIntervalAlways', 'precision': 3},
	'/Alarms/LowVoltage': {'code': 'AL', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighVoltage': {'code': 'AH', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowStarterVoltage': {'code': 'ALS', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighStarterVoltage': {'code': 'AHS', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowSoc': {'code': 'ASoc', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowTemperature': {'code': 'ALT', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighTemperature': {'code': 'AHT', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/MidVoltage': {'code': 'AM', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowFusedVoltage': {'code': 'ALF', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighFusedVoltage': {'code': 'AHF', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/FuseBlown': {'code': 'AFB', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighInternalTemperature': {'code': 'AHIT', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Relay/0/State': {'code': 'Relay', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/History/DeepestDischarge': {'code': 'H1', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/LastDischarge': {'code': 'H2', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/AverageDischarge': {'code': 'H3', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/ChargeCycles': {'code': 'H4', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/FullDischarges': {'code': 'H5', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/TotalAhDrawn': {'code': 'H6', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/MinimumVoltage': {'code': 'H7', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/MaximumVoltage': {'code': 'H8', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/TimeSinceLastFullCharge': {'code': 'H9', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/AutomaticSyncs': {'code': 'H10', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/LowVoltageAlarms': {'code': 'H11', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/HighVoltageAlarms': {'code': 'H12', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/LowStarterVoltageAlarms': {'code': 'H13', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/HighStarterVoltageAlarms': {'code': 'H14', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/MinimumStarterVoltage': {'code': 'H15', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/MaximumStarterVoltage': {'code': 'H16', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/LowFusedVoltageAlarms': {'code': 'H17', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/History/HighFusedVoltageAlarms': {'code': 'H18', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/History/MinimumFusedVoltage': {'code': 'H19', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/History/MaximumFusedVoltage': {'code': 'H20', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/History/DischargedEnergy': {'code': 'H21', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/ChargedEnergy': {'code': 'H22', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2}
},
'com.victronenergy.solarcharger': {
	'/ProductId': {'code': 'ScM', 'whenToLog': 'configChange'},
	'/FirmwareVersion': {'code': 'ScVt', 'whenToLog': 'configChange'},
	'/Serial': {'code': 'ScSN', 'whenToLog': 'configChange'},
	'/Dc/0/Voltage': {'code': 'ScV', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/0/Current': {'code': 'ScI', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Dc/0/Temperature': {'code': 'ScT', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Load/State': {'code': 'SLs', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Load/I': {'code': 'SLI', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Mode': {'code': 'Scs', 'whenToLog': 'onIntervalAlwaysAndOnEvent', 'accessLevel': 'operator'},
	'/State': {'code': 'ScS', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Pv/V': {'code': 'PVV', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Pv/I': {'code': 'PVI', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Equalization/Pending': {'code': 'EqP', 'whenToLog': 'onIntervalAlways'},
	'/Equalization/TimeRemaining': {'code': 'EqT', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Relay/0/State': {'code': 'SRelay', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowVoltage': {'code': 'SceL', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighVoltage': {'code': 'SceH', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/History/Daily/0/Yield': {'code': 'YT', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/History/Daily/0/MaxPower': {'code': 'MCPT', 'whenToLog': 'onIntervalAlways'},
	'/History/Daily/1/Yield': {'code': 'YY', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/History/Daily/1/MaxPower': {'code': 'MCPY', 'whenToLog': 'onIntervalAlways'},
	'/ErrorCode': {'code': 'ScERR', 'whenToLog': 'onIntervalAlwaysAndOnEvent'}
},
'com.victronenergy.system': {
	'/Ac/PvOnOutput/L1/Power': {'code': 'P', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/PvOnOutput/L2/Power': {'code': 'P2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/PvOnOutput/L3/Power': {'code': 'P3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/PvOnGrid/L1/Power': {'code': 'Pi', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/PvOnGrid/L2/Power': {'code': 'Pi2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/PvOnGrid/L3/Power': {'code': 'Pi3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/Pv/Power': {'code': 'Pdc', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Consumption/L1/Power': {'code': 'a1', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Consumption/L2/Power': {'code': 'a2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Consumption/L3/Power': {'code': 'a3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Grid/L1/Power': {'code': 'g1', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Grid/L2/Power': {'code': 'g2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Grid/L3/Power': {'code': 'g3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Genset/L1/Power': {'code': 'gs1', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Genset/L2/Power': {'code': 'gs2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/Genset/L3/Power': {'code': 'gs3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/System/Power': {'code': 'dc', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/Battery/Voltage': {'code': 'bv', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/Battery/Current': {'code': 'bc', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/Battery/Power': {'code': 'bp', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/Vebus/Current': {'code': 'vc', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Dc/Vebus/Power': {'code': 'vp', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/Battery/Soc': {'code': 'bs', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Dc/Battery/State': {'code': 'bst', 'whenToLog': 'onIntervalAlways'},
	'/Dc/Battery/ConsumedAmphours': {'code': 'ba', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/ActiveBatteryService': {'code': 'abs', 'whenToLog': 'configChange'},
	'/Dc/Battery/TimeToGo': {'code': 'bt', 'whenToLog': 'onIntervalAlways', 'precision': 2}
},
'com.victronenergy.pvinverter': {
	'/ProductId': {'code': 'pM', 'whenToLog': 'configChange'},
	'/FroniusDeviceType': {'code': 'pF', 'whenToLog': 'configChange'},
	'/FirmwareVersion': {'code': 'pV', 'whenToLog': 'configChange'},
	'/Position': {'code': 'pL', 'whenToLog': 'configChange'},
	'/Serial': {'code': 'ps', 'whenToLog': 'configChange'},
	'/Ac/L1/Voltage': {'code': 'pV1', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/L1/Current': {'code': 'pI1', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/L1/Power': {'code': 'pP1', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/L1/Energy/Forward': {'code': 'pE1', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/L2/Voltage': {'code': 'pV2', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/L2/Current': {'code': 'pI2', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/L2/Power': {'code': 'pP2', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/L2/Energy/Forward': {'code': 'pE2', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/L3/Voltage': {'code': 'pV3', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Ac/L3/Current': {'code': 'pI3', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Ac/L3/Power': {'code': 'pP3', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/L3/Energy/Forward': {'code': 'pE3', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/StatusCode': {'code': 'pS', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/ErrorCode': {'code': 'pE', 'whenToLog': 'onIntervalAlwaysAndOnEvent'}
},
'com.victronenergy.bms': {
	'/ProductId': {'code': 'liM', 'whenToLog': 'configChange'},
	'/FirmwareVersion': {'code': 'liV', 'whenToLog': 'configChange'},
	'/State': {'code': 'liS', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Error': {'code': 'liE', 'whenToLog': 'onIntervalAlways'},
	'/SystemSwitch': {'code': 'Sw', 'whenToLog': 'onIntervalAlways', 'accessLevel': 'admin'},
	'/Balancing': {'code': 'B', 'whenToLog': 'onIntervalAlways'},
	'/System/NrOfBatteries': {'code': 'nB', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/System/BatteriesParallel': {'code': 'BP', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/System/BatteriesSeries': {'code': 'BS', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/System/NrOfCellsPerBattery': {'code': 'NrC', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/System/MinCellVoltage': {'code': 'mcV', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/System/MaxCellVoltage': {'code': 'McV', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/Diagnostics/ShutDownsDueError': {'code': 'Se', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/Diagnostics/LastError1': {'code': 'Le1', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/Diagnostics/LastError2': {'code': 'Le2', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/Diagnostics/LastError3': {'code': 'Le3', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/Diagnostics/LastError4': {'code': 'Le4', 'whenToLog': 'onIntervalOnlyWhenChanged'},
	'/Io/AllowToCharge': {'code': 'aCh', 'whenToLog': 'onIntervalAlways'},
	'/Io/AllowToDischarge': {'code': 'aD', 'whenToLog': 'onIntervalAlways'},
	'/Io/ExternalRelay': {'code': 'eRelay', 'whenToLog': 'onIntervalAlways'},
	'/History/MinimumCellVoltage': {'code': 'liH1', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2},
	'/History/MaximumCellVoltage': {'code': 'liH2', 'whenToLog': 'onIntervalOnlyWhenChanged', 'precision': 2}
},
'com.victronenergy.motordrive': {
	'/Motor/RPM': {'code': 'mr', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Motor/Temperature': {'code': 'mt', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/0/Voltage': {'code': 'coV', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Dc/0/Current': {'code': 'coC', 'whenToLog': 'onIntervalAlways', 'precision': 1},
	'/Dc/0/Power': {'code': 'coP', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Controller/Temperature': {'code': 'coT', 'whenToLog': 'onIntervalAlways', 'precision': 0}
},
'com.victronenergy.charger': {
	'/ProductId': {'code': 'cP', 'whenToLog': 'configChange'},
	'/FirmwareVersion': {'code': 'cF', 'whenToLog': 'configChange'},
	'/Serial': {'code': 'cS', 'whenToLog': 'configChange'},
	'/Dc/0/Voltage': {'code': 'c0V', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/0/Current': {'code': 'c0I', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/0/Temperature': {'code': 'c0T', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/1/Voltage': {'code': 'c1V', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/1/Current': {'code': 'c1I', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Dc/2/Voltage': {'code': 'c2V', 'whenToLog': 'onIntervalAlways', 'precision': 2},
	'/Dc/2/Current': {'code': 'c2I', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/In/L1/I': {'code': 'cI', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/In/L1/P': {'code': 'cPo', 'whenToLog': 'onIntervalAlways', 'precision': 0},
	'/Ac/In/CurrentLimit': {'code': 'cIl', 'whenToLog': 'onIntervalAlways', 'accessLevel': 'operator', 'precision': 0},
	'/Mode': {'code': 'cM', 'whenToLog': 'onIntervalAlwaysAndOnEvent', 'accessLevel': 'operator'},
	'/State': {'code': 'cSt', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/ErrorCode': {'code': 'cE', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Relay/0/State': {'code': 'cR', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/LowVoltage': {'code': 'cAl', 'whenToLog': 'onIntervalAlwaysAndOnEvent'},
	'/Alarms/HighVoltage': {'code': 'cAh', 'whenToLog': 'onIntervalAlwaysAndOnEvent'}
}}
