# `_MTLIOAccelMTLEvent`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOAccelMTLEvent`
- Protocols: `MTLEventSPI`
- 5 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelDevice<MTLDevice>" _device;
Q _labelTraceID;
@"NSString" _label;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _labelLock;
B _enableBarrier;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",C,D) label;
@property (TB,N,V_enableBarrier) enableBarrier;
@property (TB,R) supportsRollback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIOAccelMTLEvent initWithDevice:];
-[_MTLIOAccelMTLEvent device];
-[_MTLIOAccelMTLEvent label];
-[_MTLIOAccelMTLEvent setLabel:];
-[_MTLIOAccelMTLEvent dealloc];
-[_MTLIOAccelMTLEvent enableBarrier];
-[_MTLIOAccelMTLEvent initWithDevice:options:];
-[_MTLIOAccelMTLEvent retainedLabel];
-[_MTLIOAccelMTLEvent setEnableBarrier:];
```
