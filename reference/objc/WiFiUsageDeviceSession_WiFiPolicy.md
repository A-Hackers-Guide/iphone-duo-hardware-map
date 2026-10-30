# `WiFiUsageDeviceSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 7 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _firstDisplayOn;
B _hasAttemptedJoinRSNO;
B _hasAttemptedJoinMRSNO;
B _hasAttemptedJoinRSNOFallback;
B _hasAttemptedJoinMRSNOFallback;
B _hasFailedJoinRSNO;
B _hasFailedJoinMRSNO;
```

## Instance methods

```
-[WiFiUsageDeviceSession linkQualityDidChange:];
-[WiFiUsageDeviceSession metricName];
-[WiFiUsageDeviceSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:];
-[WiFiUsageDeviceSession eventDictionary:];
-[WiFiUsageDeviceSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageDeviceSession systemWakeStateDidChange:wokenByWiFi:];
-[WiFiUsageDeviceSession displayStateDidChange:];
-[WiFiUsageDeviceSession sessionDidStart];
-[WiFiUsageDeviceSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:];
-[WiFiUsageDeviceSession copyWithZone:];
```
