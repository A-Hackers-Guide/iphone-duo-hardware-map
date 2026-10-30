# `_IOGPUMetalMTLEvent`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMTLEvent`
- Protocols: `MTLEvent`
- 4 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice<MTLDevice>" _device;
Q _labelTraceID;
@"NSString" _label;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _labelLock;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",C,D) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_IOGPUMetalMTLEvent initWithDevice:];
-[_IOGPUMetalMTLEvent device];
-[_IOGPUMetalMTLEvent label];
-[_IOGPUMetalMTLEvent setLabel:];
-[_IOGPUMetalMTLEvent dealloc];
-[_IOGPUMetalMTLEvent initWithDevice:options:];
-[_IOGPUMetalMTLEvent retainedLabel];
```
