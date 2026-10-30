# `SBDashBoardIdleTimerProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerObserving`, `BSDescriptionProviding`
- 5 instance variables, 7 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<SBIdleTimer>" _idleTimer;
@"<SBFIdleTimerBehaviorProviding>" _idleTimerProvider;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"NSMutableSet" _disabledIdleTimerAssertions;
@"<SBDashBoardIdleTimerProviderDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBDashBoardIdleTimerProviderDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBIdleTimer>",&,N,V_idleTimer) idleTimer;
@property (TB,R,N,GisIdleTimerEnabled) idleTimerEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardIdleTimerProvider idleTimer];
-[SBDashBoardIdleTimerProvider setIdleTimer:];
-[SBDashBoardIdleTimerProvider initWithDelegate:];
-[SBDashBoardIdleTimerProvider addDisabledIdleTimerAssertionReason:];
-[SBDashBoardIdleTimerProvider succinctDescriptionBuilder];
-[SBDashBoardIdleTimerProvider idleTimerDidRefresh:];
-[SBDashBoardIdleTimerProvider dealloc];
-[SBDashBoardIdleTimerProvider removeDisabledIdleTimerAssertionReason:];
-[SBDashBoardIdleTimerProvider descriptionWithMultilinePrefix:];
-[SBDashBoardIdleTimerProvider succinctDescription];
-[SBDashBoardIdleTimerProvider idleTimerDidExpire:];
-[SBDashBoardIdleTimerProvider setDelegate:];
-[SBDashBoardIdleTimerProvider _copyIdleTimerBehaviorForBehaviorProvider:];
-[SBDashBoardIdleTimerProvider updateIdleTimerWithIdleDimProvider:reason:];
-[SBDashBoardIdleTimerProvider delegate];
-[SBDashBoardIdleTimerProvider resetIdleTimer];
-[SBDashBoardIdleTimerProvider _proposeIdleTimerBehavior:forReason:];
-[SBDashBoardIdleTimerProvider isIdleTimerEnabled];
-[SBDashBoardIdleTimerProvider isDisabledAssertionActiveForReason:];
-[SBDashBoardIdleTimerProvider idleTimerDidWarn:];
-[SBDashBoardIdleTimerProvider effectiveIdleTimerBehavior];
-[SBDashBoardIdleTimerProvider _proposeEffectiveIdleTimerBehaviorForReason:];
-[SBDashBoardIdleTimerProvider descriptionBuilderWithMultilinePrefix:];
```
