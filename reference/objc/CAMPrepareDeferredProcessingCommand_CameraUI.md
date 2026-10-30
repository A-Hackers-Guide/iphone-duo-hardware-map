# `CAMPrepareDeferredProcessingCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"CAMStillImageCaptureRequest" __request;
@"PLCameraDeferredProcessingCoordinator" __deferredProcessingCoordinator;
```

## Properties

```
@property (T@"CAMStillImageCaptureRequest",R,N,V__request) _request;
@property (T@"PLCameraDeferredProcessingCoordinator",R,N,V__deferredProcessingCoordinator) _deferredProcessingCoordinator;
```

## Class methods

```
+[CAMPrepareDeferredProcessingCommand _prewarmQueue];
```

## Instance methods

```
-[CAMPrepareDeferredProcessingCommand executeWithContext:];
-[CAMPrepareDeferredProcessingCommand copyWithZone:];
-[CAMPrepareDeferredProcessingCommand _deferredProcessingCoordinator];
-[CAMPrepareDeferredProcessingCommand _request];
-[CAMPrepareDeferredProcessingCommand initWithRequest:coordinator:];
```
