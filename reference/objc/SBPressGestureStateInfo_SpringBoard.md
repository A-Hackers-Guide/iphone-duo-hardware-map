# `SBPressGestureStateInfo`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isCoalescing;
q _state;
d _expirationTime;
q _stateUponExpiration;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (TB,N,V_isCoalescing) isCoalescing;
@property (Td,N,V_expirationTime) expirationTime;
@property (Tq,N,V_stateUponExpiration) stateUponExpiration;
```

## Instance methods

```
-[SBPressGestureStateInfo setState:];
-[SBPressGestureStateInfo isCoalescing];
-[SBPressGestureStateInfo init];
-[SBPressGestureStateInfo setExpirationTime:];
-[SBPressGestureStateInfo expirationTime];
-[SBPressGestureStateInfo state];
-[SBPressGestureStateInfo setIsCoalescing:];
-[SBPressGestureStateInfo setStateUponExpiration:];
-[SBPressGestureStateInfo stateUponExpiration];
```
