# `BLSHBacklightEnvironmentStateMachine`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHEnvironmentTransitionStateDelegate`, `BSInvalidatable`
- 28 instance variables, 14 properties, 27 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSHBacklightEnvironmentPresentation" _lock_presentation;
@"NSString" _delegateLoggingName;
@"<BLSHInactiveBudgetPolicing_Private>" _inactiveBudgetPolicy;
@"<BLSHOSTimerProviding>" _osTimerProvider;
@"<BLSHBacklightPlatformProvider>" _platformProvider;
@"<BLSHDisplayFlipbookStateProvider>" _displayFlipbookStateProvider;
@"NSMapTable" _transitionStates;
@"NSMutableSet" _lock_updatingVisualStateTransitionStates;
@"NSMutableSet" _lock_updatingDateSpecifierTransitionStates;
@"BLSHPresentationDateSpecifier" _updatingSpecifier;
@"NSMutableArray" _performEventHistory;
@"NSMutableArray" _didBeginUpdateHistory;
@"NSMutableArray" _didCompleteUpdateHistory;
@"BLSSetPresentationOperation" _lock_setPresentationOperation;
q _lock_targetBacklightState;
q _lock_performEventTargetBacklightState;
@"NSMutableSet" _lock_staleEnvironmentsThatNeedDeferredUpdate;
@"NSMutableArray" _lock_addingEnvironmentsContexts;
B _pendingNotifyBeganUpdatingState;
B _updatingState;
B _lock_updatingFlipbookVisualState;
B _updatingFlipbookIsFlipbook;
q _lock_updatingFlipbookBacklightState;
@"BLSHPresentationDateSpecifier" _updatingFlipbookSpecifier;
B _lock_invalidated;
Q _stateHandler;
@"<BLSHBacklightEnvironmentStateMachineDelegate>" _lock_delegate;
```

## Properties

```
@property (T@"BLSHBacklightEnvironmentPresentation",R,N) presentation;
@property (T@"<BLSHBacklightEnvironmentStateMachineDelegate>",R,W,N,V_lock_delegate) lock_delegate;
@property (T@"NSSet",R,C,N) updatingVisualStateTransitionStates;
@property (T@"NSSet",R,C,N) updatingDateSpecifierTransitionStates;
@property (TB,R,N) pendingNotifyBeganUpdatingState;
@property (TB,R,N,GisUpdatingState) updatingState;
@property (TB,R,N,GisUpdatingPresentation) updatingPresentation;
@property (T@"<BLSHInactiveBudgetPolicing_Private>",R,N,V_inactiveBudgetPolicy) inactiveBudgetPolicy;
@property (T@"<BLSHOSTimerProviding>",R,N,V_osTimerProvider) osTimerProvider;
@property (T@"NSString",R,C,N) delegateLoggingName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBacklightEnvironmentStateMachine presentation];
-[BLSHBacklightEnvironmentStateMachine debugDescription];
-[BLSHBacklightEnvironmentStateMachine dealloc];
-[BLSHBacklightEnvironmentStateMachine delegateLoggingName];
-[BLSHBacklightEnvironmentStateMachine invalidate];
-[BLSHBacklightEnvironmentStateMachine description];
-[BLSHBacklightEnvironmentStateMachine isUpdatingState];
-[BLSHBacklightEnvironmentStateMachine osTimerProvider];
-[BLSHBacklightEnvironmentStateMachine pendingNotifyBeganUpdatingState];
-[BLSHBacklightEnvironmentStateMachine inactiveBudgetPolicy];
-[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:displayFlipbookStateProvider:inactiveBudgetPolicy:osTimerProvider:platformProvider:];
-[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:];
-[BLSHBacklightEnvironmentStateMachine isUpdatingPresentation];
-[BLSHBacklightEnvironmentStateMachine lock_delegate];
-[BLSHBacklightEnvironmentStateMachine performEvent:withInitialSpecifier:performBacklightRamp:];
-[BLSHBacklightEnvironmentStateMachine populateEnvironmentStateMachineStruct:];
-[BLSHBacklightEnvironmentStateMachine setPresentation:withTargetBacklightState:];
-[BLSHBacklightEnvironmentStateMachine transitionState:didBeginUpdateToBacklightState:visualState:];
-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:];
-[BLSHBacklightEnvironmentStateMachine transitionState:didUpdateToDateSpecifier:];
-[BLSHBacklightEnvironmentStateMachine updateAllEnvironmentsInPresentation];
-[BLSHBacklightEnvironmentStateMachine updateEnvironment:];
-[BLSHBacklightEnvironmentStateMachine updateFlipbookVisualState:backlightState:withInitialSpecifier:];
-[BLSHBacklightEnvironmentStateMachine updateToExplicitVisualState:specifier:];
-[BLSHBacklightEnvironmentStateMachine updateToSpecifier:];
-[BLSHBacklightEnvironmentStateMachine updatingDateSpecifierTransitionStates];
-[BLSHBacklightEnvironmentStateMachine updatingVisualStateTransitionStates];
```
