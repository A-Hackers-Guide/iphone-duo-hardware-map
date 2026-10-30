# `IOGPUMetalIOHandleCompressed`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLIOHandleCompressed`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalDevice<MTLDevice>" _dev;
I _vnioID;
Q _globalTraceObjectID;
```

## Properties

```
@property (TI,R,V_vnioID) vnioID;
```

## Instance methods

```
-[IOGPUMetalIOHandleCompressed setLabel:];
-[IOGPUMetalIOHandleCompressed globalTraceObjectID];
-[IOGPUMetalIOHandleCompressed dealloc];
-[IOGPUMetalIOHandleCompressed initWithDevice:path:compressionType:error:uncached:];
-[IOGPUMetalIOHandleCompressed vnioID];
```
