# `CAMStageLightAnimator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"CAGradientLayer" _gradientLayer;
@"CAShapeLayer" _circleLayer;
Q _state;
Q __appearingAnimationCount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _circleBaseFrame;
```

## Properties

```
@property (TQ,N,S_setAppearingAnimationCount:,V__appearingAnimationCount) _appearingAnimationCount;
@property (TB,R,N,G_isAppearing) _appearing;
@property (T@"CAGradientLayer",R,N,V_gradientLayer) gradientLayer;
@property (T@"CAShapeLayer",R,N,V_circleLayer) circleLayer;
@property (TQ,N,V_state) state;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_circleBaseFrame) circleBaseFrame;
```

## Instance methods

```
-[CAMStageLightAnimator setState:];
-[CAMStageLightAnimator gradientLayer];
-[CAMStageLightAnimator state];
-[CAMStageLightAnimator circleBaseFrame];
-[CAMStageLightAnimator _gradientPropertiesForGeometry:];
-[CAMStageLightAnimator _animateAppearing];
-[CAMStageLightAnimator _animateBounceIfNeeded];
-[CAMStageLightAnimator _animateCircleColorWithDuration:timing:];
-[CAMStageLightAnimator _animateCircleFromGeometry:toGeometry:duration:timing:repeats:completion:];
-[CAMStageLightAnimator _animateCircleGeometry:count:duration:timing:repeats:completion:];
-[CAMStageLightAnimator _animateCircleToGeometry:duration:timing:completion:];
-[CAMStageLightAnimator _animateGradientFromProperties:toProperties:duration:timing:repeats:];
-[CAMStageLightAnimator _animateGradientProperties:count:duration:timing:repeats:];
-[CAMStageLightAnimator _animateGradientToProperties:duration:timing:];
-[CAMStageLightAnimator _animateHidden];
-[CAMStageLightAnimator _animateSearchingIfNeededFromState:];
-[CAMStageLightAnimator _appearingAnimationCount];
-[CAMStageLightAnimator _circleGeometryForState:];
-[CAMStageLightAnimator _circleLineWidth];
-[CAMStageLightAnimator _currentCircleGeometry];
-[CAMStageLightAnimator _currentGradientProperties];
-[CAMStageLightAnimator _didFinishAppearing];
-[CAMStageLightAnimator _gradientGeometryForState:];
-[CAMStageLightAnimator _isAppearing];
-[CAMStageLightAnimator _setAppearingAnimationCount:];
-[CAMStageLightAnimator circleLayer];
-[CAMStageLightAnimator initWithGradientLayer:circleLayer:];
-[CAMStageLightAnimator setCircleBaseFrame:];
-[CAMStageLightAnimator setCircleBaseFrame:animated:];
```
