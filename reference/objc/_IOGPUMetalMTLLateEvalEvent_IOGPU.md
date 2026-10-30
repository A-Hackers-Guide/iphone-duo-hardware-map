# `_IOGPUMetalMTLLateEvalEvent`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMTLLateEvalEvent`
- Protocols: `MTLLateEvalEvent`
- 4 instance variables, 7 properties, 9 instance methods, 0 class methods

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
@property (TQ,D) signaledValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_IOGPUMetalMTLLateEvalEvent initWithDevice:];
-[_IOGPUMetalMTLLateEvalEvent device];
-[_IOGPUMetalMTLLateEvalEvent label];
-[_IOGPUMetalMTLLateEvalEvent setLabel:];
-[_IOGPUMetalMTLLateEvalEvent dealloc];
-[_IOGPUMetalMTLLateEvalEvent newSharedEventHandle];
-[_IOGPUMetalMTLLateEvalEvent notifyListener:atValue:block:];
-[_IOGPUMetalMTLLateEvalEvent waitUntilSignaledValue:timeoutMS:];
-[_IOGPUMetalMTLLateEvalEvent retainedLabel];
```
