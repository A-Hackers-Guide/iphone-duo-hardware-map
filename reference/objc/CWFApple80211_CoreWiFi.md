# `CWFApple80211`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 115 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSThread" _callbackThread;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{_Apple80211=} _a11Ref;
@"NSMutableDictionary" _mutableInterfaceNameEventMap;
B _isMonitoringEvents;
@"NSArray" _cachedCapabilities;
i _virtualInterfaceRole;
@"NSString" _interfaceName;
@"NSString" _virtualInterfaceParent;
@? _eventHandler;
```

## Properties

```
@property (T@"NSString",R,C,N,V_interfaceName) interfaceName;
@property (Ti,R,N,V_virtualInterfaceRole) virtualInterfaceRole;
@property (T@"NSString",R,C,N,V_virtualInterfaceParent) virtualInterfaceParent;
@property (T@?,C,V_eventHandler) eventHandler;
```

## Class methods

```
+[CWFApple80211 convertSensingParameters:toDriverAPParams:error:];
+[CWFApple80211 convertSensingParametersCollection:toDriverStructure:error:];
+[CWFApple80211 convertSingleSensingParameter:toDriverStructure:error:];
```

## Instance methods

```
-[CWFApple80211 virtualInterfaceRole];
-[CWFApple80211 maxLinkSpeed:];
-[CWFApple80211 opMode:];
-[CWFApple80211 virtualInterfaceRole:];
-[CWFApple80211 setUCMExtProfile:error:];
-[CWFApple80211 linkChangedEventData:];
-[CWFApple80211 setChannel:error:];
-[CWFApple80211 txPower:];
-[CWFApple80211 __MCSIndex:];
-[CWFApple80211 eventHandler];
-[CWFApple80211 AWDLSyncState:];
-[CWFApple80211 supportedPHYModes:];
-[CWFApple80211 powersave:];
-[CWFApple80211 AWDLSidecarDiagnostics:];
-[CWFApple80211 setEventHandler:];
-[CWFApple80211 chainAck:];
-[CWFApple80211 stopMonitoringEventWithType:interfaceName:];
-[CWFApple80211 __guardInterval:];
-[CWFApple80211 hardwareSupportedChannels:];
-[CWFApple80211 AWDLSyncChannelSequence:];
-[CWFApple80211 __VHTNumberOfSpatialStreams:];
-[CWFApple80211 init];
-[CWFApple80211 blockedBands:];
-[CWFApple80211 AWDLSyncEnabled:];
-[CWFApple80211 AWDLExtensionStateMachineParameters:];
-[CWFApple80211 BSSID:];
-[CWFApple80211 channelsInfo:];
-[CWFApple80211 dealloc];
-[CWFApple80211 csiFWStats:];
-[CWFApple80211 beaconCache:];
-[CWFApple80211 perAntennaRSSI:];
-[CWFApple80211 LQMConfig:];
-[CWFApple80211 bluetoothCoexistenceProfiles5GHz:];
-[CWFApple80211 __apple80211RefWithInterfaceName:];
-[CWFApple80211 __VHTGuardInterval:];
-[CWFApple80211 isAWDLEnabled];
-[CWFApple80211 powerOn:];
-[CWFApple80211 interfaceName];
-[CWFApple80211 isMonitoringEventType:interfaceName:];
-[CWFApple80211 wowEnabled:];
-[CWFApple80211 MCSIndex:];
-[CWFApple80211 bluetoothCoexistenceProfiles2GHz:];
-[CWFApple80211 authType:];
-[CWFApple80211 txNSS:];
-[CWFApple80211 desense:];
-[CWFApple80211 virtualInterfaceParent:];
-[CWFApple80211 powerTableInfo:];
-[CWFApple80211 AWDLSyncParameters:];
-[CWFApple80211 capabilities:];
-[CWFApple80211 __VHTMCSIndex:];
-[CWFApple80211 currentNetwork:];
-[CWFApple80211 startMonitoringEventWithType:interfaceName:];
-[CWFApple80211 cachedCapabilities];
-[CWFApple80211 LQMSummary:];
-[CWFApple80211 AWDLEncryptionType:];
-[CWFApple80211 hardwareMACAddress:];
-[CWFApple80211 AWDLStrategy:];
-[CWFApple80211 NANRadioSchedule:];
-[CWFApple80211 AWDLMasterChannel:];
-[CWFApple80211 interfaceNames:];
-[CWFApple80211 invalidate];
-[CWFApple80211 RSSI:];
-[CWFApple80211 countryCode:];
-[CWFApple80211 csiConfig:];
-[CWFApple80211 AWDLPeerDatabase:];
-[CWFApple80211 txRate:];
-[CWFApple80211 guardInterval:];
-[CWFApple80211 rxRate:];
-[CWFApple80211 AWDLStatistics:];
-[CWFApple80211 AWDLGuardTime:];
-[CWFApple80211 desenseLevel:];
-[CWFApple80211 supportedChannelsWithCountryCode:error:];
-[CWFApple80211 virtualInterfaceNames:];
-[CWFApple80211 DTIMInterval:];
-[CWFApple80211 AWDLAvailabilityWindowAPAlignment:];
-[CWFApple80211 txChainPower:];
-[CWFApple80211 AWDLPresenceMode:];
-[CWFApple80211 AWDLElectionMetric:];
-[CWFApple80211 AWDLSocialTimeSlots:];
-[CWFApple80211 initWithInterfaceName:];
-[CWFApple80211 AWDLBTLEStateParameters:];
-[CWFApple80211 rangingCapabilities:];
-[CWFApple80211 __numberOfSpatialStreams:];
-[CWFApple80211 powerState:];
-[CWFApple80211 description];
-[CWFApple80211 virtualInterfaceParent];
-[CWFApple80211 AWDLSecondaryMasterChannel:];
-[CWFApple80211 AWDLOpMode:];
-[CWFApple80211 hostAPStationList:];
-[CWFApple80211 setLQMConfig:error:];
-[CWFApple80211 SSID:];
-[CWFApple80211 numberOfSpatialStreams:];
-[CWFApple80211 bluetoothCoexistenceConfig:];
-[CWFApple80211 AWDLPeerTrafficRegistration:];
-[CWFApple80211 noise:];
-[CWFApple80211 AWDLAFTxMode:];
-[CWFApple80211 AWDLElectionRSSIThresholds:];
-[CWFApple80211 activePHYMode:];
-[CWFApple80211 AWDLContinuousElectionAlgorithmEnabled:];
-[CWFApple80211 __supportedChannelsWithCountryCode:error:];
-[CWFApple80211 AWDLElectionID:];
-[CWFApple80211 maxNSSForAP:];
-[CWFApple80211 __apple80211FindServiceWithInterfaceName:];
-[CWFApple80211 bluetoothCoexistenceMode:];
-[CWFApple80211 channel:];
-[CWFApple80211 countryBandSupport:];
-[CWFApple80211 powerDebugInfo:];
-[CWFApple80211 leakyAPStats:];
-[CWFApple80211 __setupEventMonitoring];
-[CWFApple80211 cca:];
-[CWFApple80211 state:];
-[CWFApple80211 backgroundScanCache:];
-[CWFApple80211 __hardwareSupportedChannels:];
-[CWFApple80211 AWDLPreferredChannels:];
-[CWFApple80211 AWDLElectionParameters:];
```
