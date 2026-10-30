# `_MTLRenderPipelineState`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAllocation`
- Protocols: `MTLRenderPipelineState`
- 22 instance variables, 46 properties, 88 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"MTLDebugInstrumentationData" _vertexDebugInstrumentationData;
@"MTLDebugInstrumentationData" _fragmentDebugInstrumentationData;
@"MTLDebugInstrumentationData" _tileDebugInstrumentationData;
@"MTLDebugInstrumentationData" _objectDebugInstrumentationData;
@"MTLDebugInstrumentationData" _meshDebugInstrumentationData;
Q _resourceIndex;
Q _gpuAddress;
q _textureWriteRoundingMode;
I _explicitVisibilityGroupID;
B _threadgroupSizeMatchesTileSize;
B _supportIndirectCommandBuffers;
Q _objectThreadExecutionWidth;
Q _meshThreadExecutionWidth;
Q _maxTotalThreadsPerObjectThreadgroup;
Q _maxTotalThreadsPerMeshThreadgroup;
Q _maxTotalThreadgroupsPerMeshGrid;
@"MTLRenderPipelineReflection" _reflection;
Q _imageBlockSampleLength;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerTileThreadgroup;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerObjectThreadgroup;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerMeshThreadgroup;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"MTLDebugInstrumentationData",&,N,V_vertexDebugInstrumentationData) vertexDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",&,N,V_fragmentDebugInstrumentationData) fragmentDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",&,N,V_tileDebugInstrumentationData) tileDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",&,N,V_objectDebugInstrumentationData) objectDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",&,N,V_meshDebugInstrumentationData) meshDebugInstrumentationData;
@property (TQ,R,V_maxTotalThreadsPerObjectThreadgroup) maxTotalThreadsPerObjectThreadgroup;
@property (TQ,R,V_maxTotalThreadsPerMeshThreadgroup) maxTotalThreadsPerMeshThreadgroup;
@property (TQ,R,V_objectThreadExecutionWidth) objectThreadExecutionWidth;
@property (TQ,R,V_meshThreadExecutionWidth) meshThreadExecutionWidth;
@property (TQ,R,V_maxTotalThreadgroupsPerMeshGrid) maxTotalThreadgroupsPerMeshGrid;
@property (Tq,R) textureWriteRoundingMode;
@property (TQ,R) uniqueIdentifier;
@property (TQ,R,N,V_resourceIndex) resourceIndex;
@property (TQ,R,N,V_gpuAddress) gpuAddress;
@property (TQ,R) fragmentGlobalConstantsBase;
@property (TQ,R) fragmentGlobalConstantsSize;
@property (TQ,R) vertexGlobalConstantsBase;
@property (TQ,R) vertexGlobalConstantsSize;
@property (TQ,R) meshGlobalConstantsBase;
@property (TQ,R) meshGlobalConstantsSize;
@property (TQ,R) objectGlobalConstantsBase;
@property (TQ,R) objectGlobalConstantsSize;
@property (TQ,R) tileGlobalConstantsBase;
@property (TQ,R) tileGlobalConstantsSize;
@property (TQ,R,N) allocatedSize;
@property (TQ,R,V_imageBlockSampleLength) imageBlockSampleLength;
@property (TQ,R) maxTotalThreadsPerThreadgroup;
@property (TB,R,V_threadgroupSizeMatchesTileSize) threadgroupSizeMatchesTileSize;
@property (TI,R,V_explicitVisibilityGroupID) explicitVisibilityGroupID;
@property (T{?=QQQ},R) requiredThreadsPerThreadgroup;
@property (T{?=QQQ},R,V_requiredThreadsPerTileThreadgroup) requiredThreadsPerTileThreadgroup;
@property (T{?=QQQ},R,V_requiredThreadsPerObjectThreadgroup) requiredThreadsPerObjectThreadgroup;
@property (T{?=QQQ},R,V_requiredThreadsPerMeshThreadgroup) requiredThreadsPerMeshThreadgroup;
@property (TQ,R) gpuHandle;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
@property (T@"MTLRenderPipelineReflection",R,V_reflection) reflection;
@property (T@"NSString",R) label;
@property (TQ,R) imageblockSampleLength;
@property (TB,R) supportIndirectCommandBuffers;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLRenderPipelineState supportIndirectCommandBuffers];
-[_MTLRenderPipelineState resourceIndex];
-[_MTLRenderPipelineState meshFunctionHandleWithFunction:];
-[_MTLRenderPipelineState imageblockSampleLength];
-[_MTLRenderPipelineState vertexDebugInstrumentationData];
-[_MTLRenderPipelineState setObjectDebugInstrumentationData:];
-[_MTLRenderPipelineState fragmentGlobalConstantsSize];
-[_MTLRenderPipelineState initWithDevice:pipelineStateDescriptor:];
-[_MTLRenderPipelineState maxTotalThreadsPerMeshThreadgroup];
-[_MTLRenderPipelineState objectGlobalConstantsSize];
-[_MTLRenderPipelineState newVisibleFunctionTableFromTileStageWithDescriptor:];
-[_MTLRenderPipelineState device];
-[_MTLRenderPipelineState fragmentDebugInstrumentationData];
-[_MTLRenderPipelineState textureWriteFPRoundingMode];
-[_MTLRenderPipelineState vertexGlobalConstantsSize];
-[_MTLRenderPipelineState meshThreadExecutionWidth];
-[_MTLRenderPipelineState requiredThreadsPerTileThreadgroup];
-[_MTLRenderPipelineState getFragmentShaderTelemetryID];
-[_MTLRenderPipelineState allocatedSize];
-[_MTLRenderPipelineState newFragmentIntersectionFunctionTableWithDescriptor:];
-[_MTLRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:];
-[_MTLRenderPipelineState setDebugInstrumentationDataForStage:stage:];
-[_MTLRenderPipelineState dealloc];
-[_MTLRenderPipelineState shaderValidation];
-[_MTLRenderPipelineState gpuAddress];
-[_MTLRenderPipelineState setMeshDebugInstrumentationData:];
-[_MTLRenderPipelineState vertexGlobalConstantsBase];
-[_MTLRenderPipelineState objectThreadExecutionWidth];
-[_MTLRenderPipelineState getMeshShaderTelemetryID];
-[_MTLRenderPipelineState newMeshIntersectionFunctionTableWithDescriptor:];
-[_MTLRenderPipelineState maxTotalThreadgroupsPerMeshGrid];
-[_MTLRenderPipelineState newTileIntersectionFunctionTableWithDescriptor:];
-[_MTLRenderPipelineState threadgroupSizeMatchesTileSize];
-[_MTLRenderPipelineState functionHandleWithName:stage:];
-[_MTLRenderPipelineState objectGlobalConstantsBase];
-[_MTLRenderPipelineState uniqueIdentifier];
-[_MTLRenderPipelineState meshGlobalConstantsSize];
-[_MTLRenderPipelineState setFragmentDebugInstrumentationData:];
-[_MTLRenderPipelineState textureWriteRoundingMode];
-[_MTLRenderPipelineState requiredThreadsPerObjectThreadgroup];
-[_MTLRenderPipelineState imageblockMemoryLengthForDimensions:];
-[_MTLRenderPipelineState getObjectShaderTelemetryID];
-[_MTLRenderPipelineState gpuHandle];
-[_MTLRenderPipelineState getVertexShaderTelemetryID];
-[_MTLRenderPipelineState tileGlobalConstantsSize];
-[_MTLRenderPipelineState requiredThreadsPerThreadgroup];
-[_MTLRenderPipelineState setVertexDebugInstrumentationData:];
-[_MTLRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[_MTLRenderPipelineState maxTotalThreadsPerThreadgroup];
-[_MTLRenderPipelineState pipelineBinaries];
-[_MTLRenderPipelineState newVisibleFunctionTableFromMeshStageWithDescriptor:];
-[_MTLRenderPipelineState imageBlockSampleLength];
-[_MTLRenderPipelineState shaderValidationState];
-[_MTLRenderPipelineState fragmentFunctionHandleWithFunction:];
-[_MTLRenderPipelineState maxTotalThreadsPerObjectThreadgroup];
-[_MTLRenderPipelineState fragmentGlobalConstantsBase];
-[_MTLRenderPipelineState explicitVisibilityGroupID];
-[_MTLRenderPipelineState newVisibleFunctionTableFromFragmentStageWithDescriptor:];
-[_MTLRenderPipelineState tileFunctionHandleWithFunction:];
-[_MTLRenderPipelineState functionHandleWithBinaryFunction:stage:];
-[_MTLRenderPipelineState newRenderPipelineDescriptorForSpecialization];
-[_MTLRenderPipelineState initWithDevice:meshRenderPipelineStateDescriptor:objectThreadExecutionWidth:meshThreadExecutionWidth:];
-[_MTLRenderPipelineState newVertexIntersectionFunctionTableWithDescriptor:];
-[_MTLRenderPipelineState functionHandleWithFunction:stage:];
-[_MTLRenderPipelineState meshGlobalConstantsBase];
-[_MTLRenderPipelineState initWithParent:];
-[_MTLRenderPipelineState setTileDebugInstrumentationData:];
-[_MTLRenderPipelineState tileGlobalConstantsBase];
-[_MTLRenderPipelineState initWithDevice:meshRenderPipelineStateDescriptor:objectThreadExecutionWidth:meshThreadExecutionWidth:maxTotalThreadgroupsPerMeshGrid:];
-[_MTLRenderPipelineState requiredThreadsPerMeshThreadgroup];
-[_MTLRenderPipelineState initWithDeviceAndTileDesc:tilePipelineStateDescriptor:];
-[_MTLRenderPipelineState newVisibleFunctionTableFromObjectStageWithDescriptor:];
-[_MTLRenderPipelineState newObjectIntersectionFunctionTableWithDescriptor:];
-[_MTLRenderPipelineState meshDebugInstrumentationData];
-[_MTLRenderPipelineState objectFunctionHandleWithFunction:];
-[_MTLRenderPipelineState reflection];
-[_MTLRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:];
-[_MTLRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:];
-[_MTLRenderPipelineState reflectionForFunctionDescriptor:];
-[_MTLRenderPipelineState gpuResourceID];
-[_MTLRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:];
-[_MTLRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[_MTLRenderPipelineState newVisibleFunctionTableFromVertexStageWithDescriptor:];
-[_MTLRenderPipelineState functionReflectionWithFunctionDescriptor:stage:];
-[_MTLRenderPipelineState tileDebugInstrumentationData];
-[_MTLRenderPipelineState vertexFunctionHandleWithFunction:];
-[_MTLRenderPipelineState objectDebugInstrumentationData];
-[_MTLRenderPipelineState initWithTileParent:];
```
