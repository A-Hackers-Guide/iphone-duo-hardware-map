# `_MTLSharedEvent`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOSurfaceSharedEvent`
- Protocols: `MTLSharedEventSPI`
- 3 instance variables, 10 properties, 17 instance methods, 1 class methods

## Instance variables

```
Q _labelTraceID;
@"NSString" _label;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _labelLock;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C,D) label;
@property (TQ,R,V_labelTraceID) labelTraceID;
@property (T@"IOSurfaceSharedEvent",R,N) IOSurfaceSharedEvent;
@property (TB,R) supportsRollback;
@property (TQ) signaledValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_MTLSharedEvent supportsSecureCoding];
```

## Instance methods

```
-[_MTLSharedEvent device];
-[_MTLSharedEvent label];
-[_MTLSharedEvent setLabel:];
-[_MTLSharedEvent dealloc];
-[_MTLSharedEvent initWithOptions:];
-[_MTLSharedEvent initWithMachPort:];
-[_MTLSharedEvent newSharedEventHandle];
-[_MTLSharedEvent notifyListener:atValue:block:];
-[_MTLSharedEvent IOSurfaceSharedEvent];
-[_MTLSharedEvent supportsRollback];
-[_MTLSharedEvent encodeConditionalEventAbortCommandArgs:];
-[_MTLSharedEvent encodeKernelSignalEventCommandArgs:value:];
-[_MTLSharedEvent encodeKernelWaitEventCommandArgs:value:];
-[_MTLSharedEvent encodeKernelWaitEventCommandArgs:value:timeout:];
-[_MTLSharedEvent initWithSharedEventHandle:];
-[_MTLSharedEvent labelTraceID];
-[_MTLSharedEvent retainedLabel];
```
