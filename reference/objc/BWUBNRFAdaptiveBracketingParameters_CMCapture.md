# `BWUBNRFAdaptiveBracketingParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWNoiseReductionAndFusionProcessorBracketingParameters`
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
-[BWUBNRFAdaptiveBracketingParameters dealloc];
-[BWUBNRFAdaptiveBracketingParameters stationary];
-[BWUBNRFAdaptiveBracketingParameters stopped];
-[BWUBNRFAdaptiveBracketingParameters adaptiveBracketingFrameParametersForGroup:];
-[BWUBNRFAdaptiveBracketingParameters adaptiveBracketingParametersForDigitalFlashMode:sphereOffsetEnabled:];
-[BWUBNRFAdaptiveBracketingParameters evZeroTargetGain];
-[BWUBNRFAdaptiveBracketingParameters generateWhiteBalanceParameters];
-[BWUBNRFAdaptiveBracketingParameters previewSNR];
-[BWUBNRFAdaptiveBracketingParameters totalIntegrationTime];
-[BWUBNRFAdaptiveBracketingParameters totalIntegrationTimeForDigitalFlashMode:frameStatistics:stationary:detectedObjects:];
```
