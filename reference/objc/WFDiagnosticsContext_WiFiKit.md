# `WFDiagnosticsContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFDiagnosticsProviderContext`
- 35 instance variables, 39 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _captive;
B _multiAP;
B _managed;
@"NSString" _BSSID;
@"NSNumber" _channel;
@"NSString" _channelPerformance;
q requestedFields;
@"NSString" _rssi;
@"NSString" _rssiPerformance;
@? refreshHandler;
@"NSString" _security;
@"NSString" _adviceString;
@"NSString" _awdl;
@"NSString" _beaconPER;
@"NSString" _bluetooth;
@"NSString" _cca;
@"NSString" _channelString;
@"NSString" _channelWidth;
@"NSString" _coexFooter;
@"NSString" _deployment;
@"NSString" _motion;
@"NSString" _gateway;
@"NSString" _internet;
@"NSString" _probeFooter;
@"NSString" _recvFrames;
@"NSString" _scan;
@"NSString" _securityAdvice;
@"NSString" _transmitPER;
@"NSDate" _networkQualityDate;
d _networkQualityResponsiveness;
@"WFNetworkScanRecord" _network;
@"WFNetworkProfile" _profile;
@"WFDetailsContext" _context;
^{__WiFiManagerClient=} _manager;
^{__WiFiDeviceClient=} _device;
```

## Properties

```
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (T@"WFNetworkProfile",&,N,V_profile) profile;
@property (T@"WFDetailsContext",&,N,V_context) context;
@property (T^{__WiFiManagerClient=},N,V_manager) manager;
@property (T^{__WiFiDeviceClient=},N,V_device) device;
@property (T@?,C,N,VrefreshHandler) refreshHandler;
@property (T@"NSString",R,N,V_security) security;
@property (T@"NSString",R,N,V_securityAdvice) securityAdvice;
@property (T@"NSString",R,N,V_BSSID) BSSID;
@property (T@"NSNumber",R,N,V_channel) channel;
@property (T@"NSString",R,N,V_channelString) channelString;
@property (T@"NSString",R,N,V_channelWidth) channelWidth;
@property (T@"NSString",R,N,V_channelPerformance) channelPerformance;
@property (T@"NSString",R,N,V_rssi) rssi;
@property (T@"NSString",R,N,V_cca) cca;
@property (T@"NSString",R,N,V_adviceString) adviceString;
@property (T@"NSString",R,N,V_beaconPER) beaconPER;
@property (T@"NSString",R,N,V_transmitPER) transmitPER;
@property (T@"NSString",R,N,V_recvFrames) recvFrames;
@property (T@"NSString",R,N,V_rssiPerformance) rssiPerformance;
@property (TB,R,N,V_captive) captive;
@property (TB,R,N,V_managed) managed;
@property (TB,R,N,V_multiAP) multiAP;
@property (T@"NSString",R,N,V_deployment) deployment;
@property (T@"NSString",R,N,V_motion) motion;
@property (T@"NSString",R,N,V_gateway) gateway;
@property (T@"NSString",R,N,V_internet) internet;
@property (T@"NSString",R,N,V_probeFooter) probeFooter;
@property (T@"NSString",R,N,V_awdl) awdl;
@property (T@"NSString",R,N,V_bluetooth) bluetooth;
@property (T@"NSString",R,N,V_scan) scan;
@property (T@"NSString",R,N,V_coexFooter) coexFooter;
@property (Td,N,V_networkQualityResponsiveness) networkQualityResponsiveness;
@property (T@"NSDate",C,N,V_networkQualityDate) networkQualityDate;
@property (Tq,R,N,VrequestedFields) requestedFields;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFDiagnosticsContext rssi];
-[WFDiagnosticsContext cca];
-[WFDiagnosticsContext managed];
-[WFDiagnosticsContext channel];
-[WFDiagnosticsContext BSSID];
-[WFDiagnosticsContext setDevice:];
-[WFDiagnosticsContext gateway];
-[WFDiagnosticsContext network];
-[WFDiagnosticsContext device];
-[WFDiagnosticsContext setManager:];
-[WFDiagnosticsContext setProfile:];
-[WFDiagnosticsContext manager];
-[WFDiagnosticsContext requestedFields];
-[WFDiagnosticsContext setRefreshHandler:];
-[WFDiagnosticsContext updateInfo:];
-[WFDiagnosticsContext profile];
-[WFDiagnosticsContext setContext:];
-[WFDiagnosticsContext channelWidth];
-[WFDiagnosticsContext security];
-[WFDiagnosticsContext refreshHandler];
-[WFDiagnosticsContext cancel];
-[WFDiagnosticsContext context];
-[WFDiagnosticsContext deployment];
-[WFDiagnosticsContext setNetwork:];
-[WFDiagnosticsContext motion];
-[WFDiagnosticsContext bluetooth];
-[WFDiagnosticsContext channelString];
-[WFDiagnosticsContext scan];
-[WFDiagnosticsContext captive];
-[WFDiagnosticsContext networkQualityDate];
-[WFDiagnosticsContext networkQualityResponsiveness];
-[WFDiagnosticsContext setNetworkQualityDate:];
-[WFDiagnosticsContext setNetworkQualityResponsiveness:];
-[WFDiagnosticsContext awdl];
-[WFDiagnosticsContext beaconPER];
-[WFDiagnosticsContext multiAP];
-[WFDiagnosticsContext rssiPerformance];
-[WFDiagnosticsContext adviceString];
-[WFDiagnosticsContext channelPerformance];
-[WFDiagnosticsContext coexFooter];
-[WFDiagnosticsContext initWithNetwork:profile:detailsContext:];
-[WFDiagnosticsContext internet];
-[WFDiagnosticsContext probeFooter];
-[WFDiagnosticsContext recvFrames];
-[WFDiagnosticsContext securityAdvice];
-[WFDiagnosticsContext transmitPER];
```
