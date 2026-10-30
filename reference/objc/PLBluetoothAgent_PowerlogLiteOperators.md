# `PLBluetoothAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 28 instance variables, 25 properties, 84 instance methods, 30 class methods

## Instance variables

```
B keepSessionAlive;
^{BTSessionImpl=} session;
^{BTLocalDeviceImpl=} localBluetoothDevice;
C _logCount;
B _hadRealBTSinceSBC;
B _hadRealBTENSinceSBC;
B _hadRealBTITSinceSBC;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLEntryNotificationOperatorComposition" _sbcChanged;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"NSString" _btHardwareChipset;
@"PLXPCListenerOperatorComposition" _leConnectionListener;
@"PLXPCListenerOperatorComposition" _btHCIListener;
@"PLXPCListenerOperatorComposition" _btA2DPListener;
@"PLXPCListenerOperatorComposition" _btHFPListener;
@"PLXPCListenerOperatorComposition" _wirelessProxListener;
@"PLXPCListenerOperatorComposition" _CBDiscoveryListener;
@"PLXPCListenerOperatorComposition" _btHCIVSEListener;
@"PLEntryNotificationOperatorComposition" _wakeEntryNotifications;
@"NSDate" _lastPowerEntryDate;
@"NSMutableDictionary" _ENScanCache;
@"PLXPCListenerOperatorComposition" _ENListener;
@"SPBeaconManager" _beaconManager;
@"PLXPCListenerOperatorComposition" _magnetListener;
@"PLXPCListenerOperatorComposition" _magnetOperationListener;
d _lastBTPower;
d _lastBTENPower;
d _lastBTITPower;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbcChanged) sbcChanged;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (T@"NSString",R,V_btHardwareChipset) btHardwareChipset;
@property (T@"PLXPCListenerOperatorComposition",&,V_leConnectionListener) leConnectionListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_btHCIListener) btHCIListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_btA2DPListener) btA2DPListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_btHFPListener) btHFPListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_wirelessProxListener) wirelessProxListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_CBDiscoveryListener) CBDiscoveryListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_btHCIVSEListener) btHCIVSEListener;
@property (T@"PLEntryNotificationOperatorComposition",R,V_wakeEntryNotifications) wakeEntryNotifications;
@property (T@"NSDate",&,V_lastPowerEntryDate) lastPowerEntryDate;
@property (TC,V_logCount) logCount;
@property (T@"NSMutableDictionary",&,V_ENScanCache) ENScanCache;
@property (T@"PLXPCListenerOperatorComposition",&,V_ENListener) ENListener;
@property (T@"SPBeaconManager",&,V_beaconManager) beaconManager;
@property (T@"PLXPCListenerOperatorComposition",&,V_magnetListener) magnetListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_magnetOperationListener) magnetOperationListener;
@property (TB,V_hadRealBTSinceSBC) hadRealBTSinceSBC;
@property (Td,V_lastBTPower) lastBTPower;
@property (TB,V_hadRealBTENSinceSBC) hadRealBTENSinceSBC;
@property (Td,V_lastBTENPower) lastBTENPower;
@property (TB,V_hadRealBTITSinceSBC) hadRealBTITSinceSBC;
@property (Td,V_lastBTITPower) lastBTITPower;
```

## Class methods

```
+[PLBluetoothAgent entryEventIntervalDefinitions];
+[PLBluetoothAgent entryEventPointDefinitions];
+[PLBluetoothAgent entryEventForwardDefinitions];
+[PLBluetoothAgent entryEventBackwardDefinitions];
+[PLBluetoothAgent entryEventNoneDefinitions];
+[PLBluetoothAgent load];
+[PLBluetoothAgent defaults];
+[PLBluetoothAgent shouldLogEnhancedStats];
+[PLBluetoothAgent entryEventBackwardDefinitionEnhancedPowerProfileStats];
+[PLBluetoothAgent entryEventBackwardDefinitionHCITrace];
+[PLBluetoothAgent entryEventPointDefinitionMagnet];
+[PLBluetoothAgent entryEventPointDefinitionMagnetOperation];
+[PLBluetoothAgent entryEventBackwardDefinitionEnhancedPowerStatsPerCore];
+[PLBluetoothAgent shouldLogMarconi];
+[PLBluetoothAgent isUseCaseListLoggingEnabled];
+[PLBluetoothAgent isEnabled];
+[PLBluetoothAgent entryEventBackwardWakeupVSE];
+[PLBluetoothAgent entryEventBackwardDefinitionA2DPPower];
+[PLBluetoothAgent getBluetooth5GKeys];
+[PLBluetoothAgent entryEventBackwardDefinitionPowerProfileStats];
+[PLBluetoothAgent entryEventBackwardDefinitionAHFPPower];
+[PLBluetoothAgent getScanCoreKeys];
+[PLBluetoothAgent areBluetooth5GAndThreadRadioLoggingEnabled];
+[PLBluetoothAgent entryEventBackwardDefinitionThreadRadioPowerProfileStats];
+[PLBluetoothAgent entryEventBackwardDefinitionCBDiscoveryStats];
+[PLBluetoothAgent shouldLogEnhancedStatsPerCore];
+[PLBluetoothAgent entryEventBackwardDefinitionWirelessProxScanDStats];
+[PLBluetoothAgent entryAggregateDefinitions];
+[PLBluetoothAgent entryEventBackwardDefinitionMaxDutyCycle];
+[PLBluetoothAgent entryEventBackwardDefinitionDetailedPowerProfileStats];
```

