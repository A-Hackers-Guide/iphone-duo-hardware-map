# `SBBlockSystemActionExecutor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSystemActionExecutor`
- 2 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemActionPreviewInvalidatable>" _previewAssertion;
B _executing;
```

## Properties

```
@property (T@"SBSystemAction<SBSystemActionActionBlockProviding>",R,N) systemAction;
```

## Instance methods

```
-[SBBlockSystemActionExecutor initWithSystemAction:];
-[SBBlockSystemActionExecutor _isExecuting];
-[SBBlockSystemActionExecutor systemAction];
-[SBBlockSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:];
-[SBBlockSystemActionExecutor _canBeExecuted];
-[SBBlockSystemActionExecutor _cancelPreviewing];
-[SBBlockSystemActionExecutor _handleExecutionBlockFinishedWithResult:];
-[SBBlockSystemActionExecutor _previewWithCoordinator:];
-[SBBlockSystemActionExecutor _requiresAuthenticationAtLeastOnceSinceBootBeforeExecution];
```
