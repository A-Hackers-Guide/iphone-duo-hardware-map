# `SBAnalyticsStateMachineEdge`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 5 properties, 9 instance methods, 2 class methods

## Instance variables

```
Q _fromState;
@? _transition;
```

## Properties

```
@property (TQ,R,N,V_fromState) fromState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAnalyticsStateMachineEdge edgeFromState:toState:uponEvent:];
+[SBAnalyticsStateMachineEdge edgeFromState:transition:];
```

## Instance methods

```
-[SBAnalyticsStateMachineEdge debugDescription];
-[SBAnalyticsStateMachineEdge succinctDescriptionBuilder];
-[SBAnalyticsStateMachineEdge descriptionWithMultilinePrefix:];
-[SBAnalyticsStateMachineEdge succinctDescription];
-[SBAnalyticsStateMachineEdge fromState];
-[SBAnalyticsStateMachineEdge description];
-[SBAnalyticsStateMachineEdge descriptionBuilderWithMultilinePrefix:];
-[SBAnalyticsStateMachineEdge handleEvent:withContext:];
-[SBAnalyticsStateMachineEdge initWithFromState:transition:];
```
