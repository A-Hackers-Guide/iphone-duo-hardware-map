# `MTLToolsHeap`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLHeapSPI`
- 0 instance variables, 19 properties, 34 instance methods, 0 class methods

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
-[MTLToolsHeap resourceOptions];
-[MTLToolsHeap currentAllocatedSize];
-[MTLToolsHeap usedSize];
-[MTLToolsHeap hazardTrackingMode];
-[MTLToolsHeap detachBacking];
-[MTLToolsHeap cpuCacheMode];
-[MTLToolsHeap newAccelerationStructureWithSize:];
-[MTLToolsHeap memoryPoolId];
-[MTLToolsHeap storageMode];
-[MTLToolsHeap unfilteredResourceOptions];
-[MTLToolsHeap newTextureWithDescriptor:offset:];
-[MTLToolsHeap newAccelerationStructureWithDescriptor:offset:];
-[MTLToolsHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[MTLToolsHeap replaceBackingWithRanges:readOnly:];
-[MTLToolsHeap formattedDescription:];
-[MTLToolsHeap protectionOptions];
-[MTLToolsHeap label];
-[MTLToolsHeap newBufferWithLength:options:offset:];
-[MTLToolsHeap newAccelerationStructureWithDescriptor:];
-[MTLToolsHeap setLabel:];
-[MTLToolsHeap allocatedSize];
-[MTLToolsHeap newAccelerationStructureWithSize:offset:];
-[MTLToolsHeap newAccelerationStructureWithSize:resourceIndex:];
-[MTLToolsHeap gpuAddress];
-[MTLToolsHeap newTextureWithDescriptor:];
-[MTLToolsHeap size];
-[MTLToolsHeap type];
-[MTLToolsHeap setPurgeableState:];
-[MTLToolsHeap maxAvailableSizeWithAlignment:];
-[MTLToolsHeap newBufferWithLength:options:];
-[MTLToolsHeap _newToolsAccelerationStructure:];
-[MTLToolsHeap _newToolsBuffer:];
-[MTLToolsHeap _newToolsTexture:];
-[MTLToolsHeap notifyResourceReleasing:];
```
