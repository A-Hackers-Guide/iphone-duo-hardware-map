# `MTLLegacySVTexture`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTexture`
- Protocols: `MTLLegacySVResource`
- 1 instance variables, 22 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _identifier;
```

## Properties

```
@property (T@"<MTLTextureSPI>",&,D,N) baseObject;
@property (TQ,R,N) gpuIdentifier;
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
-[MTLLegacySVTexture length];
-[MTLLegacySVTexture newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:];
-[MTLLegacySVTexture newTextureViewWithPixelFormat:resourceIndex:];
-[MTLLegacySVTexture newTextureViewWithDescriptor:];
-[MTLLegacySVTexture newCompressedTextureViewWithPixelFormat:textureType:level:slice:];
-[MTLLegacySVTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[MTLLegacySVTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[MTLLegacySVTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[MTLLegacySVTexture newTextureViewWithPixelFormat:];
-[MTLLegacySVTexture baseObject];
-[MTLLegacySVTexture gpuIdentifier];
-[MTLLegacySVTexture handleForOffset:];
-[MTLLegacySVTexture initWithTexture:heap:device:];
-[MTLLegacySVTexture initWithTextureView:parentBuffer:heap:device:];
-[MTLLegacySVTexture initWithTextureView:parentTexture:heap:device:];
-[MTLLegacySVTexture underlyingGPUAddress];
-[MTLLegacySVTexture useWithComputeEncoder:usage:];
-[MTLLegacySVTexture useWithRenderEncoder:usage:stages:];
```
