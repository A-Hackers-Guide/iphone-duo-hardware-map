# `MTLToolsTexture`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLTextureImplementation`
- 2 instance variables, 60 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"<MTLTexture>" _parentTexture;
@"<MTLBuffer>" _buffer;
```

## Properties

```
@property (T@"<MTLTexture>",R,V_parentTexture) parentTexture;
@property (T@"<MTLBuffer>",R,V_buffer) buffer;
@property (TQ,R) bufferOffset;
@property (TQ,R) bufferBytesPerRow;
@property (Tq,R) sparseTextureTier;
@property (T^{__IOSurface=},R) iosurface;
@property (TQ,R) iosurfacePlane;
@property (TQ,R) rotation;
@property (TB,R) isCompressed;
@property (Tq,R) compressionFeedback;
@property (TQ,?,R) uniqueIdentifier;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R,N) gpuAddress;
@property (TI,R) swizzleKey;
@property (TQ,R) numFaces;
@property (TB,R) isDrawable;
@property (TQ,R) sparseSurfaceDefaultValue;
@property (TQ,R,N) compressionFootprint;
@property (TQ,R,N) colorSpaceConversionMatrix;
@property (TQ,R) gpuHandle;
@property (Tq,?,R) writeAccessPattern;
@property (T@"<MTLResource>",R) rootResource;
@property (TQ,R) parentRelativeLevel;
@property (TQ,R) parentRelativeSlice;
@property (TQ,R) textureType;
@property (TQ,R) pixelFormat;
@property (TQ,R) width;
@property (TQ,R) height;
@property (TQ,R) depth;
@property (TQ,R) mipmapLevelCount;
@property (TQ,R) sampleCount;
@property (TQ,R) arrayLength;
@property (TQ,R) usage;
@property (TB,R,GisShareable) shareable;
@property (TB,R,GisFramebufferOnly) framebufferOnly;
@property (TQ,R) firstMipmapInTail;
@property (TQ,R) tailSizeInBytes;
@property (TB,R) isSparse;
@property (TB,R) allowGPUOptimizedContents;
@property (Tq,R) compressionType;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (T{?=CCCC},R,N) swizzle;
@property (Tf,R) minLOD;
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
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
```

## Instance methods

```
-[MTLToolsTexture arrayLength];
-[MTLToolsTexture usage];
-[MTLToolsTexture buffer];
-[MTLToolsTexture resourceIndex];
-[MTLToolsTexture compressionType];
-[MTLToolsTexture depth];
-[MTLToolsTexture iosurface];
-[MTLToolsTexture mipmapLevelCount];
-[MTLToolsTexture newSharedTextureHandle];
-[MTLToolsTexture copyFromPixels:rowBytes:imageBytes:toSlice:mipmapLevel:origin:size:];
-[MTLToolsTexture rotation];
-[MTLToolsTexture bufferBytesPerRow];
-[MTLToolsTexture parentRelativeLevel];
-[MTLToolsTexture formattedDescription:];
-[MTLToolsTexture isCompressed];
-[MTLToolsTexture dealloc];
-[MTLToolsTexture textureType];
-[MTLToolsTexture gpuAddress];
-[MTLToolsTexture canGenerateMipmapLevels];
-[MTLToolsTexture rootResource];
-[MTLToolsTexture replaceRegion:mipmapLevel:withBytes:bytesPerRow:];
-[MTLToolsTexture numFaces];
-[MTLToolsTexture swizzle];
-[MTLToolsTexture isDrawable];
-[MTLToolsTexture getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:];
-[MTLToolsTexture uniqueIdentifier];
-[MTLToolsTexture compressionFootprint];
-[MTLToolsTexture compressionFeedback];
-[MTLToolsTexture replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:];
-[MTLToolsTexture gpuHandle];
-[MTLToolsTexture newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:];
-[MTLToolsTexture allowGPUOptimizedContents];
-[MTLToolsTexture newTextureViewWithPixelFormat:resourceIndex:];
-[MTLToolsTexture sampleCount];
-[MTLToolsTexture parentTexture];
-[MTLToolsTexture newTextureViewWithDescriptor:];
-[MTLToolsTexture colorSpaceConversionMatrix];
-[MTLToolsTexture tailSize];
-[MTLToolsTexture generateMipmapLevel:slice:];
-[MTLToolsTexture newCompressedTextureViewWithPixelFormat:textureType:level:slice:];
-[MTLToolsTexture isSparse];
-[MTLToolsTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[MTLToolsTexture tailSizeInBytes];
-[MTLToolsTexture isFramebufferOnly];
-[MTLToolsTexture bufferOffset];
-[MTLToolsTexture pixelFormat];
-[MTLToolsTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[MTLToolsTexture swizzleKey];
-[MTLToolsTexture getBytes:bytesPerRow:fromRegion:mipmapLevel:];
-[MTLToolsTexture width];
-[MTLToolsTexture gpuResourceID];
-[MTLToolsTexture isShareable];
-[MTLToolsTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[MTLToolsTexture writeAccessPattern];
-[MTLToolsTexture iosurfacePlane];
-[MTLToolsTexture height];
-[MTLToolsTexture copyFromSlice:mipmapLevel:origin:size:toPixels:rowBytes:imageBytes:];
-[MTLToolsTexture parentRelativeSlice];
-[MTLToolsTexture newTextureViewWithPixelFormat:];
-[MTLToolsTexture sparseSurfaceDefaultValue];
-[MTLToolsTexture firstMipmapInTail];
-[MTLToolsTexture minLOD];
-[MTLToolsTexture sparseTextureTier];
-[MTLToolsTexture compressionMetadata];
-[MTLToolsTexture initWithBaseObject:parent:buffer:];
-[MTLToolsTexture initWithBaseObject:parent:parentTexture:];
-[MTLToolsTexture realRootResource];
```
