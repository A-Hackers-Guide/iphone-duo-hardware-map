# `WiFiUsageRangingSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _sessionStartTimestamp;
@"NSDate" _sessionLinkUpTimestamp;
@"NSDate" _peerDiscoveryTimestamp;
@"NSDate" _rangingStartedTimestamp;
@"NSDate" _rangingCompletionTimestamp;
Q _selfPreferredChannel;
Q _selfMainChannel;
Q _selfChannelFlags;
Q _peerPreferredChannel;
Q _peerMainChannel;
Q _peerChannelFlags;
Q _numRequestedMeasurements;
Q _numValidMeasurements;
q _measurementStatus;
Q _measurementFlags;
d _linkUpLatency;
d _rangingLatency;
@"NSMutableArray" _rttSamples;
@"NSString" _requester;
```

## Instance methods

```
-[WiFiUsageRangingSession rangingCompletedWithValidCount:resultStatus:resultFlags:];
-[WiFiUsageRangingSession init];
-[WiFiUsageRangingSession metricName];
-[WiFiUsageRangingSession rangingStartedWithNumMeasurements:];
-[WiFiUsageRangingSession addRangingRttSampleWithRssi:rtt:snr:flags:channel:coreId:bitErrorRate:phyError:andPeerSnr:andPeerCoreId:andPeerBitErrorRate:andPeerPhyError:];
-[WiFiUsageRangingSession rangingSessionRequestedWithSelfPreferredChannel:selfMainChannel:selfChannelFlags:peerPreferredChannel:peerMainChannel:peerChannelFlags:requester:];
-[WiFiUsageRangingSession sessionSummary:];
-[WiFiUsageRangingSession rangingLinkUp];
```
