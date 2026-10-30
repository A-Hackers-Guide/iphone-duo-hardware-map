# `AGXG19FamilySampledRenderContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AGXG19FamilyRenderContext`
- 1 instance variables, 0 properties, 23 instance methods, 0 class methods

## Instance variables

```
^v _sampled_impl;
```

## Instance methods

```
-[AGXG19FamilySampledRenderContext drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[AGXG19FamilySampledRenderContext drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:];
-[AGXG19FamilySampledRenderContext drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:];
-[AGXG19FamilySampledRenderContext drawPrimitives:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilySampledRenderContext setRenderPipelineState:];
-[AGXG19FamilySampledRenderContext drawMeshThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilySampledRenderContext dealloc];
-[AGXG19FamilySampledRenderContext drawPatches:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilySampledRenderContext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:];
-[AGXG19FamilySampledRenderContext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:];
-[AGXG19FamilySampledRenderContext drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilySampledRenderContext drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[AGXG19FamilySampledRenderContext drawPrimitives:vertexStart:vertexCount:];
-[AGXG19FamilySampledRenderContext drawPrimitives:vertexStart:vertexCount:instanceCount:];
-[AGXG19FamilySampledRenderContext drawIndexedPatches:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilySampledRenderContext drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[AGXG19FamilySampledRenderContext dispatchThreadsPerTile:];
-[AGXG19FamilySampledRenderContext drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[AGXG19FamilySampledRenderContext dispatchThreadsPerTile:inRegion:];
-[AGXG19FamilySampledRenderContext dispatchThreadsPerTile:inRegion:withRenderTargetArrayIndex:];
-[AGXG19FamilySampledRenderContext endEncodingAndRetrieveProgramAddressTable];
-[AGXG19FamilySampledRenderContext destroyImpl];
-[AGXG19FamilySampledRenderContext initWithCommandBuffer:descriptor:subEncoderIndex:framebuffer:programInfoBuffer:capacity:];
```
