# `MTLDebugIndirectRenderCommand`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIndirectRenderCommand`
- 3 instance variables, 2 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"MTLIndirectCommandBufferDescriptor" _desc;
Q _index;
@"<MTLIndirectCommandBufferSPI>" _iCB;
```

## Properties

```
@property (TQ,R) index;
@property (T@"<MTLIndirectCommandBuffer>",R) indirectCommandBuffer;
```

## Instance methods

```
-[MTLDebugIndirectRenderCommand drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLDebugIndirectRenderCommand setFrontFacingWinding:];
-[MTLDebugIndirectRenderCommand setBlendColorRed:green:blue:alpha:];
-[MTLDebugIndirectRenderCommand setCullMode:];
-[MTLDebugIndirectRenderCommand setVertexBuffer:offset:attributeStride:atIndex:];
-[MTLDebugIndirectRenderCommand setFragmentBuffer:offset:atIndex:];
-[MTLDebugIndirectRenderCommand setRenderPipelineState:];
-[MTLDebugIndirectRenderCommand dealloc];
-[MTLDebugIndirectRenderCommand setTriangleFillMode:];
-[MTLDebugIndirectRenderCommand index];
-[MTLDebugIndirectRenderCommand setObjectBuffer:offset:atIndex:];
-[MTLDebugIndirectRenderCommand setStencilReferenceValue:];
-[MTLDebugIndirectRenderCommand setMeshBuffer:offset:atIndex:];
-[MTLDebugIndirectRenderCommand setViewports:count:];
-[MTLDebugIndirectRenderCommand drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLDebugIndirectRenderCommand drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLDebugIndirectRenderCommand setViewport:];
-[MTLDebugIndirectRenderCommand setScissorRects:count:];
-[MTLDebugIndirectRenderCommand setDepthStencilState:];
-[MTLDebugIndirectRenderCommand setObjectThreadgroupMemoryLength:atIndex:];
-[MTLDebugIndirectRenderCommand setDepthClipMode:];
-[MTLDebugIndirectRenderCommand setDepthBias:slopeScale:clamp:];
-[MTLDebugIndirectRenderCommand setScissorRect:];
-[MTLDebugIndirectRenderCommand setDepthTestMinBound:maxBound:];
-[MTLDebugIndirectRenderCommand setVertexBuffer:offset:atIndex:];
-[MTLDebugIndirectRenderCommand setStencilFrontReferenceValue:backReferenceValue:];
-[MTLDebugIndirectRenderCommand drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLDebugIndirectRenderCommand clearBarrier];
-[MTLDebugIndirectRenderCommand drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[MTLDebugIndirectRenderCommand drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:tessellationFactorBuffer:tessellationFactorBufferOffset:tessellationFactorBufferInstanceStride:];
-[MTLDebugIndirectRenderCommand setBarrier];
-[MTLDebugIndirectRenderCommand indirectCommandBuffer];
-[MTLDebugIndirectRenderCommand initWithBaseObject:descriptor:indexCount:indirectCommandBuffer:];
```
