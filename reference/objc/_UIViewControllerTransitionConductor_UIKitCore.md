# `_UIViewControllerTransitionConductor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 13 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _needsDeferredTransition;
B _hostIsAppearingAnimated;
B _interactiveTransition;
i _deferredTransitionType;
@"UIViewController<_UIViewControllerTransitionConductorDelegate>" _delegate;
@"<UIViewControllerAnimatedTransitioning>" _transitionController;
@"<UIViewControllerInteractiveTransitioning>" _interactiveTransitionController;
d _customNavigationTransitionDuration;
@"UIView" _transitionContainerView;
@"_UIViewControllerAnimatedTransitionHandoffData" _pendingPreemptionHandoffData;
@"_UIViewControllerTransitionManager" _transitionManager;
```

## Properties

```
@property (T@"_UIViewControllerTransitionManager",&,N,V_transitionManager) transitionManager;
@property (T@"UIViewController<_UIViewControllerTransitionConductorDelegate>",R,W,N,V_delegate) delegate;
@property (T@"<UIViewControllerAnimatedTransitioning>",&,N,V_transitionController) transitionController;
@property (T@"<UIViewControllerInteractiveTransitioning>",&,N,V_interactiveTransitionController) interactiveTransitionController;
@property (TB,N,V_needsDeferredTransition) needsDeferredTransition;
@property (TB,N,V_hostIsAppearingAnimated) hostIsAppearingAnimated;
@property (Ti,N,V_deferredTransitionType) deferredTransitionType;
@property (Td,N,V_customNavigationTransitionDuration) customNavigationTransitionDuration;
@property (TB,N,GisInteractiveTransition,V_interactiveTransition) interactiveTransition;
@property (T@"_UIViewControllerOneToOneTransitionContext",R,N) transitionContext;
@property (T@"<UIViewControllerTransitionCoordinator>",R,N) transitionCoordinator;
@property (T@"UIView",&,N,V_transitionContainerView) transitionContainerView;
@property (T@"_UIViewControllerAnimatedTransitionHandoffData",&,N,V_pendingPreemptionHandoffData) pendingPreemptionHandoffData;
```

## Instance methods

```
-[_UIViewControllerTransitionConductor transitionCoordinator];
-[_UIViewControllerTransitionConductor navigationToolbarTransitionController];
-[_UIViewControllerTransitionConductor hostIsAppearingAnimated];
-[_UIViewControllerTransitionConductor shouldCrossFadeNavigationBarVisibility];
-[_UIViewControllerTransitionConductor navigationBarTransitionVariant];
-[_UIViewControllerTransitionConductor _startTransition:fromViewController:toViewController:];
-[_UIViewControllerTransitionConductor setTransitionManager:];
-[_UIViewControllerTransitionConductor shouldAnimateBottomBarVisibility];
-[_UIViewControllerTransitionConductor needsDeferredTransition];
-[_UIViewControllerTransitionConductor setCustomNavigationTransitionDuration:];
-[_UIViewControllerTransitionConductor transitionContext];
-[_UIViewControllerTransitionConductor navigationBarHidingDurationWithDefaultDuration:];
-[_UIViewControllerTransitionConductor _beginAnimationTrackingInteractive:];
-[_UIViewControllerTransitionConductor pendingPreemptionHandoffData];
-[_UIViewControllerTransitionConductor setInteractiveTransitionController:];
-[_UIViewControllerTransitionConductor setDeferredTransitionType:];
-[_UIViewControllerTransitionConductor setPendingPreemptionHandoffData:];
-[_UIViewControllerTransitionConductor initWithDelegate:transitionManager:];
-[_UIViewControllerTransitionConductor setHostIsAppearingAnimated:];
-[_UIViewControllerTransitionConductor willPerformCustomTransition];
-[_UIViewControllerTransitionConductor transitionContainerView];
-[_UIViewControllerTransitionConductor navigationBarTransitionOverlay];
-[_UIViewControllerTransitionConductor customNavigationTransitionDuration];
-[_UIViewControllerTransitionConductor interruptibleNavigationTransitionAnimator];
-[_UIViewControllerTransitionConductor setTransitionController:];
-[_UIViewControllerTransitionConductor stopTransitionsImmediately];
-[_UIViewControllerTransitionConductor setNeedsDeferredTransition];
-[_UIViewControllerTransitionConductor transitionController];
-[_UIViewControllerTransitionConductor shouldCrossFadeBottomBars];
-[_UIViewControllerTransitionConductor startDeferredTransitionIfNeeded];
-[_UIViewControllerTransitionConductor interactiveTransitionController];
-[_UIViewControllerTransitionConductor setInteractiveTransition:];
-[_UIViewControllerTransitionConductor _finishAnimationTracking];
-[_UIViewControllerTransitionConductor delegate];
-[_UIViewControllerTransitionConductor deferredTransitionType];
-[_UIViewControllerTransitionConductor transitionManager];
-[_UIViewControllerTransitionConductor setTransitionContainerView:];
-[_UIViewControllerTransitionConductor shouldCrossFadeNavigationBar];
-[_UIViewControllerTransitionConductor _startCustomTransition:];
-[_UIViewControllerTransitionConductor isInteractiveTransition];
-[_UIViewControllerTransitionConductor hasInterruptibleNavigationTransition];
-[_UIViewControllerTransitionConductor setNeedsDeferredTransition:];
```
