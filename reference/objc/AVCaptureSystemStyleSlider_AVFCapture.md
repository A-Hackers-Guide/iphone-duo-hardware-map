# `AVCaptureSystemStyleSlider`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 8 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _sessionReference;
@? _action;
q _parameter;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"CAMOverlayServiceSlider" _overlayControl;
B _observing;
B _changeSmartStyleInProcess;
B _smartStyleHasChanged;
```

## Class methods

```
+[AVCaptureSystemStyleSlider initialize];
```

## Instance methods

```
-[AVCaptureSystemStyleSlider observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureSystemStyleSlider initWithSession:parameter:action:];
-[AVCaptureSystemStyleSlider installObservers];
-[AVCaptureSystemStyleSlider actionQueue];
-[AVCaptureSystemStyleSlider dealloc];
-[AVCaptureSystemStyleSlider enqueueActionWithUpdate:];
-[AVCaptureSystemStyleSlider initWithSession:parameter:];
-[AVCaptureSystemStyleSlider overlayUpdate];
-[AVCaptureSystemStyleSlider removeObservers];
-[AVCaptureSystemStyleSlider overlayControl];
-[AVCaptureSystemStyleSlider overlayVisibilityDidChange:];
```
