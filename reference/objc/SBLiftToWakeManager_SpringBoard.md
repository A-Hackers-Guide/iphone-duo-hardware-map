# `SBLiftToWakeManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalEventHandling`, `SBLiftToWakeObserver`, `BSInvalidatable`
- 10 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SBLiftToWakeController" _liftToWakeController;
@"SBBacklightController" _backlightController;
@"SBLockScreenManager" _lockScreenManager;
@"SBPolicyAggregator" _accessor_policyAggregator;
@"SBIdleTimerGlobalCoordinator" _accessor_idleTimerCoordinator;
@"<SBLiftToWakeManagerBumpWakeArbiter>" _accessor_bumpWakeArbiter;
B _gestureWokeScreen;
B _observing;
B _significantUserInteractionOccuredSinceWake;
B _invalidated;
```

## Properties

```
@property (T@"SBLiftToWakeController",&,N,G_liftToWakeController,S_setLiftToWakeController:,V_liftToWakeController) liftToWakeController;
@property (T@"SBPolicyAggregator",&,N,G_policyAggregator,S_setPolicyAggregator:,V_accessor_policyAggregator) policyAggregator;
@property (T@"SBIdleTimerGlobalCoordinator",&,N,G_idleTimerCoordinator,S_setIdleTimerCoordinator:,V_accessor_idleTimerCoordinator) idleTimerCoordinator;
@property (T@"<SBLiftToWakeManagerBumpWakeArbiter>",&,N,G_bumpWakeArbiter,S_setBumpWakeArbiter:,V_accessor_bumpWakeArbiter) bumpWakeArbiter;
@property (TB,N,G_gestureWokeScreen,S_setGestureWokeScreen:,V_gestureWokeScreen) gestureWokeScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBLiftToWakeManager handleEvent:];
-[SBLiftToWakeManager wouldHandleButtonEvent:];
-[SBLiftToWakeManager _idleTimerCoordinator];
-[SBLiftToWakeManager dealloc];
-[SBLiftToWakeManager liftToWakeController:didObserveTransition:deviceOrientation:];
-[SBLiftToWakeManager invalidate];
-[SBLiftToWakeManager _ignoredTransition:];
-[SBLiftToWakeManager description];
-[SBLiftToWakeManager conformsToCSEventHandling];
-[SBLiftToWakeManager coverSheetIdentifier];
-[SBLiftToWakeManager participantState];
-[SBLiftToWakeManager _setIdleTimerCoordinator:];
-[SBLiftToWakeManager _backlightWillTurnOn:];
-[SBLiftToWakeManager _bumpWakeArbiter];
-[SBLiftToWakeManager _gestureWokeScreen];
-[SBLiftToWakeManager _hardWakeForTransition:orientation:lockScreenManager:];
-[SBLiftToWakeManager _isLockScreenMainPageVisible];
-[SBLiftToWakeManager _liftToWakeController];
-[SBLiftToWakeManager _policyAggregator];
-[SBLiftToWakeManager _setBumpWakeArbiter:];
-[SBLiftToWakeManager _setGestureWokeScreen:];
-[SBLiftToWakeManager _setLiftToWakeController:];
-[SBLiftToWakeManager _setPolicyAggregator:];
-[SBLiftToWakeManager initWithLiftToWakeController:backlightController:lockScreenManager:];
```
