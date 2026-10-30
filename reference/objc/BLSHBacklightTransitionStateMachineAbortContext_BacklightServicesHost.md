# `BLSHBacklightTransitionStateMachineAbortContext`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHWatchdogAbortContext`
- 17 instance variables, 12 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"BLSHBacklightAggregateState" _currentState;
@"BLSHBacklightMutableTargetState" _targetState;
@"NSArray" _activeEvents;
@"NSArray" _abortedEvents;
@"BLSHPendingEnvironmentUpdateOperation" _pendingEnvironmentUpdate;
@"BLSHPendingUpdatePresentation" _pendingUpdatePresentation;
@"BLSHPendingUpdateToSpecifier" _pendingUpdateToSpecifier;
@"BLSHPendingUpdateDisplayMode" _pendingUpdateDisplayMode;
@"BLSHEnsureFlipbookCurrentOperation" _ensureFlipbookCurrentOperation;
@"NSArray" _queuedEventsToPerform;
@"BLSBacklightChangeEvent" _pendingPrewarmedEvent;
@"BLSHBacklightEnvironmentStateMachine" _environmentStateMachine;
@"SWSystemSleepMonitorAggregateState" _sleepMonitorAggregateState;
Q _abortTimestamp;
I _payloadSize;
Q _abortReason;
r^v _payload;
```

## Properties

```
@property (TQ,R,N,V_abortReason) abortReason;
@property (Tr^v,R,N,V_payload) payload;
@property (TI,R,N,V_payloadSize) payloadSize;
@property (TB,R,N) hasEnsureFlipbookCurrent;
@property (T@"NSString",R,C,N) abortReasonString;
@property (TB,?,R,N) wantsPanic;
@property (Td,?,R,N) panicDelay;
@property (TB,?,R,N) wantsWaitPastFireForCompletionAndTailspin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHBacklightTransitionStateMachineAbortContext backlightChangeRequestExplanationIdentifierFromString:];
```

## Instance methods

```
-[BLSHBacklightTransitionStateMachineAbortContext dealloc];
-[BLSHBacklightTransitionStateMachineAbortContext payload];
-[BLSHBacklightTransitionStateMachineAbortContext description];
-[BLSHBacklightTransitionStateMachineAbortContext hasEnsureFlipbookCurrent];
-[BLSHBacklightTransitionStateMachineAbortContext payloadSize];
-[BLSHBacklightTransitionStateMachineAbortContext _populatePayload];
-[BLSHBacklightTransitionStateMachineAbortContext abortReason];
-[BLSHBacklightTransitionStateMachineAbortContext abortReasonString];
-[BLSHBacklightTransitionStateMachineAbortContext initWithCurrentState:targetState:activeEvents:abortedEvents:pendingEnvironmentUpdate:pendingUpdatePresentation:pendingUpdateToSpecifier:pendingUpdateDisplayMode:ensureFlipbookCurrentOperation:queuedEventsToPerform:pendingPrewarmedEvent:environmentStateMachine:sleepMonitorAggregateState:];
-[BLSHBacklightTransitionStateMachineAbortContext setSleepImminentAbortReason];
-[BLSHBacklightTransitionStateMachineAbortContext wantsPanic];
```
