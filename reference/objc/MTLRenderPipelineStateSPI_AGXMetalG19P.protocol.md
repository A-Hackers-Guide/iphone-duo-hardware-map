# `MTLRenderPipelineStateSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLRenderPipelineState`, `MTLPipelineStateWithProgramAddressTable`
- 0 instance variables, 30 properties, 53 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[MTLRenderPipelineStateSPI meshFunctionHandleWithFunction:];
-[MTLRenderPipelineStateSPI vertexDebugInstrumentationData];
-[MTLRenderPipelineStateSPI fragmentGlobalConstantsSize];
-[MTLRenderPipelineStateSPI maxTotalThreadsPerMeshThreadgroup];
-[MTLRenderPipelineStateSPI objectGlobalConstantsSize];
-[MTLRenderPipelineStateSPI newVisibleFunctionTableFromTileStageWithDescriptor:];
-[MTLRenderPipelineStateSPI fragmentDebugInstrumentationData];
-[MTLRenderPipelineStateSPI vertexGlobalConstantsSize];
-[MTLRenderPipelineStateSPI meshThreadExecutionWidth];
-[MTLRenderPipelineStateSPI getFragmentShaderTelemetryID];
-[MTLRenderPipelineStateSPI allocatedSize];
-[MTLRenderPipelineStateSPI newFragmentIntersectionFunctionTableWithDescriptor:];
-[MTLRenderPipelineStateSPI newRenderPipelineStateWithAdditionalBinaryFunctions:fragmentAdditionalBinaryFunctions:error:];
-[MTLRenderPipelineStateSPI vertexGlobalConstantsBase];
-[MTLRenderPipelineStateSPI objectThreadExecutionWidth];
-[MTLRenderPipelineStateSPI newTileIntersectionFunctionTableWithDescriptor:];
-[MTLRenderPipelineStateSPI objectGlobalConstantsBase];
-[MTLRenderPipelineStateSPI uniqueIdentifier];
-[MTLRenderPipelineStateSPI meshGlobalConstantsSize];
-[MTLRenderPipelineStateSPI textureWriteRoundingMode];
-[MTLRenderPipelineStateSPI requiredThreadsPerObjectThreadgroup];
-[MTLRenderPipelineStateSPI gpuHandle];
-[MTLRenderPipelineStateSPI getVertexShaderTelemetryID];
-[MTLRenderPipelineStateSPI tileGlobalConstantsSize];
-[MTLRenderPipelineStateSPI newTileRenderPipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLRenderPipelineStateSPI newVisibleFunctionTableFromMeshStageWithDescriptor:];
-[MTLRenderPipelineStateSPI shaderValidationState];
-[MTLRenderPipelineStateSPI fragmentFunctionHandleWithFunction:];
-[MTLRenderPipelineStateSPI maxTotalThreadsPerObjectThreadgroup];
-[MTLRenderPipelineStateSPI fragmentGlobalConstantsBase];
-[MTLRenderPipelineStateSPI newVisibleFunctionTableFromFragmentStageWithDescriptor:];
-[MTLRenderPipelineStateSPI tileFunctionHandleWithFunction:];
-[MTLRenderPipelineStateSPI newVertexIntersectionFunctionTableWithDescriptor:];
-[MTLRenderPipelineStateSPI meshGlobalConstantsBase];
-[MTLRenderPipelineStateSPI tileGlobalConstantsBase];
-[MTLRenderPipelineStateSPI requiredThreadsPerMeshThreadgroup];
-[MTLRenderPipelineStateSPI newVisibleFunctionTableFromObjectStageWithDescriptor:];
-[MTLRenderPipelineStateSPI meshDebugInstrumentationData];
-[MTLRenderPipelineStateSPI objectFunctionHandleWithFunction:];
-[MTLRenderPipelineStateSPI reflection];
-[MTLRenderPipelineStateSPI reflectionForFunctionDescriptor:];
-[MTLRenderPipelineStateSPI newVisibleFunctionTableFromVertexStageWithDescriptor:];
-[MTLRenderPipelineStateSPI functionReflectionWithFunctionDescriptor:stage:];
-[MTLRenderPipelineStateSPI tileDebugInstrumentationData];
-[MTLRenderPipelineStateSPI vertexFunctionHandleWithFunction:];
-[MTLRenderPipelineStateSPI objectDebugInstrumentationData];
-[MTLRenderPipelineStateSPI newFragmentShaderDebugInfo];
-[MTLRenderPipelineStateSPI newVertexShaderDebugInfo];
-[MTLRenderPipelineStateSPI resourceIndex];
-[MTLRenderPipelineStateSPI gpuAddress];
-[MTLRenderPipelineStateSPI newMeshIntersectionFunctionTableWithDescriptor:];
-[MTLRenderPipelineStateSPI explicitVisibilityGroupID];
-[MTLRenderPipelineStateSPI newObjectIntersectionFunctionTableWithDescriptor:];
```
