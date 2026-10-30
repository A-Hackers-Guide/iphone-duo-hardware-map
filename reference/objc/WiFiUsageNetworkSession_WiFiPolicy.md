# `WiFiUsageNetworkSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 11 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"WiFiUsageNetworkDetails" _lastNetworkDetails;
B _linkUp;
@"NSDate" _lastLinkUpTime;
@"NSDate" _lastLinkDownTime;
d _networkUsageDuration;
B _dnuEnabled;
@"NSMutableSet" _neighborBssList;
@"NSMutableSet" _otherBssList;
@"NSMutableSet" _roamTargetBssList;
@"NSMutableArray" _accumulatedNeighborBssList;
@"NSObject<OS_dispatch_queue>" _WiFiLinkStateBiomeEventQueue;
```

## Instance methods

```
-[WiFiUsageNetworkSession sessionDidEnd];
-[WiFiUsageNetworkSession cellularWRMScoreDidChange:];
-[WiFiUsageNetworkSession metricName];
-[WiFiUsageNetworkSession accumulateNeighborBssList:];
-[WiFiUsageNetworkSession processForgetNetwork:];
-[WiFiUsageNetworkSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:];
-[WiFiUsageNetworkSession _isInternalDeviceAndAppleInternalNetwork];
-[WiFiUsageNetworkSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageNetworkSession displayStateDidChange:];
-[WiFiUsageNetworkSession sessionDidStart];
-[WiFiUsageNetworkSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:];
-[WiFiUsageNetworkSession scanningStateDidChange:client:neighborBSS:otherBSS:];
-[WiFiUsageNetworkSession roamingStateDidChange:reason:andStatus:andLatency:andRoamData:andPingPongStats:];
-[WiFiUsageNetworkSession isSessionHarvestable];
```
