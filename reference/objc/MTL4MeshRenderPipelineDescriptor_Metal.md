# `MTL4MeshRenderPipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4PipelineDescriptor`
- 26 instance variables, 26 properties, 60 instance methods, 0 class methods

## Instance variables

```
B _objectThreadgroupSizeIsMultipleOfThreadExecutionWidth;
B _meshThreadgroupSizeIsMultipleOfThreadExecutionWidth;
B _rasterizationEnabled;
B _supportObjectBinaryLinking;
B _supportMeshBinaryLinking;
B _supportFragmentBinaryLinking;
@"MTL4StaticLinkingDescriptor" _fragmentStaticLinkingDescriptor;
@"MTL4StaticLinkingDescriptor" _meshStaticLinkingDescriptor;
@"MTL4StaticLinkingDescriptor" _objectStaticLinkingDescriptor;
q _supportIndirectCommandBuffers;
@"MTL4FunctionDescriptor" _objectFunctionDescriptor;
@"MTL4FunctionDescriptor" _meshFunctionDescriptor;
@"MTL4FunctionDescriptor" _fragmentFunctionDescriptor;
Q _maxTotalThreadsPerObjectThreadgroup;
Q _maxTotalThreadsPerMeshThreadgroup;
Q _payloadMemoryLength;
Q _maxTotalThreadgroupsPerMeshGrid;
Q _rasterSampleCount;
q _alphaToCoverageState;
q _alphaToOneState;
Q _maxVertexAmplificationCount;
@"MTL4RenderPipelineColorAttachmentDescriptorArray" _colorAttachments;
q _colorAttachmentMappingState;
Q _colorSampleCount;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerObjectThreadgroup;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerMeshThreadgroup;
```

## Properties

```
@property (TQ,N,V_colorSampleCount) colorSampleCount;
@property (T@"MTL4FunctionDescriptor",C,N,V_objectFunctionDescriptor) objectFunctionDescriptor;
@property (T@"MTL4FunctionDescriptor",C,N,V_meshFunctionDescriptor) meshFunctionDescriptor;
@property (T@"MTL4FunctionDescriptor",C,N,V_fragmentFunctionDescriptor) fragmentFunctionDescriptor;
@property (TQ,N,V_maxTotalThreadsPerObjectThreadgroup) maxTotalThreadsPerObjectThreadgroup;
@property (TQ,N,V_maxTotalThreadsPerMeshThreadgroup) maxTotalThreadsPerMeshThreadgroup;
@property (T{?=QQQ},N,V_requiredThreadsPerObjectThreadgroup) requiredThreadsPerObjectThreadgroup;
@property (T{?=QQQ},N,V_requiredThreadsPerMeshThreadgroup) requiredThreadsPerMeshThreadgroup;
@property (TB,N,V_objectThreadgroupSizeIsMultipleOfThreadExecutionWidth) objectThreadgroupSizeIsMultipleOfThreadExecutionWidth;
@property (TB,N,V_meshThreadgroupSizeIsMultipleOfThreadExecutionWidth) meshThreadgroupSizeIsMultipleOfThreadExecutionWidth;
@property (TQ,N,V_payloadMemoryLength) payloadMemoryLength;
@property (TQ,N,V_maxTotalThreadgroupsPerMeshGrid) maxTotalThreadgroupsPerMeshGrid;
@property (TQ,N,V_rasterSampleCount) rasterSampleCount;
@property (Tq,N,V_alphaToCoverageState) alphaToCoverageState;
@property (Tq,N,V_alphaToOneState) alphaToOneState;
@property (TB,N,GisRasterizationEnabled,V_rasterizationEnabled) rasterizationEnabled;
@property (TQ,N,V_maxVertexAmplificationCount) maxVertexAmplificationCount;
@property (T@"MTL4RenderPipelineColorAttachmentDescriptorArray",R,V_colorAttachments) colorAttachments;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_objectStaticLinkingDescriptor) objectStaticLinkingDescriptor;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_meshStaticLinkingDescriptor) meshStaticLinkingDescriptor;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_fragmentStaticLinkingDescriptor) fragmentStaticLinkingDescriptor;
@property (TB,N,V_supportObjectBinaryLinking) supportObjectBinaryLinking;
@property (TB,N,V_supportMeshBinaryLinking) supportMeshBinaryLinking;
@property (TB,N,V_supportFragmentBinaryLinking) supportFragmentBinaryLinking;
@property (Tq,N,V_colorAttachmentMappingState) colorAttachmentMappingState;
@property (Tq,N,V_supportIndirectCommandBuffers) supportIndirectCommandBuffers;
```

## Instance methods

