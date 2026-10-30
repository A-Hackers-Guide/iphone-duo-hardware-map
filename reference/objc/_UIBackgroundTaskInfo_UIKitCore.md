# `_UIBackgroundTaskInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
Q _taskId;
@? _expireHandler;
@"BKSProcessAssertion" _processAssertion;
@"NSString" _taskName;
q _creationTime;
B _alreadyWarnedAboutExpiration;
```

## Class methods

```
+[_UIBackgroundTaskInfo backgroundTaskAssertionQueue];
```

## Instance methods

```
-[_UIBackgroundTaskInfo initWithProcessAssertion:taskName:expirationHandler:];
-[_UIBackgroundTaskInfo dealloc];
-[_UIBackgroundTaskInfo invalidate];
-[_UIBackgroundTaskInfo description];
-[_UIBackgroundTaskInfo fireExpirationHandler];
```
