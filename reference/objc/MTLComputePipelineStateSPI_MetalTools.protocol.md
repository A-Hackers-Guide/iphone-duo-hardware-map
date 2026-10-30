# `MTLComputePipelineStateSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLComputePipelineState`, `MTLPipelineStateWithProgramAddressTable`
- 0 instance variables, 12 properties, 17 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[MTLComputePipelineStateSPI functionHandleWithBinaryFunction:];
-[MTLComputePipelineStateSPI allocatedSize];
-[MTLComputePipelineStateSPI uniqueIdentifier];
-[MTLComputePipelineStateSPI textureWriteRoundingMode];
-[MTLComputePipelineStateSPI gpuHandle];
-[MTLComputePipelineStateSPI shaderValidationState];
-[MTLComputePipelineStateSPI debugInstrumentationData];
-[MTLComputePipelineStateSPI reflection];
-[MTLComputePipelineStateSPI functionHandleWithName:];
-[MTLComputePipelineStateSPI staticThreadgroupMemoryLength];
-[MTLComputePipelineStateSPI functionReflectionWithFunctionDescriptor:];
-[MTLComputePipelineStateSPI getComputeKernelTelemetryID];
-[MTLComputePipelineStateSPI globalConstantsBase];
-[MTLComputePipelineStateSPI globalConstantsSize];
-[MTLComputePipelineStateSPI newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:];
-[MTLComputePipelineStateSPI resourceIndex];
-[MTLComputePipelineStateSPI gpuAddress];
```
