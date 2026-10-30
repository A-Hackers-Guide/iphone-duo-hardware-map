# `IOGPUMetalTexture`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResource`
- 35 instance variables, 34 properties, 65 instance methods, 1 class methods

## Instance variables

```
@"IOGPUMetalTexture" _parentTexture;
Q _parentRelativeLevel;
Q _parentRelativeSlice;
@"IOGPUMetalBuffer" _buffer;
I _swizzle;
B _writeSwizzleEnabled;
B _isCompressed;
@"IOGPUMetalBuffer" _primaryBuffer;
^{__IOSurface=} _iosurface;
Q _iosurfacePlane;
Q _textureType;
Q _pixelFormat;
Q _usage;
Q _rotation;
Q _width;
Q _height;
Q _depth;
Q _mipmapLevelCount;
Q _sampleCount;
Q _arrayLength;
Q _numFaces;
B _shareable;
B _framebufferOnly;
B _isDrawable;
B _rootResourceIsSuballocatedBuffer;
s _primaryHeapIndex;
s _primaryBufferIndex;
Q _primaryBufferOffset;
Q _length;
Q _bufferOffset;
Q _bufferBytesPerRow;
^v _pointer;
@? _deallocator;
B _allowGPUOptimizedContents;
q _placementSparsePageSize;
```

## Properties

```
@property (TQ,R) uniqueIdentifier;
@property (T@"IOGPUMetalResource",R) rootResource;
@property (T@"IOGPUMetalTexture",R) parentTexture;
@property (TQ,R,V_parentRelativeLevel) parentRelativeLevel;
@property (TQ,R,V_parentRelativeSlice) parentRelativeSlice;
@property (T@"IOGPUMetalBuffer",R) buffer;
@property (TQ,R) bufferOffset;
@property (TQ,R) bufferBytesPerRow;
@property (T^{__IOSurface=},R,V_iosurface) iosurface;
@property (TQ,R,V_iosurfacePlane) iosurfacePlane;
@property (TQ,R) allocatedSize;
@property (TQ,R,V_rotation) rotation;
@property (T{?=CCCC},R) swizzle;
@property (TI,R) swizzleKey;
@property (TB,R,V_isCompressed) isCompressed;
@property (Tq,R,D) compressionFeedback;
@property (TQ,R,V_textureType) textureType;
@property (TQ,R,V_pixelFormat) pixelFormat;
@property (TQ,R,V_usage) usage;
@property (TQ,R,V_width) width;
@property (TQ,R,V_height) height;
@property (TQ,R,V_depth) depth;
@property (TQ,R,V_mipmapLevelCount) mipmapLevelCount;
@property (TQ,R,V_sampleCount) sampleCount;
@property (TQ,R,V_arrayLength) arrayLength;
@property (TQ,R,V_numFaces) numFaces;
@property (TB,R,GisShareable,V_shareable) shareable;
@property (TB,R,GisFramebufferOnly,V_framebufferOnly) framebufferOnly;
@property (TB,R,V_isDrawable) isDrawable;
@property (TB,R,V_rootResourceIsSuballocatedBuffer) rootResourceIsSuballocatedBuffer;
@property (TB,R,V_allowGPUOptimizedContents) allowGPUOptimizedContents;
@property (TQ,R,N) gpuHandle;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (Tq,R,V_placementSparsePageSize) placementSparsePageSize;
```

## Class methods

```
+[IOGPUMetalTexture initNewTextureDataWithDevice:descriptor:sysMemSize:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:];
```

## Instance methods

