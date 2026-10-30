# `AGXG19FamilyBuffer`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AGXBuffer`
- Protocols: `MTLBuffer`
- 0 instance variables, 16 properties, 7 instance methods, 0 class methods

## Properties

```
@property (Tq,R) sparseBufferTier;
@property (TQ,R) length;
@property (TQ,R) gpuAddress;
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
-[AGXG19FamilyBuffer removeAllDebugMarkers];
-[AGXG19FamilyBuffer addDebugMarker:range:];
-[AGXG19FamilyBuffer dealloc];
-[AGXG19FamilyBuffer initResourceGroupUsage];
-[AGXG19FamilyBuffer newTensorWithDescriptor:offset:error:];
-[AGXG19FamilyBuffer newTextureWithDescriptor:offset:bytesPerRow:];
-[AGXG19FamilyBuffer sparseBufferTier];
```
