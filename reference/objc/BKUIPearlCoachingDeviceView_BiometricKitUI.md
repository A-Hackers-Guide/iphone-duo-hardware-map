# `BKUIPearlCoachingDeviceView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 10 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _isDisplayZoomEnabled;
B _animationRunning;
B _inSheet;
q _orientation;
@"UIImage" _deviceImage;
@"UIImageView" _deviceView;
@"BKUIRotationArrowAnimationLayer" _animationLayer;
@"NSLayoutConstraint" _heightConstraint;
@"NSLayoutConstraint" _widthConstraint;
@"<UITraitChangeRegistration>" _traitChangeRegistration;
```

## Properties

```
@property (T@"UIImage",&,N,V_deviceImage) deviceImage;
@property (T@"UIImageView",&,N,V_deviceView) deviceView;
@property (T@"BKUIRotationArrowAnimationLayer",&,N,V_animationLayer) animationLayer;
@property (TB,N,V_animationRunning) animationRunning;
@property (TB,N,V_inSheet) inSheet;
@property (T@"NSLayoutConstraint",&,N,V_heightConstraint) heightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_widthConstraint) widthConstraint;
@property (T@"<UITraitChangeRegistration>",&,N,V_traitChangeRegistration) traitChangeRegistration;
@property (Tq,R,N,V_orientation) orientation;
@property (TB,N,V_isDisplayZoomEnabled) isDisplayZoomEnabled;
```

## Instance methods

```
-[BKUIPearlCoachingDeviceView setHeightConstraint:];
-[BKUIPearlCoachingDeviceView heightConstraint];
-[BKUIPearlCoachingDeviceView setOrientation:];
-[BKUIPearlCoachingDeviceView startAnimation];
-[BKUIPearlCoachingDeviceView orientation];
-[BKUIPearlCoachingDeviceView layoutSubviews];
-[BKUIPearlCoachingDeviceView widthConstraint];
-[BKUIPearlCoachingDeviceView setWidthConstraint:];
-[BKUIPearlCoachingDeviceView stopAnimation];
-[BKUIPearlCoachingDeviceView animationLayer];
-[BKUIPearlCoachingDeviceView setAnimationLayer:];
-[BKUIPearlCoachingDeviceView setTraitChangeRegistration:];
-[BKUIPearlCoachingDeviceView traitChangeRegistration];
-[BKUIPearlCoachingDeviceView setDeviceImage:];
-[BKUIPearlCoachingDeviceView deviceImage];
-[BKUIPearlCoachingDeviceView inSheet];
-[BKUIPearlCoachingDeviceView _colorForStroke];
-[BKUIPearlCoachingDeviceView animationRunning];
-[BKUIPearlCoachingDeviceView deviceView];
-[BKUIPearlCoachingDeviceView initWithSheetLayout:];
-[BKUIPearlCoachingDeviceView isDisplayZoomEnabled];
-[BKUIPearlCoachingDeviceView resetDevice];
-[BKUIPearlCoachingDeviceView rotateDeviceToAngle:animated:completion:];
-[BKUIPearlCoachingDeviceView setAnimationRunning:];
-[BKUIPearlCoachingDeviceView setDeviceHidden:animated:completion:];
-[BKUIPearlCoachingDeviceView setDeviceView:];
-[BKUIPearlCoachingDeviceView setInSheet:];
-[BKUIPearlCoachingDeviceView setIsDisplayZoomEnabled:];
```
