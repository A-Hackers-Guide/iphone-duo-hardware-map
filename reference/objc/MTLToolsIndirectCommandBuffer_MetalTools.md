# `MTLToolsIndirectCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLIndirectCommandBufferSPI`
- 0 instance variables, 19 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TQ,R) uniqueIdentifier;
@property (TQ,R) storageMode;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,?,R,D,N) resourceIndex;
@property (TQ,R) gpuHandle;
@property (TQ,R) size;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
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
-[MTLToolsIndirectCommandBuffer resourceIndex];
-[MTLToolsIndirectCommandBuffer storageMode];
-[MTLToolsIndirectCommandBuffer gpuAddress];
-[MTLToolsIndirectCommandBuffer uniqueIdentifier];
-[MTLToolsIndirectCommandBuffer size];
-[MTLToolsIndirectCommandBuffer gpuHandle];
-[MTLToolsIndirectCommandBuffer gpuResourceID];
-[MTLToolsIndirectCommandBuffer resetWithRange:];
-[MTLToolsIndirectCommandBuffer getHeader:headerSize:];
-[MTLToolsIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[MTLToolsIndirectCommandBuffer indirectRenderCommandAtIndex:];
```
