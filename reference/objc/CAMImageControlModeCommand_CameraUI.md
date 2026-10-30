# `CAMImageControlModeCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
B __capturing;
q __captureMode;
```

## Properties

```
@property (Tq,R,N,V__captureMode) _captureMode;
@property (TB,R,N,V__capturing) _capturing;
```

## Instance methods

```
-[CAMImageControlModeCommand _captureMode];
-[CAMImageControlModeCommand executeWithContext:];
-[CAMImageControlModeCommand copyWithZone:];
-[CAMImageControlModeCommand _applyImageControlMode:toDevice:];
-[CAMImageControlModeCommand _applyImageControlModeWithPreviewMode:captureMode:fallbackMode:toDevice:];
-[CAMImageControlModeCommand _capturing];
-[CAMImageControlModeCommand initWithCaptureMode:capturing:];
```
