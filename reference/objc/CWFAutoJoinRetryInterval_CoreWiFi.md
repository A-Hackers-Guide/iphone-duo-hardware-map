# `CWFAutoJoinRetryInterval`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _BSSChannelsOnly;
B _passiveScan;
B _allowAutoHotspotFallback;
B _includeAdjacent5GHzChannel;
B _includeOnlyRemaining5GHzChannels;
B _alwaysIncludeRemainingNon2GHzChannels;
B _alwaysInclude6GHzPSCChannels;
Q _interval;
Q _count;
Q _maxBSSChannelCount;
Q _maxBSSChannelAge;
Q _dwellTime;
```

## Properties

```
@property (TQ,N,V_interval) interval;
@property (TQ,N,V_count) count;
@property (TB,N,V_BSSChannelsOnly) BSSChannelsOnly;
@property (TQ,N,V_maxBSSChannelCount) maxBSSChannelCount;
@property (TQ,N,V_maxBSSChannelAge) maxBSSChannelAge;
@property (TQ,N,V_dwellTime) dwellTime;
@property (TB,N,V_passiveScan) passiveScan;
@property (TB,N,V_allowAutoHotspotFallback) allowAutoHotspotFallback;
@property (TB,N,V_includeAdjacent5GHzChannel) includeAdjacent5GHzChannel;
@property (TB,N,V_includeOnlyRemaining5GHzChannels) includeOnlyRemaining5GHzChannels;
@property (TB,N,V_alwaysIncludeRemainingNon2GHzChannels) alwaysIncludeRemainingNon2GHzChannels;
@property (TB,N,V_alwaysInclude6GHzPSCChannels) alwaysInclude6GHzPSCChannels;
```

## Instance methods

```
-[CWFAutoJoinRetryInterval setIncludeAdjacent5GHzChannel:];
-[CWFAutoJoinRetryInterval alwaysIncludeRemainingNon2GHzChannels];
-[CWFAutoJoinRetryInterval setMaxBSSChannelAge:];
-[CWFAutoJoinRetryInterval maxBSSChannelAge];
-[CWFAutoJoinRetryInterval setIncludeOnlyRemaining5GHzChannels:];
-[CWFAutoJoinRetryInterval maxBSSChannelCount];
-[CWFAutoJoinRetryInterval alwaysInclude6GHzPSCChannels];
-[CWFAutoJoinRetryInterval dwellTime];
-[CWFAutoJoinRetryInterval passiveScan];
-[CWFAutoJoinRetryInterval setAlwaysIncludeRemainingNon2GHzChannels:];
-[CWFAutoJoinRetryInterval setMaxBSSChannelCount:];
-[CWFAutoJoinRetryInterval includeOnlyRemaining5GHzChannels];
-[CWFAutoJoinRetryInterval BSSChannelsOnly];
-[CWFAutoJoinRetryInterval setPassiveScan:];
-[CWFAutoJoinRetryInterval setDwellTime:];
-[CWFAutoJoinRetryInterval includeAdjacent5GHzChannel];
-[CWFAutoJoinRetryInterval setCount:];
-[CWFAutoJoinRetryInterval setBSSChannelsOnly:];
-[CWFAutoJoinRetryInterval setInterval:];
-[CWFAutoJoinRetryInterval interval];
-[CWFAutoJoinRetryInterval setAllowAutoHotspotFallback:];
-[CWFAutoJoinRetryInterval count];
-[CWFAutoJoinRetryInterval setAlwaysInclude6GHzPSCChannels:];
-[CWFAutoJoinRetryInterval allowAutoHotspotFallback];
-[CWFAutoJoinRetryInterval autoJoinRetryInterval:count:];
-[CWFAutoJoinRetryInterval description];
-[CWFAutoJoinRetryInterval copyWithZone:];
```
