# `AGXG19FamilyIndirectRenderCommand`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalIndirectRenderCommand`
- Protocols: `MTLIndirectRenderCommandSPI`
- 2 instance variables, 4 properties, 68 instance methods, 0 class methods

## Instance variables

```
^v _encoder;
I _index;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyIndirectRenderCommand drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[AGXG19FamilyIndirectRenderCommand setFrontFacingWinding:];
-[AGXG19FamilyIndirectRenderCommand setBlendColorRed:green:blue:alpha:];
-[AGXG19FamilyIndirectRenderCommand setCullMode:];
-[AGXG19FamilyIndirectRenderCommand setVertexBuffer:offset:attributeStride:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setFragmentBuffer:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setRenderPipelineState:];
-[AGXG19FamilyIndirectRenderCommand reset];
-[AGXG19FamilyIndirectRenderCommand setTriangleFillMode:];
-[AGXG19FamilyIndirectRenderCommand setObjectBuffer:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setStencilReferenceValue:];
-[AGXG19FamilyIndirectRenderCommand setMeshBuffer:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setViewports:count:];
-[AGXG19FamilyIndirectRenderCommand drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyIndirectRenderCommand drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[AGXG19FamilyIndirectRenderCommand setThreadgroupMemoryLength:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setViewport:];
-[AGXG19FamilyIndirectRenderCommand setScissorRects:count:];
-[AGXG19FamilyIndirectRenderCommand setDepthStencilState:];
-[AGXG19FamilyIndirectRenderCommand setObjectThreadgroupMemoryLength:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setDepthClipMode:];
-[AGXG19FamilyIndirectRenderCommand setDepthBias:slopeScale:clamp:];
-[AGXG19FamilyIndirectRenderCommand setScissorRect:];
-[AGXG19FamilyIndirectRenderCommand setDepthTestMinBound:maxBound:];
-[AGXG19FamilyIndirectRenderCommand setVertexBuffer:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:];
-[AGXG19FamilyIndirectRenderCommand drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilyIndirectRenderCommand getScissorRects];
-[AGXG19FamilyIndirectRenderCommand clearBarrier];
-[AGXG19FamilyIndirectRenderCommand drawArguments];
-[AGXG19FamilyIndirectRenderCommand drawIndexedArguments];
-[AGXG19FamilyIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[AGXG19FamilyIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:tessellationFactorBufferScale:];
-[AGXG19FamilyIndirectRenderCommand drawIndexedPatchesArguments];
-[AGXG19FamilyIndirectRenderCommand drawMeshThreadgroupsArguments];
-[AGXG19FamilyIndirectRenderCommand drawMeshThreadsArguments];
-[AGXG19FamilyIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[AGXG19FamilyIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:tessellationFactorBufferScale:];
-[AGXG19FamilyIndirectRenderCommand drawPatchesArguments];
-[AGXG19FamilyIndirectRenderCommand getBlendColor];
-[AGXG19FamilyIndirectRenderCommand getCommandType];
-[AGXG19FamilyIndirectRenderCommand getCullMode];
-[AGXG19FamilyIndirectRenderCommand getDepthBiasInfo];
-[AGXG19FamilyIndirectRenderCommand getDepthClipMode];
-[AGXG19FamilyIndirectRenderCommand getDepthStencilStateUniqueIdentifier];
-[AGXG19FamilyIndirectRenderCommand getDepthTestBounds];
-[AGXG19FamilyIndirectRenderCommand getFragmentBufferAddressAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getFragmentBufferAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getFrontFacingWinding];
-[AGXG19FamilyIndirectRenderCommand getMeshBufferAddressAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getObjectBufferAddressAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getObjectThreadgroupMemoryLengthAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getPipelineStateUniqueIdentifier];
-[AGXG19FamilyIndirectRenderCommand getStencilReferenceValues];
-[AGXG19FamilyIndirectRenderCommand getTessellationFactorArguments];
-[AGXG19FamilyIndirectRenderCommand getTriangleFillMode];
-[AGXG19FamilyIndirectRenderCommand getVertexAttributeStrideAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getVertexBufferAddressAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getVertexBufferAtIndex:];
-[AGXG19FamilyIndirectRenderCommand getViewports];
-[AGXG19FamilyIndirectRenderCommand hasBarrier];
-[AGXG19FamilyIndirectRenderCommand setBarrier];
-[AGXG19FamilyIndirectRenderCommand setToolsDispatchBufferSPI:atIndex:stages:];
-[AGXG19FamilyIndirectRenderCommand getPipelineState];
-[AGXG19FamilyIndirectRenderCommand initWithEncoder:withIndex:];
-[AGXG19FamilyIndirectRenderCommand setFragmentArguments:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setTileArguments:offset:atIndex:];
-[AGXG19FamilyIndirectRenderCommand setVertexArguments:offset:atIndex:];
```
