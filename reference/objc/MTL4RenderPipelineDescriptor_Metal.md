# `MTL4RenderPipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4PipelineDescriptor`
- 17 instance variables, 17 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _rasterizationEnabled;
B _supportVertexBinaryLinking;
B _supportFragmentBinaryLinking;
@"MTL4StaticLinkingDescriptor" _fragmentStaticLinkingDescriptor;
@"MTL4StaticLinkingDescriptor" _vertexStaticLinkingDescriptor;
@"MTLVertexDescriptor" _vertexDescriptor;
q _supportIndirectCommandBuffers;
@"MTL4FunctionDescriptor" _vertexFunctionDescriptor;
@"MTL4FunctionDescriptor" _fragmentFunctionDescriptor;
Q _rasterSampleCount;
q _alphaToCoverageState;
q _alphaToOneState;
Q _maxVertexAmplificationCount;
@"MTL4RenderPipelineColorAttachmentDescriptorArray" _colorAttachments;
Q _inputPrimitiveTopology;
q _colorAttachmentMappingState;
Q _colorSampleCount;
```

## Properties

```
@property (TQ,N,V_colorSampleCount) colorSampleCount;
@property (T@"MTL4FunctionDescriptor",C,N,V_vertexFunctionDescriptor) vertexFunctionDescriptor;
@property (T@"MTL4FunctionDescriptor",C,N,V_fragmentFunctionDescriptor) fragmentFunctionDescriptor;
@property (T@"MTLVertexDescriptor",C,N,V_vertexDescriptor) vertexDescriptor;
@property (TQ,N,V_rasterSampleCount) rasterSampleCount;
@property (Tq,N,V_alphaToCoverageState) alphaToCoverageState;
@property (Tq,N,V_alphaToOneState) alphaToOneState;
@property (TB,N,GisRasterizationEnabled,V_rasterizationEnabled) rasterizationEnabled;
@property (TQ,N,V_maxVertexAmplificationCount) maxVertexAmplificationCount;
@property (T@"MTL4RenderPipelineColorAttachmentDescriptorArray",R,V_colorAttachments) colorAttachments;
@property (TQ,N,V_inputPrimitiveTopology) inputPrimitiveTopology;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_vertexStaticLinkingDescriptor) vertexStaticLinkingDescriptor;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_fragmentStaticLinkingDescriptor) fragmentStaticLinkingDescriptor;
@property (TB,N,V_supportVertexBinaryLinking) supportVertexBinaryLinking;
@property (TB,N,V_supportFragmentBinaryLinking) supportFragmentBinaryLinking;
@property (Tq,N,V_colorAttachmentMappingState) colorAttachmentMappingState;
@property (Tq,N,V_supportIndirectCommandBuffers) supportIndirectCommandBuffers;
```

## Instance methods

```
-[MTL4RenderPipelineDescriptor supportIndirectCommandBuffers];
-[MTL4RenderPipelineDescriptor maxVertexAmplificationCount];
-[MTL4RenderPipelineDescriptor setSupportIndirectCommandBuffers:];
-[MTL4RenderPipelineDescriptor colorAttachments];
-[MTL4RenderPipelineDescriptor setColorSampleCount:];
-[MTL4RenderPipelineDescriptor setRasterSampleCount:];
-[MTL4RenderPipelineDescriptor vertexDescriptor];
-[MTL4RenderPipelineDescriptor init];
-[MTL4RenderPipelineDescriptor setInputPrimitiveTopology:];
-[MTL4RenderPipelineDescriptor rasterSampleCount];
-[MTL4RenderPipelineDescriptor dealloc];
-[MTL4RenderPipelineDescriptor setRasterizationEnabled:];
-[MTL4RenderPipelineDescriptor reset];
-[MTL4RenderPipelineDescriptor isRasterizationEnabled];
-[MTL4RenderPipelineDescriptor vertexStaticLinkingDescriptor];
-[MTL4RenderPipelineDescriptor setVertexStaticLinkingDescriptor:];
-[MTL4RenderPipelineDescriptor colorSampleCount];
-[MTL4RenderPipelineDescriptor inputPrimitiveTopology];
-[MTL4RenderPipelineDescriptor setColorAttachmentMappingState:];
-[MTL4RenderPipelineDescriptor fragmentStaticLinkingDescriptor];
-[MTL4RenderPipelineDescriptor colorAttachmentMappingState];
-[MTL4RenderPipelineDescriptor fragmentFunctionDescriptor];
-[MTL4RenderPipelineDescriptor setFragmentFunctionDescriptor:];
-[MTL4RenderPipelineDescriptor setMaxVertexAmplificationCount:];
-[MTL4RenderPipelineDescriptor hash];
-[MTL4RenderPipelineDescriptor setVertexFunctionDescriptor:];
-[MTL4RenderPipelineDescriptor vertexFunctionDescriptor];
-[MTL4RenderPipelineDescriptor setFragmentStaticLinkingDescriptor:];
-[MTL4RenderPipelineDescriptor copyWithZone:];
-[MTL4RenderPipelineDescriptor isEqual:];
-[MTL4RenderPipelineDescriptor setVertexDescriptor:];
-[MTL4RenderPipelineDescriptor alphaToOneState];
-[MTL4RenderPipelineDescriptor _fragmentStaticLinkingDescriptorNoAlloc];
-[MTL4RenderPipelineDescriptor _vertexStaticLinkingDescriptorNoAlloc];
-[MTL4RenderPipelineDescriptor alphaToCoverageState];
-[MTL4RenderPipelineDescriptor setAlphaToCoverageState:];
-[MTL4RenderPipelineDescriptor setAlphaToOneState:];
-[MTL4RenderPipelineDescriptor setSupportFragmentBinaryLinking:];
-[MTL4RenderPipelineDescriptor setSupportVertexBinaryLinking:];
-[MTL4RenderPipelineDescriptor supportFragmentBinaryLinking];
-[MTL4RenderPipelineDescriptor supportVertexBinaryLinking];
```
