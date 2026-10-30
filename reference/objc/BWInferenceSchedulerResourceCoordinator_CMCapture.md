# `BWInferenceSchedulerResourceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _requestedPoolSizeByFormat;
@"NSMutableDictionary" _pixelBufferPoolByFormat;
```

## Class methods

```
+[BWInferenceSchedulerResourceCoordinator initialize];
```

## Instance methods

```
-[BWInferenceSchedulerResourceCoordinator init];
-[BWInferenceSchedulerResourceCoordinator dealloc];
-[BWInferenceSchedulerResourceCoordinator formatsWithRequestedPoolsRemainingAfterSubtractingFormats:];
-[BWInferenceSchedulerResourceCoordinator pixelBufferPoolForFormat:];
-[BWInferenceSchedulerResourceCoordinator preparePixelBufferPoolsWithBackPressureDrivenPipelining:];
-[BWInferenceSchedulerResourceCoordinator requestPixelBufferPoolForFormat:size:];
-[BWInferenceSchedulerResourceCoordinator requestPixelBufferPoolForRequirement:size:];
```
