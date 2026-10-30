# `AGXTexture`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalTexture`
- Protocols: `MTLTextureImplementation`, `AGXResource`
- 8 instance variables, 69 properties, 74 instance methods, 0 class methods

## Instance variables

```
B _hasCPUMapping;
@"IOGPUMetalResource" _backingResourceCached;
Q _alignment;
Q _cpuSizeBytes;
Q _gpuSizeBytes;
Q _gpuMetadataSizeBytes;
Q _gpuResidencySizeBytes;
Q _bytesPerRow;
```

## Properties

```
@property (TQ,GgetAlignment,V_alignment) _alignment;
@property (TQ,GgetCPUSizeBytes,V_cpuSizeBytes) _cpuSizeBytes;
@property (TQ,GgetGPUSizeBytes,V_gpuSizeBytes) _gpuSizeBytes;
@property (TQ,GgetGPUMetadataSizeBytes,V_gpuMetadataSizeBytes) _gpuMetadataSizeBytes;
@property (TQ,GgetGPUResidencySizeBytes,V_gpuResidencySizeBytes) _gpuResidencySizeBytes;
@property (TQ,GgetBytesPerRow,V_bytesPerRow) _bytesPerRow;
@property (TB,R,D,GisMemoryless) _memoryless;
@property (TB,R,GisSparse) _sparse;
@property (Ti,R,GsparseResourceType) _sparseResourceType;
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
@property (T@"<MTLTexture>",R) parentTexture;
@property (TQ,R) parentRelativeLevel;
@property (TQ,R) parentRelativeSlice;
@property (T@"<MTLBuffer>",R) buffer;
@property (TQ,R) bufferOffset;
@property (TQ,R) bufferBytesPerRow;
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
@property (Tq,R) sparseTextureTier;
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
-[AGXTexture set_cpuSizeBytes:];
-[AGXTexture initWithHeap:desc:];
-[AGXTexture initWithDevice:desc:isSuballocDisabled:];
-[AGXTexture initWithTexture:pixelFormat:textureType:levels:slices:swizzle:];
-[AGXTexture set_gpuResidencySizeBytes:];
-[AGXTexture initWithDevice:bytes:length:desc:deallocator:];
-[AGXTexture backingResource];
-[AGXTexture initWithImplHeapMemoryless:descriptor:length:];
-[AGXTexture initWithTexture:pixelFormat:resourceIndex:];
-[AGXTexture initWithImplHeap:resource:descriptor:length:atOffset:];
-[AGXTexture dealloc];
-[AGXTexture initWithTexture:descriptor:];
-[AGXTexture getBytesPerRow];
-[AGXTexture getGPUSizeBytes];
-[AGXTexture canGenerateMipmapLevels];
-[AGXTexture updateBindDataWithAddresses:gpuVirtualAddress:];
-[AGXTexture initWithTexture:pixelFormat:textureType:levels:slices:resourceIndex:];
-[AGXTexture initImplWithTexture:pixelFormat:textureType:levels:slices:];
-[AGXTexture getGPUResidencySizeBytes];
-[AGXTexture updateBindDataWithTexture:pixelFormat:textureType:levels:slices:];
-[AGXTexture getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:];
-[AGXTexture initWithSparseHeap:desc:sparsePageSize:];
-[AGXTexture initWithTexture:pixelFormat:textureType:levels:slices:];
-[AGXTexture initImplWithTexture:pixelFormat:textureType:levels:slices:swizzle:];
-[AGXTexture initImplWithCompressedTexture:pixelFormat:textureType:level:];
-[AGXTexture initImplWithDevice:Descriptor:iosurface:plane:slice:buffer:bytesPerRow:allowNPOT:sparsePageSize:isCompressedIOSurface:isHeapBacked:];
-[AGXTexture initWithBuffer:desc:offset:bytesPerRow:];
-[AGXTexture replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:];
-[AGXTexture newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:];
-[AGXTexture set_gpuSizeBytes:];
-[AGXTexture validateBufferTextureWithSize:];
-[AGXTexture newTextureViewWithPixelFormat:resourceIndex:];
-[AGXTexture initWithCompressedTexture:pixelFormat:textureType:level:slice:];
-[AGXTexture initImplWithTexture:descriptor:];
-[AGXTexture isMemoryless];
-[AGXTexture sparseResourceType];
-[AGXTexture initImplWithTexture:pixelFormat:textureType:levels:slices:resourceIndex:];
-[AGXTexture newTextureViewWithDescriptor:];
-[AGXTexture updateBindDataWithCompressedTexture:pixelFormat:textureType:level:slice:];
-[AGXTexture setSparseHeap:];
-[AGXTexture colorSpaceConversionMatrix];
-[AGXTexture tailSize];
-[AGXTexture getGPUMetadataSizeBytes];
-[AGXTexture getAlignment];
-[AGXTexture generateMipmapLevel:slice:];
-[AGXTexture newCompressedTextureViewWithPixelFormat:textureType:level:slice:];
-[AGXTexture isSparse];
-[AGXTexture initWithTexture:pixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[AGXTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[AGXTexture tailSizeInBytes];
-[AGXTexture initNewTextureData:];
-[AGXTexture initImplWithTexture:pixelFormat:];
-[AGXTexture initImplWithTexture:pixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[AGXTexture finalizeTextureCreation];
-[AGXTexture initWithTexture:pixelFormat:];
-[AGXTexture initWithDevice:desc:iosurface:plane:slice:];
-[AGXTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[AGXTexture updateBindDataWithAddresses:cpuMetadataAddress:gpuVirtualAddress:isCompressible:shouldInitMetadata:];
-[AGXTexture finalizeCompressedTextureViewCreation];
-[AGXTexture set_bytesPerRow:];
-[AGXTexture updateBindDataWithAddresses:gpuVirtualAddress:shouldInitMetadata:];
-[AGXTexture getPlacementSparseSizeBytes];
-[AGXTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[AGXTexture initImplWithCompressedTexture:pixelFormat:textureType:level:resourceIndex:];
-[AGXTexture initWithSharedTextureHandle:device:desc:compressionMode:];
-[AGXTexture getCPUSizeBytes];
-[AGXTexture set_gpuMetadataSizeBytes:];
-[AGXTexture initWithHeap:desc:atOffset:];
-[AGXTexture initWithDevice:desc:sparsePageSize:];
-[AGXTexture set_alignment:];
-[AGXTexture initImplWithTexture:pixelFormat:resourceIndex:];
-[AGXTexture newTextureViewWithPixelFormat:];
-[AGXTexture sparseSurfaceDefaultValue];
-[AGXTexture firstMipmapInTail];
```
