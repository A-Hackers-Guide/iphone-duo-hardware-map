# `MTLDebugHeap`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsHeap`
- Protocols: `MTLDebugResourcePurgeable`
- 4 instance variables, 2 properties, 28 instance methods, 0 class methods

## Instance variables

```
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
@"MTLDebugDevice" _debugDevice;
q _maxCompatiblePlacementSparsePageSize;
```

## Properties

```
@property (T@"MTLDebugDevice",R,N,V_debugDevice) debugDevice;
@property (Tq,R,N,V_maxCompatiblePlacementSparsePageSize) maxCompatiblePlacementSparsePageSize;
```

## Instance methods

```
-[MTLDebugHeap detachBacking];
-[MTLDebugHeap newAccelerationStructureWithSize:];
-[MTLDebugHeap newTextureWithDescriptor:offset:];
-[MTLDebugHeap newAccelerationStructureWithDescriptor:offset:];
-[MTLDebugHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[MTLDebugHeap replaceBackingWithRanges:readOnly:];
-[MTLDebugHeap newBufferWithLength:options:offset:];
-[MTLDebugHeap newAccelerationStructureWithDescriptor:];
-[MTLDebugHeap newAccelerationStructureWithSize:offset:];
-[MTLDebugHeap newAccelerationStructureWithSize:resourceIndex:];
-[MTLDebugHeap newTextureWithDescriptor:];
-[MTLDebugHeap setPurgeableState:];
-[MTLDebugHeap maxAvailableSizeWithAlignment:];
-[MTLDebugHeap maxCompatiblePlacementSparsePageSize];
-[MTLDebugHeap newBufferWithLength:options:];
-[MTLDebugHeap purgeableStateValidForRendering];
-[MTLDebugHeap _newDebugAccelerationStructure:];
-[MTLDebugHeap debugDevice];
-[MTLDebugHeap initWithHeap:device:];
-[MTLDebugHeap initWithHeap:device:maxCompatiblePlacementSparsePageSize:];
-[MTLDebugHeap lockPurgeableState];
-[MTLDebugHeap unlockPurgeableState];
-[MTLDebugHeap validateHeapResourceOptions:isTexture:isIOSurface:context:];
-[MTLDebugHeap validateHeapTextureUsage:options:context:];
-[MTLDebugHeap validateOffset:withRequirements:];
-[MTLDebugHeap validatePixelFormatWithHeap:context:];
-[MTLDebugHeap validateRaytracingHeap];
-[MTLDebugHeap validateTextureAtomicFlags:context:];
```
