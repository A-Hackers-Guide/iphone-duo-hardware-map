# `UIKeyboardTaskSubqueue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"UIKeyboardTaskExecutionContext" _context;
```

## Class methods

```
+[UIKeyboardTaskSubqueue subqueueWithExecutionContext:];
```

## Instance methods

```
-[UIKeyboardTaskSubqueue dispatchAsync:];
-[UIKeyboardTaskSubqueue dispatchAsync:breadcrumb:];
-[UIKeyboardTaskSubqueue initWithExecutionContext:];
-[UIKeyboardTaskSubqueue returnExecutionToParentQueue];
```
