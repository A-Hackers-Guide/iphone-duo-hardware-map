# `LACThreadSafeQueue`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableArray" _elements;
B _isDraining;
```

## Properties

```
@property (Tq,R) count;
```

## Instance methods

```
-[LACThreadSafeQueue init];
-[LACThreadSafeQueue count];
-[LACThreadSafeQueue dequeue];
-[LACThreadSafeQueue enqueue:];
-[LACThreadSafeQueue drain:];
```
