# `VISRotationCorrectionEstimator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
f _timeScale;
B _isInitialized;
d _prevTime;
{?="vector"} _prevRotation;
_accumulatedCorrection;
@"HighPassIIR2FilterFloat3" highPassFilter1;
@"HighPassIIR2FilterFloat3" highPassFilter2;
_estimatedCorrection;
```

## Properties

```
@property (T,R,N,V_estimatedCorrection) estimatedCorrection;
```

## Instance methods

```
-[VISRotationCorrectionEstimator reset];
-[VISRotationCorrectionEstimator initWithTimeScale:];
-[VISRotationCorrectionEstimator estimatedCorrection];
-[VISRotationCorrectionEstimator updateWithRotation:atTime:];
```
