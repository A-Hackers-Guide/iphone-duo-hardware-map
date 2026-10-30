# `WFDiagnosticsProviderContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WFProviderContext`
- 0 instance variables, 29 properties, 32 instance methods, 0 class methods

## Properties

```
@property (T@?,C,N) refreshHandler;
@property (T@"NSString",R,N) security;
@property (T@"NSString",R,N) securityAdvice;
@property (T@"NSString",R,N) BSSID;
@property (T@"NSNumber",R,N) channel;
@property (T@"NSString",R,N) channelString;
@property (T@"NSString",R,N) channelWidth;
@property (T@"NSString",R,N) channelPerformance;
@property (T@"NSString",R,N) rssi;
@property (T@"NSString",R,N) cca;
@property (T@"NSString",R,N) adviceString;
@property (T@"NSString",R,N) beaconPER;
@property (T@"NSString",R,N) transmitPER;
@property (T@"NSString",R,N) recvFrames;
@property (T@"NSString",R,N) rssiPerformance;
@property (TB,R,N) captive;
@property (TB,R,N) managed;
@property (TB,R,N) multiAP;
@property (T@"NSString",R,N) deployment;
@property (T@"NSString",R,N) motion;
@property (T@"NSString",R,N) gateway;
@property (T@"NSString",R,N) internet;
@property (T@"NSString",R,N) probeFooter;
@property (T@"NSString",R,N) awdl;
@property (T@"NSString",R,N) bluetooth;
@property (T@"NSString",R,N) scan;
@property (T@"NSString",R,N) coexFooter;
@property (Td,N) networkQualityResponsiveness;
@property (T@"NSDate",C,N) networkQualityDate;
```

## Instance methods

```
-[WFDiagnosticsProviderContext rssi];
-[WFDiagnosticsProviderContext cca];
-[WFDiagnosticsProviderContext managed];
-[WFDiagnosticsProviderContext channel];
-[WFDiagnosticsProviderContext BSSID];
-[WFDiagnosticsProviderContext gateway];
-[WFDiagnosticsProviderContext setRefreshHandler:];
-[WFDiagnosticsProviderContext channelWidth];
-[WFDiagnosticsProviderContext security];
-[WFDiagnosticsProviderContext refreshHandler];
-[WFDiagnosticsProviderContext deployment];
-[WFDiagnosticsProviderContext motion];
-[WFDiagnosticsProviderContext bluetooth];
-[WFDiagnosticsProviderContext channelString];
-[WFDiagnosticsProviderContext scan];
-[WFDiagnosticsProviderContext captive];
-[WFDiagnosticsProviderContext networkQualityDate];
-[WFDiagnosticsProviderContext networkQualityResponsiveness];
-[WFDiagnosticsProviderContext setNetworkQualityDate:];
-[WFDiagnosticsProviderContext setNetworkQualityResponsiveness:];
-[WFDiagnosticsProviderContext awdl];
-[WFDiagnosticsProviderContext beaconPER];
-[WFDiagnosticsProviderContext multiAP];
-[WFDiagnosticsProviderContext rssiPerformance];
-[WFDiagnosticsProviderContext adviceString];
-[WFDiagnosticsProviderContext channelPerformance];
-[WFDiagnosticsProviderContext coexFooter];
-[WFDiagnosticsProviderContext internet];
-[WFDiagnosticsProviderContext probeFooter];
-[WFDiagnosticsProviderContext recvFrames];
-[WFDiagnosticsProviderContext securityAdvice];
-[WFDiagnosticsProviderContext transmitPER];
```
