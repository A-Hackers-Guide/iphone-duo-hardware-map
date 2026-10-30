# `UIKeyboardTaskQueue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _executingOnMainThread;
@"NSConditionLock" _lock;
@"NSMutableArray" _tasks;
@"NSMutableArray" _deferredTasks;
@"UIKeyboardTaskExecutionContext" _executionContext;
@"UIKeyboardTaskEntry" _mainThreadContinuation;
@"NSArray" _activeOriginator;
@? _activeTaskBreadcrumb;
@? _diagnosticTrampoline;
```

## Properties

```
@property (T@"UIKeyboardTaskExecutionContext",&,N,V_executionContext) executionContext;
@property (T@"NSArray",&,N,V_activeOriginator) activeOriginator;
@property (T@?,C,N,V_activeTaskBreadcrumb) activeTaskBreadcrumb;
@property (T@?,C,N,V_diagnosticTrampoline) diagnosticTrampoline;
```

## Instance methods

```
-[UIKeyboardTaskQueue performSingleTask:breadcrumb:];
-[UIKeyboardTaskQueue addAndReturnTask:breadcrumb:];
-[UIKeyboardTaskQueue activeTaskBreadcrumb];
-[UIKeyboardTaskQueue addDeferredTask:];
-[UIKeyboardTaskQueue setExecutionContext:];
-[UIKeyboardTaskQueue performTaskOnMainThread:breadcrumb:waitUntilDone:];
-[UIKeyboardTaskQueue addTask:];
-[UIKeyboardTaskQueue init];
-[UIKeyboardTaskQueue addDeferredTask:breadcrumb:];
-[UIKeyboardTaskQueue performTask:breadcrumb:];
-[UIKeyboardTaskQueue performTask:];
-[UIKeyboardTaskQueue setActiveTaskBreadcrumb:];
-[UIKeyboardTaskQueue scheduleTask:timeInterval:repeats:];
-[UIKeyboardTaskQueue activeOriginator];
-[UIKeyboardTaskQueue isMainThreadExecutingTask];
-[UIKeyboardTaskQueue promoteDeferredTaskIfIdle];
-[UIKeyboardTaskQueue tryLockWhenReadyForMainThread];
-[UIKeyboardTaskQueue executionContext];
-[UIKeyboardTaskQueue _lockWhenReadyForMainThread];
-[UIKeyboardTaskQueue performSingleTask:];
-[UIKeyboardTaskQueue isEmpty];
-[UIKeyboardTaskQueue performDeferredTaskIfIdle];
-[UIKeyboardTaskQueue setActiveOriginator:];
-[UIKeyboardTaskQueue continueExecutionOnMainThread];
-[UIKeyboardTaskQueue lock];
-[UIKeyboardTaskQueue setDiagnosticTrampoline:];
-[UIKeyboardTaskQueue waitUntilAllTasksAreFinished];
-[UIKeyboardTaskQueue waitUntilTaskIsFinished:];
-[UIKeyboardTaskQueue scheduleTask:timeInterval:repeats:breadcrumb:];
-[UIKeyboardTaskQueue finishExecution];
-[UIKeyboardTaskQueue unlock];
-[UIKeyboardTaskQueue lockWhenReadyForMainThread];
-[UIKeyboardTaskQueue addTask:breadcrumb:];
-[UIKeyboardTaskQueue diagnosticTrampoline];
```
