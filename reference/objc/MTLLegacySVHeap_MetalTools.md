# `MTLLegacySVHeap`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsHeap`
- 7 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _enableResourceUsageValidation;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferLock;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _bufferIndices;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _textureLock;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _textureIndices;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accelerationStructureLock;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _accelerationStructureIndices;
```

## Instance methods

```
-[MTLLegacySVHeap newAccelerationStructureWithSize:];
-[MTLLegacySVHeap newTextureWithDescriptor:offset:];
-[MTLLegacySVHeap newAccelerationStructureWithDescriptor:offset:];
-[MTLLegacySVHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[MTLLegacySVHeap newBufferWithLength:options:offset:];
-[MTLLegacySVHeap newAccelerationStructureWithDescriptor:];
-[MTLLegacySVHeap newAccelerationStructureWithSize:offset:];
-[MTLLegacySVHeap newAccelerationStructureWithSize:resourceIndex:];
-[MTLLegacySVHeap newTextureWithDescriptor:];
-[MTLLegacySVHeap newBufferWithLength:options:];
-[MTLLegacySVHeap initWithHeap:descriptor:device:];
-[MTLLegacySVHeap _newGPUDebugAccelerationStructure:];
-[MTLLegacySVHeap enumerateAccelerationStructureIndices:];
-[MTLLegacySVHeap enumerateBufferIndices:];
-[MTLLegacySVHeap enumerateTextureIndices:];
-[MTLLegacySVHeap notifyResourceReleasing:];
```
