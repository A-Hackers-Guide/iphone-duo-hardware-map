# `_UIFocusRotaryIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _visible;
d _wheelPosition;
Q _activeAxis;
Q _failedMovementHeading;
@"UIView" _ringView;
@"UIView" _fingerPositionContainerView;
@"UIView" _fingerPositionView;
@"UIView" _roundPointerView;
@"UIView" _rotaryScrubCenterPunchout;
@"UIViewPropertyAnimator" _rotaryScrubHideAnimator;
@"UIViewPropertyAnimator" _rotaryScrubUnhideAnimator;
@"UIViewPropertyAnimator" _rotaryScrubBackwardsFingerPositionAnimator;
@"_UIFocusRotaryRingArrowView" _upArrow;
@"_UIFocusRotaryRingArrowView" _rightArrow;
@"_UIFocusRotaryRingArrowView" _downArrow;
@"_UIFocusRotaryRingArrowView" _leftArrow;
```

## Class methods

```
+[_UIFocusRotaryIndicatorView createRotaryIndicatorInView:];
```

## Instance methods

```
-[_UIFocusRotaryIndicatorView didMoveToWindow];
-[_UIFocusRotaryIndicatorView dealloc];
-[_UIFocusRotaryIndicatorView layoutSubviews];
-[_UIFocusRotaryIndicatorView initWithFrame:];
-[_UIFocusRotaryIndicatorView _calculateCurrentRotaryAxis];
-[_UIFocusRotaryIndicatorView _transformForWheelPosition:];
-[_UIFocusRotaryIndicatorView _updateArrowDisplay];
-[_UIFocusRotaryIndicatorView _updateArrowsForCurrentFocus];
-[_UIFocusRotaryIndicatorView showArrowsForAxis:];
-[_UIFocusRotaryIndicatorView toggleVisible:animated:];
-[_UIFocusRotaryIndicatorView updateFailedMovementHeading:];
-[_UIFocusRotaryIndicatorView updateWheelPosition:];
```
