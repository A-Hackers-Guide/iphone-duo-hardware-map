# `TVL1_v3`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _mtlContext;
@"<MTLCommandQueue>" _commandQueue;
[5@"<MTLComputePipelineState>"] _computePipelines;
^{__CVBuffer=} _R_a_pxbuf;
[32@"<MTLTexture>"] _R_a_tex;
^{__CVBuffer=} _R_d_pxbuf;
[32@"<MTLTexture>"] _R_d_tex;
^{__CVBuffer=} _R_b_pxbuf;
[32@"<MTLTexture>"] _R_b_tex;
[2^{__CVBuffer}] _p_pxbuf;
[32[2@"<MTLTexture>"]] _p_tex;
[2^{__CVBuffer}] _uv_relax_pxbuf;
[32[2@"<MTLTexture>"]] _uv_relax_tex;
[2^{__CVBuffer}] _uv_pxbuf;
[32[2@"<MTLTexture>"]] _uv_tex;
@"<MTLTexture>" _uv_tex_user_ref;
B _isValid;
i _countScales;
@"PyrGPU" _pyramidReference;
{CGSize="width"d"height"d} _outputDisparityResolution;
```

## Properties

```
@property (TB,R,N,V_isValid) isValid;
@property (Ti,R,N,V_countScales) countScales;
@property (T{CGSize=dd},R,N,V_outputDisparityResolution) outputDisparityResolution;
@property (T@"PyrGPU",&,N,V_pyramidReference) pyramidReference;
```

## Instance methods

```
-[TVL1_v3 releaseResources];
-[TVL1_v3 dealloc];
-[TVL1_v3 isValid];
-[TVL1_v3 allocateResources];
-[TVL1_v3 initWithMetalContext:];
-[TVL1_v3 _setupBuffer];
-[TVL1_v3 _setupPipelines];
-[TVL1_v3 countScales];
-[TVL1_v3 doLocalRegularizationWithCommandBuffer:in_tex:level:parameters:];
-[TVL1_v3 _doUpscaleDualWithCommandBuffer:in_tex:out_tex:];
-[TVL1_v3 _doUpscaleSingleWithCommandBuffer:in_tex:out_tex:coeff:];
-[TVL1_v3 _setupTexture];
-[TVL1_v3 doInitPrimalDualWithCommandBuffer:disparity_value:idx_swap_uv:idx_swap_p:level:];
-[TVL1_v3 doSolveChambollePrimalDualWithCommandBuffer:idx_swap_uv_in_out:idx_swap_p_in_out:in_res_tes:in_hes_tes:out_uv_tex:level:iterations:box_cstr_range:disparity_scaling_factor:parameters:];
-[TVL1_v3 doUpscalePrimalDualWithCommandBuffer:idx_swap_uv_in_out:idx_swap_p_in_out:level:coeff:];
-[TVL1_v3 outputDisparityResolution];
-[TVL1_v3 pyramidReference];
-[TVL1_v3 setPyramidReference:];
-[TVL1_v3 texturePAtLevel:idx_swap_p:];
-[TVL1_v3 textureRaAtLevel:];
-[TVL1_v3 textureRbAtLevel:];
-[TVL1_v3 textureRdAtLevel:];
-[TVL1_v3 textureUVAtLevel:idx_swap_uv:];
-[TVL1_v3 textureUVRelaxAtLevel:idx_swap_uv:];
```
