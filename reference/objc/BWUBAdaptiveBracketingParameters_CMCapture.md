# `BWUBAdaptiveBracketingParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWNoiseReductionAndFusionProcessorBracketingParameters`
- 6 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UBProgressiveBracketingParameters" _progressiveBracketingParameters;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _adaptiveBracketingFrameParametersLock;
@"NSArray" _adaptiveBracketingFrameParameters;
B _stopped;
# _progressiveBracketingStatisticsClass;
@"UBProgressiveBracketingStatistics" _lastProgressiveBracketingStatisticsForTotalIntegrationTimesProvider;
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
-[BWUBAdaptiveBracketingParameters dealloc];
-[BWUBAdaptiveBracketingParameters stationary];
-[BWUBAdaptiveBracketingParameters stopped];
-[BWUBAdaptiveBracketingParameters adaptiveBracketingFrameParametersForGroup:];
-[BWUBAdaptiveBracketingParameters adaptiveBracketingParametersForDigitalFlashMode:sphereOffsetEnabled:];
-[BWUBAdaptiveBracketingParameters evZeroTargetGain];
-[BWUBAdaptiveBracketingParameters generateWhiteBalanceParameters];
-[BWUBAdaptiveBracketingParameters previewSNR];
-[BWUBAdaptiveBracketingParameters totalIntegrationTime];
-[BWUBAdaptiveBracketingParameters totalIntegrationTimeForDigitalFlashMode:frameStatistics:stationary:detectedObjects:];
```
