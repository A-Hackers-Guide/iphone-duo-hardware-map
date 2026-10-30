# `PLWifiAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 30 instance variables, 30 properties, 102 instance methods, 31 class methods

## Instance variables

```
@"PLEntry" _lastEntryForMetricd;
@"PLCFNotificationOperatorComposition" _notificationWiFiChanged;
^{__WiFiManagerClient=} _wifiManager;
^{__WiFiDeviceClient=} _wifiDevice;
^{__WiFiDeviceClient=} _wifiAwdlDevice;
^{__WiFiDeviceClient=} _wifiHotspotDevice;
@"PLEntryNotificationOperatorComposition" _batteryLevelChanged;
@"PLEntryNotificationOperatorComposition" _sbcLevelChanged;
@"PLEntryNotificationOperatorComposition" _deviceWake;
@"PLNSNotificationOperatorComposition" _thermalMonitorListener;
@"PLXPCListenerOperatorComposition" _remoteControlSessionListener;
Q _lastLoggedTimestamp;
Q _locationScanDuration;
Q _pipelineScanDuration;
Q _autoJoinScanDuration;
Q _setupScanDuration;
Q _unknownScanDuration;
@"WiFiP2PAWDLStateMonitor" _monitor;
@"NSString" _wifiChipset;
@"NSString" _wifiManufacturer;
Q _remainingAllowedRSSIEntryCount;
d _wifi_segment_power_data;
d _wifi_segment_power_idle;
d _wifi_segment_power_location;
d _wifi_segment_power_pipeline;
@"NSDate" _wifi_segment_lastWrittenDate;
d _wifi_segment_lastWrittenTimestamp;
@"NSDate" _wifi_segment_date;
d _wifi_segment_timestamp;
@"PLEntryNotificationOperatorComposition" _remoteSessionCallback;
```

## Properties

```
@property (T@"PLEntry",&,N,V_lastEntryForMetricd) lastEntryForMetricd;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationWiFiChanged) notificationWiFiChanged;
@property (T^{__WiFiManagerClient=},N,V_wifiManager) wifiManager;
@property (T^{__WiFiDeviceClient=},N,V_wifiDevice) wifiDevice;
@property (T^{__WiFiDeviceClient=},N,V_wifiAwdlDevice) wifiAwdlDevice;
@property (T^{__WiFiDeviceClient=},N,V_wifiHotspotDevice) wifiHotspotDevice;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChanged) batteryLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbcLevelChanged) sbcLevelChanged;
@property (T@"PLEntryNotificationOperatorComposition",&,V_deviceWake) deviceWake;
@property (T@"PLNSNotificationOperatorComposition",&,V_thermalMonitorListener) thermalMonitorListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_remoteControlSessionListener) remoteControlSessionListener;
@property (TQ,V_lastLoggedTimestamp) lastLoggedTimestamp;
@property (TQ,V_locationScanDuration) locationScanDuration;
@property (TQ,V_pipelineScanDuration) pipelineScanDuration;
@property (TQ,V_autoJoinScanDuration) autoJoinScanDuration;
@property (TQ,V_setupScanDuration) setupScanDuration;
@property (TQ,V_unknownScanDuration) unknownScanDuration;
@property (T@"WiFiP2PAWDLStateMonitor",&,V_monitor) monitor;
@property (T@"NSString",R,V_wifiChipset) wifiChipset;
@property (T@"NSString",R,V_wifiManufacturer) wifiManufacturer;
@property (TQ,V_remainingAllowedRSSIEntryCount) remainingAllowedRSSIEntryCount;
@property (Td,V_wifi_segment_power_data) wifi_segment_power_data;
@property (Td,V_wifi_segment_power_idle) wifi_segment_power_idle;
@property (Td,V_wifi_segment_power_location) wifi_segment_power_location;
@property (Td,V_wifi_segment_power_pipeline) wifi_segment_power_pipeline;
@property (T@"NSDate",&,V_wifi_segment_lastWrittenDate) wifi_segment_lastWrittenDate;
@property (Td,V_wifi_segment_lastWrittenTimestamp) wifi_segment_lastWrittenTimestamp;
@property (T@"NSDate",&,V_wifi_segment_date) wifi_segment_date;
@property (Td,V_wifi_segment_timestamp) wifi_segment_timestamp;
@property (T@"PLEntryNotificationOperatorComposition",&,V_remoteSessionCallback) remoteSessionCallback;
```

