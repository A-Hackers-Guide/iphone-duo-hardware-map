# `CABatchHandle`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 0 properties, 8 instance methods, 2 class methods

## Instance variables

```
Q _handle_name;
Q _batch_name;
I _port;
{SpinLock="_l"{?="x"i}} _lock;
B _invalidated;
```

## Class methods

```
+[CABatchHandle supportsSecureCoding];
+[CABatchHandle createFromXPCRepresentation:];
```

## Instance methods

```
-[CABatchHandle createXPCRepresentation];
-[CABatchHandle init];
-[CABatchHandle dealloc];
-[CABatchHandle invalidate];
-[CABatchHandle encodeWithCoder:];
-[CABatchHandle description];
-[CABatchHandle initWithCoder:];
-[CABatchHandle copyWithZone:];
```
