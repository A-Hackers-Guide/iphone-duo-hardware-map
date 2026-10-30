# `SBAtomicObjectQueue`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableArray" _data;
```

## Instance methods

```
-[SBAtomicObjectQueue init];
-[SBAtomicObjectQueue dequeue];
-[SBAtomicObjectQueue enqueue:];
```
