# `MTLDebugRenderPipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderPipelineState`
- 18 instance variables, 12 properties, 66 instance methods, 0 class methods

## Instance variables

```
Q _maxVertexCount;
Q _maxInstanceCount;
Q _maxPatchCount;
Q _rasterSampleCount;
[8Q] _colorPixelFormat;
Q _depthPixelFormat;
Q _stencilPixelFormat;
Q _vertexDescriptorLayoutCount;
[31{?="bufferIndex"Q"bufferStride"Q}] _vertexDescriptorLayouts;
B _threadgroupSizeMatchesTileSize;
Q _attachmentWriteMask;
@"MTLRenderPipelineReflection" _validationReflection;
@"MTLRenderPipelineDescriptor" _descriptor;
@"MTLTileRenderPipelineDescriptor" _tileDescriptor;
@"MTLMeshRenderPipelineDescriptor" _meshDescriptor;
@"MTL4RenderPipelineDescriptor" _mtl4Descriptor;
@"MTL4TileRenderPipelineDescriptor" _mtl4TileDescriptor;
@"MTL4MeshRenderPipelineDescriptor" _mtl4MeshDescriptor;
```

## Properties

```
@property (TB,R,N) rasterizationEnabled;
@property (T@"MTLRenderPipelineDescriptor",R,N,V_descriptor) descriptor;
@property (T@"MTLRenderPipelineReflection",R,N,V_validationReflection) validationReflection;
@property (TQ,R,N,V_attachmentWriteMask) attachmentWriteMask;
@property (T@"MTLTileRenderPipelineDescriptor",R,N,V_tileDescriptor) tileDescriptor;
@property (TB,R,GisMeshShaderPipeline) meshShaderPipeline;
@property (T@"MTLMeshRenderPipelineDescriptor",R,N,V_meshDescriptor) meshDescriptor;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
@property (T@"MTL4RenderPipelineDescriptor",R,N,V_mtl4Descriptor) mtl4Descriptor;
@property (T@"MTL4TileRenderPipelineDescriptor",R,N,V_mtl4TileDescriptor) mtl4TileDescriptor;
@property (T@"MTL4MeshRenderPipelineDescriptor",R,N,V_mtl4MeshDescriptor) mtl4MeshDescriptor;
```

## Instance methods

```
-[MTLDebugRenderPipelineState rasterizationEnabled];
-[MTLDebugRenderPipelineState meshFunctionHandleWithFunction:];
-[MTLDebugRenderPipelineState descriptor];
-[MTLDebugRenderPipelineState newVisibleFunctionTableFromTileStageWithDescriptor:];
-[MTLDebugRenderPipelineState formattedDescription:];
-[MTLDebugRenderPipelineState newFragmentIntersectionFunctionTableWithDescriptor:];
-[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:];
-[MTLDebugRenderPipelineState dealloc];
-[MTLDebugRenderPipelineState shaderValidation];
-[MTLDebugRenderPipelineState newMeshIntersectionFunctionTableWithDescriptor:];
-[MTLDebugRenderPipelineState newTileIntersectionFunctionTableWithDescriptor:];
-[MTLDebugRenderPipelineState functionHandleWithName:stage:];
-[MTLDebugRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLDebugRenderPipelineState newVisibleFunctionTableFromMeshStageWithDescriptor:];
-[MTLDebugRenderPipelineState shaderValidationState];
-[MTLDebugRenderPipelineState fragmentFunctionHandleWithFunction:];
-[MTLDebugRenderPipelineState newVisibleFunctionTableFromFragmentStageWithDescriptor:];
-[MTLDebugRenderPipelineState tileFunctionHandleWithFunction:];
-[MTLDebugRenderPipelineState functionHandleWithBinaryFunction:stage:];
-[MTLDebugRenderPipelineState newRenderPipelineDescriptorForSpecialization];
-[MTLDebugRenderPipelineState newVertexIntersectionFunctionTableWithDescriptor:];
-[MTLDebugRenderPipelineState functionHandleWithFunction:stage:];
-[MTLDebugRenderPipelineState description];
-[MTLDebugRenderPipelineState newVisibleFunctionTableFromObjectStageWithDescriptor:];
-[MTLDebugRenderPipelineState newObjectIntersectionFunctionTableWithDescriptor:];
-[MTLDebugRenderPipelineState objectFunctionHandleWithFunction:];
-[MTLDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:];
-[MTLDebugRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:];
-[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:];
-[MTLDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLDebugRenderPipelineState newVisibleFunctionTableFromVertexStageWithDescriptor:];
-[MTLDebugRenderPipelineState vertexFunctionHandleWithFunction:];
-[MTLDebugRenderPipelineState isAncestorOf:];
-[MTLDebugRenderPipelineState _findMasterStruct:includeImageBlockData:];
-[MTLDebugRenderPipelineState _updateCachedMTL4MeshPipelineState];
-[MTLDebugRenderPipelineState _updateCachedMTL4PipelineState];
-[MTLDebugRenderPipelineState _updateCachedMTL4TilePipelineState];
-[MTLDebugRenderPipelineState _updateCachedMeshPipelineState];
-[MTLDebugRenderPipelineState _updateCachedPipelineState];
-[MTLDebugRenderPipelineState _updateCachedTilePipelineState];
-[MTLDebugRenderPipelineState _validateThreadgroupSize:stage:context:];
-[MTLDebugRenderPipelineState attachmentWriteMask];
-[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:binaryFunction:stage:];
-[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:parentFunction:stage:];
-[MTLDebugRenderPipelineState functionHandleToDebugFunctionHandle:stage:];
-[MTLDebugRenderPipelineState functionHandleWithFunction:stage:selector:];
-[MTLDebugRenderPipelineState getParameter:];
-[MTLDebugRenderPipelineState hasMetal4Descriptor];
-[MTLDebugRenderPipelineState initWithPipelineState:reflection:parent:descriptor:];
-[MTLDebugRenderPipelineState initWithPipelineState:reflection:parent:meshDescriptor:];
-[MTLDebugRenderPipelineState initWithPipelineState:reflection:parent:tileDescriptor:];
-[MTLDebugRenderPipelineState initWithRenderPipelineState:parent:mtl4Descriptor:];
-[MTLDebugRenderPipelineState initWithRenderPipelineState:reflection:parent:mtl4Descriptor:];
-[MTLDebugRenderPipelineState isImageBlockLayoutInputCompatibleWithOutputOf:];
-[MTLDebugRenderPipelineState isMeshShaderPipeline];
-[MTLDebugRenderPipelineState meshDescriptor];
-[MTLDebugRenderPipelineState mtl4Descriptor];
-[MTLDebugRenderPipelineState mtl4MeshDescriptor];
-[MTLDebugRenderPipelineState mtl4TileDescriptor];
-[MTLDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:withStage:selector:];
-[MTLDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:selector:];
-[MTLDebugRenderPipelineState outputImageBlockData];
-[MTLDebugRenderPipelineState tileDescriptor];
-[MTLDebugRenderPipelineState validateBinaryFunctions:stage:];
-[MTLDebugRenderPipelineState validateHandleForSetFunction:];
-[MTLDebugRenderPipelineState validationReflection];
```