```
-[MTL4MeshRenderPipelineDescriptor supportIndirectCommandBuffers];
-[MTL4MeshRenderPipelineDescriptor maxVertexAmplificationCount];
-[MTL4MeshRenderPipelineDescriptor setSupportIndirectCommandBuffers:];
-[MTL4MeshRenderPipelineDescriptor colorAttachments];
-[MTL4MeshRenderPipelineDescriptor setColorSampleCount:];
-[MTL4MeshRenderPipelineDescriptor setMeshStaticLinkingDescriptor:];
-[MTL4MeshRenderPipelineDescriptor setRasterSampleCount:];
-[MTL4MeshRenderPipelineDescriptor maxTotalThreadsPerMeshThreadgroup];
-[MTL4MeshRenderPipelineDescriptor objectStaticLinkingDescriptor];
-[MTL4MeshRenderPipelineDescriptor init];
-[MTL4MeshRenderPipelineDescriptor rasterSampleCount];
-[MTL4MeshRenderPipelineDescriptor meshStaticLinkingDescriptor];
-[MTL4MeshRenderPipelineDescriptor objectThreadgroupSizeIsMultipleOfThreadExecutionWidth];
-[MTL4MeshRenderPipelineDescriptor dealloc];
-[MTL4MeshRenderPipelineDescriptor setMeshFunctionDescriptor:];
-[MTL4MeshRenderPipelineDescriptor setRasterizationEnabled:];
-[MTL4MeshRenderPipelineDescriptor reset];
-[MTL4MeshRenderPipelineDescriptor isRasterizationEnabled];
-[MTL4MeshRenderPipelineDescriptor setMaxTotalThreadsPerMeshThreadgroup:];
-[MTL4MeshRenderPipelineDescriptor maxTotalThreadgroupsPerMeshGrid];
-[MTL4MeshRenderPipelineDescriptor meshFunctionDescriptor];
-[MTL4MeshRenderPipelineDescriptor colorSampleCount];
-[MTL4MeshRenderPipelineDescriptor requiredThreadsPerObjectThreadgroup];
-[MTL4MeshRenderPipelineDescriptor setMaxTotalThreadsPerObjectThreadgroup:];
-[MTL4MeshRenderPipelineDescriptor setObjectThreadgroupSizeIsMultipleOfThreadExecutionWidth:];
-[MTL4MeshRenderPipelineDescriptor maxTotalThreadsPerObjectThreadgroup];
-[MTL4MeshRenderPipelineDescriptor setColorAttachmentMappingState:];
-[MTL4MeshRenderPipelineDescriptor fragmentStaticLinkingDescriptor];
-[MTL4MeshRenderPipelineDescriptor meshThreadgroupSizeIsMultipleOfThreadExecutionWidth];
-[MTL4MeshRenderPipelineDescriptor setRequiredThreadsPerMeshThreadgroup:];
-[MTL4MeshRenderPipelineDescriptor colorAttachmentMappingState];
-[MTL4MeshRenderPipelineDescriptor fragmentFunctionDescriptor];
-[MTL4MeshRenderPipelineDescriptor setObjectFunctionDescriptor:];
-[MTL4MeshRenderPipelineDescriptor setFragmentFunctionDescriptor:];
-[MTL4MeshRenderPipelineDescriptor setMaxVertexAmplificationCount:];
-[MTL4MeshRenderPipelineDescriptor requiredThreadsPerMeshThreadgroup];
-[MTL4MeshRenderPipelineDescriptor hash];
-[MTL4MeshRenderPipelineDescriptor setObjectStaticLinkingDescriptor:];
-[MTL4MeshRenderPipelineDescriptor setFragmentStaticLinkingDescriptor:];
-[MTL4MeshRenderPipelineDescriptor copyWithZone:];
-[MTL4MeshRenderPipelineDescriptor isEqual:];
-[MTL4MeshRenderPipelineDescriptor setMeshThreadgroupSizeIsMultipleOfThreadExecutionWidth:];
-[MTL4MeshRenderPipelineDescriptor objectFunctionDescriptor];
-[MTL4MeshRenderPipelineDescriptor setRequiredThreadsPerObjectThreadgroup:];
-[MTL4MeshRenderPipelineDescriptor alphaToOneState];
-[MTL4MeshRenderPipelineDescriptor _fragmentStaticLinkingDescriptorNoAlloc];
-[MTL4MeshRenderPipelineDescriptor _meshStaticLinkingDescriptorNoAlloc];
-[MTL4MeshRenderPipelineDescriptor _objectStaticLinkingDescriptorNoAlloc];
-[MTL4MeshRenderPipelineDescriptor alphaToCoverageState];
-[MTL4MeshRenderPipelineDescriptor payloadMemoryLength];
-[MTL4MeshRenderPipelineDescriptor setAlphaToCoverageState:];
-[MTL4MeshRenderPipelineDescriptor setAlphaToOneState:];
-[MTL4MeshRenderPipelineDescriptor setMaxTotalThreadgroupsPerMeshGrid:];
-[MTL4MeshRenderPipelineDescriptor setPayloadMemoryLength:];
-[MTL4MeshRenderPipelineDescriptor setSupportFragmentBinaryLinking:];
-[MTL4MeshRenderPipelineDescriptor setSupportMeshBinaryLinking:];
-[MTL4MeshRenderPipelineDescriptor setSupportObjectBinaryLinking:];
-[MTL4MeshRenderPipelineDescriptor supportFragmentBinaryLinking];
-[MTL4MeshRenderPipelineDescriptor supportMeshBinaryLinking];
-[MTL4MeshRenderPipelineDescriptor supportObjectBinaryLinking];
```
