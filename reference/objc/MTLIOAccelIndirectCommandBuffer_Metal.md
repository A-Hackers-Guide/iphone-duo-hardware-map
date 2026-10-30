# `MTLIOAccelIndirectCommandBuffer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelResource`
- 7 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelBuffer" _privateICBuffer;
Q _maxCommandCount;
Q _commandBufferType;
@"<MTLIndirectComputeCommandEncoder>" _privateIndirectComputeEncoder;
@"<MTLIndirectRenderCommandEncoder>" _privateIndirectRenderEncoder;
@"MTLIndirectCommandBufferDescriptor" _descriptor;
{MTLIndirectCommandBufferHeader="headerSize"Q"commandTypes"I"inheritPipelineState"B"inheritBuffers"B"maxVertexBufferBindCount"C"maxFragmentBufferBindCount"C"maxKernelBufferBindCount"C"maxObjectBufferBindCount"C"maxMeshBufferBindCount"C"supportRayTracing"B"supportDynamicAttributeStride"B"maxKernelThreadgroupMemoryBindCount"C"maxObjectThreadgroupMemoryBindCount"C"maxScissorRectCount"C"maxViewportCount"C"inheritDepthStencilState"B"inheritDepthBias"B"inheritStencilReferenceValues"B"inheritDepthClipMode"B"inheritCullMode"B"inheritFrontFacingWinding"B"inheritTriangleFillMode"B"inheritDepthTestBounds"B"inheritScissorRects"B"inheritViewports"B"inheritBlendColor"B"allowOverrideRenderStates"q"size"Q} _internalHeader;
```

## Properties

```
@property (T@"MTLIOAccelBuffer",R) privateICBuffer;
@property (TQ,R) commandBufferType;
@property (T@"MTLIndirectCommandBufferDescriptor",R) descriptor;
@property (TQ,R) storageMode;
@property (TQ,R) size;
@property (T{MTLResourceID=Q},R) gpuResourceID;
```

## Instance methods

```
-[MTLIOAccelIndirectCommandBuffer isComplete];
-[MTLIOAccelIndirectCommandBuffer storageMode];
-[MTLIOAccelIndirectCommandBuffer descriptor];
-[MTLIOAccelIndirectCommandBuffer dealloc];
-[MTLIOAccelIndirectCommandBuffer uniqueIdentifier];
-[MTLIOAccelIndirectCommandBuffer waitUntilComplete];
-[MTLIOAccelIndirectCommandBuffer size];
-[MTLIOAccelIndirectCommandBuffer gpuHandle];
-[MTLIOAccelIndirectCommandBuffer setPurgeableState:];
-[MTLIOAccelIndirectCommandBuffer isAliasable];
-[MTLIOAccelIndirectCommandBuffer gpuResourceID];
-[MTLIOAccelIndirectCommandBuffer makeAliasable];
-[MTLIOAccelIndirectCommandBuffer privateICBuffer];
-[MTLIOAccelIndirectCommandBuffer resetWithRange:];
-[MTLIOAccelIndirectCommandBuffer commandBufferType];
-[MTLIOAccelIndirectCommandBuffer doesAliasAllResources:count:];
-[MTLIOAccelIndirectCommandBuffer doesAliasAnyResources:count:];
-[MTLIOAccelIndirectCommandBuffer doesAliasResource:];
-[MTLIOAccelIndirectCommandBuffer getHeader:headerSize:];
-[MTLIOAccelIndirectCommandBuffer indirectComputeCommandAtIndex:];
-[MTLIOAccelIndirectCommandBuffer indirectRenderCommandAtIndex:];
-[MTLIOAccelIndirectCommandBuffer initWithBuffer:descriptor:maxCommandCount:];
```
