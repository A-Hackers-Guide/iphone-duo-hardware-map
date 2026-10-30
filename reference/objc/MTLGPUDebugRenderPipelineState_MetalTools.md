# `MTLGPUDebugRenderPipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsRenderPipelineState`
- 25 instance variables, 27 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _binaryFunctionData;
@"MTLRenderPipelineReflection" _internalReflection;
@"MTLRenderPipelineReflection" _userReflection;
@"MTLGPUDebugImageData" _vertexFunctionData;
@"MTLGPUDebugImageData" _fragmentFunctionData;
@"MTLGPUDebugImageData" _tileFunctionData;
@"MTLGPUDebugImageData" _objectFunctionData;
@"MTLGPUDebugImageData" _meshFunctionData;
@"NSMutableArray" _retainedFunctions;
@"MTLGPUDebugBuffer" _indirectStateBuffer;
B _supportsIndirectCommandBuffers;
Q _indirectStateGPUAddress;
Q _vertexGlobalConstantsHandle;
Q _fragmentGlobalConstantsHandle;
Q _tileGlobalConstantsHandle;
Q _objectGlobalConstantsHandle;
Q _meshGlobalConstantsHandle;
q _shaderValidation;
q _shaderValidationState;
i _vertexMaxCallStackDepth;
i _fragmentMaxCallStackDepth;
i _meshMaxCallStackDepth;
i _objectMaxCallStackDepth;
i _tileMaxCallStackDepth;
@"NSString" _UID;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_binaryFunctionData) binaryFunctionData;
@property (T@"MTLGPUDebugImageData",R,N) vertexFunctionData;
@property (T@"MTLGPUDebugImageData",R,N) fragmentFunctionData;
@property (T@"MTLGPUDebugImageData",R,N) tileFunctionData;
@property (T@"MTLGPUDebugImageData",R,N) objectFunctionData;
@property (T@"MTLGPUDebugImageData",R,N) meshFunctionData;
@property (T@"MTLRenderPipelineReflection",R,N) internalReflection;
@property (T@"MTLRenderPipelineReflection",R,N) userReflection;
@property (T@"MTLGPUDebugBuffer",R,N) vertexConstantsBuffer;
@property (T@"MTLGPUDebugBuffer",R,N) fragmentConstantsBuffer;
@property (T@"MTLGPUDebugBuffer",R,N) tileConstantsBuffer;
@property (T@"MTLGPUDebugBuffer",R,N) objectConstantsBuffer;
@property (T@"MTLGPUDebugBuffer",R,N) meshConstantsBuffer;
@property (T@"MTLGPUDebugBuffer",R,N) indirectStateBuffer;
@property (TQ,R,N) vertexGlobalConstantsHandle;
@property (TQ,R,N) fragmentGlobalConstantsHandle;
@property (TQ,R,N) tileGlobalConstantsHandle;
@property (TQ,R,N) objectGlobalConstantsHandle;
@property (TQ,R,N) meshGlobalConstantsHandle;
@property (Ti,R,N,V_vertexMaxCallStackDepth) vertexMaxCallStackDepth;
@property (Ti,R,N,V_fragmentMaxCallStackDepth) fragmentMaxCallStackDepth;
@property (Ti,R,N,V_meshMaxCallStackDepth) meshMaxCallStackDepth;
@property (Ti,R,N,V_objectMaxCallStackDepth) objectMaxCallStackDepth;
@property (Ti,R,N,V_tileMaxCallStackDepth) tileMaxCallStackDepth;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
@property (T@"NSString",&,N,V_UID) UID;
```

## Instance methods

```
-[MTLGPUDebugRenderPipelineState UID];
-[MTLGPUDebugRenderPipelineState newVisibleFunctionTableFromTileStageWithDescriptor:];
-[MTLGPUDebugRenderPipelineState newFragmentIntersectionFunctionTableWithDescriptor:];
-[MTLGPUDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:];
-[MTLGPUDebugRenderPipelineState dealloc];
-[MTLGPUDebugRenderPipelineState shaderValidation];
-[MTLGPUDebugRenderPipelineState newMeshIntersectionFunctionTableWithDescriptor:];
-[MTLGPUDebugRenderPipelineState newTileIntersectionFunctionTableWithDescriptor:];
-[MTLGPUDebugRenderPipelineState functionHandleWithName:stage:];
-[MTLGPUDebugRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLGPUDebugRenderPipelineState newVisibleFunctionTableFromMeshStageWithDescriptor:];
-[MTLGPUDebugRenderPipelineState shaderValidationState];
-[MTLGPUDebugRenderPipelineState newVisibleFunctionTableFromFragmentStageWithDescriptor:];
-[MTLGPUDebugRenderPipelineState functionHandleWithBinaryFunction:stage:];
-[MTLGPUDebugRenderPipelineState newVertexIntersectionFunctionTableWithDescriptor:];
-[MTLGPUDebugRenderPipelineState functionHandleWithFunction:stage:];
-[MTLGPUDebugRenderPipelineState newVisibleFunctionTableFromObjectStageWithDescriptor:];
-[MTLGPUDebugRenderPipelineState newObjectIntersectionFunctionTableWithDescriptor:];
-[MTLGPUDebugRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:];
-[MTLGPUDebugRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:];
-[MTLGPUDebugRenderPipelineState setUID:];
-[MTLGPUDebugRenderPipelineState gpuResourceID];
-[MTLGPUDebugRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:];
-[MTLGPUDebugRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLGPUDebugRenderPipelineState newVisibleFunctionTableFromVertexStageWithDescriptor:];
-[MTLGPUDebugRenderPipelineState _initConstantsBuffer:];
-[MTLGPUDebugRenderPipelineState binaryFunctionData];
-[MTLGPUDebugRenderPipelineState fragmentConstantsBuffer];
-[MTLGPUDebugRenderPipelineState fragmentFunctionData];
-[MTLGPUDebugRenderPipelineState fragmentGlobalConstantsHandle];
-[MTLGPUDebugRenderPipelineState fragmentMaxCallStackDepth];
-[MTLGPUDebugRenderPipelineState indirectStateBuffer];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:descriptor:device:needsReflectionProperty:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:descriptor:dynamicLinkingDescriptor:device:needsReflectionProperty:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:descriptor:unwrappedDescriptor:reflection:device:pipelineOptions:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:meshDescriptor:unwrappedDescriptor:reflection:device:pipelineOptions:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:originalObject:descriptor:device:needsReflectionProperty:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:tileDescriptor:reflection:device:pipelineOptions:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:vertexBinaryFunctions:fragmentBinaryFunctions:tileBinaryFunctions:objectBinaryFunctions:meshBinaryFunctions:withState:device:needsReflectionProperty:];
-[MTLGPUDebugRenderPipelineState initWithRenderPipelineState:vertexBinaryFunctions:fragmentBinaryFunctions:tileBinaryFunctions:objectBinaryFunctions:meshBinaryFunctions:withState:device:pipelineOptions:];
-[MTLGPUDebugRenderPipelineState internalReflection];
-[MTLGPUDebugRenderPipelineState meshConstantsBuffer];
-[MTLGPUDebugRenderPipelineState meshFunctionData];
-[MTLGPUDebugRenderPipelineState meshGlobalConstantsHandle];
-[MTLGPUDebugRenderPipelineState meshMaxCallStackDepth];
-[MTLGPUDebugRenderPipelineState objectConstantsBuffer];
-[MTLGPUDebugRenderPipelineState objectFunctionData];
-[MTLGPUDebugRenderPipelineState objectGlobalConstantsHandle];
-[MTLGPUDebugRenderPipelineState objectMaxCallStackDepth];
-[MTLGPUDebugRenderPipelineState releaseReflection];
-[MTLGPUDebugRenderPipelineState setGlobalConstantsHandlesWithVertex:fragment:tile:object:mesh:];
-[MTLGPUDebugRenderPipelineState tileConstantsBuffer];
-[MTLGPUDebugRenderPipelineState tileFunctionData];
-[MTLGPUDebugRenderPipelineState tileGlobalConstantsHandle];
-[MTLGPUDebugRenderPipelineState tileMaxCallStackDepth];
-[MTLGPUDebugRenderPipelineState unwrapBinaryFunctions:];
-[MTLGPUDebugRenderPipelineState userReflection];
-[MTLGPUDebugRenderPipelineState vertexConstantsBuffer];
-[MTLGPUDebugRenderPipelineState vertexFunctionData];
-[MTLGPUDebugRenderPipelineState vertexGlobalConstantsHandle];
-[MTLGPUDebugRenderPipelineState vertexMaxCallStackDepth];
```
