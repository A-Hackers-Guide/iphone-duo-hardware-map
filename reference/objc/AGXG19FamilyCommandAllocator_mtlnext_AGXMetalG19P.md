# `AGXG19FamilyCommandAllocator_mtlnext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetal4CommandAllocator`
- Protocols: `MTL4CommandAllocatorGGDSPI`
- 3 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
^v _impl;
B commandBufferActivity;
@"AccelerationStructureCommandRecorder" _adsCommandRecorder;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyCommandAllocator_mtlnext initWithDevice:];
-[AGXG19FamilyCommandAllocator_mtlnext initWithDevice:descriptor:];
-[AGXG19FamilyCommandAllocator_mtlnext allocatedSize];
-[AGXG19FamilyCommandAllocator_mtlnext dealloc];
-[AGXG19FamilyCommandAllocator_mtlnext reset];
-[AGXG19FamilyCommandAllocator_mtlnext initWithDeviceAndAliasToDevicePools:];
-[AGXG19FamilyCommandAllocator_mtlnext alertCommandBufferActivityStart];
-[AGXG19FamilyCommandAllocator_mtlnext accelerationStructureCommandRecorder];
-[AGXG19FamilyCommandAllocator_mtlnext initResourcePools:];
```