## Instance methods

```
-[PLBluetoothAgent isDiscoverable];
-[PLBluetoothAgent isConnected];
-[PLBluetoothAgent hadRealBTENSinceSBC];
-[PLBluetoothAgent btHFPListener];
-[PLBluetoothAgent setBtA2DPListener:];
-[PLBluetoothAgent modelBluetoothOffPower];
-[PLBluetoothAgent lastPowerEntryDate];
-[PLBluetoothAgent setLastBTPower:];
-[PLBluetoothAgent magnetListener];
-[PLBluetoothAgent setMagnetOperationListener:];
-[PLBluetoothAgent logEventForwardPairedDevices];
-[PLBluetoothAgent leConnectionListener];
-[PLBluetoothAgent lastBTPower];
-[PLBluetoothAgent init];
-[PLBluetoothAgent handleSBCForBluetooth];
-[PLBluetoothAgent attachSession];
-[PLBluetoothAgent logwithBTOnCheck];
-[PLBluetoothAgent setHadRealBTITSinceSBC:];
-[PLBluetoothAgent logEventIntervalConnectedDevices];
-[PLBluetoothAgent setLastBTITPower:];
-[PLBluetoothAgent dealloc];
-[PLBluetoothAgent initOperatorDependancies];
-[PLBluetoothAgent logEventIntervalLeConnectedDevices:withRequest:];
-[PLBluetoothAgent btHardwareChipset];
-[PLBluetoothAgent bluetoothSessionEvent:onSession:withResult:];
-[PLBluetoothAgent btHCIListener];
-[PLBluetoothAgent btHCIVSEListener];
-[PLBluetoothAgent localBluetoothDevice];
-[PLBluetoothAgent advertisingDataDescription::];
-[PLBluetoothAgent lastBTENPower];
-[PLBluetoothAgent isConnectable];
-[PLBluetoothAgent logEventBackwardMaxDutyCycle:];
-[PLBluetoothAgent beaconManager];
-[PLBluetoothAgent btHardwareChipsetQuery];
-[PLBluetoothAgent setThermalMonitorListener:];
-[PLBluetoothAgent setWirelessProxListener:];
-[PLBluetoothAgent setBtHCIVSEListener:];
-[PLBluetoothAgent setHadRealBTENSinceSBC:];
-[PLBluetoothAgent logEventPointMagnet:];
-[PLBluetoothAgent logEventBackwardHFP:];
-[PLBluetoothAgent hadRealBTITSinceSBC];
-[PLBluetoothAgent ENListener];
-[PLBluetoothAgent lastBTITPower];
-[PLBluetoothAgent setLastBTENPower:];
-[PLBluetoothAgent sessionTerminated:withResult:];
-[PLBluetoothAgent setBtHCIListener:];
-[PLBluetoothAgent logEventIntervalWakeVSE:];
-[PLBluetoothAgent logEventForwardDeviceState];
-[PLBluetoothAgent setHadRealBTSinceSBC:];
-[PLBluetoothAgent sbcChanged];
-[PLBluetoothAgent setENScanCache:];
-[PLBluetoothAgent setLastPowerEntryDate:];
-[PLBluetoothAgent hadRealBTSinceSBC];
-[PLBluetoothAgent logCount];
-[PLBluetoothAgent btA2DPListener];
-[PLBluetoothAgent setBtHFPListener:];
-[PLBluetoothAgent logEventBackwardWirelessProximity:];
-[PLBluetoothAgent magnetOperationListener];
-[PLBluetoothAgent setBeaconManager:];
-[PLBluetoothAgent setENListener:];
-[PLBluetoothAgent setLeConnectionListener:];
-[PLBluetoothAgent modelBluetoothPower:];
-[PLBluetoothAgent setBatteryLevelChanged:];
-[PLBluetoothAgent logEventBackwardCBDiscovery:];
-[PLBluetoothAgent logEventIntervalHCIRawData:];
-[PLBluetoothAgent ENScanCache];
-[PLBluetoothAgent log];
-[PLBluetoothAgent logEventBackwardPowerProfileStats];
-[PLBluetoothAgent setMagnetListener:];
-[PLBluetoothAgent setSbcChanged:];
-[PLBluetoothAgent setLogCount:];
-[PLBluetoothAgent sessionAttached:withResult:];
-[PLBluetoothAgent modulePowered];
-[PLBluetoothAgent wakeEntryNotifications];
-[PLBluetoothAgent setCBDiscoveryListener:];
-[PLBluetoothAgent thermalMonitorListener];
-[PLBluetoothAgent wirelessProxListener];
-[PLBluetoothAgent logEventBackwardA2DP:];
-[PLBluetoothAgent logEventBackwardPowerStatsPerCore];
-[PLBluetoothAgent batteryLevelChanged];
-[PLBluetoothAgent CBDiscoveryListener];
-[PLBluetoothAgent bluetoothDeviceEvent:onDevice:withResult:];
-[PLBluetoothAgent bluetoothPresent];
-[PLBluetoothAgent logEventPointMagnetOperation:];
```
