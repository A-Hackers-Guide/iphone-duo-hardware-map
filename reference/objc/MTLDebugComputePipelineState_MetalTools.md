# `MTLDebugComputePipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsComputePipelineState`
- 13 instance variables, 6 properties, 28 instance methods, 0 class methods

## Instance variables

```
[3Q] _maxThreadPositionInGrid;
[3Q] _maxThreadsPerGrid;
[3Q] _maxThreadPositionInThreadgroup;
[3Q] _maxThreadIndexInThreadgroup;
[3Q] _maxThreadsPerThreadgroup;
[3Q] _maxThreadgroupPositionInGrid;
[3Q] _maxThreadgroupsPerGrid;
[3Q] _maxStageInGridSize;
[3Q] _maxStageInGridOrigin;
@"MTLComputePipelineReflection" _validationReflection;
@"<MTLFunction>" _function;
@"MTLComputePipelineDescriptor" _descriptor;
@"MTL4ComputePipelineDescriptor" _mtl4Descriptor;
```

## Properties

```
@property (T@"<MTLFunction>",R,N,V_function) function;
@property (T@"MTLComputePipelineDescriptor",R,N,V_descriptor) descriptor;
@property (T@"MTLComputePipelineReflection",R,N,V_validationReflection) validationReflection;
@property (Tq,R,N) shaderValidation;
@property (Tq,R,N) shaderValidationState;
@property (T@"MTL4ComputePipelineDescriptor",R,N,V_mtl4Descriptor) mtl4Descriptor;
```

## Instance methods

```
-[MTLDebugComputePipelineState functionHandleWithFunction:];
-[MTLDebugComputePipelineState functionHandleWithBinaryFunction:];
-[MTLDebugComputePipelineState initCommon];
-[MTLDebugComputePipelineState function];
-[MTLDebugComputePipelineState descriptor];
-[MTLDebugComputePipelineState formattedDescription:];
-[MTLDebugComputePipelineState dealloc];
-[MTLDebugComputePipelineState shaderValidation];
-[MTLDebugComputePipelineState newIntersectionFunctionTableWithDescriptor:];
-[MTLDebugComputePipelineState shaderValidationState];
-[MTLDebugComputePipelineState description];
-[MTLDebugComputePipelineState functionHandleWithName:];
-[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:error:];
-[MTLDebugComputePipelineState newComputePipelineStateWithBinaryFunctions:error:];
-[MTLDebugComputePipelineState newVisibleFunctionTableWithDescriptor:];
-[MTLDebugComputePipelineState isAncestorOf:];
-[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:resourceIndices:error:];
-[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:];
-[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:binaryFunction:];
-[MTLDebugComputePipelineState functionHandleToDebugFunctionHandle:parentFunction:];
-[MTLDebugComputePipelineState getParameter:];
-[MTLDebugComputePipelineState initWithComputePipelineState:parent:mtl4Descriptor:];
-[MTLDebugComputePipelineState initWithComputePipelineState:reflection:parent:descriptor:];
-[MTLDebugComputePipelineState initWithComputePipelineState:reflection:parent:mtl4Descriptor:];
-[MTLDebugComputePipelineState mtl4Descriptor];
-[MTLDebugComputePipelineState newComputePipelineStateWithAdditionalBinaryFunctions:];
-[MTLDebugComputePipelineState validateHandleForSetFunction:];
-[MTLDebugComputePipelineState validationReflection];
```
