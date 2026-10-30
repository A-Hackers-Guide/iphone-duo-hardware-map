# `MTLToolsRenderPipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLRenderPipelineStateSPI`
- 1 instance variables, 45 properties, 79 instance methods, 0 class methods

## Instance variables

```
B _needsReflectionProperty;
```

## Properties

```
@property (TB,R,N,V_needsReflectionProperty) needsReflectionProperty;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R,N) gpuAddress;
@property (T@"MTLRenderPipelineReflection",R) reflection;
@property (Tq,R) textureWriteRoundingMode;
@property (TQ,R,N) allocatedSize;
@property (Tq,R,N) shaderValidationState;
@property (TQ,R) uniqueIdentifier;
@property (T@"MTLDebugInstrumentationData",R,&,N) vertexDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",R,&,N) fragmentDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",R,&,N) tileDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",R,&,N) objectDebugInstrumentationData;
@property (T@"MTLDebugInstrumentationData",R,&,N) meshDebugInstrumentationData;
@property (TQ,R) maxTotalThreadsPerObjectThreadgroup;
@property (TQ,R) maxTotalThreadsPerMeshThreadgroup;
@property (TQ,R) objectThreadExecutionWidth;
@property (TQ,R) meshThreadExecutionWidth;
@property (T{?=QQQ},R) requiredThreadsPerObjectThreadgroup;
@property (T{?=QQQ},R) requiredThreadsPerMeshThreadgroup;
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
@property (TI,?,R,N) explicitVisibilityGroupID;
@property (TQ,R) gpuHandle;
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) maxTotalThreadsPerThreadgroup;
@property (TB,R) threadgroupSizeMatchesTileSize;
@property (TQ,R) imageblockSampleLength;
@property (TB,R) supportIndirectCommandBuffers;
@property (TQ,R) maxTotalThreadgroupsPerMeshGrid;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (Tq,R,N) shaderValidation;
@property (T{?=QQQ},R) requiredThreadsPerTileThreadgroup;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsRenderPipelineState supportIndirectCommandBuffers];
-[MTLToolsRenderPipelineState resourceIndex];
-[MTLToolsRenderPipelineState meshFunctionHandleWithFunction:];
-[MTLToolsRenderPipelineState imageblockSampleLength];
-[MTLToolsRenderPipelineState vertexDebugInstrumentationData];
-[MTLToolsRenderPipelineState fragmentGlobalConstantsSize];
-[MTLToolsRenderPipelineState maxTotalThreadsPerMeshThreadgroup];
-[MTLToolsRenderPipelineState objectGlobalConstantsSize];
-[MTLToolsRenderPipelineState newVisibleFunctionTableFromTileStageWithDescriptor:];
-[MTLToolsRenderPipelineState device];
-[MTLToolsRenderPipelineState fragmentDebugInstrumentationData];
-[MTLToolsRenderPipelineState label];
-[MTLToolsRenderPipelineState vertexGlobalConstantsSize];
-[MTLToolsRenderPipelineState meshThreadExecutionWidth];
-[MTLToolsRenderPipelineState requiredThreadsPerTileThreadgroup];
-[MTLToolsRenderPipelineState getFragmentShaderTelemetryID];
-[MTLToolsRenderPipelineState allocatedSize];
-[MTLToolsRenderPipelineState newFragmentIntersectionFunctionTableWithDescriptor:];
-[MTLToolsRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:];
-[MTLToolsRenderPipelineState dealloc];
-[MTLToolsRenderPipelineState shaderValidation];
-[MTLToolsRenderPipelineState gpuAddress];
-[MTLToolsRenderPipelineState vertexGlobalConstantsBase];
-[MTLToolsRenderPipelineState objectThreadExecutionWidth];
-[MTLToolsRenderPipelineState newMeshIntersectionFunctionTableWithDescriptor:];
-[MTLToolsRenderPipelineState maxTotalThreadgroupsPerMeshGrid];
-[MTLToolsRenderPipelineState newTileIntersectionFunctionTableWithDescriptor:];
-[MTLToolsRenderPipelineState threadgroupSizeMatchesTileSize];
-[MTLToolsRenderPipelineState functionHandleWithName:stage:];
-[MTLToolsRenderPipelineState objectGlobalConstantsBase];
-[MTLToolsRenderPipelineState uniqueIdentifier];
-[MTLToolsRenderPipelineState meshGlobalConstantsSize];
-[MTLToolsRenderPipelineState textureWriteRoundingMode];
-[MTLToolsRenderPipelineState requiredThreadsPerObjectThreadgroup];
-[MTLToolsRenderPipelineState imageblockMemoryLengthForDimensions:];
-[MTLToolsRenderPipelineState gpuHandle];
-[MTLToolsRenderPipelineState getVertexShaderTelemetryID];
-[MTLToolsRenderPipelineState tileGlobalConstantsSize];
-[MTLToolsRenderPipelineState newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLToolsRenderPipelineState maxTotalThreadsPerThreadgroup];
-[MTLToolsRenderPipelineState pipelineBinaries];
-[MTLToolsRenderPipelineState newVisibleFunctionTableFromMeshStageWithDescriptor:];
-[MTLToolsRenderPipelineState shaderValidationState];
-[MTLToolsRenderPipelineState fragmentFunctionHandleWithFunction:];
-[MTLToolsRenderPipelineState maxTotalThreadsPerObjectThreadgroup];
-[MTLToolsRenderPipelineState fragmentGlobalConstantsBase];
-[MTLToolsRenderPipelineState explicitVisibilityGroupID];
-[MTLToolsRenderPipelineState newVisibleFunctionTableFromFragmentStageWithDescriptor:];
-[MTLToolsRenderPipelineState tileFunctionHandleWithFunction:];
-[MTLToolsRenderPipelineState functionHandleWithBinaryFunction:stage:];
-[MTLToolsRenderPipelineState newRenderPipelineDescriptorForSpecialization];
-[MTLToolsRenderPipelineState newVertexIntersectionFunctionTableWithDescriptor:];
-[MTLToolsRenderPipelineState functionHandleWithFunction:stage:];
-[MTLToolsRenderPipelineState meshGlobalConstantsBase];
-[MTLToolsRenderPipelineState tileGlobalConstantsBase];
-[MTLToolsRenderPipelineState requiredThreadsPerMeshThreadgroup];
-[MTLToolsRenderPipelineState newVisibleFunctionTableFromObjectStageWithDescriptor:];
-[MTLToolsRenderPipelineState newObjectIntersectionFunctionTableWithDescriptor:];
-[MTLToolsRenderPipelineState meshDebugInstrumentationData];
-[MTLToolsRenderPipelineState objectFunctionHandleWithFunction:];
-[MTLToolsRenderPipelineState reflection];
-[MTLToolsRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:];
-[MTLToolsRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:];
-[MTLToolsRenderPipelineState reflectionForFunctionDescriptor:];
-[MTLToolsRenderPipelineState gpuResourceID];
-[MTLToolsRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:];
-[MTLToolsRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLToolsRenderPipelineState newVisibleFunctionTableFromVertexStageWithDescriptor:];
-[MTLToolsRenderPipelineState functionReflectionWithFunctionDescriptor:stage:];
-[MTLToolsRenderPipelineState tileDebugInstrumentationData];
-[MTLToolsRenderPipelineState vertexFunctionHandleWithFunction:];
-[MTLToolsRenderPipelineState objectDebugInstrumentationData];
-[MTLToolsRenderPipelineState initWithBaseObject:parent:];
-[MTLToolsRenderPipelineState newFragmentShaderDebugInfo];
-[MTLToolsRenderPipelineState newVertexShaderDebugInfo];
-[MTLToolsRenderPipelineState initWithBaseObject:parent:needsReflectionProperty:];
-[MTLToolsRenderPipelineState needsReflectionProperty];
-[MTLToolsRenderPipelineState newIntersectionFunctionTableWithDescriptor:selector:];
-[MTLToolsRenderPipelineState newVisibleFunctionTableWithDescriptor:selector:];
```
