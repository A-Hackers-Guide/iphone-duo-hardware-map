# `AVCaptureSystemLensSelector`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 8 instance variables, 3 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureDevice" _device;
@? _action;
@"NSDictionary" _displayValuesByZoomFactorValue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"CAMOverlayServiceSlider" _overlayControl;
B _observing;
B _changesVideoZoomFactor;
@"NSObject<OS_dispatch_queue>" _actionQueue;
```

## Properties

```
@property (TB,N) changesVideoZoomFactor;
@property (TB,N) pickerChangesVideoZoomFactor;
@property (T@"NSDictionary",C,N) displayValuesByZoomFactorValue;
```

## Class methods

```
+[AVCaptureSystemLensSelector initialize];
```

## Instance methods

```
-[AVCaptureSystemLensSelector initWithDevice:];
-[AVCaptureSystemLensSelector observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureSystemLensSelector device];
-[AVCaptureSystemLensSelector installObservers];
-[AVCaptureSystemLensSelector pickerChangesVideoZoomFactor];
-[AVCaptureSystemLensSelector actionQueue];
-[AVCaptureSystemLensSelector dealloc];
-[AVCaptureSystemLensSelector enqueueActionWithUpdate:];
-[AVCaptureSystemLensSelector setDisplayValuesByZoomFactorValue:];
-[AVCaptureSystemLensSelector _initWithDevice:action:];
-[AVCaptureSystemLensSelector overlayUpdate];
-[AVCaptureSystemLensSelector setChangesVideoZoomFactor:];
-[AVCaptureSystemLensSelector removeObservers];
-[AVCaptureSystemLensSelector displayValuesByZoomFactorValue];
-[AVCaptureSystemLensSelector description];
-[AVCaptureSystemLensSelector initWithDevice:action:];
-[AVCaptureSystemLensSelector setPickerChangesVideoZoomFactor:];
-[AVCaptureSystemLensSelector overlayControl];
-[AVCaptureSystemLensSelector changesVideoZoomFactor];
-[AVCaptureSystemLensSelector _overlayUpdateWithVideoZoomFactor:];
```
