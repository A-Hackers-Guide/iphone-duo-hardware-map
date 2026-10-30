# `AGXG19FamilyHeap`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalHeap`
- Protocols: `MTLHeapSPI`
- 0 instance variables, 19 properties, 16 instance methods, 0 class methods

## Properties

```
@property (TQ,R) unfilteredResourceOptions;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,?,R,N) protectionOptions;
@property (TQ,R,N) memoryPoolId;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) storageMode;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (TQ,R) size;
@property (TQ,R) usedSize;
@property (TQ,R) currentAllocatedSize;
@property (Tq,R) type;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyHeap emitResourceInfoTraceEvent];
-[AGXG19FamilyHeap initWithDevice:descriptor:];
-[AGXG19FamilyHeap newBufferWithDescriptor:offset:];
-[AGXG19FamilyHeap newAccelerationStructureWithSize:];
-[AGXG19FamilyHeap newAccelerationStructureWithDescriptor:offset:];
-[AGXG19FamilyHeap newTextureWithDescriptor:atOffset:];
-[AGXG19FamilyHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[AGXG19FamilyHeap newBufferWithDescriptor:];
-[AGXG19FamilyHeap newAccelerationStructureWithDescriptor:];
-[AGXG19FamilyHeap newAccelerationStructureWithSize:offset:];
-[AGXG19FamilyHeap newAccelerationStructureWithSize:resourceIndex:];
-[AGXG19FamilyHeap dealloc];
-[AGXG19FamilyHeap newTextureWithDescriptor:];
-[AGXG19FamilyHeap newBufferWithLength:options:atOffset:];
-[AGXG19FamilyHeap newBufferWithLength:options:];
-[AGXG19FamilyHeap emitHeapResourceInfoSignpost:];
```
