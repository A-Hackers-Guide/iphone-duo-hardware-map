# `SBAbstractSystemActionExecutor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemActionExecuting`
- 5 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _executionCompletions;
@"SBSystemAction" _systemAction;
Q _executionGeneration;
d _executionStartTime;
d _executionEndTime;
```

## Properties

```
@property (T@"SBSystemAction",R,N,V_systemAction) systemAction;
@property (TB,R,N) canBeExecuted;
@property (TB,R,N,GisExecuting) executing;
@property (TQ,R,N,V_executionGeneration) executionGeneration;
@property (Td,R,N,V_executionStartTime) executionStartTime;
@property (Td,R,N,V_executionEndTime) executionEndTime;
@property (TB,R,N) requiresAuthenticationAtLeastOnceSinceBootBeforeExecution;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAbstractSystemActionExecutor isExecuting];
-[SBAbstractSystemActionExecutor executionEndTime];
-[SBAbstractSystemActionExecutor executionStartTime];
-[SBAbstractSystemActionExecutor initWithSystemAction:];
-[SBAbstractSystemActionExecutor _isExecuting];
-[SBAbstractSystemActionExecutor systemAction];
-[SBAbstractSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:];
-[SBAbstractSystemActionExecutor _canBeExecuted];
-[SBAbstractSystemActionExecutor _cancelPreviewing];
-[SBAbstractSystemActionExecutor _finishExecutingWithResult:];
-[SBAbstractSystemActionExecutor _previewWithCoordinator:];
-[SBAbstractSystemActionExecutor _requiresAuthenticationAtLeastOnceSinceBootBeforeExecution];
-[SBAbstractSystemActionExecutor canBeExecuted];
-[SBAbstractSystemActionExecutor cancelPreviewing];
-[SBAbstractSystemActionExecutor executeWithContext:executionHandler:completion:];
-[SBAbstractSystemActionExecutor executionGeneration];
-[SBAbstractSystemActionExecutor previewWithCoordinator:];
-[SBAbstractSystemActionExecutor requiresAuthenticationAtLeastOnceSinceBootBeforeExecution];
```
