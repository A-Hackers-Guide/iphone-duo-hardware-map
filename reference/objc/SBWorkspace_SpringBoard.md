# `SBWorkspace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerProviding`, `SBIdleTimerCoordinating`
- 2 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"FBWorkspaceEventQueue" _eventQueue;
@"SBWorkspaceTransaction" _currentTransaction;
```

## Properties

```
@property (T@"FBWorkspaceEventQueue",R,N,V_eventQueue) eventQueue;
@property (T@"SBWorkspaceTransaction",R,N,V_currentTransaction) currentTransaction;
@property (TB,R,N) hasIdleTimerBehaviors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWorkspace mainWorkspace];
```

## Instance methods

```
-[SBWorkspace requestTransitionWithOptions:builder:validator:];
-[SBWorkspace createRequestWithOptions:];
-[SBWorkspace eventQueue];
-[SBWorkspace currentTransaction];
-[SBWorkspace idleTimerProvider:didProposeBehavior:forReason:];
-[SBWorkspace init];
-[SBWorkspace transactionForTransitionRequest:];
-[SBWorkspace createRequestForApplicationActivation:options:];
-[SBWorkspace _executeTransitionRequest:options:validator:];
-[SBWorkspace requestTransitionWithOptions:displayConfiguration:builder:validator:];
-[SBWorkspace executeTransitionRequest:withValidator:];
-[SBWorkspace requestTransitionWithBuilder:];
-[SBWorkspace executeTransitionRequest:];
-[SBWorkspace createRequestWithOptions:displayConfiguration:];
-[SBWorkspace hasIdleTimerBehaviors];
-[SBWorkspace initWithEventQueue:];
-[SBWorkspace requestTransitionWithOptions:displayConfiguration:builder:];
-[SBWorkspace createRequestForApplicationActivation:withDisplayConfiguration:options:];
-[SBWorkspace coordinatorRequestedIdleTimerBehavior:];
```
