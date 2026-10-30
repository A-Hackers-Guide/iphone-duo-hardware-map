# `CAMTimerIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 10 properties, 41 instance methods, 0 class methods

## Instance variables

```
B __performingStyleAnimation;
q _style;
q _remainingTicks;
@"UIView" __dimmingView;
@"UILabel" __countdownLabel;
q __startingTicks;
q __labelOrientation;
@"CAMAnimationDelegate" __animationDelegate;
q __deferredLabelOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _labelBounds;
```

## Properties

```
@property (T@"UIView",R,N,V__dimmingView) _dimmingView;
@property (T@"UILabel",R,N,V__countdownLabel) _countdownLabel;
@property (Tq,R,N,V__startingTicks) _startingTicks;
@property (Tq,N,S_setLabelOrientation:,V__labelOrientation) _labelOrientation;
@property (T@"CAMAnimationDelegate",R,N,V__animationDelegate) _animationDelegate;
@property (TB,N,G_isPerformingStyleAnimation,S_setPerformingStyleAnimation:,V__performingStyleAnimation) _performingStyleAnimation;
@property (Tq,N,S_setDeferredOrientation:,V__deferredLabelOrientation) _deferredLabelOrientation;
@property (Tq,N,V_style) style;
@property (Tq,R,N,V_remainingTicks) remainingTicks;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_labelBounds) labelBounds;
```

## Instance methods

```
-[CAMTimerIndicatorView setOrientation:animated:];
-[CAMTimerIndicatorView _labelOrientation];
-[CAMTimerIndicatorView _setPerformingStyleAnimation:];
-[CAMTimerIndicatorView startCountdownWithAnimationDelegate:];
-[CAMTimerIndicatorView _setLabelOrientation:];
-[CAMTimerIndicatorView _deferredLabelOrientation];
-[CAMTimerIndicatorView setStyle:animated:];
-[CAMTimerIndicatorView _layoutCountdownLabelForLargeStyle];
-[CAMTimerIndicatorView _updateCountdownLabelWithTicksRemaining:];
-[CAMTimerIndicatorView _commonCAMTimerIndicatorViewInitialization];
-[CAMTimerIndicatorView stopCountdown];
-[CAMTimerIndicatorView _finalDimmingAnimation];
-[CAMTimerIndicatorView remainingTicks];
-[CAMTimerIndicatorView layoutSubviews];
-[CAMTimerIndicatorView style];
-[CAMTimerIndicatorView _landscapeSwapBoundsCoordinates:];
-[CAMTimerIndicatorView setStyle:];
-[CAMTimerIndicatorView _layoutCountdownLabelForSmallStyle];
-[CAMTimerIndicatorView _transitionDimmingViewFromStyle:];
-[CAMTimerIndicatorView _countdownLabel];
-[CAMTimerIndicatorView _isPerformingStyleAnimation];
-[CAMTimerIndicatorView _handleOrientationChange:];
-[CAMTimerIndicatorView labelBounds];
-[CAMTimerIndicatorView _setDeferredOrientation:];
-[CAMTimerIndicatorView _addDecrementAnimationForTick:];
-[CAMTimerIndicatorView _layoutCountdownLabelForStyle:];
-[CAMTimerIndicatorView _addDimmingAnimationForTick:];
-[CAMTimerIndicatorView initWithCoder:];
-[CAMTimerIndicatorView decrement];
-[CAMTimerIndicatorView _decrementAnimationForTick:];
-[CAMTimerIndicatorView font];
-[CAMTimerIndicatorView _fontForStyle:];
-[CAMTimerIndicatorView _dimmingView];
-[CAMTimerIndicatorView setLabelBounds:];
-[CAMTimerIndicatorView _startingTicks];
-[CAMTimerIndicatorView _animationDelegate];
-[CAMTimerIndicatorView _updateFromChangeToStyle:animated:];
-[CAMTimerIndicatorView initWithFrame:];
-[CAMTimerIndicatorView _dimmingAnimationForTick:];
-[CAMTimerIndicatorView resetWithNumberOfTicks:showBeforeAnimationStarts:];
-[CAMTimerIndicatorView setFont:];
```
