# `IOGPUMetalBuffer`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResource`
- 10 instance variables, 6 properties, 32 instance methods, 0 class methods

## Instance variables

```
^v _pointer;
@? _deallocator;
@"IOGPUMetalBuffer" _primaryBuffer;
s _primaryHeapIndex;
s _primaryBufferIndex;
Q _primaryBufferOffset;
Q _length;
^{__IOSurface=} _iosurface;
^{__IOSurface=} _aneIOSurface;
q _placementSparsePageSize;
```

## Properties

```
@property (TQ,R) length;
@property (T^v,R,N) contents;
@property (T^{__IOSurface=},R,V_iosurface) iosurface;
@property (TQ,R) allocatedSize;
@property (T^{__IOSurface=},R) _aneIOSurface;
@property (Tq,R,V_placementSparsePageSize) placementSparsePageSize;
```

## Instance methods

```
-[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:args:argsSize:deallocator:];
-[IOGPUMetalBuffer didModifyRange:];
-[IOGPUMetalBuffer replaceBackingWithBytesNoCopy:length:deallocator:];
-[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:args:argsSize:deallocator:];
-[IOGPUMetalBuffer iosurface];
-[IOGPUMetalBuffer initWithDevice:addressRanges:addressRangeCount:length:options:gpuAddress:args:argsSize:];
-[IOGPUMetalBuffer removeAllDebugMarkers];
-[IOGPUMetalBuffer copyAnnotations];
-[IOGPUMetalBuffer initWithPrimaryBuffer:heapIndex:bufferIndex:bufferOffset:length:args:argsSize:gpuTag:];
-[IOGPUMetalBuffer initWithHeap:resource:offset:length:];
-[IOGPUMetalBuffer initWithPrimaryBuffer:heapIndex:bufferIndex:bufferOffset:length:args:argsSize:];
-[IOGPUMetalBuffer detachBacking];
-[IOGPUMetalBuffer setOwnerWithIdentity:];
-[IOGPUMetalBuffer placementSparsePageSize];
-[IOGPUMetalBuffer _aneIOSurface];
-[IOGPUMetalBuffer initWithDevice:pointer:length:options:sysMemSize:gpuAddress:args:argsSize:deallocator:];
-[IOGPUMetalBuffer initWithHeap:resource:offset:length:gpuTag:];
-[IOGPUMetalBuffer addDebugMarker:range:];
-[IOGPUMetalBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[IOGPUMetalBuffer initWithDevice:iosurface:gpuAddress:args:argsSize:];
-[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:args:argsSize:deallocator:];
-[IOGPUMetalBuffer emitResourceInfoTraceEvent];
-[IOGPUMetalBuffer initWithDevice:iosurface:args:argsSize:];
-[IOGPUMetalBuffer initWithDevice:pointer:length:options:sysMemSize:vidMemSize:args:argsSize:deallocator:];
-[IOGPUMetalBuffer initWithDevice:pointer:length:alignment:options:sysMemSize:gpuAddress:gpuTag:placementSparsePageSize:placementSparseResidencyBytes:args:argsSize:deallocator:];
-[IOGPUMetalBuffer contents];
-[IOGPUMetalBuffer replaceBackingWithRanges:readOnly:];
-[IOGPUMetalBuffer formattedDescription:];
-[IOGPUMetalBuffer allocatedSize];
-[IOGPUMetalBuffer dealloc];
-[IOGPUMetalBuffer length];
-[IOGPUMetalBuffer description];
```
