# `SBSystemActionExecuting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"SBSystemAction",R,N) systemAction;
@property (TB,R,N) canBeExecuted;
@property (TB,R,N,GisExecuting) executing;
@property (TQ,R,N) executionGeneration;
@property (Td,R,N) executionStartTime;
@property (Td,R,N) executionEndTime;
@property (TB,R,N) requiresAuthenticationAtLeastOnceSinceBootBeforeExecution;
```

## Instance methods

```
-[SBSystemActionExecuting isExecuting];
-[SBSystemActionExecuting executionEndTime];
-[SBSystemActionExecuting executionStartTime];
-[SBSystemActionExecuting systemAction];
-[SBSystemActionExecuting canBeExecuted];
-[SBSystemActionExecuting cancelPreviewing];
-[SBSystemActionExecuting executeWithContext:executionHandler:completion:];
-[SBSystemActionExecuting executionGeneration];
-[SBSystemActionExecuting previewWithCoordinator:];
-[SBSystemActionExecuting requiresAuthenticationAtLeastOnceSinceBootBeforeExecution];
```
