# `SBAnalyticsStateMachineEventHandler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFAnalyticsBackendEventHandling`
- 2 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
Q _currentState;
@"NSMutableArray" _edges;
```

## Properties

```
@property (TQ,R,N,V_currentState) currentState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAnalyticsStateMachineEventHandler init];
-[SBAnalyticsStateMachineEventHandler currentState];
-[SBAnalyticsStateMachineEventHandler handleEvent:withContext:];
-[SBAnalyticsStateMachineEventHandler addEdge:];
```
