# `MTL4DebugRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsRenderCommandEncoder`
- 34 instance variables, 0 properties, 66 instance methods, 0 class methods

## Instance variables

```
@"MTL4DebugCommandEncoder" _debugCommandEncoder;
@"MTL4RenderPassDescriptor" _descriptor;
{MTL4DebugRenderCommandEncoderState="canSetRenderPipelineState"b1"canSetViewport"b1"canSetVertexAmplificationFactor"b1"canSetCullMode"b1"canSetDepthClipMode"b1"canSetDepthBias"b1"canSetScissorRect"b1"canSetTriangleFillMode"b1"canSetBlendColor"b1"canSetDepthStencilState"b1"canSetStencilReferenceValue"b1"canSetVisibilityResultMode"b1"canSetFrontFacingWinding"b1"hasSetRenderPipelineState"b1"hasSetViewport"b1"hasSetVertexAmplificationFactor"b1"hasSetCullMode"b1"hasSetDepthClipMode"b1"hasSetDepthBias"b1"hasSetScissorRect"b1"hasSetTriangleFillMode"b1"hasSetBlendColor"b1"hasSetDepthStencilState"b1"hasSetStencilReferenceValue"b1"hasSetVisibilityResultMode"b1"hasSetFrontFacingWinding"b1} _encoderState;
I _unknownStoreActions;
[31{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _currentThreadgroupMemoryArguments;
[31{MTLDebugFunctionArgument="isValid"B"hasBeenUsed"B"type"Q"object"@"baseLevel"Q"bufferLength"Q"bufferOffset"Q"bufferAttributeStride"Q"threadgroupMemoryLength"Q"threadgroupMemoryOffset"Q"hasLodClamp"B"lodMinClamp"f"lodMaxClamp"f}] _currentObjectThreadgroupMemoryLengths;
@"<MTLRenderPipelineState>" _currentRenderPipelineState;
{vector<MTLViewport, std::allocator<MTLViewport>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _currentViewports;
Q _currentVertexAmplificationCount;
Q _currentCullMode;
Q _currentDepthClipMode;
f _currentDepthBias;
f _currentDepthTestMinBound;
f _currentDepthTestMaxBound;
f _currentDepthSlopeScale;
f _currentDepthClamp;
{vector<MTLScissorRect, std::allocator<MTLScissorRect>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _currentScissorRects;
Q _currentTriangleFillMode;
f _currentBlendColorRed;
f _currentBlendColorGreen;
f _currentBlendColorBlue;
f _currentBlendColorAlpha;
@"<MTLDepthStencilState>" _currentDepthStencilState;
I _currentStencilFrontReferenceValue;
I _currentStencilBackReferenceValue;
Q _currentVisibilityResultMode;
Q _currentVisibilityResultModeOffset;
{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>="__tree_"{__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _allVisibilityOffsets;
Q _currentFrontFacingWinding;
Q _width;
Q _height;
Q _resolvedColorSampleCount;
Q _resolvedRasterSampleCount;
@"MTLLogicalToPhysicalColorAttachmentMap" _colorAttachmentMap;
```

## Instance methods

