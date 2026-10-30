# `_UIAsyncInvocationObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _postCompletionQueue;
@"NSObject<OS_dispatch_queue>" _completionQueueManagementQueue;
B _suspendedPostCompletionQueue;
B _resumedPostCompletionQueue;
```

## Class methods

```
+[_UIAsyncInvocationObserver whenInvocationsCompleteForObservers:do:];
```

## Instance methods

```
-[_UIAsyncInvocationObserver init];
-[_UIAsyncInvocationObserver whenCompleteDo:];
-[_UIAsyncInvocationObserver _didCompleteInvocation];
```
