# `UIViewControllerBuiltinTransitionViewAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerAnimatedTransitioning_Internal`
- 6 instance variables, 14 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<UIViewControllerContextTransitioning>" _transitionContext;
B _removeFromView;
i _transition;
@ _delegate;
@"UIView" _toView;
@"UIView" _fromView;
```

## Properties

```
@property (T@,W,N,V_delegate) delegate;
@property (T@"UIView",W,N,V_toView) toView;
@property (T@"UIView",W,N,V_fromView) fromView;
@property (TB,N,V_removeFromView) removeFromView;
@property (Ti,N,V_transition) transition;
@property (Tq,?,R,N) _navigationBarTransitionVariant;
@property (T@"UIView",?,R,N) _navigationBarTransitionOverlay;
@property (TB,?,R,N) _shouldCrossFadeNavigationBarVisibility;
@property (TB,?,R,N) _shouldCrossFadeBottomBars;
@property (TB,?,R,N) _shouldAnimateBottomBarVisibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIViewControllerBuiltinTransitionViewAnimator transition];
-[UIViewControllerBuiltinTransitionViewAnimator removeFromView];
-[UIViewControllerBuiltinTransitionViewAnimator animateTransition:];
-[UIViewControllerBuiltinTransitionViewAnimator setToView:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionDuration:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionViewShouldUseViewControllerCallbacks];
-[UIViewControllerBuiltinTransitionViewAnimator _prepareKeyboardForTransition:fromView:];
-[UIViewControllerBuiltinTransitionViewAnimator setRemoveFromView:];
-[UIViewControllerBuiltinTransitionViewAnimator initWithTransition:];
-[UIViewControllerBuiltinTransitionViewAnimator toView];
-[UIViewControllerBuiltinTransitionViewAnimator transitionView:endOriginForToView:forTransition:defaultOrigin:];
-[UIViewControllerBuiltinTransitionViewAnimator durationForTransition:];
-[UIViewControllerBuiltinTransitionViewAnimator setDelegate:];
-[UIViewControllerBuiltinTransitionViewAnimator _adjustOrigin:givenOtherOrigin:forTransition:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionView:endOriginForFromView:forTransition:defaultOrigin:];
-[UIViewControllerBuiltinTransitionViewAnimator fromView];
-[UIViewControllerBuiltinTransitionViewAnimator delegate];
-[UIViewControllerBuiltinTransitionViewAnimator setFromView:];
-[UIViewControllerBuiltinTransitionViewAnimator _animationWillEnd:didComplete:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionView:beginOriginForToView:forTransition:defaultOrigin:];
-[UIViewControllerBuiltinTransitionViewAnimator setTransition:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionViewDidStart:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionView:startCustomTransitionWithDuration:];
-[UIViewControllerBuiltinTransitionViewAnimator transitionViewDidComplete:fromView:toView:removeFromView:];
```