```
-[IOGPUMetalTexture arrayLength];
-[IOGPUMetalTexture usage];
-[IOGPUMetalTexture buffer];
-[IOGPUMetalTexture depth];
-[IOGPUMetalTexture iosurface];
-[IOGPUMetalTexture hazardTrackingMode];
-[IOGPUMetalTexture copyAnnotations];
-[IOGPUMetalTexture mipmapLevelCount];
-[IOGPUMetalTexture setOwnerWithIdentity:];
-[IOGPUMetalTexture rootResourceIsSuballocatedBuffer];
-[IOGPUMetalTexture placementSparsePageSize];
-[IOGPUMetalTexture initWithBuffer:descriptor:sysMemOffset:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:];
-[IOGPUMetalTexture emitResourceInfoTraceEvent];
-[IOGPUMetalTexture newSharedTextureHandle];
-[IOGPUMetalTexture copyFromPixels:rowBytes:imageBytes:toSlice:mipmapLevel:origin:size:];
-[IOGPUMetalTexture _setLabel:];
-[IOGPUMetalTexture initWithTexture:pixelFormat:textureType:levels:slices:swizzle:];
-[IOGPUMetalTexture rotation];
-[IOGPUMetalTexture bufferBytesPerRow];
-[IOGPUMetalTexture parentRelativeLevel];
-[IOGPUMetalTexture formattedDescription:];
-[IOGPUMetalTexture allocatedSize];
-[IOGPUMetalTexture isCompressed];
-[IOGPUMetalTexture dealloc];
-[IOGPUMetalTexture textureType];
-[IOGPUMetalTexture initWithDevice:descriptor:sysMemPointer:sysMemSize:sysMemLength:sysMemRowBytes:args:argsSize:deallocator:];
-[IOGPUMetalTexture rootResource];
-[IOGPUMetalTexture replaceRegion:mipmapLevel:withBytes:bytesPerRow:];
-[IOGPUMetalTexture numFaces];
-[IOGPUMetalTexture swizzle];
-[IOGPUMetalTexture isDrawable];
-[IOGPUMetalTexture initWithBuffer:descriptor:sysMemOffset:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:isStrideTexture:];
-[IOGPUMetalTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:];
-[IOGPUMetalTexture initWithTexture:pixelFormat:textureType:levels:slices:];
-[IOGPUMetalTexture uniqueIdentifier];
-[IOGPUMetalTexture initWithTextureInternal:pixelFormat:textureType:levels:slices:swizzle:compressedView:];
-[IOGPUMetalTexture compressionFeedback];
-[IOGPUMetalTexture gpuHandle];
-[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:placementSparseResidencyBytes:args:argsSize:];
-[IOGPUMetalTexture allowGPUOptimizedContents];
-[IOGPUMetalTexture sampleCount];
-[IOGPUMetalTexture initWithCompressedTexture:pixelFormat:textureType:level:slice:];
-[IOGPUMetalTexture parentTexture];
-[IOGPUMetalTexture initWithPrimaryBuffer:heapIndex:bufferIndex:bufferOffset:length:descriptor:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:];
-[IOGPUMetalTexture isSparse];
-[IOGPUMetalTexture description];
-[IOGPUMetalTexture isFramebufferOnly];
-[IOGPUMetalTexture bufferOffset];
-[IOGPUMetalTexture initWithTexture:pixelFormat:];
-[IOGPUMetalTexture pixelFormat];
-[IOGPUMetalTexture swizzleKey];
-[IOGPUMetalTexture getBytes:bytesPerRow:fromRegion:mipmapLevel:];
-[IOGPUMetalTexture isAliasable];
-[IOGPUMetalTexture width];
-[IOGPUMetalTexture gpuResourceID];
-[IOGPUMetalTexture makeAliasable];
-[IOGPUMetalTexture isShareable];
-[IOGPUMetalTexture initWithDevice:descriptor:sysMemSize:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:];
-[IOGPUMetalTexture iosurfacePlane];
-[IOGPUMetalTexture height];
-[IOGPUMetalTexture copyFromSlice:mipmapLevel:origin:size:toPixels:rowBytes:imageBytes:];
-[IOGPUMetalTexture initWithHeap:resource:offset:length:device:descriptor:];
-[IOGPUMetalTexture initWithDevice:descriptor:placementSparseBytes:placementSparsePageSize:placementSparseMetaDataBytes:args:argsSize:];
-[IOGPUMetalTexture parentRelativeSlice];
-[IOGPUMetalTexture initWithBuffer:descriptor:offset:bytesPerRow:];
```
