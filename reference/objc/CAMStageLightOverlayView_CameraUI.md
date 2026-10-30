# `CAMStageLightOverlayView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 11 instance variables, 11 properties, 26 instance methods, 3 class methods

## Instance variables

```
B _active;
B _visible;
q _orientation;
d _bottomContentInset;
@"UIView" __tintView;
@"UIImageView" __vignetteView;
@"CAShapeLayer" __circleLayer;
Q __activeTimerID;
@"CAGradientLayer" __gradientLayer;
@"CAMStageLightAnimator" __animator;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _viewportFrame;
```

## Properties

```
@property (T@"UIView",R,N,V__tintView) _tintView;
@property (T@"UIImageView",R,N,V__vignetteView) _vignetteView;
@property (T@"CAShapeLayer",R,N,V__circleLayer) _circleLayer;
@property (TQ,N,S_setActiveTimerID:,V__activeTimerID) _activeTimerID;
@property (T@"CAGradientLayer",R,N,V__gradientLayer) _gradientLayer;
@property (T@"CAMStageLightAnimator",&,N,S_setAnimator:,V__animator) _animator;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,GisVisible,V_visible) visible;
@property (Tq,N,V_orientation) orientation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewportFrame) viewportFrame;
@property (Td,N,V_bottomContentInset) bottomContentInset;
```

## Class methods

```
+[CAMStageLightOverlayView _useLargeLayoutForViewportSize:];
+[CAMStageLightOverlayView _circleDiameterForViewportSize:orientation:screenScale:];
+[CAMStageLightOverlayView circleFrameForViewport:orientation:bottomContentInset:screenScale:];
```

## Instance methods

```
-[CAMStageLightOverlayView viewportFrame];
-[CAMStageLightOverlayView setOrientation:animated:];
-[CAMStageLightOverlayView setOrientation:];
-[CAMStageLightOverlayView _circleLayer];
-[CAMStageLightOverlayView setVisible:];
-[CAMStageLightOverlayView setBottomContentInset:];
-[CAMStageLightOverlayView orientation];
-[CAMStageLightOverlayView _animator];
-[CAMStageLightOverlayView isVisible];
-[CAMStageLightOverlayView layoutSubviews];
-[CAMStageLightOverlayView setActive:];
-[CAMStageLightOverlayView setViewportFrame:];
-[CAMStageLightOverlayView bottomContentInset];
-[CAMStageLightOverlayView _setAnimator:];
-[CAMStageLightOverlayView isActive];
-[CAMStageLightOverlayView initWithFrame:];
-[CAMStageLightOverlayView _gradientLayer];
-[CAMStageLightOverlayView setActive:animated:];
-[CAMStageLightOverlayView setVisible:animated:];
-[CAMStageLightOverlayView _tintView];
-[CAMStageLightOverlayView _activeTimerID];
-[CAMStageLightOverlayView _circleFrameForOrientation:];
-[CAMStageLightOverlayView _setActiveTimerID:];
-[CAMStageLightOverlayView _updateAnimatorState];
-[CAMStageLightOverlayView _updateShadowViewsAnimated:];
-[CAMStageLightOverlayView _vignetteView];
```
