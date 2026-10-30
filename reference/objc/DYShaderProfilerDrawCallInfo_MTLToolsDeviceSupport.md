# `DYShaderProfilerDrawCallInfo`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 16 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSString" _vertexShaderKey;
@"NSString" _fragmentShaderKey;
@"NSString" _computeKernelKey;
@"NSArray" _allShaderKeys;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _vertexTiming;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _fragmentTiming;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _computeTiming;
{DYShaderProfilerTiming="_cycle"{Statistics="average"d"min"d"max"d}"_time"{Statistics="average"d"min"d"max"d}} _timing;
I _drawCallIndex;
I _encoderIndex;
I _functionIndex;
I _commandBufferIndex;
I _pipelineStateIndex;
i _subCommandIndex;
Q _encoderStateId;
Q _encoderFunctionIndex;
Q _pipelineStateId;
Q _pipelineStateFunctionIndex;
@"DYShaderProfilerProgramInfo" _programInfo;
```

## Properties

```
@property (T@"NSArray",&,N,V_allShaderKeys) allShaderKeys;
@property (TI,N,V_drawCallIndex) drawCallIndex;
@property (TI,N,V_functionIndex) functionIndex;
@property (TI,N,V_pipelineStateIndex) pipelineStateIndex;
@property (TQ,N,V_pipelineStateId) pipelineStateId;
@property (TQ,N,V_pipelineStateFunctionIndex) pipelineStateFunctionIndex;
@property (TI,N,V_encoderIndex) encoderIndex;
@property (TQ,N,V_encoderStateId) encoderStateId;
@property (TQ,N,V_encoderFunctionIndex) encoderFunctionIndex;
@property (TI,N,V_commandBufferIndex) commandBufferIndex;
@property (Ti,N,V_subCommandIndex) subCommandIndex;
@property (T@"DYShaderProfilerProgramInfo",&,N,V_programInfo) programInfo;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_vertexTiming) vertexTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_fragmentTiming) fragmentTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_computeTiming) computeTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_timing) timing;
```

## Instance methods

```
-[DYShaderProfilerDrawCallInfo init];
-[DYShaderProfilerDrawCallInfo timing];
-[DYShaderProfilerDrawCallInfo encoderFunctionIndex];
-[DYShaderProfilerDrawCallInfo setEncoderFunctionIndex:];
-[DYShaderProfilerDrawCallInfo subCommandIndex];
-[DYShaderProfilerDrawCallInfo functionIndex];
-[DYShaderProfilerDrawCallInfo setFunctionIndex:];
-[DYShaderProfilerDrawCallInfo setSubCommandIndex:];
-[DYShaderProfilerDrawCallInfo pipelineStateId];
-[DYShaderProfilerDrawCallInfo setProgramInfo:];
-[DYShaderProfilerDrawCallInfo allShaderKeys];
-[DYShaderProfilerDrawCallInfo commandBufferIndex];
-[DYShaderProfilerDrawCallInfo computeTiming];
-[DYShaderProfilerDrawCallInfo drawCallIndex];
-[DYShaderProfilerDrawCallInfo encoderIndex];
-[DYShaderProfilerDrawCallInfo encoderStateId];
-[DYShaderProfilerDrawCallInfo fragmentTiming];
-[DYShaderProfilerDrawCallInfo pipelineStateFunctionIndex];
-[DYShaderProfilerDrawCallInfo pipelineStateIndex];
-[DYShaderProfilerDrawCallInfo programInfo];
-[DYShaderProfilerDrawCallInfo setAllShaderKeys:];
-[DYShaderProfilerDrawCallInfo setCommandBufferIndex:];
-[DYShaderProfilerDrawCallInfo setDrawCallIndex:];
-[DYShaderProfilerDrawCallInfo setEncoderIndex:];
-[DYShaderProfilerDrawCallInfo setEncoderStateId:];
-[DYShaderProfilerDrawCallInfo setPipelineStateFunctionIndex:];
-[DYShaderProfilerDrawCallInfo setPipelineStateId:];
-[DYShaderProfilerDrawCallInfo setPipelineStateIndex:];
-[DYShaderProfilerDrawCallInfo vertexTiming];
```
