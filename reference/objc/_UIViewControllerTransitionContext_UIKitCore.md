# `_UIViewControllerTransitionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerContextTransitioningEx`
- 28 instance variables, 38 properties, 91 instance methods, 2 class methods

## Instance variables

```
@"<UIViewControllerAnimatedTransitioning>" __animator;
@"UIView" _containerView;
d _previousPercentComplete;
@"NSArray" _disabledViews;
{?="interactorImplementsCompletionSpeed"b1"interactorImplementsCompletionCurve"b1"ranAlongsideAnimations"b1"transitionWasCancelled"b1"transitionIsCompleting"b1"transitionHasCompleted"b1"transitionIsInterruptible"b1"performingLayoutToLayoutTransition"b1} _transitionContextFlags;
B __allowUserInteraction;
B _rotating;
B _animated;
B __needsBottomBarCrossfade;
B __transitioningBottomBarIsTabBar;
B __transitionWasPreempted;
B _initiallyInteractive;
B _currentlyInteractive;
B __isPresentation;
@"NSArray" __containerViews;
d __percentOffset;
@"<UIViewControllerInteractiveTransitioning>" __interactor;
d __duration;
@? __willCompleteHandler;
@? __completionHandler;
@? __didCompleteHandler;
@"NSMutableArray" __interactiveUpdateHandlers;
d __completionVelocity;
q __completionCurve;
@"_UIViewControllerTransitionCoordinator" __auxContext;
q __state;
@? __postInteractiveCompletionHandler;
q _presentationStyle;
```

## Properties

```
@property (TB,R,N) _ranAlongsideAnimations;
@property (T@"NSMutableArray",&,N,V__interactiveUpdateHandlers) _interactiveUpdateHandlers;
@property (TB,N,S_setTransitionWasPreempted:,V__transitionWasPreempted) _transitionWasPreempted;
@property (TB,N,G_initiallyInteractive,S_setInitiallyInteractive:,V_initiallyInteractive) initiallyInteractive;
@property (TB,N,GisCurrentlyInteractive,S_setCurrentlyInteractive:,V_currentlyInteractive) currentlyInteractive;
@property (TB,N,GisInterruptible,S_setInterruptible:) interruptible;
@property (Td,N,S_setCompletionVelocity:,V__completionVelocity) _completionVelocity;
@property (Tq,N,S_setCompletionCurve:,V__completionCurve) _completionCurve;
@property (TB,N,S_setTransitionIsCompleting:) _transitionIsCompleting;
@property (TB,R,N) _transitionHasCompleted;
@property (T@"_UIViewControllerTransitionCoordinator",&,N,S_setAuxContext:,V__auxContext) _auxContext;
@property (Tq,N,S_setState:,V__state) _state;
@property (T@?,C,N,S_setPostInteractiveCompletionHandler:,V__postInteractiveCompletionHandler) _postInteractiveCompletionHandler;
@property (Tq,N,S_setPresentationStyle:,V_presentationStyle) presentationStyle;
@property (TB,N,S_setIsPresentation:,V__isPresentation) _isPresentation;
@property (T@"NSArray",&,N,S_setContainerViews:,V__containerViews) _containerViews;
@property (Td,N,S_setPercentOffset:,V__percentOffset) _percentOffset;
@property (T@"<UIViewControllerAnimatedTransitioning>",W,N,S_setAnimator:) _animator;
@property (T@"<UIViewControllerInteractiveTransitioning>",W,N,S_setInteractor:,V__interactor) _interactor;
@property (TB,N,G_allowUserInteraction,S_setAllowUserInteraction:,V__allowUserInteraction) _allowUserInteraction;
@property (TB,N,G_isRotating,S_setRotating:,V_rotating) rotating;
@property (T{CGAffineTransform=dddddd},R,N,G_affineTransform) affineTransform;
@property (TB,R,N,GisAnimated,V_animated) animated;
@property (Td,N,S_setDuration:,V__duration) _duration;
@property (TB,N,S_setNeedsBottomBarCrossfade:,V__needsBottomBarCrossfade) _needsBottomBarCrossfade;
@property (TB,N,S_setTransitioningBottomBarIsTabBar:,V__transitioningBottomBarIsTabBar) _transitioningBottomBarIsTabBar;
@property (TB,N,G_isPerformingLayoutToLayoutTransition,S_setPerformingLayoutToLayoutTransition:) _performingLayoutToLayoutTransition;
@property (T@?,C,N,S_setWillCompleteHandler:,V__willCompleteHandler) _willCompleteHandler;
@property (T@?,C,N,S_setCompletionHandler:,V__completionHandler) _completionHandler;
@property (T@?,C,N,S_setDidCompleteHandler:,V__didCompleteHandler) _didCompleteHandler;
@property (T@"UIView",R,N) containerView;
@property (TB,R,N,GisInteractive) interactive;
@property (TB,R,N) transitionWasCancelled;
@property (T{CGAffineTransform=dddddd},R,N) targetTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewControllerTransitionContext _associatedTransitionContextsForInteractionController:];
+[_UIViewControllerTransitionContext _associatedTransitionContextForAnimationController:];
```

## Instance methods

