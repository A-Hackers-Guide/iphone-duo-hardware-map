# `AVCaptureSystemZoomSlider`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 8 instance variables, 0 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureDevice" _device;
@? _action;
d _maxVideoZoomFactor;
@"NSDictionary" _displayValuesByZoomFactorValue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"CAMOverlayServiceSlider" _overlayControl;
B _observingDeviceVideoZoomFactor;
B _changeZoomInProcess;
```

## Class methods

```
+[AVCaptureSystemZoomSlider initialize];
```

## Instance methods

```
-[AVCaptureSystemZoomSlider initWithDevice:];
-[AVCaptureSystemZoomSlider observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureSystemZoomSlider device];
-[AVCaptureSystemZoomSlider installObservers];
-[AVCaptureSystemZoomSlider actionQueue];
-[AVCaptureSystemZoomSlider dealloc];
-[AVCaptureSystemZoomSlider enqueueActionWithUpdate:];
-[AVCaptureSystemZoomSlider setDisplayValuesByZoomFactorValue:];
-[AVCaptureSystemZoomSlider _initWithDevice:action:];
-[AVCaptureSystemZoomSlider _rebuildOverlayControlIfNecessary];
-[AVCaptureSystemZoomSlider overlayUpdate];
-[AVCaptureSystemZoomSlider removeObservers];
-[AVCaptureSystemZoomSlider setMaxVideoZoomFactor:];
-[AVCaptureSystemZoomSlider displayValuesByZoomFactorValue];
-[AVCaptureSystemZoomSlider description];
-[AVCaptureSystemZoomSlider maxVideoZoomFactor];
-[AVCaptureSystemZoomSlider initWithDevice:action:];
-[AVCaptureSystemZoomSlider overlayControl];
```
