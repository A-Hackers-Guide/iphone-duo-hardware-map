# `_MTLComputePipelineState`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAllocation`
- Protocols: `MTLComputePipelineState`
- 8 instance variables, 25 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"MTLDebugInstrumentationData" _debugInstrumentationData;
B _supportIndirectCommandBuffers;
q _textureWriteRoundingMode;
Q _resourceIndex;
Q _gpuAddress;
@"MTLComputePipelineReflection" _reflection;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerThreadgroup;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"MTLDebugInstrumentationData",&,N,V_debugInstrumentationData) debugInstrumentationData;
@property (TQ,R) uniqueIdentifier;
@property (Tq,R) textureWriteRoundingMode;
@property (TQ,R,N,V_resourceIndex) resourceIndex;
@property (TQ,R,N,V_gpuAddress) gpuAddress;
@property (TQ,R) globalConstantsBase;
@property (TQ,R) globalConstantsSize;
@property (TQ,R,N) allocatedSize;
@property (TQ,R) gpuHandle;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
@property (T@"MTLComputePipelineReflection",R,V_reflection) reflection;
@property (T{?=QQQ},R,V_requiredThreadsPerThreadgroup) requiredThreadsPerThreadgroup;
@property (Tq,R,D) forwardProgressUsage;
@property (T@"NSString",R) label;
@property (TQ,R,D) maxTotalThreadsPerThreadgroup;
@property (TQ,R,D) threadExecutionWidth;
@property (TQ,R,D) staticThreadgroupMemoryLength;
@property (TB,R) supportIndirectCommandBuffers;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLComputePipelineState supportIndirectCommandBuffers];
-[_MTLComputePipelineState functionHandleWithFunction:];
-[_MTLComputePipelineState resourceIndex];
-[_MTLComputePipelineState functionHandleWithBinaryFunction:];
-[_MTLComputePipelineState initWithDevice:pipelineStateDescriptor:];
-[_MTLComputePipelineState formattedDescription:];
-[_MTLComputePipelineState device];
-[_MTLComputePipelineState textureWriteFPRoundingMode];
-[_MTLComputePipelineState allocatedSize];
-[_MTLComputePipelineState dealloc];
-[_MTLComputePipelineState shaderValidation];
-[_MTLComputePipelineState gpuAddress];
-[_MTLComputePipelineState uniqueIdentifier];
-[_MTLComputePipelineState textureWriteRoundingMode];
-[_MTLComputePipelineState imageblockMemoryLengthForDimensions:];
-[_MTLComputePipelineState setDebugInstrumentationData:];
-[_MTLComputePipelineState gpuHandle];
-[_MTLComputePipelineState requiredThreadsPerThreadgroup];
-[_MTLComputePipelineState newIntersectionFunctionTableWithDescriptor:];
-[_MTLComputePipelineState pipelineBinaries];
-[_MTLComputePipelineState shaderValidationState];
-[_MTLComputePipelineState initWithParent:];
-[_MTLComputePipelineState description];
-[_MTLComputePipelineState debugInstrumentationData];
-[_MTLComputePipelineState reflection];
-[_MTLComputePipelineState gpuResourceID];
-[_MTLComputePipelineState functionHandleWithName:];
-[_MTLComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[_MTLComputePipelineState newComputePipelineStateWithBinaryFunctions:error:];
-[_MTLComputePipelineState newVisibleFunctionTableWithDescriptor:];
-[_MTLComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:];
-[_MTLComputePipelineState functionReflectionWithFunctionDescriptor:];
-[_MTLComputePipelineState getComputeKernelTelemetryID];
-[_MTLComputePipelineState globalConstantsBase];
-[_MTLComputePipelineState globalConstantsSize];
-[_MTLComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:];
```
