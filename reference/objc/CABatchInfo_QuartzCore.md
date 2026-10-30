# `CABatchInfo`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q _batch_name;
I _port;
{SpinLock="_l"{?="x"i}} _lock;
B _invalidated;
```

## Instance methods

```
-[CABatchInfo newBatchHandle];
-[CABatchInfo dealloc];
-[CABatchInfo newXPCBatchHandle];
```