## Class methods

```
+[PLWifiAgent entryEventPointDefinitions];
+[PLWifiAgent entryEventForwardDefinitions];
+[PLWifiAgent entryEventBackwardDefinitions];
+[PLWifiAgent entryEventNoneDefinitions];
+[PLWifiAgent load];
+[PLWifiAgent isEnabled];
+[PLWifiAgent entryEventForwardDefinitionRSSI];
+[PLWifiAgent entryEventBackwardDefinitionAutoJoin];
+[PLWifiAgent entryEventBackwardDefinitionBeaconProfile];
+[PLWifiAgent entryEventBackwardDefinitionControlCPUPowerStats];
+[PLWifiAgent entryEventBackwardDefinitionCumulativeBasic];
+[PLWifiAgent entryEventBackwardDefinitionCumulativeBasicMac];
+[PLWifiAgent entryEventBackwardDefinitionCumulativeMultiCore];
+[PLWifiAgent entryEventBackwardDefinitionDiffBasic];
+[PLWifiAgent entryEventBackwardDefinitionHotspotPowerStats];
+[PLWifiAgent entryEventBackwardDefinitionScanForwardStats];
+[PLWifiAgent entryEventBackwardDefinitionScans];
+[PLWifiAgent entryEventBackwardDefinitionUserScan];
+[PLWifiAgent entryEventForwardDefinitionAWDLState];
+[PLWifiAgent entryEventForwardDefinitionHotspotState];
+[PLWifiAgent entryEventForwardDefinitionModuleInfo];
+[PLWifiAgent entryEventForwardDefinitionPowerState];
+[PLWifiAgent entryEventForwardDefinitionWifiAssist];
+[PLWifiAgent entryEventPointDefinitionAWDLServicesAndPorts];
+[PLWifiAgent entryEventPointDefinitionJoin];
+[PLWifiAgent entryEventPointDefinitionRemoteControlSession];
+[PLWifiAgent entryEventPointDefinitionWake];
+[PLWifiAgent entryEventPointDefinitionWifiInstantPower];
+[PLWifiAgent isBeaconLoggingEnabled];
+[PLWifiAgent isScanForwardLoggingEnabled];
+[PLWifiAgent isScanLoggingEnabled];
```

## Instance methods

