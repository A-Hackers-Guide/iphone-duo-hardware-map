# `_UIStateMachine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
r^{?={_UIStateMachineMeta=QQQ}^{_UIStateMachineDebugging}[0{?=@?[0{_UIStateTransition=@?@?b16b8b8}]}]} _spec;
B _externalSpec;
Q _state;
```

## Properties

```
@property (T^v,R,N) spec;
@property (TQ,R,N,V_state) state;
```

## Instance methods

```
-[_UIStateMachine spec];
-[_UIStateMachine dealloc];
-[_UIStateMachine state];
-[_UIStateMachine handleEvent:withContext:];
-[_UIStateMachine initWithSpec:initialState:];
-[_UIStateMachine initWithStates:events:initialState:];
-[_UIStateMachine setStateChangeObserver:observer:];
-[_UIStateMachine setStaticTransitionFromState:withEvent:toState:];
-[_UIStateMachine setTransitionHandlerForState:withEvent:transitionHandler:];
-[_UIStateMachine setTransitionHandlerForState:withEvent:transitionHandler:postTransitionHandler:];
```
