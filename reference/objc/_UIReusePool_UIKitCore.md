# `_UIReusePool`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 6 instance methods, 3 class methods

## Instance variables

```
@"NSMutableSet" _reuseSet;
Q _purgePolicy;
@"NSObject<OS_dispatch_queue>" _reuseSetAccessQueue;
```

## Properties

```
@property (TQ,R,N) purgePolicy;
```

## Class methods

```
+[_UIReusePool initialize];
+[_UIReusePool __applicationDidEnterBackground:];
+[_UIReusePool __applicationWillEnterForeground:];
```

## Instance methods

```
-[_UIReusePool init];
-[_UIReusePool addObject:];
-[_UIReusePool drainPool];
-[_UIReusePool initWithPolicy:];
-[_UIReusePool purgePolicy];
-[_UIReusePool reusableObject];
```
