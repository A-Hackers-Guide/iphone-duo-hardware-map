# `MTLComputePipelineState` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLAllocation`, `NSObject`
- 0 instance variables, 11 properties, 20 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R) label;
@property (T@"MTLComputePipelineReflection",R) reflection;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) maxTotalThreadsPerThreadgroup;
@property (TQ,R) threadExecutionWidth;
@property (TQ,R) staticThreadgroupMemoryLength;
@property (TB,R) supportIndirectCommandBuffers;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (Tq,R,N) shaderValidation;
@property (T{?=QQQ},R) requiredThreadsPerThreadgroup;
@property (Tq,R) forwardProgressUsage;
```

## Instance methods

```
-[MTLComputePipelineState supportIndirectCommandBuffers];
-[MTLComputePipelineState functionHandleWithFunction:];
-[MTLComputePipelineState functionHandleWithBinaryFunction:];
-[MTLComputePipelineState device];
-[MTLComputePipelineState label];
-[MTLComputePipelineState shaderValidation];
-[MTLComputePipelineState imageblockMemoryLengthForDimensions:];
-[MTLComputePipelineState requiredThreadsPerThreadgroup];
-[MTLComputePipelineState newIntersectionFunctionTableWithDescriptor:];
-[MTLComputePipelineState maxTotalThreadsPerThreadgroup];
-[MTLComputePipelineState forwardProgressUsage];
-[MTLComputePipelineState reflection];
-[MTLComputePipelineState gpuResourceID];
-[MTLComputePipelineState threadExecutionWidth];
-[MTLComputePipelineState functionHandleWithName:];
-[MTLComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLComputePipelineState newComputePipelineStateWithBinaryFunctions:error:];
-[MTLComputePipelineState newVisibleFunctionTableWithDescriptor:];
-[MTLComputePipelineState recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:];
-[MTLComputePipelineState staticThreadgroupMemoryLength];
```
