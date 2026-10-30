# `MTLIndirectRenderCommandSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLIndirectRenderCommand`
- 0 instance variables, 0 properties, 46 instance methods, 0 class methods

## Instance methods

```
-[MTLIndirectRenderCommandSPI setBlendColorRed:green:blue:alpha:];
-[MTLIndirectRenderCommandSPI setObjectBuffer:offset:atIndex:];
-[MTLIndirectRenderCommandSPI setStencilReferenceValue:];
-[MTLIndirectRenderCommandSPI setMeshBuffer:offset:atIndex:];
-[MTLIndirectRenderCommandSPI setViewports:count:];
-[MTLIndirectRenderCommandSPI drawMeshThreadgroups:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLIndirectRenderCommandSPI setViewport:];
-[MTLIndirectRenderCommandSPI setScissorRects:count:];
-[MTLIndirectRenderCommandSPI setScissorRect:];
-[MTLIndirectRenderCommandSPI setDepthTestMinBound:maxBound:];
-[MTLIndirectRenderCommandSPI setStencilFrontReferenceValue:backReferenceValue:];
-[MTLIndirectRenderCommandSPI drawMeshThreads:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:];
-[MTLIndirectRenderCommandSPI getScissorRects];
-[MTLIndirectRenderCommandSPI clearBarrier];
-[MTLIndirectRenderCommandSPI drawArguments];
-[MTLIndirectRenderCommandSPI drawIndexedArguments];
-[MTLIndirectRenderCommandSPI drawIndexedPatchesArguments];
-[MTLIndirectRenderCommandSPI drawMeshThreadgroupsArguments];
-[MTLIndirectRenderCommandSPI drawMeshThreadsArguments];
-[MTLIndirectRenderCommandSPI drawPatchesArguments];
-[MTLIndirectRenderCommandSPI getBlendColor];
-[MTLIndirectRenderCommandSPI getCommandType];
-[MTLIndirectRenderCommandSPI getCullMode];
-[MTLIndirectRenderCommandSPI getDepthBiasInfo];
-[MTLIndirectRenderCommandSPI getDepthClipMode];
-[MTLIndirectRenderCommandSPI getDepthStencilState];
-[MTLIndirectRenderCommandSPI getDepthStencilStateUniqueIdentifier];
-[MTLIndirectRenderCommandSPI getDepthTestBounds];
-[MTLIndirectRenderCommandSPI getFragmentBufferAddressAtIndex:];
-[MTLIndirectRenderCommandSPI getFragmentBufferAtIndex:];
-[MTLIndirectRenderCommandSPI getFrontFacingWinding];
-[MTLIndirectRenderCommandSPI getMeshBufferAddressAtIndex:];
-[MTLIndirectRenderCommandSPI getObjectBufferAddressAtIndex:];
-[MTLIndirectRenderCommandSPI getObjectThreadgroupMemoryLengthAtIndex:];
-[MTLIndirectRenderCommandSPI getOptimizedStatus];
-[MTLIndirectRenderCommandSPI getPipelineStateUniqueIdentifier];
-[MTLIndirectRenderCommandSPI getStencilReferenceValues];
-[MTLIndirectRenderCommandSPI getTessellationFactorArguments];
-[MTLIndirectRenderCommandSPI getTriangleFillMode];
-[MTLIndirectRenderCommandSPI getVertexAttributeStrideAtIndex:];
-[MTLIndirectRenderCommandSPI getVertexBufferAddressAtIndex:];
-[MTLIndirectRenderCommandSPI getVertexBufferAtIndex:];
-[MTLIndirectRenderCommandSPI getViewports];
-[MTLIndirectRenderCommandSPI hasBarrier];
-[MTLIndirectRenderCommandSPI setBarrier];
-[MTLIndirectRenderCommandSPI setToolsDispatchBufferSPI:atIndex:stages:];
```
