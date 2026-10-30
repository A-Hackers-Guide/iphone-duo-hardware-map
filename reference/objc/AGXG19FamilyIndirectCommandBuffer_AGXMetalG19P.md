# `AGXG19FamilyIndirectCommandBuffer`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalIndirectCommandBuffer`
- Protocols: `MTLIndirectCommandBuffer`
- 4 instance variables, 15 properties, 8 instance methods, 0 class methods

## Instance variables

```
i _type;
@"AGXG19FamilyBuffer" _buffer;
(Impl="render"^{IndirectCommandBuffer}"compute"^{IndirectComputeCommandBuffer}) _impl;
(Encoder="render"^{IndirectRenderCommandEncoder}"compute"^{IndirectComputeCommandEncoder}) _encoder;
```

## Properties

```
@property (TQ,R) size;
@property (T{MTLResourceID=Q},R) gpuResourceID;
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
-[AGXG19FamilyIndirectCommandBuffer resourceIndex];
-[AGXG19FamilyIndirectCommandBuffer dealloc];
-[AGXG19FamilyIndirectCommandBuffer uniqueIdentifier];
-[AGXG19FamilyIndirectCommandBuffer resetWithRange:];
-[AGXG19FamilyIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[AGXG19FamilyIndirectCommandBuffer indirectRenderCommandAtIndex:];
-[AGXG19FamilyIndirectCommandBuffer initWithBuffer:descriptor:maxCommandCount:];
-[AGXG19FamilyIndirectCommandBuffer initWithDevice:descriptor:count:options:isSuballocDisabled:];
```
