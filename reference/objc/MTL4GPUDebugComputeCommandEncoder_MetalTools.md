# `MTL4GPUDebugComputeCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsComputeCommandEncoder`
- Protocols: `MTLGPUDebugCommandEncoder`
- 11 instance variables, 5 properties, 73 instance methods, 0 class methods

## Instance variables

```
I useResourceIteration;
B _enableUseResourceValidation;
I _commandBufferJumpNestingLevel;
^{Options=IiiiI{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}} _options;
{MTLGPUDebugThreadgroupLengths="threadgroupSizes"[31I]"entries"[32{GPUDebugThreadgroupTableEntry="offset"I"length"I}]"needsFlush"B} _threadgroup;
{GPUDebugEventUUIDPacket="crc"Q"pipelineStateID"Q"entryPointImageID"Q"encoderID"I"commandInfo"I} _dispatchID;
@"MTLGPUDebugComputePipelineState" _currentPipeline;
[31{GPUDebugEncoderBoundBufAddress="gpuAddress"Q"stride"Q}] _computeEncoderBoundBufAddressTable;
[31{GPUDebugEncoderBoundBuffers="resource"@"<MTLResource>""offset"Q"stride"Q"type"Q}] _computeEncoderBoundBuffers;
[40Q] _internalBindingTable;
@"<MTL4ArgumentTable>" currentArgumentTable;
```

## Properties

```
@property (TI,R) encoderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4GPUDebugComputeCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4GPUDebugComputeCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MTL4GPUDebugComputeCommandEncoder endEncoding];
-[MTL4GPUDebugComputeCommandEncoder copyFromTexture:toTexture:];
-[MTL4GPUDebugComputeCommandEncoder dealloc];
-[MTL4GPUDebugComputeCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:];
-[MTL4GPUDebugComputeCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MTL4GPUDebugComputeCommandEncoder optimizeContentsForCPUAccess:slice:level:];
-[MTL4GPUDebugComputeCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTL4GPUDebugComputeCommandEncoder setComputePipelineState:];
-[MTL4GPUDebugComputeCommandEncoder optimizeContentsForGPUAccess:];
-[MTL4GPUDebugComputeCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTL4GPUDebugComputeCommandEncoder resetCommandsInBuffer:withRange:];
-[MTL4GPUDebugComputeCommandEncoder optimizeContentsForCPUAccess:];
-[MTL4GPUDebugComputeCommandEncoder optimizeContentsForGPUAccess:slice:level:];
-[MTL4GPUDebugComputeCommandEncoder copyFromBuffer:sourceOffset:toBuffer:destinationOffset:size:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4GPUDebugComputeCommandEncoder generateMipmapsForTexture:];
-[MTL4GPUDebugComputeCommandEncoder setArgumentTable:];
-[MTL4GPUDebugComputeCommandEncoder beginVirtualSubstream];
-[MTL4GPUDebugComputeCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:];
-[MTL4GPUDebugComputeCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTL4GPUDebugComputeCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:sourcePlane:toTensor:destinationOrigin:destinationDimensions:destinationPlane:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:];
-[MTL4GPUDebugComputeCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:];
-[MTL4GPUDebugComputeCommandEncoder deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:];
-[MTL4GPUDebugComputeCommandEncoder deserializePrimitiveAccelerationStructure:fromBuffer:];
-[MTL4GPUDebugComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:threadsPerThreadgroup:];
-[MTL4GPUDebugComputeCommandEncoder dispatchThreadsWithIndirectBuffer:];
-[MTL4GPUDebugComputeCommandEncoder encodeEndDoWhile:comparison:referenceValue:];
-[MTL4GPUDebugComputeCommandEncoder encodeEndIf];
-[MTL4GPUDebugComputeCommandEncoder encodeEndWhile];
-[MTL4GPUDebugComputeCommandEncoder encodeStartDoWhile];
-[MTL4GPUDebugComputeCommandEncoder encodeStartIf:offset:comparison:referenceValue:];
-[MTL4GPUDebugComputeCommandEncoder encodeStartWhile:offset:comparison:referenceValue:];
-[MTL4GPUDebugComputeCommandEncoder endVirtualSubstream];
-[MTL4GPUDebugComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4GPUDebugComputeCommandEncoder fillBuffer:range:value:];
-[MTL4GPUDebugComputeCommandEncoder nextVirtualSubstream];
-[MTL4GPUDebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:];
-[MTL4GPUDebugComputeCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:options:];
-[MTL4GPUDebugComputeCommandEncoder waitForVirtualSubstream:];
-[MTL4GPUDebugComputeCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:];
-[MTL4GPUDebugComputeCommandEncoder commandInfo];
-[MTL4GPUDebugComputeCommandEncoder setComputePipelineStateBuffers:];
-[MTL4GPUDebugComputeCommandEncoder needsDeepResidencyCheckForAccelerationStructure:withDescriptor:];
-[MTL4GPUDebugComputeCommandEncoder addInCommandResourcesFromBVHDescriptor:commandInfo:];
-[MTL4GPUDebugComputeCommandEncoder addInCommandResourcesFromGeometryDescriptor:];
-[MTL4GPUDebugComputeCommandEncoder bindInternalBuffer:index:];
-[MTL4GPUDebugComputeCommandEncoder bindInternalBufferWithOffset:offset:index:];
-[MTL4GPUDebugComputeCommandEncoder bindInternalValue:index:];
-[MTL4GPUDebugComputeCommandEncoder blitAccelerationStructureType:toAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder blitInstanceTypetoAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder blitPrimitiveTypetoAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder blitTypeFromAccelerationStructure:toAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder blitTypeFromAccelerationStructureDescriptor:toAccelerationStructure:];
-[MTL4GPUDebugComputeCommandEncoder copyFromInternalBuffer:sourceOffset:toInternalBuffer:destinationOffset:size:];
-[MTL4GPUDebugComputeCommandEncoder encoderID];
-[MTL4GPUDebugComputeCommandEncoder flushBindings];
-[MTL4GPUDebugComputeCommandEncoder initWithComputeCommandEncoder:commandBuffer:encoderID:];
-[MTL4GPUDebugComputeCommandEncoder internalValueAtIndex:];
-[MTL4GPUDebugComputeCommandEncoder performDeepResidencyCheckWithDescriptor:commandInfo:];
-[MTL4GPUDebugComputeCommandEncoder retrieveBufferFromBufferRange:];
-[MTL4GPUDebugComputeCommandEncoder setBufferUsageTable:textureUsageTable:tensorResidencyTable:bvhUsageTable:textureTypeTable:];
-[MTL4GPUDebugComputeCommandEncoder setInternalBytes:length:atIndex:];
-[MTL4GPUDebugComputeCommandEncoder temporaryBufferWithBytes:length:];
-[MTL4GPUDebugComputeCommandEncoder temporaryBufferWithLength:];
```
