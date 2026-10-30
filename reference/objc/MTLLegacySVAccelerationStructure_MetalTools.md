# `MTLLegacySVAccelerationStructure`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsAccelerationStructure`
- Protocols: `MTLLegacySVResource`
- 4 instance variables, 23 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _accelerationStructureHandle;
Q _accelerationStructureType;
@"<MTLBuffer>" _debugBuf;
@"<MTLBuffer>" _childrenWrappersBuffer;
```

## Properties

```
@property (T@"<MTLAccelerationStructure>",&,D,N) baseObject;
@property (TQ,R,N,V_accelerationStructureHandle) accelerationStructureHandle;
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
-[MTLLegacySVAccelerationStructure dealloc];
-[MTLLegacySVAccelerationStructure gpuAddress];
-[MTLLegacySVAccelerationStructure length];
-[MTLLegacySVAccelerationStructure gpuResourceID];
-[MTLLegacySVAccelerationStructure _setupIdentifier];
-[MTLLegacySVAccelerationStructure accelerationStructureHandle];
-[MTLLegacySVAccelerationStructure childrenWrappersBuffer];
-[MTLLegacySVAccelerationStructure debugBuf];
-[MTLLegacySVAccelerationStructure handleForOffset:];
-[MTLLegacySVAccelerationStructure initWithAccelerationStructure:device:];
-[MTLLegacySVAccelerationStructure initWithAccelerationStructure:device:type:];
-[MTLLegacySVAccelerationStructure initWithAccelerationStructure:heap:];
-[MTLLegacySVAccelerationStructure setChildrenWrappersBuffer:];
-[MTLLegacySVAccelerationStructure underlyingGPUAddress];
-[MTLLegacySVAccelerationStructure useWithComputeEncoder:usage:];
-[MTLLegacySVAccelerationStructure useWithRenderEncoder:usage:stages:];
```
