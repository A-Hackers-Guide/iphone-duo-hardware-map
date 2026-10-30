# `IOGPUMetalIndirectCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalResource`
- 7 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"IOGPUMetalBuffer" _privateICBuffer;
Q _maxCommandCount;
Q _commandBufferType;
@"<MTLIndirectComputeCommandEncoder>" _privateIndirectComputeEncoder;
@"<MTLIndirectRenderCommandEncoder>" _privateIndirectRenderEncoder;
@"MTLIndirectCommandBufferDescriptor" _descriptor;
{MTLIndirectCommandBufferHeader="headerSize"Q"commandTypes"I"inheritPipelineState"B"inheritBuffers"B"maxVertexBufferBindCount"C"maxFragmentBufferBindCount"C"maxKernelBufferBindCount"C"maxObjectBufferBindCount"C"maxMeshBufferBindCount"C"supportRayTracing"B"supportDynamicAttributeStride"B"maxKernelThreadgroupMemoryBindCount"C"maxObjectThreadgroupMemoryBindCount"C"maxScissorRectCount"C"maxViewportCount"C"inheritDepthStencilState"B"inheritDepthBias"B"inheritStencilReferenceValues"B"inheritDepthClipMode"B"inheritCullMode"B"inheritFrontFacingWinding"B"inheritTriangleFillMode"B"inheritDepthTestBounds"B"inheritScissorRects"B"inheritViewports"B"inheritBlendColor"B"allowOverrideRenderStates"q"size"Q} _internalHeader;
```

## Properties

```
@property (T@"IOGPUMetalBuffer",R) privateICBuffer;
@property (TQ,R) commandBufferType;
@property (T@"MTLIndirectCommandBufferDescriptor",R) descriptor;
@property (TQ,R) storageMode;
@property (TQ,R) size;
@property (TQ,R,N) gpuHandle;
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Instance methods

```
-[IOGPUMetalIndirectCommandBuffer isComplete];
-[IOGPUMetalIndirectCommandBuffer storageMode];
-[IOGPUMetalIndirectCommandBuffer descriptor];
-[IOGPUMetalIndirectCommandBuffer dealloc];
-[IOGPUMetalIndirectCommandBuffer uniqueIdentifier];
-[IOGPUMetalIndirectCommandBuffer waitUntilComplete];
-[IOGPUMetalIndirectCommandBuffer size];
-[IOGPUMetalIndirectCommandBuffer gpuHandle];
-[IOGPUMetalIndirectCommandBuffer setPurgeableState:];
-[IOGPUMetalIndirectCommandBuffer isAliasable];
-[IOGPUMetalIndirectCommandBuffer gpuResourceID];
-[IOGPUMetalIndirectCommandBuffer makeAliasable];
-[IOGPUMetalIndirectCommandBuffer privateICBuffer];
-[IOGPUMetalIndirectCommandBuffer resetWithRange:];
-[IOGPUMetalIndirectCommandBuffer commandBufferType];
-[IOGPUMetalIndirectCommandBuffer doesAliasAllResources:count:];
-[IOGPUMetalIndirectCommandBuffer doesAliasAnyResources:count:];
-[IOGPUMetalIndirectCommandBuffer doesAliasResource:];
-[IOGPUMetalIndirectCommandBuffer getHeader:headerSize:];
-[IOGPUMetalIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[IOGPUMetalIndirectCommandBuffer indirectRenderCommandAtIndex:];
-[IOGPUMetalIndirectCommandBuffer initWithBuffer:descriptor:maxCommandCount:];
```
