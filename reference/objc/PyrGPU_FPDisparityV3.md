# `PyrGPU`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 5 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _mtlContext;
@"<MTLCommandQueue>" _commandQueue;
[2@"<MTLComputePipelineState>"] _computePipelines;
[3[3@"<MTLComputePipelineState>"]] _KernelDownscaleImage1;
{CGSize="width"d"height"d} _input_res;
{CGSize="width"d"height"d} _max_input_res;
[32{?="real_res"{CGSize="width"d"height"d}"kernel_filter"i"scaling_factor""resampling_factor""idx_ref"i"use_antialiasing"B}] _pyrInfoArray;
[32{CGSize="width"d"height"d}] _pyr_int_dims;
[32{CGSize="width"d"height"d}] _pyr_real_dims;
[32^{__CVBuffer}] _pyr_pxbuf;
[32@"<MTLTexture>"] _pyr_tex;
[32@"<MTLTexture>"] _pyr_u32_alias_tex;
[2^{__CVBuffer}] _antialiasing_pxbuf;
B _isValid;
B _useAntialiasingForDownsamplingToFinestResolution;
i _countScales;
```

## Properties

```
@property (TB,R,N,V_isValid) isValid;
@property (Ti,R,N,V_countScales) countScales;
@property (T^{CGSize=dd},R,N) pyramidDimensions;
@property (T^{CGSize=dd},R,N) realPyramidDimensions;
@property (TB,N,V_useAntialiasingForDownsamplingToFinestResolution) useAntialiasingForDownsamplingToFinestResolution;
```

## Class methods

```
+[PyrGPU _determineFilterFromResolution:toResolution:];
```

## Instance methods

```
-[PyrGPU releaseResources];
-[PyrGPU dealloc];
-[PyrGPU isValid];
-[PyrGPU initWithMetalContext:];
-[PyrGPU _setupPipelines];
-[PyrGPU _createTextureViewsFromResolution:];
-[PyrGPU _doRPDDownscale1WithCommandBuffer:in_tex:out_tex:scaling_factor:];
-[PyrGPU _downscale2XBelowWithCommandBuffer:in_tex:out_tex:scaling_factor:];
-[PyrGPU _downscaleAntialiasingWithCommandBuffer:in_tex:out_tex:in_ref_res:out_ref_res:];
-[PyrGPU allocateResourcesWithMaxInputResolution:];
-[PyrGPU countScales];
-[PyrGPU doImagePyramidWithCommandBuffer:in_tex:];
-[PyrGPU populatePyramidSchemeFromReference:inputResolution:];
-[PyrGPU populatePyramidSchemeFromResolution:toResolution:scalingFactor:scales:allowSuccessiveDownscale2x:];
-[PyrGPU pyramidDimensions];
-[PyrGPU realPyramidDimensions];
-[PyrGPU setUseAntialiasingForDownsamplingToFinestResolution:];
-[PyrGPU textureRGBAU8AtScale:];
-[PyrGPU textureU32AliasAtScale:];
-[PyrGPU useAntialiasingForDownsamplingToFinestResolution];
-[PyrGPU downscale2XEqualWithCommandBuffer:in_u32_alias_tex:out_u32_alias_tex:];
```
