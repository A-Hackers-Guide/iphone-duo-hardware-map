# `MTLRenderPipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 34 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _supportAddingVertexBinaryFunctions;
B _supportAddingFragmentBinaryFunctions;
@"NSArray" _vertexPreloadedLibraries;
@"NSArray" _fragmentPreloadedLibraries;
Q _maxVertexCallStackDepth;
Q _maxFragmentCallStackDepth;
```

## Properties

```
@property (T@"NSString",C,D,N) label;
@property (T@"<MTLFunction>",&,D,N) vertexFunction;
@property (T@"<MTLFunction>",&,D,N) fragmentFunction;
@property (T@"MTLVertexDescriptor",C,D,N) vertexDescriptor;
@property (TQ,D,N) sampleCount;
@property (TQ,D,N) rasterSampleCount;
@property (TB,D,N,GisAlphaToCoverageEnabled) alphaToCoverageEnabled;
@property (TB,D,N,GisAlphaToOneEnabled) alphaToOneEnabled;
@property (TB,D,N,GisRasterizationEnabled) rasterizationEnabled;
@property (TQ,D,N) maxVertexAmplificationCount;
@property (T@"MTLRenderPipelineColorAttachmentDescriptorArray",R,D) colorAttachments;
@property (TQ,D,N) depthAttachmentPixelFormat;
@property (TQ,D,N) stencilAttachmentPixelFormat;
@property (TQ,D,N) inputPrimitiveTopology;
@property (TQ,D,N) tessellationPartitionMode;
@property (TQ,D,N) maxTessellationFactor;
@property (TB,D,N,GisTessellationFactorScaleEnabled) tessellationFactorScaleEnabled;
@property (TQ,D,N) tessellationFactorFormat;
@property (TQ,D,N) tessellationControlPointIndexType;
@property (TQ,D,N) tessellationFactorStepFunction;
@property (TQ,D,N) tessellationOutputWindingOrder;
@property (T@"MTLPipelineBufferDescriptorArray",R,D) vertexBuffers;
@property (T@"MTLPipelineBufferDescriptorArray",R,D) fragmentBuffers;
@property (TB,D,N) supportIndirectCommandBuffers;
@property (T@"NSArray",C,D,N) binaryArchives;
@property (T@"NSArray",C,N,V_vertexPreloadedLibraries) vertexPreloadedLibraries;
@property (T@"NSArray",C,N,V_fragmentPreloadedLibraries) fragmentPreloadedLibraries;
@property (T@"MTLLinkedFunctions",C,D,N) vertexLinkedFunctions;
@property (T@"MTLLinkedFunctions",C,D,N) fragmentLinkedFunctions;
@property (TB,N,V_supportAddingVertexBinaryFunctions) supportAddingVertexBinaryFunctions;
@property (TB,N,V_supportAddingFragmentBinaryFunctions) supportAddingFragmentBinaryFunctions;
@property (TQ,N,V_maxVertexCallStackDepth) maxVertexCallStackDepth;
@property (TQ,N,V_maxFragmentCallStackDepth) maxFragmentCallStackDepth;
@property (Tq,D,N) shaderValidation;
```

## Class methods

```
+[MTLRenderPipelineDescriptor allocWithZone:];
+[MTLRenderPipelineDescriptor alloc];
```

## Instance methods

```
-[MTLRenderPipelineDescriptor setVertexPreloadedLibraries:];
-[MTLRenderPipelineDescriptor reset];
-[MTLRenderPipelineDescriptor setFragmentPreloadedLibraries:];
-[MTLRenderPipelineDescriptor setMaxFragmentCallStackDepth:];
-[MTLRenderPipelineDescriptor maxFragmentCallStackDepth];
-[MTLRenderPipelineDescriptor supportAddingFragmentBinaryFunctions];
-[MTLRenderPipelineDescriptor setMaxVertexCallStackDepth:];
-[MTLRenderPipelineDescriptor setSupportAddingVertexBinaryFunctions:];
-[MTLRenderPipelineDescriptor vertexPreloadedLibraries];
-[MTLRenderPipelineDescriptor maxVertexCallStackDepth];
-[MTLRenderPipelineDescriptor fragmentPreloadedLibraries];
-[MTLRenderPipelineDescriptor copyWithZone:];
-[MTLRenderPipelineDescriptor supportAddingVertexBinaryFunctions];
-[MTLRenderPipelineDescriptor setSupportAddingFragmentBinaryFunctions:];
```
