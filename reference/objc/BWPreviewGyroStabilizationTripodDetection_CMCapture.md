# `BWPreviewGyroStabilizationTripodDetection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
[60B] _stationary;
i _inputIndex;
i _ringCount;
i _previousLikelyPhysicalTripodCount;
f _tripodMaxAngleThresholdInstant;
f _tripodMaxAngleThresholdAccumulate;
f _physicalTripodLikelyMaxAngleThreshold;
f _physicalTripodGuaranteedMaxAngleThreshold;
B _isStationary;
B _isLikelyPhysicalTripod;
B _isPhysicalTripod;
```

## Properties

```
@property (TB,R,N) empty;
@property (TB,R,N,V_isStationary) isStationary;
@property (TB,R,N,V_isLikelyPhysicalTripod) isLikelyPhysicalTripod;
@property (TB,R,N,V_isPhysicalTripod) isPhysicalTripod;
```

## Instance methods

```
-[BWPreviewGyroStabilizationTripodDetection empty];
-[BWPreviewGyroStabilizationTripodDetection reset];
-[BWPreviewGyroStabilizationTripodDetection isStationary];
-[BWPreviewGyroStabilizationTripodDetection _detectPhysicalTripodUsingMaxAngleInstant:frameRateNormalization:];
-[BWPreviewGyroStabilizationTripodDetection _isCameraStationary];
-[BWPreviewGyroStabilizationTripodDetection _updateWithMaxAngleInstant:maxAngleAccumulate:];
-[BWPreviewGyroStabilizationTripodDetection detectTripodStateUsingMaxAngleInstant:maxAngleAccumulate:frameRateNormalizationFactor:];
-[BWPreviewGyroStabilizationTripodDetection initWithTripodDetectionThresholds:tripodMaxAngleThresholdAccumulate:physicalTripodLikelyMaxAngleThreshold:physicalTripodGuaranteedMaxAngleThreshold:];
-[BWPreviewGyroStabilizationTripodDetection isLikelyPhysicalTripod];
-[BWPreviewGyroStabilizationTripodDetection isPhysicalTripod];
```
