# `MTLGPUDebugHeap`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsHeap`
- 7 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _enableResourceUsageValidation;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferLock;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _bufferIndices;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _textureLock;
{vector<std::pair<unsigned int, MTLTextureType>, std::allocator<std::pair<unsigned int, MTLTextureType>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _textureIndicesAndTypes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accelerationStructureLock;
{vector<unsigned int, std::allocator<unsigned int>>="__begin_"^I"__end_"^I""{?="__cap_"^I}} _accelerationStructureIndices;
```

## Instance methods

```
-[MTLGPUDebugHeap newAccelerationStructureWithSize:];
-[MTLGPUDebugHeap newTextureWithDescriptor:offset:];
-[MTLGPUDebugHeap newAccelerationStructureWithDescriptor:offset:];
-[MTLGPUDebugHeap newAccelerationStructureWithSize:offset:resourceIndex:];
-[MTLGPUDebugHeap newBufferWithLength:options:offset:];
-[MTLGPUDebugHeap newAccelerationStructureWithDescriptor:];
-[MTLGPUDebugHeap newAccelerationStructureWithSize:offset:];
-[MTLGPUDebugHeap newAccelerationStructureWithSize:resourceIndex:];
-[MTLGPUDebugHeap newTextureWithDescriptor:];
-[MTLGPUDebugHeap newBufferWithLength:options:];
-[MTLGPUDebugHeap initWithHeap:descriptor:device:];
-[MTLGPUDebugHeap _newGPUDebugAccelerationStructure:];
-[MTLGPUDebugHeap enumerateAccelerationStructureIndices:];
-[MTLGPUDebugHeap enumerateBufferIndices:];
-[MTLGPUDebugHeap enumerateTextureIndicesAndTypes:];
-[MTLGPUDebugHeap notifyResourceReleasing:];
```
