# `MTLToolsIndirectRenderCommand`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLIndirectRenderCommandSPI`
- 0 instance variables, 4 properties, 61 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsIndirectRenderCommand drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLToolsIndirectRenderCommand setFrontFacingWinding:];
-[MTLToolsIndirectRenderCommand setBlendColorRed:green:blue:alpha:];
-[MTLToolsIndirectRenderCommand setCullMode:];
-[MTLToolsIndirectRenderCommand setVertexBuffer:offset:attributeStride:atIndex:];
-[MTLToolsIndirectRenderCommand setFragmentBuffer:offset:atIndex:];
-[MTLToolsIndirectRenderCommand setRenderPipelineState:];
-[MTLToolsIndirectRenderCommand reset];
-[MTLToolsIndirectRenderCommand setTriangleFillMode:];
-[MTLToolsIndirectRenderCommand setObjectBuffer:offset:atIndex:];
-[MTLToolsIndirectRenderCommand setStencilReferenceValue:];
-[MTLToolsIndirectRenderCommand setMeshBuffer:offset:atIndex:];
-[MTLToolsIndirectRenderCommand setViewports:count:];
-[MTLToolsIndirectRenderCommand drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLToolsIndirectRenderCommand drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLToolsIndirectRenderCommand setViewport:];
-[MTLToolsIndirectRenderCommand setScissorRects:count:];
-[MTLToolsIndirectRenderCommand setDepthStencilState:];
-[MTLToolsIndirectRenderCommand setObjectThreadgroupMemoryLength:atIndex:];
-[MTLToolsIndirectRenderCommand setDepthClipMode:];
-[MTLToolsIndirectRenderCommand setDepthBias:slopeScale:clamp:];
-[MTLToolsIndirectRenderCommand setScissorRect:];
-[MTLToolsIndirectRenderCommand setDepthTestMinBound:maxBound:];
-[MTLToolsIndirectRenderCommand setVertexBuffer:offset:atIndex:];
-[MTLToolsIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:];
-[MTLToolsIndirectRenderCommand drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLToolsIndirectRenderCommand getScissorRects];
-[MTLToolsIndirectRenderCommand clearBarrier];
-[MTLToolsIndirectRenderCommand drawArguments];
-[MTLToolsIndirectRenderCommand drawIndexedArguments];
-[MTLToolsIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[MTLToolsIndirectRenderCommand drawIndexedPatchesArguments];
-[MTLToolsIndirectRenderCommand drawMeshThreadgroupsArguments];
-[MTLToolsIndirectRenderCommand drawMeshThreadsArguments];
-[MTLToolsIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[MTLToolsIndirectRenderCommand drawPatchesArguments];
-[MTLToolsIndirectRenderCommand getBlendColor];
-[MTLToolsIndirectRenderCommand getCommandType];
-[MTLToolsIndirectRenderCommand getCullMode];
-[MTLToolsIndirectRenderCommand getDepthBiasInfo];
-[MTLToolsIndirectRenderCommand getDepthClipMode];
-[MTLToolsIndirectRenderCommand getDepthStencilState];
-[MTLToolsIndirectRenderCommand getDepthStencilStateUniqueIdentifier];
-[MTLToolsIndirectRenderCommand getDepthTestBounds];
-[MTLToolsIndirectRenderCommand getFragmentBufferAddressAtIndex:];
-[MTLToolsIndirectRenderCommand getFragmentBufferAtIndex:];
-[MTLToolsIndirectRenderCommand getFrontFacingWinding];
-[MTLToolsIndirectRenderCommand getMeshBufferAddressAtIndex:];
-[MTLToolsIndirectRenderCommand getObjectBufferAddressAtIndex:];
-[MTLToolsIndirectRenderCommand getObjectThreadgroupMemoryLengthAtIndex:];
-[MTLToolsIndirectRenderCommand getOptimizedStatus];
-[MTLToolsIndirectRenderCommand getPipelineStateUniqueIdentifier];
-[MTLToolsIndirectRenderCommand getStencilReferenceValues];
-[MTLToolsIndirectRenderCommand getTessellationFactorArguments];
-[MTLToolsIndirectRenderCommand getTriangleFillMode];
-[MTLToolsIndirectRenderCommand getVertexAttributeStrideAtIndex:];
-[MTLToolsIndirectRenderCommand getVertexBufferAddressAtIndex:];
-[MTLToolsIndirectRenderCommand getVertexBufferAtIndex:];
-[MTLToolsIndirectRenderCommand getViewports];
-[MTLToolsIndirectRenderCommand hasBarrier];
-[MTLToolsIndirectRenderCommand setBarrier];
```
