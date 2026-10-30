# `BWNRFAdaptiveBracketingParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWAdaptiveBracketingParameters`, `BWAdaptiveBracketingDigitalFlashTotalIntegrationTimesProvider`
- 5 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _adaptiveBracketingParametersLock;
@"NRFProgressiveBracketingParameters" _progressiveBracketingParameters;
B _stopped;
# _progressiveBracketingStatisticsClass;
@"NRFProgressiveBracketingStatistics" _lastProgressiveBracketingStatisticsForTotalIntegrationTimesProvider;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWNRFAdaptiveBracketingParameters dealloc];
-[BWNRFAdaptiveBracketingParameters stationary];
-[BWNRFAdaptiveBracketingParameters stopped];
-[BWNRFAdaptiveBracketingParameters adaptiveBracketingFrameParametersForGroup:];
-[BWNRFAdaptiveBracketingParameters adaptiveBracketingParametersForDigitalFlashMode:sphereOffsetEnabled:];
-[BWNRFAdaptiveBracketingParameters evZeroTargetGain];
-[BWNRFAdaptiveBracketingParameters generateWhiteBalanceParameters];
-[BWNRFAdaptiveBracketingParameters previewSNR];
-[BWNRFAdaptiveBracketingParameters totalIntegrationTime];
-[BWNRFAdaptiveBracketingParameters totalIntegrationTimeForDigitalFlashMode:frameStatistics:stationary:detectedObjects:];
```
