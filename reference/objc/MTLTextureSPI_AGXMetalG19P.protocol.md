# `MTLTextureSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLTexture`, `MTLResourceSPI`
- 0 instance variables, 16 properties, 23 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[MTLTextureSPI iosurface];
-[MTLTextureSPI rotation];
-[MTLTextureSPI isCompressed];
-[MTLTextureSPI numFaces];
-[MTLTextureSPI isDrawable];
-[MTLTextureSPI compressionFootprint];
-[MTLTextureSPI compressionFeedback];
-[MTLTextureSPI gpuHandle];
-[MTLTextureSPI colorSpaceConversionMatrix];
-[MTLTextureSPI swizzleKey];
-[MTLTextureSPI iosurfacePlane];
-[MTLTextureSPI sparseSurfaceDefaultValue];
-[MTLTextureSPI compressionMetadata];
-[MTLTextureSPI resourceIndex];
-[MTLTextureSPI gpuAddress];
-[MTLTextureSPI canGenerateMipmapLevels];
-[MTLTextureSPI uniqueIdentifier];
-[MTLTextureSPI newTextureViewWithPixelFormat:textureType:levels:slices:resourceIndex:];
-[MTLTextureSPI newTextureViewWithPixelFormat:resourceIndex:];
-[MTLTextureSPI generateMipmapLevel:slice:];
-[MTLTextureSPI newCompressedTextureViewWithPixelFormat:textureType:level:slice:];
-[MTLTextureSPI newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:resourceIndex:];
-[MTLTextureSPI writeAccessPattern];
```
