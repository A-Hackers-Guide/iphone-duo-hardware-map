# `SBLockScreenIdleTimerCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDashBoardIdleTimerProviderDelegate`, `SBIdleTimerCoordinating`, `SBIdleTimerProviding`
- 3 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SBDashBoardIdleTimerProvider" _dashBoardIdleTimerProvider;
@"NSHashTable" _observers;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
```

## Properties

```
@property (T@"SBDashBoardIdleTimerProvider",&,N,V_dashBoardIdleTimerProvider) dashBoardIdleTimerProvider;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"SBIdleTimerCoordinatorHelper",&,N,V_idleTimerCoordinatorHelper) idleTimerCoordinatorHelper;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBLockScreenIdleTimerCoordinator idleTimerProvider:didProposeBehavior:forReason:];
-[SBLockScreenIdleTimerCoordinator idleTimerDidRefresh:];
-[SBLockScreenIdleTimerCoordinator removeObserver:];
-[SBLockScreenIdleTimerCoordinator init];
-[SBLockScreenIdleTimerCoordinator idleTimerDidExpire:];
-[SBLockScreenIdleTimerCoordinator addObserver:];
-[SBLockScreenIdleTimerCoordinator shouldUseLockScreenIdleTimer];
-[SBLockScreenIdleTimerCoordinator resetIdleTimer];
-[SBLockScreenIdleTimerCoordinator hasIdleTimerBehaviors];
-[SBLockScreenIdleTimerCoordinator setObservers:];
-[SBLockScreenIdleTimerCoordinator observers];
-[SBLockScreenIdleTimerCoordinator idleTimerDidWarn:];
-[SBLockScreenIdleTimerCoordinator coordinatorRequestedIdleTimerBehavior:];
-[SBLockScreenIdleTimerCoordinator dashBoardIdleTimerProvider];
-[SBLockScreenIdleTimerCoordinator dashBoardIdleTimerProvider:didProposeBehavior:reason:];
-[SBLockScreenIdleTimerCoordinator idleTimerCoordinatorHelper];
-[SBLockScreenIdleTimerCoordinator idleTimerDidChange:];
-[SBLockScreenIdleTimerCoordinator idleTimerWillRefresh:];
-[SBLockScreenIdleTimerCoordinator requestIdleTimerBehaviorForReason:];
-[SBLockScreenIdleTimerCoordinator requestIdleTimerDisabledAssertionFromController:reason:];
-[SBLockScreenIdleTimerCoordinator requestRemoveIdleTimerDisabledAssertionFromController:reason:];
-[SBLockScreenIdleTimerCoordinator setDashBoardIdleTimerProvider:];
-[SBLockScreenIdleTimerCoordinator setIdleTimerCoordinatorHelper:];
-[SBLockScreenIdleTimerCoordinator updateIdleTimerBehaviorFromIdleTimerController:reason:];
```
