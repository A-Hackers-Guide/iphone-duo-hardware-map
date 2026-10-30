# `MTLGPUDebugComputePipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputePipelineState`
- 16 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"MTLGPUDebugImageData" _kernelFunctionData;
@"MTLComputePipelineReflection" _internalReflection;
@"MTLComputePipelineReflection" _userReflection;
@"NSMutableArray" _binaryFunctionData;
Q _constantOffset;
I _threadgroupArgumentOffset;
I _activeThreadgroupMask;
@"MTLGPUDebugBuffer" _indirectStateBuffer;
B _supportsIndirectCommandBuffers;
Q _indirectStateGPUAddress;
Q _globalConstantsHandle;
q _shaderValidation;
q _shaderValidationState;
@"NSMutableArray" _retainedFunctions;
i _maxCallStackDepth;
@"NSString" _UID;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_binaryFunctionData) binaryFunctionData;
@property (T@"MTLGPUDebugImageData",R,N) kernelFunctionData;
@property (T@"MTLComputePipelineReflection",R,N) internalReflection;
@property (T@"MTLComputePipelineReflection",R,N) userReflection;
@property (T@"MTLGPUDebugBuffer",R,N) globalConstantsBuffer;
@property (TQ,R,N) constantOffset;
@property (TQ,R) staticThreadgroupMemoryLength;
@property (Ti,R,N,V_maxCallStackDepth) maxCallStackDepth;
@property (T@"MTLGPUDebugBuffer",R,N) indirectStateBuffer;
@property (TQ,R,N) globalConstantsHandle;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
@property (T@"NSString",&,N,V_UID) UID;
```

## Instance methods

```
-[MTLGPUDebugComputePipelineState UID];
-[MTLGPUDebugComputePipelineState functionHandleWithFunction:];
-[MTLGPUDebugComputePipelineState functionHandleWithBinaryFunction:];
-[MTLGPUDebugComputePipelineState maxCallStackDepth];
-[MTLGPUDebugComputePipelineState dealloc];
-[MTLGPUDebugComputePipelineState shaderValidation];
-[MTLGPUDebugComputePipelineState newIntersectionFunctionTableWithDescriptor:];
-[MTLGPUDebugComputePipelineState shaderValidationState];
-[MTLGPUDebugComputePipelineState setUID:];
-[MTLGPUDebugComputePipelineState gpuResourceID];
-[MTLGPUDebugComputePipelineState functionHandleWithName:];
-[MTLGPUDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLGPUDebugComputePipelineState newComputePipelineStateWithBinaryFunctions:error:];
-[MTLGPUDebugComputePipelineState newVisibleFunctionTableWithDescriptor:];
-[MTLGPUDebugComputePipelineState staticThreadgroupMemoryLength];
-[MTLGPUDebugComputePipelineState _initConstantsBuffer:];
-[MTLGPUDebugComputePipelineState binaryFunctionData];
-[MTLGPUDebugComputePipelineState constantOffset];
-[MTLGPUDebugComputePipelineState globalConstantsBuffer];
-[MTLGPUDebugComputePipelineState globalConstantsHandle];
-[MTLGPUDebugComputePipelineState indirectStateBuffer];
-[MTLGPUDebugComputePipelineState initWithComputePipelineState:binaryFunctions:withState:device:needsReflectionProperty:];
-[MTLGPUDebugComputePipelineState initWithComputePipelineState:binaryFunctions:withState:device:pipelineOptions:];
-[MTLGPUDebugComputePipelineState initWithComputePipelineState:descriptor:device:needsReflectionProperty:];
-[MTLGPUDebugComputePipelineState initWithComputePipelineState:descriptor:dynamicLinkingDescriptor:device:needsReflectionProperty:];
-[MTLGPUDebugComputePipelineState initWithComputePipelineState:descriptor:unwrappedDescriptor:reflection:device:pipelineOptions:];
-[MTLGPUDebugComputePipelineState internalReflection];
-[MTLGPUDebugComputePipelineState kernelFunctionData];
-[MTLGPUDebugComputePipelineState releaseReflection];
-[MTLGPUDebugComputePipelineState setGlobalConstantsHandle:];
-[MTLGPUDebugComputePipelineState userReflection];
```
