# `_UIZoomTransitionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerPreemptableAnimatedTransitioning`, `UIViewControllerAnimatedTransitioning`, `UIViewControllerInteractiveTransitioning`, `UIViewControllerAnimatedTransitioning_Internal`, `_UIDismissInteractionDelegate`, `UIViewControllerAnimatedTransitioning_Keyboard`
- 21 instance variables, 12 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"_UIZoomViewControllerTransition" clientTransition;
B isZoomingIn;
? owningViewController;
@"_UIDismissInteraction" dismissInteraction;
activeTransitionContext;
isForNavigation;
animator;
dimmingView;
foregroundView;
backgroundView;
viewToScaleBack;
isPreempting;
shimPropertyAnimator;
shimAnimationView;
transitionOverlayView;
fallbackSourceView;
@"_UIViewAlphaOverrideAssertion" sourceViewHidingAssertion;
showcasePortal;
toolbarTransitionController;
style;
behaviors;
```

## Properties

```
@property (T@"_UIZoomViewControllerTransition",N,&,VclientTransition) clientTransition;
@property (TB,N,VisZoomingIn) isZoomingIn;
@property (T@"UIViewController",N,W,VowningViewController) owningViewController;
@property (T@"_UIDismissInteraction",N,&,VdismissInteraction) dismissInteraction;
@property (T@"_UIViewAlphaOverrideAssertion",N,&,VsourceViewHidingAssertion) sourceViewHidingAssertion;
@property (TB,N,R) wantsInteractiveStart;
@property (Tq,N,R) _navigationBarTransitionVariant;
@property (T@"UIView",N,R) _navigationBarTransitionOverlay;
@property (TB,N,R) _shouldCrossFadeBottomBars;
@property (TB,N,R) _shouldCrossFadeNavigationBarVisibility;
@property (TB,N,R) _shouldAnimateBottomBarVisibility;
@property (TB,N,R) prefersPreemptionEnabledForPresentations;
```

## Instance methods

```
-[_UIZoomTransitionController sourceViewHidingAssertion];
-[_UIZoomTransitionController trackingViewForInteraction:];
-[_UIZoomTransitionController owningViewController];
-[_UIZoomTransitionController _shouldCrossFadeNavigationBarVisibility];
-[_UIZoomTransitionController dismissInteraction:didCancelWithVelocity:originalPosition:];
-[_UIZoomTransitionController animateTransition:];
-[_UIZoomTransitionController setOwningViewController:];
-[_UIZoomTransitionController transitionDuration:];
-[_UIZoomTransitionController init];
-[_UIZoomTransitionController _interactionController];
-[_UIZoomTransitionController _navigationBarTransitionVariant];
-[_UIZoomTransitionController _shouldCrossFadeBottomBars];
-[_UIZoomTransitionController startInteractiveTransition:];
-[_UIZoomTransitionController dismissInteraction:didBeginAtLocation:withVelocity:];
-[_UIZoomTransitionController prepareToAnimateKeyboard:];
-[_UIZoomTransitionController prefersPreemptionEnabledForPresentations];
-[_UIZoomTransitionController interruptibleAnimatorForTransition:];
-[_UIZoomTransitionController didMoveToParent:];
-[_UIZoomTransitionController hysteresisForInteraction:];
-[_UIZoomTransitionController clientTransition];
-[_UIZoomTransitionController setIsZoomingIn:];
-[_UIZoomTransitionController _shouldAnimateBottomBarVisibility];
-[_UIZoomTransitionController animateKeyboard:];
-[_UIZoomTransitionController wantsInteractiveStart];
-[_UIZoomTransitionController wantsToCommandeerKeyboardTransition];
-[_UIZoomTransitionController dismissInteraction:didIssueUpdate:];
-[_UIZoomTransitionController preemptWithContext:];
-[_UIZoomTransitionController dismissInteraction];
-[_UIZoomTransitionController _navigationToolbarTransitionControllerForContext:];
-[_UIZoomTransitionController didDismissViewController];
-[_UIZoomTransitionController _navigationBarTransitionOverlay];
-[_UIZoomTransitionController dismissInteraction:didDismissWithVelocity:];
-[_UIZoomTransitionController dismissInteraction:shouldBeginWithAxis:location:velocity:proposal:];
-[_UIZoomTransitionController setClientTransition:];
-[_UIZoomTransitionController setDismissInteraction:];
-[_UIZoomTransitionController setSourceViewHidingAssertion:];
-[_UIZoomTransitionController willBeginAfterPreemptionWithContext:data:];
-[_UIZoomTransitionController completeKeyboard:];
-[_UIZoomTransitionController isZoomingIn];
-[_UIZoomTransitionController shouldPreemptWithContext:];
```
