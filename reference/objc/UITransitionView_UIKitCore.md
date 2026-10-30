# `UITransitionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `NSCoding`
- 12 instance variables, 4 properties, 45 instance methods, 1 class methods

## Instance variables

```
@"UIView" _fromView;
@"UIView" _toView;
@"NSMutableArray" _frozenSubviews;
@"UIResponder" _firstResponderToRemember;
@ _delegate;
@"UIWindow" _originalWindow;
{?="animationInProgress"b1"ignoresInteractionEvents"b1"shouldNotifyDidCompleteImmediately"b1"useViewControllerAppearanceCallbacks"b1"shouldRestoreFromViewAlpha"b1"shouldRestoreGroupOpacity"b1"groupOpacityToRestoreForFromView"b1"groupOpacityToRestoreForToView"b1"shouldRasterize"b1"enableRotationAfterTransition"b1"removeFromView"b1} _transitionViewFlags;
d _curlUpRevealedHeight;
i _textEffectsVisibilityLevel;
Q _transitionID;
B _ignoreDirectTouchEvents;
q _animationTimingCurve;
```

## Properties

```
@property (Td,R,N) _curlUpRevealedHeight;
@property (TB,N) shouldNotifyDidCompleteImmediately;
@property (Tq,N,V_animationTimingCurve) animationTimingCurve;
@property (TB,N,V_ignoreDirectTouchEvents) ignoreDirectTouchEvents;
```

## Class methods

```
+[UITransitionView defaultDurationForTransition:];
```

## Instance methods

```
-[UITransitionView _traitCollectionForChildEnvironment:];
-[UITransitionView didMoveToWindow];
-[UITransitionView willMoveToSuperview:];
-[UITransitionView isTransitioning];
-[UITransitionView _didCompleteTransition:];
-[UITransitionView layoutSubviews];
-[UITransitionView hitTest:withEvent:];
-[UITransitionView toView];
-[UITransitionView _viewDidMoveFromScreen:toScreen:];
-[UITransitionView setBounds:];
-[UITransitionView durationForTransition:];
-[UITransitionView setDelegate:];
-[UITransitionView safeAreaInsetsDidChange];
-[UITransitionView encodeWithCoder:];
-[UITransitionView fromView];
-[UITransitionView delegate];
-[UITransitionView setFrame:];
-[UITransitionView initWithCoder:];
-[UITransitionView traitCollectionDidChange:];
-[UITransitionView _shouldAnimatePropertyWithKey:];
-[UITransitionView _sceneRegionsDidChange];
-[UITransitionView initWithFrame:];
-[UITransitionView textEffectsVisibilityLevel];
-[UITransitionView _completeRunningTransition];
-[UITransitionView _curlUpRevealedHeight];
-[UITransitionView _didStartTransition];
-[UITransitionView _isTransitioningFromFromView:];
-[UITransitionView _sceneSafeAreaAlignedEdgesDidChange];
-[UITransitionView _shouldDisableGroupOpacityOnAlphaTransitions];
-[UITransitionView _startTransition:withDuration:];
-[UITransitionView _transitionDidStopFinished:];
-[UITransitionView animationTimingCurve];
-[UITransitionView ignoreDirectTouchEvents];
-[UITransitionView ignoresInteractionEvents];
-[UITransitionView notifyDidCompleteTransition:];
-[UITransitionView rasterizesOnTransition];
-[UITransitionView setAnimationTimingCurve:];
-[UITransitionView setIgnoreDirectTouchEvents:];
-[UITransitionView setIgnoresInteractionEvents:];
-[UITransitionView setRasterizesOnTransition:];
-[UITransitionView setShouldNotifyDidCompleteImmediately:];
-[UITransitionView shouldNotifyDidCompleteImmediately];
-[UITransitionView transition:fromView:toView:];
-[UITransitionView transition:fromView:toView:removeFromView:];
-[UITransitionView transition:toView:];
```
