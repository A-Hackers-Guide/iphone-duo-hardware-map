# `SBLinkSystemActionExecutor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSystemActionExecutor`
- Protocols: `WFWorkflowRunnerClientDelegate`
- 3 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemActionPreviewInvalidatable>" _previewAssertion;
@"WFStaccatoWorkflowRunnerClient" _runnerClient;
@"NSObject<OS_dispatch_queue>" _prewarmQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLinkSystemActionExecutor workflowRunnerClient:didFinishRunningWorkflowWithOutput:error:cancelled:];
-[SBLinkSystemActionExecutor workflowRunnerClient:didStartRunningWorkflowWithProgress:];
-[SBLinkSystemActionExecutor initWithSystemAction:];
-[SBLinkSystemActionExecutor _isExecuting];
-[SBLinkSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:];
-[SBLinkSystemActionExecutor _canBeExecuted];
-[SBLinkSystemActionExecutor _cancelPreviewing];
-[SBLinkSystemActionExecutor _finishExecutingWithResult:];
-[SBLinkSystemActionExecutor _previewWithCoordinator:];
-[SBLinkSystemActionExecutor _requiresAuthenticationAtLeastOnceSinceBootBeforeExecution];
```
