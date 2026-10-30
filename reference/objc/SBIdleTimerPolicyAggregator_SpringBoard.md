# `SBIdleTimerPolicyAggregator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerObserving`, `SBIdleTimerGlobalCoordinatorDelegate`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBProximitySensorCoordinator" _proximitySensorCoordinator;
@"SBScreenLongevityController" _screenLongevityController;
@"<SBIdleTimer>" _idleTimer;
@"<SBIdleTimerIdleEventHandler>" _idleEventHandler;
b1 _disableAutoDimming;
```

## Properties

```
@property (T@"<SBIdleTimer>",&,N,S_setIdleTimer:,V_idleTimer) idleTimer;
@property (T@"SBBacklightCoordinator",&,N,V_backlightCoordinator) backlightCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerPolicyAggregator idleTimer];
-[SBIdleTimerPolicyAggregator idleTimerDidRefresh:];
-[SBIdleTimerPolicyAggregator idleTimerDidExpire:];
-[SBIdleTimerPolicyAggregator idleTimerDidResetForUserAttention:];
-[SBIdleTimerPolicyAggregator setBacklightCoordinator:];
-[SBIdleTimerPolicyAggregator idleTimerDidWarn:];
-[SBIdleTimerPolicyAggregator backlightCoordinator];
-[SBIdleTimerPolicyAggregator _setIdleTimer:];
-[SBIdleTimerPolicyAggregator idleTimerGlobalCoordinator:didActivateIdleTimer:];
-[SBIdleTimerPolicyAggregator initWithProximitySensorCoordinator:idleEventHandler:screenLongevityController:];
```
