# `SBUIAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransaction`
- Protocols: `SBSceneHandleObserver`, `UIViewControllerInteractiveTransitioning`, `SBViewControllerTransitionContextDelegate`, `SBUIAnimationStepping`, `SBUIAnimationControllerCoordinating`
- 17 instance variables, 28 properties, 97 instance methods, 3 class methods

## Instance variables

```
@"<SBUIAnimationControllerTransitionContextProvider>" _transitionContextProvider;
@"BSBlockTransaction" _animationTransaction;
@"BSBlockTransaction" _notifyObserversTransaction;
@"BSBlockTransaction" _cleanupTransaction;
@"NSSet" _sceneHandlesBeingObserved;
@"NSSet" _entitiesToObserve;
@"NSSet" _startTransactionDependencies;
@"NSMutableArray" _coordinatingChildRelationships;
@"NSMutableArray" _steppedCoordinatingChildAnimations;
@"SBAnimationStepper" _stepper;
@"UIWindow" _transitionWindow;
@"UIView" _transitionContainer;
i _animationState;
B _didNotifyObserversOfCompletion;
B _needsCATransactionActivate;
@"SBViewControllerTransitionContext" _transition;
@? _animationTransactionCompletion;
```

## Properties

```
@property (T@"SBViewControllerTransitionContext",&,N,V_transition) transition;
@property (T@"<SBUIAnimationControllerTransitionContextProvider>",&,N,V_transitionContextProvider) transitionContextProvider;
@property (T@?,C,N,V_animationTransactionCompletion) animationTransactionCompletion;
@property (T@"BSTransaction",R,N,V_animationTransaction) animationTransaction;
@property (T@"BSTransaction",R,N,V_notifyObserversTransaction) notifyObserversTransaction;
@property (T@"BSTransaction",R,N,V_cleanupTransaction) cleanupTransaction;
@property (TB,N,V_needsCATransactionActivate) needsCATransactionActivate;
@property (T@"UIView",R,N,V_transitionContainer) containerView;
@property (T@"NSSet",R,C,N) toApplicationSceneEntities;
@property (T@"SBApplicationSceneEntity",R,N) toApplicationSceneEntity;
@property (T@"NSSet",R,C,N) fromApplicationSceneEntities;
@property (T@"SBApplicationSceneEntity",R,N) fromApplicationSceneEntity;
@property (TB,R,N) transitionSupportsCancelling;
@property (TB,R,N) transitionSupportsRestarting;
@property (TB,R,N) transitionWasCancelled;
@property (TB,R,N) transitionWasRestarted;
@property (TB,R,N,GisInteractive) interactive;
@property (T@"<SBViewControllerTransitionCoordinator>",R,N) transitionCoordinator;
@property (T@"BSAnimationSettings",R,N) animationSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,?,R,N) completionSpeed;
@property (Tq,?,R,N) completionCurve;
@property (TB,?,R,N) wantsInteractiveStart;
@property (TB,R,N,GisStepped) stepped;
@property (Td,N) stepPercentage;
```

## Class methods

```
+[SBUIAnimationController _removeAlertItemsPendingReason:];
+[SBUIAnimationController _addAlertItemsPendingReason:];
+[SBUIAnimationController isPendingAlertItemsWithReason:];
```

## Instance methods