```
-[PLWifiAgent wifiManager];
-[PLWifiAgent monitor];
-[PLWifiAgent setWifiManager:];
-[PLWifiAgent init];
-[PLWifiAgent setMonitor:];
-[PLWifiAgent initOperatorDependancies];
-[PLWifiAgent sbcLevelChanged];
-[PLWifiAgent setSbcLevelChanged:];
-[PLWifiAgent setThermalMonitorListener:];
-[PLWifiAgent setDeviceWake:];
-[PLWifiAgent setWifiDevice:];
-[PLWifiAgent setBatteryLevelChanged:];
-[PLWifiAgent log];
-[PLWifiAgent thermalMonitorListener];
-[PLWifiAgent batteryLevelChanged];
-[PLWifiAgent wifiDevice];
-[PLWifiAgent deviceWake];
-[PLWifiAgent hasWiFi];
-[PLWifiAgent logFromWiFiNoAvailableCallback:withAvailability:withWakeParams:];
-[PLWifiAgent setWifi_segment_power_location:];
-[PLWifiAgent logEventBackwardWifiProperties:];
-[PLWifiAgent modelWiFiPower:];
-[PLWifiAgent setWifi_segment_power_pipeline:];
-[PLWifiAgent autoJoinScanDuration];
-[PLWifiAgent decodeWifiEventLinkReason:];
-[PLWifiAgent findWifiDevice];
-[PLWifiAgent getCurrentChannelWidth:];
-[PLWifiAgent handleRemoteSessionCallbackWithUserInfo:];
-[PLWifiAgent isWiFiPowered];
-[PLWifiAgent isWowEnabled];
-[PLWifiAgent isWowSupported];
-[PLWifiAgent lastEntryForMetricd];
-[PLWifiAgent lastLoggedTimestamp];
-[PLWifiAgent locationScanDuration];
-[PLWifiAgent logAWDLStateEntry:];
-[PLWifiAgent logEventBackwardControlCPUPowerStats];
-[PLWifiAgent logEventBackwardCumulativeProperties];
-[PLWifiAgent logEventBackwardDiffProperties];
-[PLWifiAgent logEventBackwardUserScanDuration];
-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:];
-[PLWifiAgent logEventBackwardWifiPropertiesMac:];
-[PLWifiAgent logEventBackwardWifiPropertiesMac:withNetworkProperties:];
-[PLWifiAgent logEventForwardAWDLState:];
-[PLWifiAgent logEventForwardHotspotState:];
-[PLWifiAgent logEventForwardModuleInfo];
-[PLWifiAgent logEventForwardPowerState:];
-[PLWifiAgent logEventForwardRSSI:];
-[PLWifiAgent logEventForwardWifiAssist:];
-[PLWifiAgent logEventPointAWDLServicesAndPorts];
-[PLWifiAgent logEventPointJoin:withStats:];
-[PLWifiAgent logEventPointMetricMonitorInstantKeys];
-[PLWifiAgent logEventPointRemoteControlSession:];
-[PLWifiAgent logEventPointWake:];
-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:];
-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:];
-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:];
-[PLWifiAgent logFromAJCallback:withFlag:withStats:];
-[PLWifiAgent logFromLinkChangeCallback:withStats:];
-[PLWifiAgent modelWiFiSegmentPower:withDataPower:withIdlePower:withLocationPower:withPipelinePower:withTotalDuration:];
-[PLWifiAgent notificationWiFiChanged];
-[PLWifiAgent pipelineScanDuration];
-[PLWifiAgent remainingAllowedRSSIEntryCount];
-[PLWifiAgent remoteControlSessionListener];
-[PLWifiAgent remoteSessionCallback];
-[PLWifiAgent setAutoJoinScanDuration:];
-[PLWifiAgent setLastEntryForMetricd:];
-[PLWifiAgent setLastLoggedTimestamp:];
-[PLWifiAgent setLocationScanDuration:];
-[PLWifiAgent setPipelineScanDuration:];
-[PLWifiAgent setRemainingAllowedRSSIEntryCount:];
-[PLWifiAgent setRemoteControlSessionListener:];
-[PLWifiAgent setRemoteSessionCallback:];
-[PLWifiAgent setSetupScanDuration:];
-[PLWifiAgent setUnknownScanDuration:];
-[PLWifiAgent setWiFiAWDLDevice:];
-[PLWifiAgent setWiFiHotspotDevice:];
-[PLWifiAgent setWifiAwdlDevice:];
-[PLWifiAgent setWifiHotspotDevice:];
-[PLWifiAgent setWifi_segment_date:];
-[PLWifiAgent setWifi_segment_lastWrittenDate:];
-[PLWifiAgent setWifi_segment_lastWrittenTimestamp:];
-[PLWifiAgent setWifi_segment_power_data:];
-[PLWifiAgent setWifi_segment_power_idle:];
-[PLWifiAgent setWifi_segment_timestamp:];
-[PLWifiAgent setupScanDuration];
-[PLWifiAgent unknownScanDuration];
-[PLWifiAgent updateEventBackwardUserScanDuration:];
-[PLWifiAgent wifiAwdlDevice];
-[PLWifiAgent wifiChipset];
-[PLWifiAgent wifiChipsetQuery];
-[PLWifiAgent wifiHotspotDevice];
-[PLWifiAgent wifiManufacturer];
-[PLWifiAgent wifiManufacturerQuery];
-[PLWifiAgent wifi_segment_date];
-[PLWifiAgent wifi_segment_lastWrittenDate];
-[PLWifiAgent wifi_segment_lastWrittenTimestamp];
-[PLWifiAgent wifi_segment_power_data];
-[PLWifiAgent wifi_segment_power_idle];
-[PLWifiAgent wifi_segment_power_location];
-[PLWifiAgent wifi_segment_power_pipeline];
-[PLWifiAgent wifi_segment_timestamp];
-[PLWifiAgent writeModeledPower];
```
