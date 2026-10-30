# `_UINavigationInteractiveTransitionBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPercentDrivenInteractiveTransition`
- Protocols: `UIViewControllerInteractiveTransitioning_Internal`, `UIGestureRecognizerDelegateInternal`, `UINavigationControllerInteractiveTransitioning`, `UIGestureRecognizerDelegate`
- 32 instance variables, 32 properties, 70 instance methods, 0 class methods

## Instance variables

```
@"UIView" _gestureRecognizerView;
@"UIPanGestureRecognizer" _gestureRecognizer;
@"_UIParallaxTransitionPanGestureRecognizer" _contentSwipeGestureRecognizer;
q __interactionState;
B __updateRequestActive;
B __transitionWasStopped;
B __stoppedTransitionWasCancelled;
@"UIViewController" __parent;
B __useAugmentedShouldPopDecisionProcedure;
B __completesTransitionOnEnd;
d _percentCompleteWhenPaused;
B _wantsInteractiveStart;
@"CADisplayLink" _displayLink;
[3d] _timestamps;
[3d] _velocities;
[3d] _accelerations;
B _shouldReverseTranslation;
B __shouldReverseLayoutDirection;
B _isInEdgeFlickPhase;
@"UIPanGestureRecognizer" _edgeSwipeGestureRecognizer;
@"_UINavigationParallaxTransition" _animationController;
@"<_UINavigationInteractiveTransitionBaseDelegate>" _delegate;
Q _sampleCount;
d _totalDistance;
d _skipTimeStamp;
d _previousTimeStamp;
d _previousDisplacement;
d _previousVelocity;
d _previousAcceleration;
d _averageVelocity;
d _averageAcceleration;
d _startingVelocity;
```

## Properties

