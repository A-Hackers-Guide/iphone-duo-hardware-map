# `UIKeyboardTaskExecutionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIKeyboardTaskExecutionContext" _parentExecutionContext;
@? _continuation;
@? _pendingCompletionBlock;
@ _info;
@"UIKeyboardTaskQueue" _executionQueue;
```

## Properties

```
@property (T@"UIKeyboardTaskQueue",R,N,V_executionQueue) executionQueue;
@property (T@,&,N,V_info) info;
```

## Instance methods

```
-[UIKeyboardTaskExecutionContext returnExecutionToParentWithInfo:];
-[UIKeyboardTaskExecutionContext info];
-[UIKeyboardTaskExecutionContext init];
-[UIKeyboardTaskExecutionContext setInfo:];
-[UIKeyboardTaskExecutionContext initWithParentContext:continuation:];
-[UIKeyboardTaskExecutionContext transferExecutionToMainThreadWithTask:breadcrumb:];
-[UIKeyboardTaskExecutionContext transferExecutionToMainThreadWithTask:];
-[UIKeyboardTaskExecutionContext takeOwnershipOfPendingCompletionBlock];
-[UIKeyboardTaskExecutionContext initWithExecutionQueue:];
-[UIKeyboardTaskExecutionContext childWithContinuation:];
-[UIKeyboardTaskExecutionContext setPendingCompletionBlock:];
-[UIKeyboardTaskExecutionContext returnExecutionToParent];
-[UIKeyboardTaskExecutionContext executionQueue];
```
