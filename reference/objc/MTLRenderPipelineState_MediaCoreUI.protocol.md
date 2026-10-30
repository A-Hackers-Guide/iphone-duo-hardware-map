# `MTLRenderPipelineState` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](../userland/System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLAllocation`, `NSObject`
- 0 instance variables, 17 properties, 26 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"MTLRenderPipelineReflection",R) reflection;
@property (TQ,R) maxTotalThreadsPerThreadgroup;
@property (TB,R) threadgroupSizeMatchesTileSize;
@property (TQ,R) imageblockSampleLength;
@property (TB,R) supportIndirectCommandBuffers;
@property (TQ,R) maxTotalThreadsPerObjectThreadgroup;
@property (TQ,R) maxTotalThreadsPerMeshThreadgroup;
@property (TQ,R) objectThreadExecutionWidth;
@property (TQ,R) meshThreadExecutionWidth;
@property (TQ,R) maxTotalThreadgroupsPerMeshGrid;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (Tq,R,N) shaderValidation;
@property (T{?=QQQ},R) requiredThreadsPerTileThreadgroup;
@property (T{?=QQQ},R) requiredThreadsPerObjectThreadgroup;
@property (T{?=QQQ},R) requiredThreadsPerMeshThreadgroup;
```

## Instance methods

```
-[MTLRenderPipelineState supportIndirectCommandBuffers];
-[MTLRenderPipelineState imageblockSampleLength];
-[MTLRenderPipelineState maxTotalThreadsPerMeshThreadgroup];
-[MTLRenderPipelineState device];
-[MTLRenderPipelineState label];
-[MTLRenderPipelineState meshThreadExecutionWidth];
-[MTLRenderPipelineState requiredThreadsPerTileThreadgroup];
-[MTLRenderPipelineState shaderValidation];
-[MTLRenderPipelineState objectThreadExecutionWidth];
-[MTLRenderPipelineState maxTotalThreadgroupsPerMeshGrid];
-[MTLRenderPipelineState threadgroupSizeMatchesTileSize];
-[MTLRenderPipelineState functionHandleWithName:stage:];
-[MTLRenderPipelineState requiredThreadsPerObjectThreadgroup];
-[MTLRenderPipelineState imageblockMemoryLengthForDimensions:];
-[MTLRenderPipelineState maxTotalThreadsPerThreadgroup];
-[MTLRenderPipelineState maxTotalThreadsPerObjectThreadgroup];
-[MTLRenderPipelineState functionHandleWithBinaryFunction:stage:];
-[MTLRenderPipelineState newRenderPipelineDescriptorForSpecialization];
-[MTLRenderPipelineState functionHandleWithFunction:stage:];
-[MTLRenderPipelineState requiredThreadsPerMeshThreadgroup];
-[MTLRenderPipelineState reflection];
-[MTLRenderPipelineState newIntersectionFunctionTableWithDescriptor:stage:];
-[MTLRenderPipelineState newRenderPipelineStateWithBinaryFunctions:error:];
-[MTLRenderPipelineState gpuResourceID];
-[MTLRenderPipelineState newVisibleFunctionTableWithDescriptor:stage:];
-[MTLRenderPipelineState newRenderPipelineStateWithAdditionalBinaryFunctions:error:];
```
