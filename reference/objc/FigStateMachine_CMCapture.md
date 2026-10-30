# `FigStateMachine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 20 instance methods, 2 class methods

## Instance variables

```
@ _owner;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _performsAtomicStateTransitions;
I _currentState;
^{FigStateMachineStateConfiguration=B@@@} _stateConfigurations;
c _stateCount;
@"NSString" _label;
```

## Properties

```
@property (TB,N,V_performsAtomicStateTransitions) performsAtomicStateTransitions;
@property (TI,R) currentState;
@property (T@"NSString",R) label;
@property (T@"NSString",R) currentStateLabel;
```

## Class methods

```
+[FigStateMachine initialize];
+[FigStateMachine indexForState:];
```

## Instance methods

```
-[FigStateMachine transitionToState:];
-[FigStateMachine label];
-[FigStateMachine dealloc];
-[FigStateMachine initWithLabel:stateCount:initialState:owner:];
-[FigStateMachine transitionToState:errorStatus:];
-[FigStateMachine whenTransitioningToState:callHandler:];
-[FigStateMachine whenTransitioningToStateFails:callHandler:];
-[FigStateMachine whenTransitioningFromState:toState:callHandler:];
-[FigStateMachine description];
-[FigStateMachine performsAtomicStateTransitions];
-[FigStateMachine setLabel:forState:];
-[FigStateMachine setPerformsAtomicStateTransitions:];
-[FigStateMachine markStateAsTerminal:];
-[FigStateMachine transitionToState:fromState:];
-[FigStateMachine labelForState:];
-[FigStateMachine whenTransitioningToStatesFail:callHandler:];
-[FigStateMachine transitionToState:fromStates:];
-[FigStateMachine currentState];
-[FigStateMachine currentStateLabel];
-[FigStateMachine whenTransitioningToStates:callHandler:];
```