```
-[_UIViewControllerTransitionContext _duration];
-[_UIViewControllerTransitionContext _state];
-[_UIViewControllerTransitionContext _setPostInteractiveCompletionHandler:];
-[_UIViewControllerTransitionContext updateInteractiveTransition:];
-[_UIViewControllerTransitionContext _runAlongsideCompletions];
-[_UIViewControllerTransitionContext _setTransitionIsCompleting:];
-[_UIViewControllerTransitionContext _setCompletionCurve:];
-[_UIViewControllerTransitionContext _needsBottomBarCrossfade];
-[_UIViewControllerTransitionContext _setPreviousPercentComplete:];
-[_UIViewControllerTransitionContext _transitionIsInFlight];
-[_UIViewControllerTransitionContext _setInterruptible:];
-[_UIViewControllerTransitionContext viewControllerForKey:];
-[_UIViewControllerTransitionContext _setState:];
-[_UIViewControllerTransitionContext viewForKey:];
-[_UIViewControllerTransitionContext __runAlongsideAnimations];
-[_UIViewControllerTransitionContext _allowUserInteraction];
-[_UIViewControllerTransitionContext _interactivityDidChange:];
-[_UIViewControllerTransitionContext init];
-[_UIViewControllerTransitionContext isAnimated];
-[_UIViewControllerTransitionContext finalFrameForViewController:];
-[_UIViewControllerTransitionContext initiallyInteractive];
-[_UIViewControllerTransitionContext transitionWasCancelled];
-[_UIViewControllerTransitionContext _setInitiallyInteractive:];
-[_UIViewControllerTransitionContext completeTransition:];
-[_UIViewControllerTransitionContext isInteractive];
-[_UIViewControllerTransitionContext dealloc];
-[_UIViewControllerTransitionContext _postInteractiveCompletionHandler];
-[_UIViewControllerTransitionContext _animator];
-[_UIViewControllerTransitionContext _previousPercentComplete];
-[_UIViewControllerTransitionContext presentationStyle];
-[_UIViewControllerTransitionContext _completionVelocity];
-[_UIViewControllerTransitionContext _updateInteractiveTransitionWithoutTrackingPercentComplete:];
-[_UIViewControllerTransitionContext _setTransitioningBottomBarIsTabBar:];
-[_UIViewControllerTransitionContext initialFrameForViewController:];
-[_UIViewControllerTransitionContext _setDuration:];
-[_UIViewControllerTransitionContext _didCompleteHandler];
-[_UIViewControllerTransitionContext cancelInteractiveTransition];
-[_UIViewControllerTransitionContext pauseInteractiveTransition];
-[_UIViewControllerTransitionContext isInterruptible];
-[_UIViewControllerTransitionContext _setTransitionWasPreempted:];
-[_UIViewControllerTransitionContext containerView];
-[_UIViewControllerTransitionContext _setPercentOffset:];
-[_UIViewControllerTransitionContext finishInteractiveTransition];
-[_UIViewControllerTransitionContext _isPerformingLayoutToLayoutTransition];
-[_UIViewControllerTransitionContext targetTransform];
-[_UIViewControllerTransitionContext _setRotating:];
-[_UIViewControllerTransitionContext _setCompletionVelocity:];
-[_UIViewControllerTransitionContext _isRotating];
-[_UIViewControllerTransitionContext _completionCurve];
-[_UIViewControllerTransitionContext isCurrentlyInteractive];
-[_UIViewControllerTransitionContext _setCompletionHandler:];
-[_UIViewControllerTransitionContext _willCompleteHandler];
-[_UIViewControllerTransitionContext _setAllowUserInteraction:];
-[_UIViewControllerTransitionContext _transitionWasPreempted];
-[_UIViewControllerTransitionContext _setAuxContext:];
-[_UIViewControllerTransitionContext _percentOffset];
-[_UIViewControllerTransitionContext _transitionCoordinator];
-[_UIViewControllerTransitionContext _setAnimator:];
-[_UIViewControllerTransitionContext _addInteractiveUpdateHandler:];
-[_UIViewControllerTransitionContext _transitionIsCompleting];
-[_UIViewControllerTransitionContext _initiallyInteractive];
-[_UIViewControllerTransitionContext _enableInteractionForDisabledViews];
-[_UIViewControllerTransitionContext _setContainerViews:];
-[_UIViewControllerTransitionContext _auxContext];
-[_UIViewControllerTransitionContext _transitionHasCompleted];
-[_UIViewControllerTransitionContext _setNeedsBottomBarCrossfade:];
-[_UIViewControllerTransitionContext _disableInteractionForViews:];
-[_UIViewControllerTransitionContext _isPresentation];
-[_UIViewControllerTransitionContext _interactor];
-[_UIViewControllerTransitionContext _runInvalidationHandlers];
-[_UIViewControllerTransitionContext setTransitionWasCancelled:];
-[_UIViewControllerTransitionContext _setIsAnimated:];
-[_UIViewControllerTransitionContext _setTransitionIsInFlight:];
-[_UIViewControllerTransitionContext _stopInteractiveTransition];
-[_UIViewControllerTransitionContext _ranAlongsideAnimations];
-[_UIViewControllerTransitionContext _containerViews];
-[_UIViewControllerTransitionContext _completionHandler];
-[_UIViewControllerTransitionContext _setDidCompleteHandler:];
-[_UIViewControllerTransitionContext _setWillCompleteHandler:];
-[_UIViewControllerTransitionContext _setInteractor:];
-[_UIViewControllerTransitionContext _setIsPresentation:];
-[_UIViewControllerTransitionContext _setPerformingLayoutToLayoutTransition:];
-[_UIViewControllerTransitionContext _setCurrentlyInteractive:];
-[_UIViewControllerTransitionContext _setPresentationStyle:];
-[_UIViewControllerTransitionContext _interactiveUpdateHandlers];
-[_UIViewControllerTransitionContext _alongsideAnimationsCount];
-[_UIViewControllerTransitionContext _transitioningBottomBarIsTabBar];
-[_UIViewControllerTransitionContext set_interactiveUpdateHandlers:];
-[_UIViewControllerTransitionContext _setContainerView:];
-[_UIViewControllerTransitionContext finalTransformForViewController:];
-[_UIViewControllerTransitionContext _affineTransform];
```
