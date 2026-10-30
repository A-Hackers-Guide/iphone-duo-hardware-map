# `_MTLIndirectRenderCommand`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLIndirectRenderCommandSPI`
- 0 instance variables, 4 properties, 64 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIndirectRenderCommand drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[_MTLIndirectRenderCommand setFrontFacingWinding:];
-[_MTLIndirectRenderCommand setBlendColorRed:green:blue:alpha:];
-[_MTLIndirectRenderCommand setCullMode:];
-[_MTLIndirectRenderCommand setVertexBuffer:offset:attributeStride:atIndex:];
-[_MTLIndirectRenderCommand setFragmentBuffer:offset:atIndex:];
-[_MTLIndirectRenderCommand setRenderPipelineState:];
-[_MTLIndirectRenderCommand reset];
-[_MTLIndirectRenderCommand setTriangleFillMode:];
-[_MTLIndirectRenderCommand setObjectBuffer:offset:atIndex:];
-[_MTLIndirectRenderCommand setStencilReferenceValue:];
-[_MTLIndirectRenderCommand setMeshBuffer:offset:atIndex:];
-[_MTLIndirectRenderCommand setViewports:count:];
-[_MTLIndirectRenderCommand drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTLIndirectRenderCommand drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[_MTLIndirectRenderCommand setViewport:];
-[_MTLIndirectRenderCommand setScissorRects:count:];
-[_MTLIndirectRenderCommand setDepthStencilState:];
-[_MTLIndirectRenderCommand setObjectThreadgroupMemoryLength:atIndex:];
-[_MTLIndirectRenderCommand setDepthClipMode:];
-[_MTLIndirectRenderCommand setDepthBias:slopeScale:clamp:];
-[_MTLIndirectRenderCommand setScissorRect:];
-[_MTLIndirectRenderCommand setDepthTestMinBound:maxBound:];
-[_MTLIndirectRenderCommand setVertexBuffer:offset:atIndex:];
-[_MTLIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:];
-[_MTLIndirectRenderCommand drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[_MTLIndirectRenderCommand getScissorRects];
-[_MTLIndirectRenderCommand clearBarrier];
-[_MTLIndirectRenderCommand drawArguments];
-[_MTLIndirectRenderCommand drawIndexedArguments];
-[_MTLIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[_MTLIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:tessellationFactorBufferScale:];
-[_MTLIndirectRenderCommand drawIndexedPatchesArguments];
-[_MTLIndirectRenderCommand drawMeshThreadgroupsArguments];
-[_MTLIndirectRenderCommand drawMeshThreadsArguments];
-[_MTLIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[_MTLIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:tessellationFactorBufferScale:];
-[_MTLIndirectRenderCommand drawPatchesArguments];
-[_MTLIndirectRenderCommand getBlendColor];
-[_MTLIndirectRenderCommand getCommandType];
-[_MTLIndirectRenderCommand getCullMode];
-[_MTLIndirectRenderCommand getDepthBiasInfo];
-[_MTLIndirectRenderCommand getDepthClipMode];
-[_MTLIndirectRenderCommand getDepthStencilState];
-[_MTLIndirectRenderCommand getDepthStencilStateUniqueIdentifier];
-[_MTLIndirectRenderCommand getDepthTestBounds];
-[_MTLIndirectRenderCommand getFragmentBufferAddressAtIndex:];
-[_MTLIndirectRenderCommand getFragmentBufferAtIndex:];
-[_MTLIndirectRenderCommand getFrontFacingWinding];
-[_MTLIndirectRenderCommand getMeshBufferAddressAtIndex:];
-[_MTLIndirectRenderCommand getObjectBufferAddressAtIndex:];
-[_MTLIndirectRenderCommand getObjectThreadgroupMemoryLengthAtIndex:];
-[_MTLIndirectRenderCommand getOptimizedStatus];
-[_MTLIndirectRenderCommand getPipelineStateUniqueIdentifier];
-[_MTLIndirectRenderCommand getStencilReferenceValues];
-[_MTLIndirectRenderCommand getTessellationFactorArguments];
-[_MTLIndirectRenderCommand getTriangleFillMode];
-[_MTLIndirectRenderCommand getVertexAttributeStrideAtIndex:];
-[_MTLIndirectRenderCommand getVertexBufferAddressAtIndex:];
-[_MTLIndirectRenderCommand getVertexBufferAtIndex:];
-[_MTLIndirectRenderCommand getViewports];
-[_MTLIndirectRenderCommand hasBarrier];
-[_MTLIndirectRenderCommand setBarrier];
-[_MTLIndirectRenderCommand setToolsDispatchBufferSPI:atIndex:stages:];
```
