# `MTLIndirectRenderCommand` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance methods

```
-[MTLIndirectRenderCommand drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLIndirectRenderCommand setFrontFacingWinding:];
-[MTLIndirectRenderCommand setCullMode:];
-[MTLIndirectRenderCommand setVertexBuffer:offset:attributeStride:atIndex:];
-[MTLIndirectRenderCommand setFragmentBuffer:offset:atIndex:];
-[MTLIndirectRenderCommand setRenderPipelineState:];
-[MTLIndirectRenderCommand reset];
-[MTLIndirectRenderCommand setTriangleFillMode:];
-[MTLIndirectRenderCommand setObjectBuffer:offset:atIndex:];
-[MTLIndirectRenderCommand setMeshBuffer:offset:atIndex:];
-[MTLIndirectRenderCommand drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLIndirectRenderCommand drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLIndirectRenderCommand setDepthStencilState:];
-[MTLIndirectRenderCommand setObjectThreadgroupMemoryLength:atIndex:];
-[MTLIndirectRenderCommand setDepthClipMode:];
-[MTLIndirectRenderCommand setDepthBias:slopeScale:clamp:];
-[MTLIndirectRenderCommand setVertexBuffer:offset:atIndex:];
-[MTLIndirectRenderCommand drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLIndirectRenderCommand clearBarrier];
-[MTLIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[MTLIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[MTLIndirectRenderCommand setBarrier];
```
