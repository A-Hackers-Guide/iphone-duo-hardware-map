# `MTLTextureDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 19 properties, 3 instance methods, 5 class methods

## Instance variables

```
q _placementSparsePageSize;
```

## Properties

```
@property (TB,D,N) forceResourceIndex;
@property (TQ,D,N) resourceIndex;
@property (TQ,D,N) textureType;
@property (TQ,D,N) pixelFormat;
@property (TQ,D,N) width;
@property (TQ,D,N) height;
@property (TQ,D,N) depth;
@property (TQ,D,N) mipmapLevelCount;
@property (TQ,D,N) sampleCount;
@property (TQ,D,N) arrayLength;
@property (TQ,D,N) resourceOptions;
@property (TQ,D,N) cpuCacheMode;
@property (TQ,D,N) storageMode;
@property (TQ,D,N) hazardTrackingMode;
@property (TQ,D,N) usage;
@property (TB,D,N) allowGPUOptimizedContents;
@property (Tq,D,N) compressionType;
@property (T{?=CCCC},D,N) swizzle;
@property (Tq,N,V_placementSparsePageSize) placementSparsePageSize;
```

## Class methods

```
+[MTLTextureDescriptor allocWithZone:];
+[MTLTextureDescriptor texture2DDescriptorWithPixelFormat:width:height:mipmapped:];
+[MTLTextureDescriptor textureBufferDescriptorWithPixelFormat:width:resourceOptions:usage:];
+[MTLTextureDescriptor alloc];
+[MTLTextureDescriptor textureCubeDescriptorWithPixelFormat:size:mipmapped:];
```

## Instance methods

```
-[MTLTextureDescriptor placementSparsePageSize];
-[MTLTextureDescriptor setPlacementSparsePageSize:];
-[MTLTextureDescriptor copyWithZone:];
```