```
-[MTL4DebugRenderCommandEncoder executeCommandsInBuffer:withRange:];
-[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTL4DebugRenderCommandEncoder setLineWidth:];
-[MTL4DebugRenderCommandEncoder setFrontFacingWinding:];
-[MTL4DebugRenderCommandEncoder setBlendColorRed:green:blue:alpha:];
-[MTL4DebugRenderCommandEncoder setColorStoreAction:atIndex:];
-[MTL4DebugRenderCommandEncoder setCullMode:];
-[MTL4DebugRenderCommandEncoder setVisibilityResultMode:offset:];
-[MTL4DebugRenderCommandEncoder endEncoding];
-[MTL4DebugRenderCommandEncoder setRenderPipelineState:];
-[MTL4DebugRenderCommandEncoder dealloc];
-[MTL4DebugRenderCommandEncoder setTriangleFillMode:];
-[MTL4DebugRenderCommandEncoder setStencilReferenceValue:];
-[MTL4DebugRenderCommandEncoder setViewports:count:];
-[MTL4DebugRenderCommandEncoder drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4DebugRenderCommandEncoder setStencilStoreAction:];
-[MTL4DebugRenderCommandEncoder setThreadgroupMemoryLength:offset:atIndex:];
-[MTL4DebugRenderCommandEncoder setViewport:];
-[MTL4DebugRenderCommandEncoder setScissorRects:count:];
-[MTL4DebugRenderCommandEncoder setVertexAmplificationCount:viewMappings:];
-[MTL4DebugRenderCommandEncoder commandBuffer];
-[MTL4DebugRenderCommandEncoder setDepthStencilState:];
-[MTL4DebugRenderCommandEncoder setDepthStoreAction:];
-[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTL4DebugRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[MTL4DebugRenderCommandEncoder setObjectThreadgroupMemoryLength:atIndex:];
-[MTL4DebugRenderCommandEncoder setDepthClipMode:];
-[MTL4DebugRenderCommandEncoder setDepthBias:slopeScale:clamp:];
-[MTL4DebugRenderCommandEncoder setDepthClipModeSPI:];
-[MTL4DebugRenderCommandEncoder setScissorRect:];
-[MTL4DebugRenderCommandEncoder setDepthTestMinBound:maxBound:];
-[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:];
-[MTL4DebugRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:];
-[MTL4DebugRenderCommandEncoder drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:];
-[MTL4DebugRenderCommandEncoder updateFence:afterEncoderStages:];
-[MTL4DebugRenderCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[MTL4DebugRenderCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[MTL4DebugRenderCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[MTL4DebugRenderCommandEncoder dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:];
-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:];
-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferLength:instanceCount:baseVertex:baseInstance:];
-[MTL4DebugRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferLength:indirectBuffer:];
-[MTL4DebugRenderCommandEncoder drawMeshThreadgroupsWithIndirectBuffer:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTL4DebugRenderCommandEncoder drawPrimitives:indirectBuffer:];
-[MTL4DebugRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:];
-[MTL4DebugRenderCommandEncoder setArgumentTable:atStages:];
-[MTL4DebugRenderCommandEncoder setColorAttachmentMap:];
-[MTL4DebugRenderCommandEncoder setCommandDataCorruptModeSPI:];
-[MTL4DebugRenderCommandEncoder setVertexAmplificationMode:value:];
-[MTL4DebugRenderCommandEncoder waitForFence:beforeEncoderStages:];
-[MTL4DebugRenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:];
-[MTL4DebugRenderCommandEncoder _resetEncoderWithDescriptor:];
-[MTL4DebugRenderCommandEncoder _updateEncoderStateAfterDispatch];
-[MTL4DebugRenderCommandEncoder _updateEncoderStateAfterDraw];
-[MTL4DebugRenderCommandEncoder _validateDispatchThreadsPerTileCommon:threadsPerTile:];
-[MTL4DebugRenderCommandEncoder _validateDrawCommon:primitiveType:instanceCount:];
-[MTL4DebugRenderCommandEncoder _validateFramebufferCompatibility:pipelineState:];
-[MTL4DebugRenderCommandEncoder _validateFunctionArguments:stages:];
-[MTL4DebugRenderCommandEncoder _validateIndexedDrawCommon:indexBuffer:indexType:indexBufferLength:];
-[MTL4DebugRenderCommandEncoder _validateLBRT:];
-[MTL4DebugRenderCommandEncoder _validateMeshDrawCommon:];
-[MTL4DebugRenderCommandEncoder _validateThreadgroupSize:stage:context:];
-[MTL4DebugRenderCommandEncoder _validateThreadsPerObjectThreadgroup:threadsPerMeshThreadgroup:context:];
-[MTL4DebugRenderCommandEncoder initWithRenderCommandEncoder:commandBuffer:descriptor:];
```
