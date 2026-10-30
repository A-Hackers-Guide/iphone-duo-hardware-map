# `WFOtherNetworkProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WFCredentialsProvider`
- 0 instance variables, 6 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) SSID;
@property (Tq,?,R,N) securityMode;
@property (TB,?,N) joining;
@property (T@"NSString",?,N) activityString;
@property (T@,?,R,N) WAPIIdentity;
@property (T@,?,R,N) WAPIRootCertificate;
```

## Instance methods

```
-[WFOtherNetworkProvider SSID];
-[WFOtherNetworkProvider setActivityString:];
-[WFOtherNetworkProvider activityString];
-[WFOtherNetworkProvider securityMode];
-[WFOtherNetworkProvider joining];
-[WFOtherNetworkProvider WAPIIdentity];
-[WFOtherNetworkProvider WAPIRootCertificate];
-[WFOtherNetworkProvider setJoining:];
```