```
@property (TQ,N,V_sampleCount) sampleCount;
@property (Td,N,V_totalDistance) totalDistance;
@property (Td,N,V_skipTimeStamp) skipTimeStamp;
@property (Td,N,V_previousTimeStamp) previousTimeStamp;
@property (Td,N,V_previousDisplacement) previousDisplacement;
@property (Td,N,V_previousVelocity) previousVelocity;
@property (Td,N,V_previousAcceleration) previousAcceleration;
@property (Td,N,V_averageVelocity) averageVelocity;
@property (Td,N,V_averageAcceleration) averageAcceleration;
@property (Td,N,V_startingVelocity) startingVelocity;
@property (TB,N,V_isInEdgeFlickPhase) isInEdgeFlickPhase;
@property (T@"UIPanGestureRecognizer",R,W,N,V_gestureRecognizer) gestureRecognizer;
@property (T@"UIPanGestureRecognizer",R,N,V_edgeSwipeGestureRecognizer) edgeSwipeGestureRecognizer;
@property (T@"UIPanGestureRecognizer",R,N,V_contentSwipeGestureRecognizer) contentSwipeGestureRecognizer;
@property (TB,N,V_shouldReverseTranslation) shouldReverseTranslation;
@property (T@"_UINavigationParallaxTransition",&,N,V_animationController) animationController;
@property (Tq,N,S_setInteractionState:,V__interactionState) _interactionState;
@property (TB,N,S_setTransitionWasStopped:,V__transitionWasStopped) _transitionWasStopped;
@property (TB,N,S_setStoppedTransitionWasCancelled:,V__stoppedTransitionWasCancelled) _stoppedTransitionWasCancelled;
@property (T@"UIViewController",W,N,S_setParent:,V__parent) _parent;
@property (TB,N,S_setUseAugmentedShouldPopDecisionProcedure:,V__useAugmentedShouldPopDecisionProcedure) _useAugmentedShouldPopDecisionProcedure;
@property (TB,N,S_setCompletesTransitionOnEnd:,V__completesTransitionOnEnd) _completesTransitionOnEnd;
@property (T@"UIGestureRecognizer",R,N,G_navigationGesture) navigationGesture;
@property (T@"<_UINavigationInteractiveTransitionBaseDelegate>",W,N,V_delegate) delegate;
@property (TB,N,S_setShouldReverseLayoutDirection:,V__shouldReverseLayoutDirection) _shouldReverseLayoutDirection;
@property (Td,?,R,N) completionSpeed;
@property (Tq,?,R,N) completionCurve;
@property (TB,?,R,N) wantsInteractiveStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationInteractiveTransitionBase animationController];
-[_UINavigationInteractiveTransitionBase _navigationGesture];
-[_UINavigationInteractiveTransitionBase previousDisplacement];
-[_UINavigationInteractiveTransitionBase gestureRecognizer:shouldReceiveTouch:];
-[_UINavigationInteractiveTransitionBase _parent];
-[_UINavigationInteractiveTransitionBase setSampleCount:];
-[_UINavigationInteractiveTransitionBase gestureRecognizer];
-[_UINavigationInteractiveTransitionBase _shouldReverseLayoutDirection];
-[_UINavigationInteractiveTransitionBase startInteractiveTransition];
-[_UINavigationInteractiveTransitionBase dealloc];
-[_UINavigationInteractiveTransitionBase contentSwipeGestureRecognizer];
-[_UINavigationInteractiveTransitionBase _transitionWasStopped];
-[_UINavigationInteractiveTransitionBase _completeStoppedInteractiveTransition];
-[_UINavigationInteractiveTransitionBase _setStoppedTransitionWasCancelled:];
-[_UINavigationInteractiveTransitionBase _gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UINavigationInteractiveTransitionBase setPreviousVelocity:];
-[_UINavigationInteractiveTransitionBase totalDistance];
-[_UINavigationInteractiveTransitionBase _resetInteractionController];
-[_UINavigationInteractiveTransitionBase averageVelocity];
-[_UINavigationInteractiveTransitionBase cancelInteractiveTransition];
-[_UINavigationInteractiveTransitionBase setPreviousAcceleration:];
-[_UINavigationInteractiveTransitionBase setAverageVelocity:];
-[_UINavigationInteractiveTransitionBase popGesture:withRemainingDuration:shouldPopWithVelocity:];
-[_UINavigationInteractiveTransitionBase _shouldPauseRunningTransition];
-[_UINavigationInteractiveTransitionBase _setShouldReverseLayoutDirection:];
-[_UINavigationInteractiveTransitionBase _interactionState];
-[_UINavigationInteractiveTransitionBase finishInteractiveTransition];
-[_UINavigationInteractiveTransitionBase setStartingVelocity:];
-[_UINavigationInteractiveTransitionBase setDelegate:];
-[_UINavigationInteractiveTransitionBase _setTransitionWasStopped:];
-[_UINavigationInteractiveTransitionBase wantsInteractiveStart];
-[_UINavigationInteractiveTransitionBase _stoppedTransitionWasCancelled];
-[_UINavigationInteractiveTransitionBase gestureRecognizerShouldBegin:];
-[_UINavigationInteractiveTransitionBase _setInteractionState:];
-[_UINavigationInteractiveTransitionBase sampleCount];
-[_UINavigationInteractiveTransitionBase _setUseAugmentedShouldPopDecisionProcedure:];
-[_UINavigationInteractiveTransitionBase setPreviousTimeStamp:];
-[_UINavigationInteractiveTransitionBase _updateStatistics:firstSample:finalSample:];
-[_UINavigationInteractiveTransitionBase isInEdgeFlickPhase];
-[_UINavigationInteractiveTransitionBase _translationCoefficient];
-[_UINavigationInteractiveTransitionBase gestureRecognizerView];
-[_UINavigationInteractiveTransitionBase shouldReverseTranslation];
-[_UINavigationInteractiveTransitionBase previousAcceleration];
-[_UINavigationInteractiveTransitionBase gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UINavigationInteractiveTransitionBase delegate];
-[_UINavigationInteractiveTransitionBase handleNavigationTransition:];
-[_UINavigationInteractiveTransitionBase _useAugmentedShouldPopDecisionProcedure];
-[_UINavigationInteractiveTransitionBase skipTimeStamp];
-[_UINavigationInteractiveTransitionBase setTotalDistance:];
-[_UINavigationInteractiveTransitionBase _supportsCoordinatedPresentationDismissal];
-[_UINavigationInteractiveTransitionBase _stopInteractiveTransition];
-[_UINavigationInteractiveTransitionBase previousTimeStamp];
-[_UINavigationInteractiveTransitionBase _setCompletesTransitionOnEnd:];
-[_UINavigationInteractiveTransitionBase _setParent:];
-[_UINavigationInteractiveTransitionBase _gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UINavigationInteractiveTransitionBase initWithGestureRecognizerView:animator:delegate:];
-[_UINavigationInteractiveTransitionBase setIsInEdgeFlickPhase:];
-[_UINavigationInteractiveTransitionBase setAverageAcceleration:];
-[_UINavigationInteractiveTransitionBase setPreviousDisplacement:];
-[_UINavigationInteractiveTransitionBase setAnimationController:];
-[_UINavigationInteractiveTransitionBase setNotInteractiveTransition];
-[_UINavigationInteractiveTransitionBase startingVelocity];
-[_UINavigationInteractiveTransitionBase averageAcceleration];
-[_UINavigationInteractiveTransitionBase setShouldReverseTranslation:];
-[_UINavigationInteractiveTransitionBase setSkipTimeStamp:];
-[_UINavigationInteractiveTransitionBase _createContentSwipeGestureRecognizer];
-[_UINavigationInteractiveTransitionBase _startingVelocity];
-[_UINavigationInteractiveTransitionBase edgeSwipeGestureRecognizer];
-[_UINavigationInteractiveTransitionBase previousVelocity];
-[_UINavigationInteractiveTransitionBase _completesTransitionOnEnd];
```
