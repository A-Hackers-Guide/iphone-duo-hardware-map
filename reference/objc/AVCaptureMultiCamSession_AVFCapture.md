# `AVCaptureMultiCamSession`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureSession`
- 2 instance variables, 2 properties, 19 instance methods, 1 class methods

## Instance variables

```
f _hardwareCost;
f _systemPressureCost;
```

## Properties

```
@property (Tf,R,N) hardwareCost;
@property (Tf,R,N) systemPressureCost;
```

## Class methods

```
+[AVCaptureMultiCamSession isMultiCamSupported];
```

## Instance methods

```
-[AVCaptureMultiCamSession _removeConnection:];
-[AVCaptureMultiCamSession _physicalDevicePowerInfoSet];
-[AVCaptureMultiCamSession observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureMultiCamSession init];
-[AVCaptureMultiCamSession _canAddOutput:failureReason:];
-[AVCaptureMultiCamSession dealloc];
-[AVCaptureMultiCamSession systemPressureCost];
-[AVCaptureMultiCamSession _addConnection:exceptionReason:];
-[AVCaptureMultiCamSession hardwareCost];
-[AVCaptureMultiCamSession _canAddConnection:failureReason:];
-[AVCaptureMultiCamSession _updateCosts];
-[AVCaptureMultiCamSession _updateHardwareCost];
-[AVCaptureMultiCamSession handleVideoInputDevice:activeFormatChanged:];
-[AVCaptureMultiCamSession _canAddInput:failureReason:];
-[AVCaptureMultiCamSession _updateSystemPressureCost];
-[AVCaptureMultiCamSession _requireMultiCamSupportedFormatsForVideoDevices];
-[AVCaptureMultiCamSession startRunning];
-[AVCaptureMultiCamSession _computeISPHardwareCost];
-[AVCaptureMultiCamSession canSetSessionPreset:];
```
