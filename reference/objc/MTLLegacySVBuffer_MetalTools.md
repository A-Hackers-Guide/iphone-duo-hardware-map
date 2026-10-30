# `MTLLegacySVBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBuffer`
- Protocols: `MTLLegacySVResource`
- 4 instance variables, 24 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _bufferIndex;
Q _offset;
Q _length;
^v _descriptorHeap;
```

## Properties

```
@property (TQ,R,N) offset;
@property (TQ,R,N) gpuAddress;
@property (T@"<MTLBuffer>",&,D,N) baseObject;
@property (TQ,N) bufferIndex;
@property (TB,R,N) isTracked;
@property (TQ,R,N) length;
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
-[MTLLegacySVBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[MTLLegacySVBuffer setBufferIndex:];
-[MTLLegacySVBuffer contents];
-[MTLLegacySVBuffer bufferIndex];
-[MTLLegacySVBuffer dealloc];
-[MTLLegacySVBuffer gpuAddress];
-[MTLLegacySVBuffer length];
-[MTLLegacySVBuffer offset];
-[MTLLegacySVBuffer newTextureWithDescriptor:offset:bytesPerRow:];
-[MTLLegacySVBuffer isTracked];
-[MTLLegacySVBuffer handleForOffset:];
-[MTLLegacySVBuffer initWithBuffer:device:];
-[MTLLegacySVBuffer initWithBuffer:device:offset:length:];
-[MTLLegacySVBuffer initWithBuffer:device:offset:length:track:];
-[MTLLegacySVBuffer initWithBuffer:heap:device:];
-[MTLLegacySVBuffer initWithBuffer:heap:device:offset:length:track:];
-[MTLLegacySVBuffer underlyingGPUAddress];
-[MTLLegacySVBuffer useWithComputeEncoder:usage:];
-[MTLLegacySVBuffer useWithRenderEncoder:usage:stages:];
```
