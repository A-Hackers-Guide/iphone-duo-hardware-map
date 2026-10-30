# `AVCaptureControlsOverlay`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayServiceConnectionClient`
- 8 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _sessionReference;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"CAMOverlayServiceConnection" _connection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _controlsLock;
@"NSDictionary" _itemsByIdentifier;
@"NSArray" _orderedIdentifiers;
B _visible;
@"NSString" _activeControlIdentifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureControlsOverlay initialize];
```

## Instance methods

```
-[AVCaptureControlsOverlay dealloc];
-[AVCaptureControlsOverlay invalidate];
-[AVCaptureControlsOverlay activate];
-[AVCaptureControlsOverlay initWithSession:];
-[AVCaptureControlsOverlay rebuildControls];
-[AVCaptureControlsOverlay updateControls:];
-[AVCaptureControlsOverlay _activateIsolated];
-[AVCaptureControlsOverlay _invalidateIsolated];
-[AVCaptureControlsOverlay _sendControlsIsolated];
-[AVCaptureControlsOverlay _updateControlIsolated:];
-[AVCaptureControlsOverlay cameraOverlayConnection:didApplyControlUpdate:];
-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeActiveControlIdentifier:];
-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeFocusLocked:];
-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeInterfaceReduced:];
-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeOverlayVisible:activeControlIdentifier:];
-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeStatus:];
-[AVCaptureControlsOverlay updateControl:];
```
