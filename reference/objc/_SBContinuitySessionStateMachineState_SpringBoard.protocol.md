# `_SBContinuitySessionStateMachineState` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BSInvalidatable`
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@?,C,N) stateUpdateHandler;
@property (T@?,C,N) stateTransitionHandler;
@property (T@?,C,N) invalidStateHandler;
@property (T@"<_SBContinuitySessionStateMachineClientExternallyBlockedReasonsProvider>",W,N) clientExternallyBlockedReasonsProvider;
```

## Instance methods

```
-[_SBContinuitySessionStateMachineState stateTransitionHandler];
-[_SBContinuitySessionStateMachineState clientExternallyBlockedReasonsProvider];
-[_SBContinuitySessionStateMachineState enteredStateFrom:];
-[_SBContinuitySessionStateMachineState exitedStateTo:];
-[_SBContinuitySessionStateMachineState invalidStateHandler];
-[_SBContinuitySessionStateMachineState noteClientDidUpdateExternallyBlockedReasons];
-[_SBContinuitySessionStateMachineState setClientExternallyBlockedReasonsProvider:];
-[_SBContinuitySessionStateMachineState setInvalidStateHandler:];
-[_SBContinuitySessionStateMachineState setStateTransitionHandler:];
-[_SBContinuitySessionStateMachineState setStateUpdateHandler:];
-[_SBContinuitySessionStateMachineState stateUpdateHandler];
```
