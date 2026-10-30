# `MTLIOAccelTexture`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelResource`
- 34 instance variables, 32 properties, 60 instance methods, 1 class methods

## Instance variables

```
@"MTLIOAccelTexture" _parentTexture;
Q _parentRelativeLevel;
Q _parentRelativeSlice;
@"MTLIOAccelBuffer" _buffer;
I _swizzle;
B _writeSwizzleEnabled;
B _isCompressed;
@"MTLIOAccelBuffer" _masterBuffer;
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
s _masterHeapIndex;
s _masterBufferIndex;
Q _masterBufferOffset;
Q _length;
Q _bufferOffset;
Q _bufferBytesPerRow;
^v _pointer;
@? _deallocator;
B _allowGPUOptimizedContents;
```

## Properties

```
@property (TQ,R) uniqueIdentifier;
@property (T@"<MTLResource>",R) rootResource;
@property (T@"<MTLTexture>",R) parentTexture;
@property (TQ,R,V_parentRelativeLevel) parentRelativeLevel;
@property (TQ,R,V_parentRelativeSlice) parentRelativeSlice;
@property (T@"<MTLBuffer>",R) buffer;
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
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Class methods

```
+[MTLIOAccelTexture initNewTextureDataWithDevice:descriptor:sysMemSize:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:];
```

## Instance methods

```
-[MTLIOAccelTexture arrayLength];
-[MTLIOAccelTexture usage];
-[MTLIOAccelTexture buffer];
-[MTLIOAccelTexture depth];
-[MTLIOAccelTexture iosurface];
-[MTLIOAccelTexture hazardTrackingMode];
-[MTLIOAccelTexture copyAnnotations];
-[MTLIOAccelTexture mipmapLevelCount];
-[MTLIOAccelTexture setOwnerWithIdentity:];
-[MTLIOAccelTexture rootResourceIsSuballocatedBuffer];
-[MTLIOAccelTexture initWithBuffer:descriptor:sysMemOffset:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:];
-[MTLIOAccelTexture newSharedTextureHandle];
-[MTLIOAccelTexture copyFromPixels:rowBytes:imageBytes:toSlice:mipmapLevel:origin:size:];
-[MTLIOAccelTexture initWithTexture:pixelFormat:textureType:levels:slices:swizzle:];
-[MTLIOAccelTexture rotation];
-[MTLIOAccelTexture bufferBytesPerRow];
-[MTLIOAccelTexture parentRelativeLevel];
-[MTLIOAccelTexture formattedDescription:];
-[MTLIOAccelTexture allocatedSize];
-[MTLIOAccelTexture isCompressed];
-[MTLIOAccelTexture dealloc];
-[MTLIOAccelTexture textureType];
-[MTLIOAccelTexture initWithDevice:descriptor:sysMemPointer:sysMemSize:sysMemLength:sysMemRowBytes:args:argsSize:deallocator:];
-[MTLIOAccelTexture rootResource];
-[MTLIOAccelTexture replaceRegion:mipmapLevel:withBytes:bytesPerRow:];
-[MTLIOAccelTexture numFaces];
-[MTLIOAccelTexture swizzle];
-[MTLIOAccelTexture isDrawable];
-[MTLIOAccelTexture initWithBuffer:descriptor:sysMemOffset:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:isStrideTexture:];
-[MTLIOAccelTexture initWithDevice:descriptor:iosurface:plane:field:args:argsSize:];
-[MTLIOAccelTexture initWithTexture:pixelFormat:textureType:levels:slices:];
-[MTLIOAccelTexture uniqueIdentifier];
-[MTLIOAccelTexture initWithTextureInternal:pixelFormat:textureType:levels:slices:swizzle:compressedView:];
-[MTLIOAccelTexture compressionFeedback];
-[MTLIOAccelTexture gpuHandle];
-[MTLIOAccelTexture allowGPUOptimizedContents];
-[MTLIOAccelTexture sampleCount];
-[MTLIOAccelTexture initWithCompressedTexture:pixelFormat:textureType:level:slice:];
-[MTLIOAccelTexture parentTexture];
-[MTLIOAccelTexture isSparse];
-[MTLIOAccelTexture description];
-[MTLIOAccelTexture isFramebufferOnly];
-[MTLIOAccelTexture bufferOffset];
-[MTLIOAccelTexture initWithTexture:pixelFormat:];
-[MTLIOAccelTexture pixelFormat];
-[MTLIOAccelTexture swizzleKey];
-[MTLIOAccelTexture getBytes:bytesPerRow:fromRegion:mipmapLevel:];
-[MTLIOAccelTexture isAliasable];
-[MTLIOAccelTexture width];
-[MTLIOAccelTexture gpuResourceID];
-[MTLIOAccelTexture makeAliasable];
-[MTLIOAccelTexture isShareable];
-[MTLIOAccelTexture initWithDevice:descriptor:sysMemSize:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:];
-[MTLIOAccelTexture iosurfacePlane];
-[MTLIOAccelTexture height];
-[MTLIOAccelTexture copyFromSlice:mipmapLevel:origin:size:toPixels:rowBytes:imageBytes:];
-[MTLIOAccelTexture initWithHeap:resource:offset:length:device:descriptor:];
-[MTLIOAccelTexture parentRelativeSlice];
-[MTLIOAccelTexture initWithBuffer:descriptor:offset:bytesPerRow:];
-[MTLIOAccelTexture initWithMasterBuffer:heapIndex:bufferIndex:bufferOffset:length:descriptor:sysMemRowBytes:vidMemSize:vidMemRowBytes:args:argsSize:];
```
