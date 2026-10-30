# `__CFN_CoreSchedulingSetRunnable`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 1 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" _sem;
@? _setup;
^{_opaque_pthread_t=q^{__darwin_pthread_handler_rec}[8176c]} _tid;
^{__CFRunLoop=} _rl;
q _performCount;
^{__CFRunLoopSource=} _pinnedSource;
[5q] _count;
```

## Class methods

```
+[__CFN_CoreSchedulingSetRunnable _run:];
```

## Instance methods

```
-[__CFN_CoreSchedulingSetRunnable dealloc];
```
