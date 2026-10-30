# `DYShaderProfilerProgramInfo`

- Image: [`/System/Library/PrivateFrameworks/MTLToolsDeviceSupport.framework/MTLToolsDeviceSupport`](../userland/System__Library__PrivateFrameworks__MTLToolsDeviceSupport.framework__MTLToolsDeviceSupport.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 12 properties, 17 instance methods, 0 class methods

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
@"NSMutableArray" _drawCallInfoList;
B _valid;
I _programPipelineIndex;
I _programIndex;
Q _pipelineStateId;
Q _pipelineStateFunctionIndex;
Q _programId;
```

## Properties

```
@property (T@"NSArray",R,N,V_allShaderKeys) allShaderKeys;
@property (TI,N,V_programIndex) programIndex;
@property (TQ,N,V_programId) programId;
@property (TQ,N,V_pipelineStateFunctionIndex) pipelineStateFunctionIndex;
@property (TB,N,V_valid) valid;
@property (TI,R,N,V_programPipelineIndex) programPipelineIndex;
@property (TQ,R,N,V_pipelineStateId) pipelineStateId;
@property (T@"NSMutableArray",R,N,V_drawCallInfoList) drawCallInfoList;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_vertexTiming) vertexTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_fragmentTiming) fragmentTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_computeTiming) computeTiming;
@property (T{DYShaderProfilerTiming={Statistics=ddd}{Statistics=ddd}},R,N,V_timing) timing;
```

## Instance methods

```
-[DYShaderProfilerProgramInfo valid];
-[DYShaderProfilerProgramInfo init];
-[DYShaderProfilerProgramInfo setValid:];
-[DYShaderProfilerProgramInfo timing];
-[DYShaderProfilerProgramInfo programId];
-[DYShaderProfilerProgramInfo setProgramId:];
-[DYShaderProfilerProgramInfo pipelineStateId];
-[DYShaderProfilerProgramInfo allShaderKeys];
-[DYShaderProfilerProgramInfo computeTiming];
-[DYShaderProfilerProgramInfo drawCallInfoList];
-[DYShaderProfilerProgramInfo fragmentTiming];
-[DYShaderProfilerProgramInfo pipelineStateFunctionIndex];
-[DYShaderProfilerProgramInfo programIndex];
-[DYShaderProfilerProgramInfo programPipelineIndex];
-[DYShaderProfilerProgramInfo setPipelineStateFunctionIndex:];
-[DYShaderProfilerProgramInfo setProgramIndex:];
-[DYShaderProfilerProgramInfo vertexTiming];
```
