# `MTLHeapDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLHeapDescriptor`
- 2 instance variables, 2 properties, 35 instance methods, 0 class methods

## Instance variables

```
^{MTLHeapDescriptorPrivate=QQQqBqQQQQq} _private;
@"MTLResourceAddressRangeArray" _addressRanges;
```

## Properties

```
@property (Tq,N) sparsePageSize;
@property (TB,N) sparsePageAccessCountersEnabled;
```

## Instance methods

```
-[MTLHeapDescriptorInternal resourceOptions];
-[MTLHeapDescriptorInternal setCpuCacheMode:];
-[MTLHeapDescriptorInternal hazardTrackingMode];
-[MTLHeapDescriptorInternal setStorageMode:];
-[MTLHeapDescriptorInternal setProtectionOptions:];
-[MTLHeapDescriptorInternal addressRanges];
-[MTLHeapDescriptorInternal setResourceOptions:];
-[MTLHeapDescriptorInternal pinnedGPUAddress];
-[MTLHeapDescriptorInternal cpuCacheMode];
-[MTLHeapDescriptorInternal setPinnedGPUAddress:];
-[MTLHeapDescriptorInternal setHazardTrackingMode:];
-[MTLHeapDescriptorInternal setMemoryPoolId:];
-[MTLHeapDescriptorInternal descriptorPrivate];
-[MTLHeapDescriptorInternal memoryPoolId];
-[MTLHeapDescriptorInternal storageMode];
-[MTLHeapDescriptorInternal sparsePageSize];
-[MTLHeapDescriptorInternal formattedDescription:];
-[MTLHeapDescriptorInternal protectionOptions];
-[MTLHeapDescriptorInternal init];
-[MTLHeapDescriptorInternal setSparsePageSize:];
-[MTLHeapDescriptorInternal dealloc];
-[MTLHeapDescriptorInternal size];
-[MTLHeapDescriptorInternal validateWithDevice:];
-[MTLHeapDescriptorInternal setType:];
-[MTLHeapDescriptorInternal type];
-[MTLHeapDescriptorInternal sparsePageAccessCountersEnabled];
-[MTLHeapDescriptorInternal hash];
-[MTLHeapDescriptorInternal description];
-[MTLHeapDescriptorInternal setMaxCompatiblePlacementSparsePageSize:];
-[MTLHeapDescriptorInternal copyWithZone:];
-[MTLHeapDescriptorInternal isEqual:];
-[MTLHeapDescriptorInternal setAddressRanges:];
-[MTLHeapDescriptorInternal maxCompatiblePlacementSparsePageSize];
-[MTLHeapDescriptorInternal setSize:];
-[MTLHeapDescriptorInternal setSparsePageAccessCountersEnabled:];
```
