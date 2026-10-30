# `MTLLegacySVComputePipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputePipelineState`
- 13 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"MTLLegacySVImageData" _kernelFunctionData;
@"MTLComputePipelineReflection" _internalReflection;
@"MTLComputePipelineReflection" _userReflection;
@"NSMutableArray" _binaryFunctionData;
Q _constantOffset;
I _threadgroupArgumentOffset;
I _activeThreadgroupMask;
@"MTLLegacySVBuffer" _indirectStateBuffer;
B _supportsIndirectCommandBuffers;
q _shaderValidation;
q _shaderValidationState;
@"NSMutableArray" _retainedFunctions;
i _maxCallStackDepth;
```

## Properties

```
@property (T@"NSArray",R,N,V_binaryFunctionData) binaryFunctionData;
@property (T@"MTLLegacySVImageData",R,N) kernelFunctionData;
@property (T@"MTLComputePipelineReflection",R,N) internalReflection;
@property (T@"MTLComputePipelineReflection",R,N) userReflection;
@property (T@"MTLLegacySVBuffer",R,N) globalConstantsBuffer;
@property (TQ,R,N) constantOffset;
@property (TQ,R) staticThreadgroupMemoryLength;
@property (Ti,R,N,V_maxCallStackDepth) maxCallStackDepth;
@property (T@"MTLLegacySVBuffer",R,N) indirectStateBuffer;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
```

## Instance methods

```
-[MTLLegacySVComputePipelineState functionHandleWithFunction:];
-[MTLLegacySVComputePipelineState maxCallStackDepth];
-[MTLLegacySVComputePipelineState dealloc];
-[MTLLegacySVComputePipelineState shaderValidation];
-[MTLLegacySVComputePipelineState newIntersectionFunctionTableWithDescriptor:];
-[MTLLegacySVComputePipelineState shaderValidationState];
-[MTLLegacySVComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLLegacySVComputePipelineState newVisibleFunctionTableWithDescriptor:];
-[MTLLegacySVComputePipelineState staticThreadgroupMemoryLength];
-[MTLLegacySVComputePipelineState _initConstantsBuffer:device:];
-[MTLLegacySVComputePipelineState binaryFunctionData];
-[MTLLegacySVComputePipelineState constantOffset];
-[MTLLegacySVComputePipelineState globalConstantsBuffer];
-[MTLLegacySVComputePipelineState indirectStateBuffer];
-[MTLLegacySVComputePipelineState initWithComputePipelineState:binaryFunctions:withState:device:pipelineOptions:];
-[MTLLegacySVComputePipelineState initWithComputePipelineState:descriptor:unwrappedDescriptor:reflection:device:pipelineOptions:];
-[MTLLegacySVComputePipelineState internalReflection];
-[MTLLegacySVComputePipelineState kernelFunctionData];
-[MTLLegacySVComputePipelineState releaseReflection];
-[MTLLegacySVComputePipelineState userReflection];
```
