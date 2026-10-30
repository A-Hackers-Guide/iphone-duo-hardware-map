# `MTLTelemetryRenderCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderCommandEncoder`
- 6 instance variables, 0 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"MTLTelemetryDevice" _telemetryDevice;
@"MTLTelemetryCommandBuffer" _telemetryCommandBuffer;
I _reDraws;
@"NSMutableSet" _anisoFragmentSamplers;
@"NSMutableDictionary" _clippedMip2DFragmentTextures;
@"MTLTelemetryRenderPipelineState" _telemetryPipeline;
```

## Instance methods

```
-[MTLTelemetryRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:];
-[MTLTelemetryRenderCommandEncoder setFragmentSamplerState:atIndex:];
-[MTLTelemetryRenderCommandEncoder drawPrimitives:indirectBuffer:indirectBufferOffset:];
-[MTLTelemetryRenderCommandEncoder endEncoding];
-[MTLTelemetryRenderCommandEncoder setRenderPipelineState:];
-[MTLTelemetryRenderCommandEncoder setFragmentTexture:atIndex:];
-[MTLTelemetryRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:];
-[MTLTelemetryRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:];
-[MTLTelemetryRenderCommandEncoder setViewports:count:];
-[MTLTelemetryRenderCommandEncoder setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MTLTelemetryRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:];
-[MTLTelemetryRenderCommandEncoder setFragmentSamplerStates:withRange:];
-[MTLTelemetryRenderCommandEncoder setViewport:];
-[MTLTelemetryRenderCommandEncoder setScissorRects:count:];
-[MTLTelemetryRenderCommandEncoder setDepthStencilState:];
-[MTLTelemetryRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:];
-[MTLTelemetryRenderCommandEncoder setFragmentTextures:withRange:];
-[MTLTelemetryRenderCommandEncoder setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MTLTelemetryRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:];
-[MTLTelemetryRenderCommandEncoder setDepthClipMode:];
-[MTLTelemetryRenderCommandEncoder memoryBarrierWithResources:count:afterStages:beforeStages:];
-[MTLTelemetryRenderCommandEncoder setScissorRect:];
-[MTLTelemetryRenderCommandEncoder memoryBarrierWithScope:afterStages:beforeStages:];
-[MTLTelemetryRenderCommandEncoder accumDrawWithType:indexType:primitiveType:vertexCount:instanceCount:];
-[MTLTelemetryRenderCommandEncoder accumScissorRectTelemetry:count:];
-[MTLTelemetryRenderCommandEncoder accumViewportTelemetry:count:];
-[MTLTelemetryRenderCommandEncoder initTelemetryWithDescriptor:commandBuffer:];
-[MTLTelemetryRenderCommandEncoder initWithRenderCommandEncoder:parent:commandBuffer:descriptor:];
-[MTLTelemetryRenderCommandEncoder initWithRenderCommandEncoder:parent:descriptor:];
```
