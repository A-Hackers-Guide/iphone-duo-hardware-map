# `AGXG19FamilyTexture`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AGXTexture`
- 1 instance variables, 1 properties, 45 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (Tq,R) sparseTextureTier;
```

## Instance methods

```
-[AGXG19FamilyTexture resourceIndex];
-[AGXG19FamilyTexture emitResourceInfoTraceEvent];
-[AGXG19FamilyTexture dealloc];
-[AGXG19FamilyTexture canGenerateMipmapLevels];
-[AGXG19FamilyTexture updateBindDataWithAddresses:gpuVirtualAddress:];
-[AGXG19FamilyTexture initImplWithTexture:pixelFormat:textureType:levels:slices:];
-[AGXG19FamilyTexture updateBindDataWithTexture:pixelFormat:textureType:levels:slices:];
-[AGXG19FamilyTexture getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:];
-[AGXG19FamilyTexture initImplWithTexture:pixelFormat:textureType:levels:slices:swizzle:];
-[AGXG19FamilyTexture uniqueIdentifier];
-[AGXG19FamilyTexture initImplWithCompressedTexture:pixelFormat:textureType:level:];
-[AGXG19FamilyTexture compressionFootprint];
-[AGXG19FamilyTexture initImplWithDevice:Descriptor:iosurface:plane:slice:buffer:bytesPerRow:allowNPOT:sparsePageSize:isCompressedIOSurface:isHeapBacked:];
-[AGXG19FamilyTexture compressionFeedback];
-[AGXG19FamilyTexture replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:];
-[AGXG19FamilyTexture validateBufferTextureWithSize:];
-[AGXG19FamilyTexture initImplWithTexture:descriptor:];
-[AGXG19FamilyTexture isMemoryless];
-[AGXG19FamilyTexture sparseResourceType];
-[AGXG19FamilyTexture initImplWithTexture:pixelFormat:textureType:levels:slices:resourceIndex:];
-[AGXG19FamilyTexture updateBindDataWithCompressedTexture:pixelFormat:textureType:level:slice:];
-[AGXG19FamilyTexture setSparseHeap:];
-[AGXG19FamilyTexture colorSpaceConversionMatrix];
-[AGXG19FamilyTexture tailSize];
-[AGXG19FamilyTexture generateMipmapLevel:slice:];
-[AGXG19FamilyTexture heap];
-[AGXG19FamilyTexture isSparse];
-[AGXG19FamilyTexture tailSizeInBytes];
-[AGXG19FamilyTexture initNewTextureData:];
-[AGXG19FamilyTexture initImplWithTexture:pixelFormat:];
-[AGXG19FamilyTexture initImplWithTexture:pixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[AGXG19FamilyTexture finalizeTextureCreation];
-[AGXG19FamilyTexture updateBindDataWithAddresses:cpuMetadataAddress:gpuVirtualAddress:isCompressible:shouldInitMetadata:];
-[AGXG19FamilyTexture finalizeCompressedTextureViewCreation];
-[AGXG19FamilyTexture updateBindDataWithAddresses:gpuVirtualAddress:shouldInitMetadata:];
-[AGXG19FamilyTexture getPlacementSparseSizeBytes];
-[AGXG19FamilyTexture writeAccessPattern];
-[AGXG19FamilyTexture initImplWithCompressedTexture:pixelFormat:textureType:level:resourceIndex:];
-[AGXG19FamilyTexture initImplWithTexture:pixelFormat:resourceIndex:];
-[AGXG19FamilyTexture sparseSurfaceDefaultValue];
-[AGXG19FamilyTexture firstMipmapInTail];
-[AGXG19FamilyTexture minLOD];
-[AGXG19FamilyTexture sparseTextureTier];
-[AGXG19FamilyTexture compressionMetadata];
-[AGXG19FamilyTexture emitTextureResourceInfoSignpost:];
```
