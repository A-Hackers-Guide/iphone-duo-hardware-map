# `CAFenceHandle`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 2 properties, 14 instance methods, 7 class methods

## Instance variables

```
Q _handle_name;
Q _fence_name;
I _port;
{Mutex="_m"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _invalidation_mutex;
{SpinLock="_l"{?="x"i}} _lock;
B _invalidated;
B _invalidate_on_dealloc;
```

## Properties

```
@property (TB,R,GisUsable) usable;
@property (TB,R,GisInvalidated) invalidated;
```

## Class methods

```
+[CAFenceHandle supportsSecureCoding];
+[CAFenceHandle handleForPort:fenceId:];
+[CAFenceHandle newFenceFromServer:];
+[CAFenceHandle handleWithPort:data:error:];
+[CAFenceHandle handleFromXPCRepresentation:];
+[CAFenceHandle newFenceFromDefaultServer];
+[CAFenceHandle handleFromXPCRepresentation:error:];
```

## Instance methods

```
-[CAFenceHandle encodeWithBlock:];
-[CAFenceHandle createXPCRepresentation];
-[CAFenceHandle init];
-[CAFenceHandle dealloc];
-[CAFenceHandle fenceId];
-[CAFenceHandle isInvalidated];
-[CAFenceHandle invalidate];
-[CAFenceHandle accessMachPort:];
-[CAFenceHandle encodeWithCoder:];
-[CAFenceHandle description];
-[CAFenceHandle initWithCoder:];
-[CAFenceHandle copyWithZone:];
-[CAFenceHandle copyPort];
-[CAFenceHandle isUsable];
```
