# `HBFGPU`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _mtlContext;
@"<MTLCommandQueue>" _commandQueue;
[5@"<MTLComputePipelineState>"] _computePipelines;
Q _maxThreadExecutionWidth;
@"<MTLBuffer>" _res_off_buf;
@"HBFGPUParameters" _params;
```

## Properties

```
@property (T@"HBFGPUParameters",N,V_params) params;
```

## Instance methods

```
-[HBFGPU waitUntilCompleted];
-[HBFGPU params];
-[HBFGPU dealloc];
-[HBFGPU setParams:];
-[HBFGPU initWithMetalContext:];
-[HBFGPU _setupPipelines];
-[HBFGPU releaseResouces];
-[HBFGPU _doBuildErrorMapWithCommandBuffer:in_res_tex:out_tex:];
-[HBFGPU _doComputeResidualErrorOffsetWithCommandBuffer:in_res_tex:];
-[HBFGPU _doComputeResidualErrorWithCommandBuffer:in_I0_u32_tex:in_I1_tex:in_uv_tex:out_tex:disparity_axis:];
-[HBFGPU _doOcclusionHandlingWithCommandBuffer:in_uv_old_tex:in_uv_new_tex:in_I0_u32_tex:in_I1_tex:out_tex:disparity_axis:disparity_scaling_factor:];
-[HBFGPU doFilterWithCommandBuffer:in_I0_u32_tex:in_I1_tex:in_uv_tex:out_uv_tex:tmp_res_tex:tmp_err_tex:tmp_uv0_tex:tmp_uv1_tex:needToComputeResidualOffset:disparity_axis:disparity_scaling_factor:];
-[HBFGPU doFilterWithCommandBuffer:in_I_tex:in_J_u32_tex:in_W_tex:out_tex:disparity_scaling_factor:];
```
