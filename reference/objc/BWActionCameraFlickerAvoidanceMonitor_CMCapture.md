# `BWActionCameraFlickerAvoidanceMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
i _flickerFrequency;
i _frameRateCompatibleFlickerFrequency;
i _confidenceThreshold;
i _confidenceHysteresis;
B _frameRateAware;
f _currentFrameRate;
i _frameRateUpdateCounter;
@"NSDictionary" _defaultMaxExposureDurationFrameworkOverrideByPortType;
```

## Properties

```
@property (Ti,N,V_flickerFrequency) flickerFrequency;
```

## Class methods

```
+[BWActionCameraFlickerAvoidanceMonitor initialize];
```

## Instance methods

```
-[BWActionCameraFlickerAvoidanceMonitor dealloc];
-[BWActionCameraFlickerAvoidanceMonitor detectFlickerWithSampleBuffer:fromCaptureStreamWithPortType:];
-[BWActionCameraFlickerAvoidanceMonitor flickerFrequency];
-[BWActionCameraFlickerAvoidanceMonitor initWithDefaultMaxExposureDurationFrameworkOverrideByPortType:];
-[BWActionCameraFlickerAvoidanceMonitor setFlickerFrequency:];
```
