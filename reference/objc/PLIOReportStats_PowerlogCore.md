# `PLIOReportStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _ioReportSample;
@"NSDate" _sampleTime;
@"NSDate" _sampleTimePrevious;
^{__IOReportSubscriptionCF=} _subscription;
@"NSDictionary" _subscribedChannels;
@"NSString" _driverName;
@"NSDictionary" _previousIOReportSample;
```

## Properties

```
@property (T@"NSString",&,V_driverName) driverName;
@property (T@"NSDictionary",&,V_previousIOReportSample) previousIOReportSample;
@property (T@"NSDictionary",&,V_ioReportSample) ioReportSample;
@property (T@"NSDate",&,V_sampleTime) sampleTime;
@property (T@"NSDate",&,V_sampleTimePrevious) sampleTimePrevious;
@property (T^{__IOReportSubscriptionCF=},V_subscription) subscription;
@property (T@"NSDictionary",&,V_subscribedChannels) subscribedChannels;
```

## Instance methods

```
-[PLIOReportStats setSubscribedChannels:];
-[PLIOReportStats subscription];
-[PLIOReportStats init];
-[PLIOReportStats dealloc];
-[PLIOReportStats setSubscription:];
-[PLIOReportStats _init];
-[PLIOReportStats subscribedChannels];
-[PLIOReportStats driverName];
-[PLIOReportStats sampleTime];
-[PLIOReportStats setSampleTime:];
-[PLIOReportStats clearSubscription];
-[PLIOReportStats getCurrentStats];
-[PLIOReportStats _calculateDeltaFromPreviousStats:toCurrentStats:];
-[PLIOReportStats _convertValue:toUnityScaleFromUnit:];
-[PLIOReportStats _parseIOReportSampleFromStats:convertingUnitToUnityScale:];
-[PLIOReportStats calculateDeltaFromPreviousSamples];
-[PLIOReportStats calculateDeltaFromPreviousSamplesConvertingUnitToUnityScale:];
-[PLIOReportStats currentValueForSimpleChannel:];
-[PLIOReportStats currentValueForStateChannel:atIndex:];
-[PLIOReportStats deltaValueForSimpleChannel:];
-[PLIOReportStats deltaValueForStateChannel:atIndex:];
-[PLIOReportStats getDeltaStats];
-[PLIOReportStats getSampleDuration];
-[PLIOReportStats initWithDriverName:withGroup:];
-[PLIOReportStats initWithGroup:andSubGroup:];
-[PLIOReportStats initWithGroup:andSubGroup:withChannelIDs:];
-[PLIOReportStats initWithGroup:andSubGroup:withChannelIDs:manualChannelOnly:];
-[PLIOReportStats ioReportSample];
-[PLIOReportStats parseIOReportSample];
-[PLIOReportStats parseSimpleDeltaSample];
-[PLIOReportStats previousIOReportSample];
-[PLIOReportStats sampleTimePrevious];
-[PLIOReportStats setDriverName:];
-[PLIOReportStats setIoReportSample:];
-[PLIOReportStats setPreviousIOReportSample:];
-[PLIOReportStats setSampleTimePrevious:];
-[PLIOReportStats subscribeToGroup:andSubGroup:];
-[PLIOReportStats subscribeToGroup:andSubGroup:withChannelIDs:];
-[PLIOReportStats subscribeToGroup:andSubGroup:withChannelIDs:manualChannelOnly:];
-[PLIOReportStats updateStats];
-[PLIOReportStats updateStatsWithBlock:];
```
