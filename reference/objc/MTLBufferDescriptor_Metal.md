# `MTLBufferDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 13 instance variables, 16 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _noCopy;
Q _length;
^v _contents;
@? _deallocator;
Q _alignment;
Q _resourceOptions;
Q _pinnedGPUAddress;
Q _parentGPUAddress;
Q _parentGPUSize;
Q _pointerTag;
@"MTLResourceAddressRangeArray" _addressRanges;
^{__IOSurface=} _iosurface;
q _placementSparsePageSize;
```

## Properties

```
@property (TQ,N,V_pinnedGPUAddress) pinnedGPUAddress;
@property (TQ,N,V_parentGPUAddress) parentGPUAddress;
@property (TQ,N,V_parentGPUSize) parentGPUSize;
@property (TQ,N,V_pointerTag) pointerTag;
@property (T@"MTLResourceAddressRangeArray",&,N,V_addressRanges) addressRanges;
@property (TQ,N,V_length) length;
@property (TQ,N,V_resourceOptions) resourceOptions;
@property (TQ,D,N) cpuCacheMode;
@property (TQ,D,N) storageMode;
@property (TQ,D,N) hazardTrackingMode;
@property (T^v,N,V_contents) contents;
@property (TB,N,V_noCopy) noCopy;
@property (T@?,N,V_deallocator) deallocator;
@property (TQ,N,V_alignment) alignment;
@property (T^{__IOSurface=},N,V_iosurface) iosurface;
@property (Tq,N,V_placementSparsePageSize) placementSparsePageSize;
```

## Instance methods

```
-[MTLBufferDescriptor resourceOptions];
-[MTLBufferDescriptor setCpuCacheMode:];
-[MTLBufferDescriptor iosurface];
-[MTLBufferDescriptor hazardTrackingMode];
-[MTLBufferDescriptor setStorageMode:];
-[MTLBufferDescriptor pointerTag];
-[MTLBufferDescriptor addressRanges];
-[MTLBufferDescriptor placementSparsePageSize];
-[MTLBufferDescriptor setResourceOptions:];
-[MTLBufferDescriptor pinnedGPUAddress];
-[MTLBufferDescriptor cpuCacheMode];
-[MTLBufferDescriptor setPinnedGPUAddress:];
-[MTLBufferDescriptor setHazardTrackingMode:];
-[MTLBufferDescriptor setContents:];
-[MTLBufferDescriptor setPlacementSparsePageSize:];
-[MTLBufferDescriptor storageMode];
-[MTLBufferDescriptor contents];
-[MTLBufferDescriptor deallocator];
-[MTLBufferDescriptor setIosurface:];
-[MTLBufferDescriptor init];
-[MTLBufferDescriptor setDeallocator:];
-[MTLBufferDescriptor dealloc];
-[MTLBufferDescriptor setAlignment:];
-[MTLBufferDescriptor setPointerTag:];
-[MTLBufferDescriptor length];
-[MTLBufferDescriptor alignment];
-[MTLBufferDescriptor parentGPUAddress];
-[MTLBufferDescriptor setParentGPUSize:];
-[MTLBufferDescriptor setParentGPUAddress:];
-[MTLBufferDescriptor hash];
-[MTLBufferDescriptor parentGPUSize];
-[MTLBufferDescriptor setNoCopy:];
-[MTLBufferDescriptor copyWithZone:];
-[MTLBufferDescriptor noCopy];
-[MTLBufferDescriptor isEqual:];
-[MTLBufferDescriptor setAddressRanges:];
-[MTLBufferDescriptor setLength:];
```
