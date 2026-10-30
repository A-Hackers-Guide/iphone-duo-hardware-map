# `MTLDebugBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBuffer`
- Protocols: `MTLDebugResourcePurgeable`
- 9 instance variables, 4 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"MTLDebugResource" _common;
Q _length;
@"MTLDebugDevice" _debugDevice;
@"NSMutableArray" _debugMarkers;
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _purgeableStateToken;
B _purgeableStateHasBeenSet;
B _isContentExposedToCPU;
r^v _pointer;
q _placementSparsePageSize;
```

## Properties

```
@property (T@"MTLDebugResource",R,N,V_common) common;
@property (Tr^v,R,N,V_pointer) pointer;
@property (Tq,R,N,V_placementSparsePageSize) placementSparsePageSize;
@property (TB,N,V_isContentExposedToCPU) isContentExposedToCPU;
```

## Instance methods

```
-[MTLDebugBuffer didModifyRange:];
-[MTLDebugBuffer replaceBackingWithBytesNoCopy:length:deallocator:];
-[MTLDebugBuffer resourceIndex];
-[MTLDebugBuffer removeAllDebugMarkers];
-[MTLDebugBuffer detachBacking];
-[MTLDebugBuffer placementSparsePageSize];
-[MTLDebugBuffer addDebugMarker:range:];
-[MTLDebugBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[MTLDebugBuffer contents];
-[MTLDebugBuffer replaceBackingWithRanges:readOnly:];
-[MTLDebugBuffer dealloc];
-[MTLDebugBuffer gpuAddress];
-[MTLDebugBuffer length];
-[MTLDebugBuffer parentGPUAddress];
-[MTLDebugBuffer setParentGPUSize:];
-[MTLDebugBuffer setParentGPUAddress:];
-[MTLDebugBuffer setPurgeableState:];
-[MTLDebugBuffer description];
-[MTLDebugBuffer parentGPUSize];
-[MTLDebugBuffer common];
-[MTLDebugBuffer makeAliasable];
-[MTLDebugBuffer newTensorWithDescriptor:offset:error:];
-[MTLDebugBuffer newTextureWithDescriptor:offset:bytesPerRow:];
-[MTLDebugBuffer doesAliasAllResources:count:];
-[MTLDebugBuffer doesAliasAnyResources:count:];
-[MTLDebugBuffer doesAliasResource:];
-[MTLDebugBuffer pointer];
-[MTLDebugBuffer purgeableStateValidForRendering];
-[MTLDebugBuffer copyDebugMarkers];
-[MTLDebugBuffer initWithBuffer:device:bytes:options:];
-[MTLDebugBuffer initWithBuffer:device:options:];
-[MTLDebugBuffer initWithBuffer:device:options:placementSparsePageSize:];
-[MTLDebugBuffer initWithBuffer:heap:device:options:];
-[MTLDebugBuffer isContentExposedToCPU];
-[MTLDebugBuffer lockPurgeableState];
-[MTLDebugBuffer setIsContentExposedToCPU:];
-[MTLDebugBuffer unlockPurgeableState];
```
