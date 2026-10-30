# `MTLTexture` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResource`
- 0 instance variables, 29 properties, 38 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLResource>",R) rootResource;
@property (T@"<MTLTexture>",R) parentTexture;
@property (TQ,R) parentRelativeLevel;
@property (TQ,R) parentRelativeSlice;
@property (T@"<MTLBuffer>",R) buffer;
@property (TQ,R) bufferOffset;
@property (TQ,R) bufferBytesPerRow;
@property (T^{__IOSurface=},R) iosurface;
@property (TQ,R) iosurfacePlane;
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
```

## Instance methods

```
-[MTLTexture arrayLength];
-[MTLTexture usage];
-[MTLTexture buffer];
-[MTLTexture compressionType];
-[MTLTexture depth];
-[MTLTexture iosurface];
-[MTLTexture mipmapLevelCount];
-[MTLTexture newSharedTextureHandle];
-[MTLTexture bufferBytesPerRow];
-[MTLTexture parentRelativeLevel];
-[MTLTexture textureType];
-[MTLTexture rootResource];
-[MTLTexture replaceRegion:mipmapLevel:withBytes:bytesPerRow:];
-[MTLTexture swizzle];
-[MTLTexture getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:];
-[MTLTexture replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:];
-[MTLTexture allowGPUOptimizedContents];
-[MTLTexture sampleCount];
-[MTLTexture parentTexture];
-[MTLTexture newTextureViewWithDescriptor:];
-[MTLTexture isSparse];
-[MTLTexture newTextureViewWithPixelFormat:textureType:levels:slices:];
-[MTLTexture tailSizeInBytes];
-[MTLTexture isFramebufferOnly];
-[MTLTexture bufferOffset];
-[MTLTexture pixelFormat];
-[MTLTexture getBytes:bytesPerRow:fromRegion:mipmapLevel:];
-[MTLTexture width];
-[MTLTexture gpuResourceID];
-[MTLTexture isShareable];
-[MTLTexture newTextureViewWithPixelFormat:textureType:levels:slices:swizzle:];
-[MTLTexture iosurfacePlane];
-[MTLTexture height];
-[MTLTexture parentRelativeSlice];
-[MTLTexture newTextureViewWithPixelFormat:];
-[MTLTexture firstMipmapInTail];
-[MTLTexture minLOD];
-[MTLTexture sparseTextureTier];
```
