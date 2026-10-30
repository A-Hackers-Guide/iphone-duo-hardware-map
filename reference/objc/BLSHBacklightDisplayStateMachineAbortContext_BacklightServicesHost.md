# `BLSHBacklightDisplayStateMachineAbortContext`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHWatchdogAbortContext`
- 11 instance variables, 12 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SWSystemSleepMonitorAggregateState" _sleepMonitorAggregateState;
Q _abortTimestamp;
q _displayMode;
q _prewarmingDisplayMode;
q _lastSteadyStateDisplayMode;
q _caDisplayState;
q _cbDisplayMode;
B _hasEnsureFlipbookCurrent;
I _payloadSize;
Q _abortReason;
r^v _payload;
```

## Properties

```
@property (TQ,R,N,V_abortReason) abortReason;
@property (Tr^v,R,N,V_payload) payload;
@property (TI,R,N,V_payloadSize) payloadSize;
@property (TB,R,N,V_hasEnsureFlipbookCurrent) hasEnsureFlipbookCurrent;
@property (T@"NSString",R,C,N) abortReasonString;
@property (TB,?,R,N) wantsPanic;
@property (Td,?,R,N) panicDelay;
@property (TB,?,R,N) wantsWaitPastFireForCompletionAndTailspin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBacklightDisplayStateMachineAbortContext dealloc];
-[BLSHBacklightDisplayStateMachineAbortContext payload];
-[BLSHBacklightDisplayStateMachineAbortContext description];
-[BLSHBacklightDisplayStateMachineAbortContext hasEnsureFlipbookCurrent];
-[BLSHBacklightDisplayStateMachineAbortContext payloadSize];
-[BLSHBacklightDisplayStateMachineAbortContext _populatePayload];
-[BLSHBacklightDisplayStateMachineAbortContext abortReason];
-[BLSHBacklightDisplayStateMachineAbortContext abortReasonString];
-[BLSHBacklightDisplayStateMachineAbortContext initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:sleepMonitorAggregateState:hasEnsureFlipbookCurrent:];
-[BLSHBacklightDisplayStateMachineAbortContext setSleepImminentAbortReason];
-[BLSHBacklightDisplayStateMachineAbortContext wantsPanic];
```
