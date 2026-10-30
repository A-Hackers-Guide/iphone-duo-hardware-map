# `MTLToolsBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLBufferSPI`
- 0 instance variables, 24 properties, 21 instance methods, 0 class methods

## Properties

```
@property (Tq,R) sparseBufferTier;
@property (T^{__IOSurface=},R) iosurface;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,N) parentGPUAddress;
@property (TQ,?,N) parentGPUSize;
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
@property (TQ,R) length;
@property (TQ,R) gpuAddress;
```

## Instance methods

```
-[MTLToolsBuffer didModifyRange:];
-[MTLToolsBuffer replaceBackingWithBytesNoCopy:length:deallocator:];
-[MTLToolsBuffer iosurface];
-[MTLToolsBuffer removeAllDebugMarkers];
-[MTLToolsBuffer detachBacking];
-[MTLToolsBuffer _aneIOSurface];
-[MTLToolsBuffer addDebugMarker:range:];
-[MTLToolsBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[MTLToolsBuffer contents];
-[MTLToolsBuffer replaceBackingWithRanges:readOnly:];
-[MTLToolsBuffer formattedDescription:];
-[MTLToolsBuffer dealloc];
-[MTLToolsBuffer gpuAddress];
-[MTLToolsBuffer length];
-[MTLToolsBuffer parentGPUAddress];
-[MTLToolsBuffer setParentGPUSize:];
-[MTLToolsBuffer setParentGPUAddress:];
-[MTLToolsBuffer parentGPUSize];
-[MTLToolsBuffer newTensorWithDescriptor:offset:error:];
-[MTLToolsBuffer newTextureWithDescriptor:offset:bytesPerRow:];
-[MTLToolsBuffer sparseBufferTier];
```
