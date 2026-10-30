# `MTLLegacySVRenderPipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderPipelineState`
- 18 instance variables, 21 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"MTLRenderPipelineReflection" _internalReflection;
@"MTLRenderPipelineReflection" _userReflection;
@"NSMutableArray" _binaryFunctionData;
@"MTLLegacySVImageData" _vertexFunctionData;
@"MTLLegacySVImageData" _fragmentFunctionData;
@"MTLLegacySVImageData" _tileFunctionData;
@"MTLLegacySVImageData" _objectFunctionData;
@"MTLLegacySVImageData" _meshFunctionData;
@"NSMutableArray" _retainedFunctions;
@"MTLLegacySVBuffer" _indirectStateBuffer;
B _supportsIndirectCommandBuffers;
q _shaderValidation;
q _shaderValidationState;
i _vertexMaxCallStackDepth;
i _fragmentMaxCallStackDepth;
i _meshMaxCallStackDepth;
i _objectMaxCallStackDepth;
i _tileMaxCallStackDepth;
```

## Properties

```
@property (T@"NSArray",R,N,V_binaryFunctionData) binaryFunctionData;
@property (T@"MTLLegacySVImageData",R,N) vertexFunctionData;
@property (T@"MTLLegacySVImageData",R,N) fragmentFunctionData;
@property (T@"MTLLegacySVImageData",R,N) tileFunctionData;
@property (T@"MTLLegacySVImageData",R,N) objectFunctionData;
@property (T@"MTLLegacySVImageData",R,N) meshFunctionData;
@property (T@"MTLRenderPipelineReflection",R,N) internalReflection;
@property (T@"MTLRenderPipelineReflection",R,N) userReflection;
@property (T@"MTLLegacySVBuffer",R,N) vertexConstantsBuffer;
@property (T@"MTLLegacySVBuffer",R,N) fragmentConstantsBuffer;
@property (T@"MTLLegacySVBuffer",R,N) tileConstantsBuffer;
@property (T@"MTLLegacySVBuffer",R,N) objectConstantsBuffer;
@property (T@"MTLLegacySVBuffer",R,N) meshConstantsBuffer;
@property (T@"MTLLegacySVBuffer",R,N) indirectStateBuffer;
@property (Ti,R,N,V_vertexMaxCallStackDepth) vertexMaxCallStackDepth;
@property (Ti,R,N,V_fragmentMaxCallStackDepth) fragmentMaxCallStackDepth;
@property (Ti,R,N,V_meshMaxCallStackDepth) meshMaxCallStackDepth;
@property (Ti,R,N,V_objectMaxCallStackDepth) objectMaxCallStackDepth;
@property (Ti,R,N,V_tileMaxCallStackDepth) tileMaxCallStackDepth;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
```

## Instance methods

```
-[MTLLegacySVRenderPipelineState newVisibleFunctionTableFromTileStageWithDescriptor:];
-[MTLLegacySVRenderPipelineState newFragmentIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:];
-[MTLLegacySVRenderPipelineState dealloc];
-[MTLLegacySVRenderPipelineState shaderValidation];
-[MTLLegacySVRenderPipelineState newMeshIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVRenderPipelineState newTileIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLLegacySVRenderPipelineState newVisibleFunctionTableFromMeshStageWithDescriptor:];
-[MTLLegacySVRenderPipelineState shaderValidationState];
-[MTLLegacySVRenderPipelineState newVisibleFunctionTableFromFragmentStageWithDescriptor:];
-[MTLLegacySVRenderPipelineState newVertexIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVRenderPipelineState functionHandleWithFunction:stage:];
-[MTLLegacySVRenderPipelineState newVisibleFunctionTableFromObjectStageWithDescriptor:];
-[MTLLegacySVRenderPipelineState newObjectIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:];
-[MTLLegacySVRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:];
-[MTLLegacySVRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLLegacySVRenderPipelineState newVisibleFunctionTableFromVertexStageWithDescriptor:];
-[MTLLegacySVRenderPipelineState _initConstantsBuffer:device:];
-[MTLLegacySVRenderPipelineState binaryFunctionData];
-[MTLLegacySVRenderPipelineState fragmentConstantsBuffer];
-[MTLLegacySVRenderPipelineState fragmentFunctionData];
-[MTLLegacySVRenderPipelineState fragmentMaxCallStackDepth];
-[MTLLegacySVRenderPipelineState indirectStateBuffer];
-[MTLLegacySVRenderPipelineState initWithRenderPipelineState:descriptor:unwrappedDescriptor:reflection:device:pipelineOptions:];
-[MTLLegacySVRenderPipelineState initWithRenderPipelineState:meshDescriptor:unwrappedDescriptor:reflection:device:pipelineOptions:];
-[MTLLegacySVRenderPipelineState initWithRenderPipelineState:tileDescriptor:reflection:device:pipelineOptions:];
-[MTLLegacySVRenderPipelineState initWithRenderPipelineState:vertexBinaryFunctions:fragmentBinaryFunctions:tileBinaryFunctions:objectBinaryFunctions:meshBinaryFunctions:withState:device:pipelineOptions:];
-[MTLLegacySVRenderPipelineState internalReflection];
-[MTLLegacySVRenderPipelineState meshConstantsBuffer];
-[MTLLegacySVRenderPipelineState meshFunctionData];
-[MTLLegacySVRenderPipelineState meshMaxCallStackDepth];
-[MTLLegacySVRenderPipelineState objectConstantsBuffer];
-[MTLLegacySVRenderPipelineState objectFunctionData];
-[MTLLegacySVRenderPipelineState objectMaxCallStackDepth];
-[MTLLegacySVRenderPipelineState releaseReflection];
-[MTLLegacySVRenderPipelineState tileConstantsBuffer];
-[MTLLegacySVRenderPipelineState tileFunctionData];
-[MTLLegacySVRenderPipelineState tileMaxCallStackDepth];
-[MTLLegacySVRenderPipelineState unwrapBinaryFunctions:];
-[MTLLegacySVRenderPipelineState userReflection];
-[MTLLegacySVRenderPipelineState vertexConstantsBuffer];
-[MTLLegacySVRenderPipelineState vertexFunctionData];
-[MTLLegacySVRenderPipelineState vertexMaxCallStackDepth];
```