```
-[SBUIAnimationController transitionDidFinish:];
-[SBUIAnimationController transitionCoordinator];
-[SBUIAnimationController transition];
-[SBUIAnimationController _animationState];
-[SBUIAnimationController _setAnimationState:];
-[SBUIAnimationController animationSettings];
-[SBUIAnimationController sceneHandle:didUpdateContentState:];
-[SBUIAnimationController _canBeInterrupted];
-[SBUIAnimationController animating];
-[SBUIAnimationController _begin];
-[SBUIAnimationController initWithTransitionContextProvider:];
-[SBUIAnimationController _prepareAnimation];
-[SBUIAnimationController removeObserver:];
-[SBUIAnimationController init];
-[SBUIAnimationController transitionWasCancelled];
-[SBUIAnimationController isInteractive];
-[SBUIAnimationController startInteractiveTransition:];
-[SBUIAnimationController dealloc];
-[SBUIAnimationController isReasonableMomentToInterrupt];
-[SBUIAnimationController shouldResignActiveForAnimation];
-[SBUIAnimationController _cleanupAnimation];
-[SBUIAnimationController containerView];
-[SBUIAnimationController addObserver:];
-[SBUIAnimationController cancelTransition];
-[SBUIAnimationController _willComplete];
-[SBUIAnimationController transitionWasRestarted];
-[SBUIAnimationController _setHidden:];
-[SBUIAnimationController _startAnimation];
-[SBUIAnimationController fromApplicationSceneEntities];
-[SBUIAnimationController setTransition:];
-[SBUIAnimationController toApplicationSceneEntities];
-[SBUIAnimationController restartTransition];
-[SBUIAnimationController isFluidSwitcherAnimationController];
-[SBUIAnimationController _didInterruptWithReason:];
-[SBUIAnimationController _animationIdentifier];
-[SBUIAnimationController _addDebugLogCategory:];
-[SBUIAnimationController isFinishedAnimating];
-[SBUIAnimationController __startAnimation];
-[SBUIAnimationController _abortAnimation];
-[SBUIAnimationController __abortAnimation];
-[SBUIAnimationController __alertItemsController];
-[SBUIAnimationController __animationShouldStart];
-[SBUIAnimationController __cleanupAnimation];
-[SBUIAnimationController __noteAnimationDidTerminate];
-[SBUIAnimationController __reportAnimationCompletion];
-[SBUIAnimationController __startTransactionDependencyForEntity:];
-[SBUIAnimationController __wantsInitialProgressStateChange];
-[SBUIAnimationController _application:processStateDidChange:];
-[SBUIAnimationController _cleanupEntityObservers];
-[SBUIAnimationController _entityObserverProgressDidChange:waitForSceneContentAvailableTransactionBlock:];
-[SBUIAnimationController _enumerateCoordinatingAnimationsWithBlock:];
-[SBUIAnimationController _enumerateCoordinatingAnimationsWithSchedulingPolicy:block:];
-[SBUIAnimationController _enumerateCoordinatingChildRelationshipsWithBlock:];
-[SBUIAnimationController _getTransitionWindow];
-[SBUIAnimationController _isNullAnimation];
-[SBUIAnimationController _noteAnimationDidFail];
-[SBUIAnimationController _noteAnimationDidFinish];
-[SBUIAnimationController _noteAnimationDidRevealApplication];
-[SBUIAnimationController _notifyObserversOfAnimationCompletion];
-[SBUIAnimationController _processStateDidChange:];
-[SBUIAnimationController _progressDependencies];
-[SBUIAnimationController _registerEntityObserversIfNecessary];
-[SBUIAnimationController _sceneHandle:didUpdateContentState:];
-[SBUIAnimationController _shouldDismissBanner];
-[SBUIAnimationController _transitionAnimator];
-[SBUIAnimationController _viewsForAnimationStepping];
-[SBUIAnimationController _waitsForActivatingSceneContentAvailableIfNecessary];
-[SBUIAnimationController _willAnimate];
-[SBUIAnimationController _willBeginWaitingForStartDependencies];
-[SBUIAnimationController _willSetupStartDependencies];
-[SBUIAnimationController addCoordinatingChildTransaction:withSchedulingPolicy:];
-[SBUIAnimationController addSteppedCoordinatingChildAnimation:];
-[SBUIAnimationController animationTransaction];
-[SBUIAnimationController animationTransactionCompletion];
-[SBUIAnimationController cleanupTransaction];
-[SBUIAnimationController coordinatingAnimationControllers];
-[SBUIAnimationController delayAnimationUntilTransactionFinishes:];
-[SBUIAnimationController delayCleanupUntilTransactionFinishes:];
-[SBUIAnimationController enableSteppingWithAnimationSettings:];
-[SBUIAnimationController finishSteppingBackwardToStart];
-[SBUIAnimationController finishSteppingForwardToEnd];
-[SBUIAnimationController fromApplicationSceneEntity];
-[SBUIAnimationController isStepped];
-[SBUIAnimationController needsCATransactionActivate];
-[SBUIAnimationController notifyObserversTransaction];
-[SBUIAnimationController setAnimationTransactionCompletion:];
-[SBUIAnimationController setNeedsCATransactionActivate:];
-[SBUIAnimationController setStepPercentage:];
-[SBUIAnimationController setTransitionContextProvider:];
-[SBUIAnimationController stepPercentage];
-[SBUIAnimationController stopDelayingAnimationForTransaction:];
-[SBUIAnimationController stopDelayingCleanupForTransaction:];
-[SBUIAnimationController toApplicationSceneEntity];
-[SBUIAnimationController transitionContextProvider];
-[SBUIAnimationController transitionSupportsCancelling];
-[SBUIAnimationController transitionSupportsRestarting];
-[SBUIAnimationController waitingToStart];
```
