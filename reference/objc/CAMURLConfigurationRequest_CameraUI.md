# `CAMURLConfigurationRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _isSiriContinuation;
B _shouldOpenControlPanel;
q _requestedCaptureMode;
q _requestedCaptureDevice;
```

## Properties

```
@property (Tq,R,N,V_requestedCaptureMode) requestedCaptureMode;
@property (Tq,R,N,V_requestedCaptureDevice) requestedCaptureDevice;
@property (TB,R,N,V_isSiriContinuation) isSiriContinuation;
@property (TB,R,N,V_shouldOpenControlPanel) shouldOpenControlPanel;
```

## Instance methods

```
-[CAMURLConfigurationRequest _initializeFromQueryDictionary:];
-[CAMURLConfigurationRequest _captureDeviceFromString:outCaptureDevice:];
-[CAMURLConfigurationRequest _captureModeFromString:outCaptureMode:];
-[CAMURLConfigurationRequest initWithQueryDictionary:];
-[CAMURLConfigurationRequest isSiriContinuation];
-[CAMURLConfigurationRequest requestedCaptureDevice];
-[CAMURLConfigurationRequest requestedCaptureMode];
-[CAMURLConfigurationRequest shouldOpenControlPanel];
```
