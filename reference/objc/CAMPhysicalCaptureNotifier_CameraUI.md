# `CAMPhysicalCaptureNotifier`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _enabled;
B _includesVolumeButtons;
@"<CAMPhysicalCaptureNotifierDelegate>" _delegate;
q _volumeUpButtonState;
q _volumeDownButtonState;
q _cameraCaseButtonState;
q _state;
@"UIView" __view;
@"<BSInvalidatable>" __cameraButtonRequest;
```

## Properties

```
@property (Tq,N,S_setState:,V_state) state;
@property (Tq,N,S_setVolumeUpButtonState:,V_volumeUpButtonState) volumeUpButtonState;
@property (Tq,N,S_setVolumeDownButtonState:,V_volumeDownButtonState) volumeDownButtonState;
@property (Tq,N,S_setCameraCaseButtonState:,V_cameraCaseButtonState) cameraCaseButtonState;
@property (T@"UIView",R,N,V__view) _view;
@property (T@"<BSInvalidatable>",&,N,V__cameraButtonRequest) _cameraButtonRequest;
@property (T@"<CAMPhysicalCaptureNotifierDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,R,N,V_includesVolumeButtons) includesVolumeButtons;
```

## Instance methods

```
-[CAMPhysicalCaptureNotifier _view];
-[CAMPhysicalCaptureNotifier _setState:];
-[CAMPhysicalCaptureNotifier dealloc];
-[CAMPhysicalCaptureNotifier isEnabled];
-[CAMPhysicalCaptureNotifier setDelegate:];
-[CAMPhysicalCaptureNotifier setEnabled:];
-[CAMPhysicalCaptureNotifier delegate];
-[CAMPhysicalCaptureNotifier state];
-[CAMPhysicalCaptureNotifier _cameraButtonRequest];
-[CAMPhysicalCaptureNotifier _handleVolumeDownButtonDownNotification:];
-[CAMPhysicalCaptureNotifier _handleVolumeDownButtonUpNotification:];
-[CAMPhysicalCaptureNotifier _handleVolumeUpButtonDownNotification:];
-[CAMPhysicalCaptureNotifier _handleVolumeUpButtonUpNotification:];
-[CAMPhysicalCaptureNotifier _setVolumeDownButtonState:];
-[CAMPhysicalCaptureNotifier _setVolumeUpButtonState:];
-[CAMPhysicalCaptureNotifier _updateCaptureButtonNotifications];
-[CAMPhysicalCaptureNotifier set_cameraButtonRequest:];
-[CAMPhysicalCaptureNotifier _handleCameraCaseButtonDownNotification:];
-[CAMPhysicalCaptureNotifier _handleCameraCaseButtonUpNotification:];
-[CAMPhysicalCaptureNotifier _setCameraCaseButtonState:];
-[CAMPhysicalCaptureNotifier _setCameraCaseShutterState:];
-[CAMPhysicalCaptureNotifier _updateStateAndNotifyDelegateIfNeededForButton:];
-[CAMPhysicalCaptureNotifier cameraCaseButtonState];
-[CAMPhysicalCaptureNotifier includesVolumeButtons];
-[CAMPhysicalCaptureNotifier initWithView:includeVolumeButtons:];
-[CAMPhysicalCaptureNotifier volumeDownButtonState];
-[CAMPhysicalCaptureNotifier volumeUpButtonState];
```
