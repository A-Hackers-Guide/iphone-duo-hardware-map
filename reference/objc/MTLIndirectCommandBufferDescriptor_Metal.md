# `MTLIndirectCommandBufferDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 29 properties, 62 instance methods, 0 class methods

## Instance variables

```
{MTLIndirectCommandBufferDescriptorState="commandTypes"Q"inheritPipelineState"B"inheritBuffers"B"maxVertexBufferBindCount"Q"maxFragmentBufferBindCount"Q"maxKernelBufferBindCount"Q"maxKernelThreadgroupMemoryBindCount"Q"maxObjectBufferBindCount"Q"maxMeshBufferBindCount"Q"maxObjectThreadgroupMemoryBindCount"Q"supportRayTracing"B"supportDynamicAttributeStride"B"maxScissorRectCount"C"maxViewportCount"C"inheritDepthStencilState"B"inheritDepthBias"B"inheritStencilReferenceValues"B"inheritDepthClipMode"B"inheritCullMode"B"inheritFrontFacingWinding"B"inheritTriangleFillMode"B"inheritDepthTestBounds"B"inheritScissorRects"B"inheritViewports"B"inheritBlendColor"B"allowOverrideRenderStates"q"resourceIndex"Q"maxToolsDispatchBindings"I"supportColorAttachmentMapping"B} _state;
```

## Properties

```
@property (TQ,N) resourceIndex;
@property (TQ,N) maxScissorRectCount;
@property (TQ,N) maxViewportCount;
@property (TB,N) inheritStencilReferenceValues;
@property (TB,N) inheritDepthTestBounds;
@property (TB,N) inheritScissorRects;
@property (TB,N) inheritViewports;
@property (TB,N) inheritBlendColor;
@property (Tq,N) allowOverrideRenderStates;
@property (TQ,N) maxToolsDispatchBindings;
@property (TQ,N) commandTypes;
@property (TB,N) inheritPipelineState;
@property (TB,N) inheritBuffers;
@property (TB,N) inheritDepthStencilState;
@property (TB,N) inheritDepthBias;
@property (TB,N) inheritDepthClipMode;
@property (TB,N) inheritCullMode;
@property (TB,N) inheritFrontFacingWinding;
@property (TB,N) inheritTriangleFillMode;
@property (TQ,N) maxVertexBufferBindCount;
@property (TQ,N) maxFragmentBufferBindCount;
@property (TQ,N) maxKernelBufferBindCount;
@property (TQ,N) maxKernelThreadgroupMemoryBindCount;
@property (TQ,N) maxObjectBufferBindCount;
@property (TQ,N) maxMeshBufferBindCount;
@property (TQ,N) maxObjectThreadgroupMemoryBindCount;
@property (TB,N) supportRayTracing;
@property (TB,N) supportDynamicAttributeStride;
@property (TB,N) supportColorAttachmentMapping;
```

## Instance methods

```
-[MTLIndirectCommandBufferDescriptor setResourceIndex:];
-[MTLIndirectCommandBufferDescriptor resourceIndex];
-[MTLIndirectCommandBufferDescriptor maxViewportCount];
-[MTLIndirectCommandBufferDescriptor init];
-[MTLIndirectCommandBufferDescriptor setSupportColorAttachmentMapping:];
-[MTLIndirectCommandBufferDescriptor hash];
-[MTLIndirectCommandBufferDescriptor copyWithZone:];
-[MTLIndirectCommandBufferDescriptor isEqual:];
-[MTLIndirectCommandBufferDescriptor supportColorAttachmentMapping];
-[MTLIndirectCommandBufferDescriptor inheritCullMode];
-[MTLIndirectCommandBufferDescriptor allowOverrideRenderStates];
-[MTLIndirectCommandBufferDescriptor commandTypes];
-[MTLIndirectCommandBufferDescriptor inheritBlendColor];
-[MTLIndirectCommandBufferDescriptor inheritBuffers];
-[MTLIndirectCommandBufferDescriptor inheritDepthBias];
-[MTLIndirectCommandBufferDescriptor inheritDepthClipMode];
-[MTLIndirectCommandBufferDescriptor inheritDepthStencilState];
-[MTLIndirectCommandBufferDescriptor inheritDepthTestBounds];
-[MTLIndirectCommandBufferDescriptor inheritFrontFacingWinding];
-[MTLIndirectCommandBufferDescriptor inheritPipelineState];
-[MTLIndirectCommandBufferDescriptor inheritScissorRects];
-[MTLIndirectCommandBufferDescriptor inheritStencilReferenceValues];
-[MTLIndirectCommandBufferDescriptor inheritTriangleFillMode];
-[MTLIndirectCommandBufferDescriptor inheritViewports];
-[MTLIndirectCommandBufferDescriptor maxFragmentBufferBindCount];
-[MTLIndirectCommandBufferDescriptor maxKernelBufferBindCount];
-[MTLIndirectCommandBufferDescriptor maxKernelThreadgroupMemoryBindCount];
-[MTLIndirectCommandBufferDescriptor maxMeshBufferBindCount];
-[MTLIndirectCommandBufferDescriptor maxObjectBufferBindCount];
-[MTLIndirectCommandBufferDescriptor maxObjectThreadgroupMemoryBindCount];
-[MTLIndirectCommandBufferDescriptor maxScissorRectCount];
-[MTLIndirectCommandBufferDescriptor maxToolsDispatchBindings];
-[MTLIndirectCommandBufferDescriptor maxVertexBufferBindCount];
-[MTLIndirectCommandBufferDescriptor setAllowOverrideRenderStates:];
-[MTLIndirectCommandBufferDescriptor setCommandTypes:];
-[MTLIndirectCommandBufferDescriptor setInheritBlendColor:];
-[MTLIndirectCommandBufferDescriptor setInheritBuffers:];
-[MTLIndirectCommandBufferDescriptor setInheritCullMode:];
-[MTLIndirectCommandBufferDescriptor setInheritDepthBias:];
-[MTLIndirectCommandBufferDescriptor setInheritDepthClipMode:];
-[MTLIndirectCommandBufferDescriptor setInheritDepthStencilState:];
-[MTLIndirectCommandBufferDescriptor setInheritDepthTestBounds:];
-[MTLIndirectCommandBufferDescriptor setInheritFrontFacingWinding:];
-[MTLIndirectCommandBufferDescriptor setInheritPipelineState:];
-[MTLIndirectCommandBufferDescriptor setInheritScissorRects:];
-[MTLIndirectCommandBufferDescriptor setInheritStencilReferenceValues:];
-[MTLIndirectCommandBufferDescriptor setInheritTriangleFillMode:];
-[MTLIndirectCommandBufferDescriptor setInheritViewports:];
-[MTLIndirectCommandBufferDescriptor setMaxFragmentBufferBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxKernelBufferBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxKernelThreadgroupMemoryBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxMeshBufferBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxObjectBufferBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxObjectThreadgroupMemoryBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxScissorRectCount:];
-[MTLIndirectCommandBufferDescriptor setMaxToolsDispatchBindings:];
-[MTLIndirectCommandBufferDescriptor setMaxVertexBufferBindCount:];
-[MTLIndirectCommandBufferDescriptor setMaxViewportCount:];
-[MTLIndirectCommandBufferDescriptor setSupportDynamicAttributeStride:];
-[MTLIndirectCommandBufferDescriptor setSupportRayTracing:];
-[MTLIndirectCommandBufferDescriptor supportDynamicAttributeStride];
-[MTLIndirectCommandBufferDescriptor supportRayTracing];
```
