# `FigCaptureCustomExposureConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _applyStatisticsLock;
f _exposureDuration;
d _minFrameRate;
d _maxFrameRate;
f _ISO;
f _lensAperture;
B _useSpotMetering;
i _requestID;
B _hasLockedExposureDuration;
B _hasLockedISO;
B _hasLockedAperture;
B _enableFNumberForAperturePriority;
B _requiresUnlockedAE;
@"NSMutableDictionary" _streamPropertyKeyByPortType;
@"NSMutableDictionary" _streamPropertyValueByPortType;
B _appliedFrameStatistics;
B _commandSubmitted;
```

## Class methods

```
+[FigCaptureCustomExposureConfiguration initialize];
```

## Instance methods

```
-[FigCaptureCustomExposureConfiguration _description];
-[FigCaptureCustomExposureConfiguration dealloc];
-[FigCaptureCustomExposureConfiguration description];
-[FigCaptureCustomExposureConfiguration _initWithExposureDuration:minFrameRate:maxFrameRate:ISO:lensAperture:useSpotMetering:requestID:];
-[FigCaptureCustomExposureConfiguration _processConfigurationForPortType:limits:];
```
