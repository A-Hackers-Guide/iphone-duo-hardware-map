# `IOGPUMetalAccelerationStructure`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResource`
- Protocols: `MTLAccelerationStructureSPI`
- 4 instance variables, 22 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalBuffer<MTLBuffer>" _buffer;
Q _bufferOffset;
@"MTLAccelerationStructureDescriptor" _descriptor;
Q _resourceIndex;
```

## Properties

```
@property (TQ,R,N) uniqueIdentifier;
@property (TQ,R,N) accelerationStructureUniqueIdentifier;
@property (T@"IOGPUMetalBuffer<MTLBuffer>",R,N) buffer;
@property (TQ,R,N) bufferOffset;
@property (T@"MTLAccelerationStructureDescriptor",&,N,V_descriptor) descriptor;
@property (TQ,R,N,V_resourceIndex) resourceIndex;
@property (TQ,R,N) gpuHandle;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R,N) size;
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
-[IOGPUMetalAccelerationStructure buffer];
-[IOGPUMetalAccelerationStructure resourceIndex];
-[IOGPUMetalAccelerationStructure setDescriptor:];
-[IOGPUMetalAccelerationStructure descriptor];
-[IOGPUMetalAccelerationStructure allocatedSize];
-[IOGPUMetalAccelerationStructure dealloc];
-[IOGPUMetalAccelerationStructure uniqueIdentifier];
-[IOGPUMetalAccelerationStructure size];
-[IOGPUMetalAccelerationStructure gpuHandle];
-[IOGPUMetalAccelerationStructure heap];
-[IOGPUMetalAccelerationStructure bufferOffset];
-[IOGPUMetalAccelerationStructure isAliasable];
-[IOGPUMetalAccelerationStructure gpuResourceID];
-[IOGPUMetalAccelerationStructure makeAliasable];
-[IOGPUMetalAccelerationStructure heapOffset];
-[IOGPUMetalAccelerationStructure accelerationStructureUniqueIdentifier];
-[IOGPUMetalAccelerationStructure copyPropertiesFromBuffer:];
-[IOGPUMetalAccelerationStructure initWithBuffer:offset:];
-[IOGPUMetalAccelerationStructure initWithBuffer:offset:resourceIndex:];
```
