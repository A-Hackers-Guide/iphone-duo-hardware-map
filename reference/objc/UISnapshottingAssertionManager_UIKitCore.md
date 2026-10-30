# `UISnapshottingAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} lock;
@"NSMutableSet" _heldAssertions;
```

## Class methods

```
+[UISnapshottingAssertionManager sharedInstance];
```

## Instance methods

```
-[UISnapshottingAssertionManager init];
-[UISnapshottingAssertionManager dealloc];
-[UISnapshottingAssertionManager _init];
-[UISnapshottingAssertionManager acquireNewAssertion];
-[UISnapshottingAssertionManager executeIfNoActiveAssertions:];
-[UISnapshottingAssertionManager relinquishAssertion:];
-[UISnapshottingAssertionManager withLock:];
```
