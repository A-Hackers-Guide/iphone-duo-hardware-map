# `CAMDisabledModeOverlayView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _disabledModeReason;
q _orientation;
@"UILabel" __messageLabel;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _viewportFrame;
```

## Properties

```
@property (T@"UILabel",R,N,V__messageLabel) _messageLabel;
@property (Tq,N,V_disabledModeReason) disabledModeReason;
@property (Tq,N,V_orientation) orientation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewportFrame) viewportFrame;
```

## Instance methods

```
-[CAMDisabledModeOverlayView viewportFrame];
-[CAMDisabledModeOverlayView setOrientation:animated:];
-[CAMDisabledModeOverlayView setOrientation:];
-[CAMDisabledModeOverlayView orientation];
-[CAMDisabledModeOverlayView layoutSubviews];
-[CAMDisabledModeOverlayView _updateText];
-[CAMDisabledModeOverlayView setViewportFrame:];
-[CAMDisabledModeOverlayView initWithFrame:];
-[CAMDisabledModeOverlayView _messageLabel];
-[CAMDisabledModeOverlayView _frameForMessageLabel];
-[CAMDisabledModeOverlayView disabledModeReason];
-[CAMDisabledModeOverlayView setDisabledModeReason:];
```
