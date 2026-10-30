# `AVCaptureSystemExposureBiasSlider`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 6 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureDevice" _device;
@? _action;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"CAMOverlayServiceSlider" _overlayControl;
B _observing;
B _changeExposureBiasInProcess;
```

## Instance methods

```
-[AVCaptureSystemExposureBiasSlider initWithDevice:];
-[AVCaptureSystemExposureBiasSlider observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureSystemExposureBiasSlider device];
-[AVCaptureSystemExposureBiasSlider installObservers];
-[AVCaptureSystemExposureBiasSlider actionQueue];
-[AVCaptureSystemExposureBiasSlider dealloc];
-[AVCaptureSystemExposureBiasSlider enqueueActionWithUpdate:];
-[AVCaptureSystemExposureBiasSlider overlayUpdate];
-[AVCaptureSystemExposureBiasSlider removeObservers];
-[AVCaptureSystemExposureBiasSlider description];
-[AVCaptureSystemExposureBiasSlider initWithDevice:action:];
-[AVCaptureSystemExposureBiasSlider overlayControl];
```
