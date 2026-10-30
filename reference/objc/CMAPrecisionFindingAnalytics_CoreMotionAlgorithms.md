# `CMAPrecisionFindingAnalytics`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 34 instance variables, 12 properties, 34 instance methods, 0 class methods

## Instance variables

```
i _revokeReason;
d _timestampOfFirstRawRange;
d _timestampOfFirstAcceptedRange;
d _timestampOfRecentDMSample;
d _timestampOfPreviousDMSample;
d _timestampOfFirstDMSample;
d _totalTimeDuringRevoke;
i _countDM;
i _countWristUp;
i _countWristDown;
i _crown;
i _wrist;
i _countRawRange;
i _countAcceptedRange;
i _countRawRangeWhileConverging;
i _countAcceptedRangeWhileConverging;
i _countRawRangeDuringRevoke;
i _countAcceptedRangeDuringRevoke;
B _wasFirstArcShown;
B _wasFirstRangeAccepted;
d _minEstimatedHeight;
d _maxEstimatedHeight;
@"NSNumber" _percentOfSessionInWristUp;
@"NSNumber" _percentOfSessionInWristDown;
@"NSNumber" _timeFromFirstRangeToFirstAcceptedRange;
@"NSNumber" _firstAcceptedRange;
@"NSNumber" _meanRawRangeFrequencyThroughoutSession;
@"NSNumber" _meanAcceptedRangeFrequencyThroughoutSession;
@"NSNumber" _meanRawRangeFrequencyWhileConverging;
@"NSNumber" _meanAcceptedRangeFrequencyWhileConverging;
@"NSNumber" _meanRawRangeFrequencyDuringRevoke;
@"NSNumber" _meanAcceptedFrequencyQualityDuringRevoke;
@"NSNumber" _maxEstimatedDeltaHeightOverSession;
@"NSNumber" _maxPercentParticlesAboveHeightThreshold;
```

## Properties

```
@property (T@"NSNumber",&,N,V_percentOfSessionInWristUp) percentOfSessionInWristUp;
@property (T@"NSNumber",&,N,V_percentOfSessionInWristDown) percentOfSessionInWristDown;
@property (T@"NSNumber",&,N,V_timeFromFirstRangeToFirstAcceptedRange) timeFromFirstRangeToFirstAcceptedRange;
@property (T@"NSNumber",&,N,V_firstAcceptedRange) firstAcceptedRange;
@property (T@"NSNumber",&,N,V_meanRawRangeFrequencyThroughoutSession) meanRawRangeFrequencyThroughoutSession;
@property (T@"NSNumber",&,N,V_meanAcceptedRangeFrequencyThroughoutSession) meanAcceptedRangeFrequencyThroughoutSession;
@property (T@"NSNumber",&,N,V_meanRawRangeFrequencyWhileConverging) meanRawRangeFrequencyWhileConverging;
@property (T@"NSNumber",&,N,V_meanAcceptedRangeFrequencyWhileConverging) meanAcceptedRangeFrequencyWhileConverging;
@property (T@"NSNumber",&,N,V_meanRawRangeFrequencyDuringRevoke) meanRawRangeFrequencyDuringRevoke;
@property (T@"NSNumber",&,N,V_meanAcceptedFrequencyQualityDuringRevoke) meanAcceptedFrequencyQualityDuringRevoke;
@property (T@"NSNumber",&,N,V_maxEstimatedDeltaHeightOverSession) maxEstimatedDeltaHeightOverSession;
@property (T@"NSNumber",&,N,V_maxPercentParticlesAboveHeightThreshold) maxPercentParticlesAboveHeightThreshold;
```

## Instance methods

```
-[CMAPrecisionFindingAnalytics init];
-[CMAPrecisionFindingAnalytics dealloc];
-[CMAPrecisionFindingAnalytics analyticsDictionary];
-[CMAPrecisionFindingAnalytics setPercentOfSessionInWristDown:];
-[CMAPrecisionFindingAnalytics feedAcceptedRange:];
-[CMAPrecisionFindingAnalytics feedDeviceMotion:];
-[CMAPrecisionFindingAnalytics feedEstimatedHeight:];
-[CMAPrecisionFindingAnalytics feedFractionAboveThreshold:];
-[CMAPrecisionFindingAnalytics feedRange:];
-[CMAPrecisionFindingAnalytics feedRevokeReason:];
-[CMAPrecisionFindingAnalytics feedWatchOrientation:];
-[CMAPrecisionFindingAnalytics firstAcceptedRange];
-[CMAPrecisionFindingAnalytics maxEstimatedDeltaHeightOverSession];
-[CMAPrecisionFindingAnalytics maxPercentParticlesAboveHeightThreshold];
-[CMAPrecisionFindingAnalytics meanAcceptedFrequencyQualityDuringRevoke];
-[CMAPrecisionFindingAnalytics meanAcceptedRangeFrequencyThroughoutSession];
-[CMAPrecisionFindingAnalytics meanAcceptedRangeFrequencyWhileConverging];
-[CMAPrecisionFindingAnalytics meanRawRangeFrequencyDuringRevoke];
-[CMAPrecisionFindingAnalytics meanRawRangeFrequencyThroughoutSession];
-[CMAPrecisionFindingAnalytics meanRawRangeFrequencyWhileConverging];
-[CMAPrecisionFindingAnalytics percentOfSessionInWristDown];
-[CMAPrecisionFindingAnalytics percentOfSessionInWristUp];
-[CMAPrecisionFindingAnalytics setFirstAcceptedRange:];
-[CMAPrecisionFindingAnalytics setMaxEstimatedDeltaHeightOverSession:];
-[CMAPrecisionFindingAnalytics setMaxPercentParticlesAboveHeightThreshold:];
-[CMAPrecisionFindingAnalytics setMeanAcceptedFrequencyQualityDuringRevoke:];
-[CMAPrecisionFindingAnalytics setMeanAcceptedRangeFrequencyThroughoutSession:];
-[CMAPrecisionFindingAnalytics setMeanAcceptedRangeFrequencyWhileConverging:];
-[CMAPrecisionFindingAnalytics setMeanRawRangeFrequencyDuringRevoke:];
-[CMAPrecisionFindingAnalytics setMeanRawRangeFrequencyThroughoutSession:];
-[CMAPrecisionFindingAnalytics setMeanRawRangeFrequencyWhileConverging:];
-[CMAPrecisionFindingAnalytics setPercentOfSessionInWristUp:];
-[CMAPrecisionFindingAnalytics setTimeFromFirstRangeToFirstAcceptedRange:];
-[CMAPrecisionFindingAnalytics timeFromFirstRangeToFirstAcceptedRange];
```
