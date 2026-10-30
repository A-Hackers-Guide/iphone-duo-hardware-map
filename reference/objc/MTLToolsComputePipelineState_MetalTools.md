# `MTLToolsComputePipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLComputePipelineStateSPI`
- 2 instance variables, 26 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"<MTLFunction>" _function;
B _needsReflectionProperty;
```

## Properties

```
@property (TB,R,N,V_needsReflectionProperty) needsReflectionProperty;
@property (Tq,R) textureWriteRoundingMode;
@property (TQ,R) staticThreadgroupMemoryLength;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,R,N) allocatedSize;
@property (TQ,R) globalConstantsBase;
@property (TQ,R) globalConstantsSize;
@property (TQ,R) uniqueIdentifier;
@property (T@"MTLDebugInstrumentationData",R,&,N) debugInstrumentationData;
@property (TQ,R) gpuHandle;
@property (Tq,R,N) shaderValidationState;
@property (T@"MTLComputePipelineReflection",R) reflection;
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) maxTotalThreadsPerThreadgroup;
@property (TQ,R) threadExecutionWidth;
@property (TB,R) supportIndirectCommandBuffers;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (Tq,R,N) shaderValidation;
@property (T{?=QQQ},R) requiredThreadsPerThreadgroup;
@property (Tq,R) forwardProgressUsage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsComputePipelineState supportIndirectCommandBuffers];
-[MTLToolsComputePipelineState functionHandleWithFunction:];
-[MTLToolsComputePipelineState resourceIndex];
-[MTLToolsComputePipelineState functionHandleWithBinaryFunction:];
-[MTLToolsComputePipelineState device];
-[MTLToolsComputePipelineState label];
-[MTLToolsComputePipelineState allocatedSize];
-[MTLToolsComputePipelineState dealloc];
-[MTLToolsComputePipelineState shaderValidation];
-[MTLToolsComputePipelineState gpuAddress];
-[MTLToolsComputePipelineState uniqueIdentifier];
-[MTLToolsComputePipelineState textureWriteRoundingMode];
-[MTLToolsComputePipelineState imageblockMemoryLengthForDimensions:];
-[MTLToolsComputePipelineState gpuHandle];
-[MTLToolsComputePipelineState requiredThreadsPerThreadgroup];
-[MTLToolsComputePipelineState newIntersectionFunctionTableWithDescriptor:];
-[MTLToolsComputePipelineState maxTotalThreadsPerThreadgroup];
-[MTLToolsComputePipelineState pipelineBinaries];
-[MTLToolsComputePipelineState shaderValidationState];
-[MTLToolsComputePipelineState debugInstrumentationData];
-[MTLToolsComputePipelineState forwardProgressUsage];
-[MTLToolsComputePipelineState reflection];
-[MTLToolsComputePipelineState gpuResourceID];
-[MTLToolsComputePipelineState threadExecutionWidth];
-[MTLToolsComputePipelineState functionHandleWithName:];
-[MTLToolsComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLToolsComputePipelineState newComputePipelineStateWithBinaryFunctions:error:];
-[MTLToolsComputePipelineState newVisibleFunctionTableWithDescriptor:];
-[MTLToolsComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:];
-[MTLToolsComputePipelineState staticThreadgroupMemoryLength];
-[MTLToolsComputePipelineState functionReflectionWithFunctionDescriptor:];
-[MTLToolsComputePipelineState getComputeKernelTelemetryID];
-[MTLToolsComputePipelineState globalConstantsBase];
-[MTLToolsComputePipelineState globalConstantsSize];
-[MTLToolsComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:];
-[MTLToolsComputePipelineState initWithBaseObject:parent:needsReflectionProperty:];
-[MTLToolsComputePipelineState needsReflectionProperty];
-[MTLToolsComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:];
```
