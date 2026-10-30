# `AVCaptureControl`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _enabled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSString" _identifier;
@"AVWeakReference" _overlayReference;
@"AVWeakReference" _sessionReference;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"AVCaptureControlsOverlay",W,N) overlay;
@property (T@"NSObject<OS_dispatch_queue>",R,N) actionQueue;
@property (T@"AVCaptureSession",W,N) session;
@property (T@"AVCaptureDevice",R,N) device;
@property (T@"CAMAbstractOverlayServiceControl",R,N) overlayControl;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Instance methods

```
-[AVCaptureControl setOverlay:];
-[AVCaptureControl identifier];
-[AVCaptureControl device];
-[AVCaptureControl installObservers];
-[AVCaptureControl actionQueue];
-[AVCaptureControl dealloc];
-[AVCaptureControl enqueueActionWithUpdate:];
-[AVCaptureControl isEnabled];
-[AVCaptureControl setSession:];
-[AVCaptureControl overlay];
-[AVCaptureControl setEnabled:];
-[AVCaptureControl overlayUpdate];
-[AVCaptureControl removeObservers];
-[AVCaptureControl overlayControl];
-[AVCaptureControl session];
-[AVCaptureControl overlayVisibilityDidChange:];
-[AVCaptureControl _enabledUpdateWithEnabled:];
-[AVCaptureControl enabledUpdate];
-[AVCaptureControl initSubclass];
-[AVCaptureControl overlayDidMakeControlActive:];
```
