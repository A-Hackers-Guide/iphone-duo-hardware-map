# `MTLGPUDebugAccelerationStructure`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsAccelerationStructure`
- Protocols: `MTLGPUDebugResource`
- 2 instance variables, 22 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q _accelerationStructureType;
@"<MTLBuffer>" _childrenWrappersBuffer;
```

## Properties

```
@property (T@"<MTLAccelerationStructure>",&,D,N) baseObject;
@property (T@"<MTLBuffer>",&,N,V_childrenWrappersBuffer) childrenWrappersBuffer;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugAccelerationStructure setLabel:];
-[MTLGPUDebugAccelerationStructure dealloc];
-[MTLGPUDebugAccelerationStructure length];
-[MTLGPUDebugAccelerationStructure _registerType];
-[MTLGPUDebugAccelerationStructure childrenWrappersBuffer];
-[MTLGPUDebugAccelerationStructure initWithAccelerationStructure:device:];
-[MTLGPUDebugAccelerationStructure initWithAccelerationStructure:device:type:];
-[MTLGPUDebugAccelerationStructure initWithAccelerationStructure:heap:];
-[MTLGPUDebugAccelerationStructure setChildrenWrappersBuffer:];
-[MTLGPUDebugAccelerationStructure useWithComputeEncoder:usage:];
-[MTLGPUDebugAccelerationStructure useWithRenderEncoder:usage:stages:];
```
