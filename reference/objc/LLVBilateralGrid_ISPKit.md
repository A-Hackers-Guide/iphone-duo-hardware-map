# `LLVBilateralGrid`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 0 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<MTLTexture>" _grid_tex;
@"<MTLBuffer>" _uniforms;
@"FigMetalContext" _metal;
B _useMetalAllocator;
@"LLVBilateralGridShaders" _shaders;
B _normalizeGridConfidence;
i _space_sigma;
f _range_sigma;
Q _input_width;
Q _input_height;
i _grid_width;
i _grid_height;
i _grid_depth;
@"<MTLTexture>" _tmp_grid_tex;
@"<MTLBuffer>" _max_grid_confidence;
@"<MTLTexture>" _bistochast_m_tex;
@"<MTLTexture>" _bistochast_n_tex;
@"<MTLTexture>" _A_tex;
@"<MTLTexture>" _x0_tex;
@"<MTLTexture>" _x1_tex;
@"<MTLTexture>" _residual0_tex;
@"<MTLTexture>" _residual1_tex;
@"<MTLTexture>" _confidence_solved_tex;
@"<MTLTexture>" _d0_tex;
@"<MTLTexture>" _d1_tex;
@"<MTLTexture>" _q_tex;
@"<MTLBuffer>" _l0_buf;
@"<MTLBuffer>" _l1_buf;
@"<MTLBuffer>" _alpha_buf;
@"<MTLBuffer>" _residual_buf;
@"<MTLBuffer>" _hasconverged_buf;
@"NSObject<OS_os_log>" _logger;
```

## Class methods

```
+[LLVBilateralGrid prewarmShaders:];
```

## Instance methods

```
-[LLVBilateralGrid initWithContext:];
-[LLVBilateralGrid dealloc];
-[LLVBilateralGrid releaseTextures];
-[LLVBilateralGrid allocateTextures];
-[LLVBilateralGrid allocGridTexture:label:];
-[LLVBilateralGrid blurAndNormalize:grid_tmp_tex:commandBuffer:];
-[LLVBilateralGrid buildWithGuideAndConfidence:target:confidence:grid_tex:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:commandBuffer:];
-[LLVBilateralGrid config:height:space_sigma:range_sigma:solver:];
-[LLVBilateralGrid filter:output:commandBuffer:];
-[LLVBilateralGrid initWithContext:normalizeGridConfidence:];
-[LLVBilateralGrid initWithDevice:normalizeGridConfidence:];
-[LLVBilateralGrid jointfilter:target:output:commandBuffer:];
-[LLVBilateralGrid setupWithConfig:width:height:];
-[LLVBilateralGrid solverBistochastize:commandBuffer:];
-[LLVBilateralGrid solverPcg:commandBuffer:];
-[LLVBilateralGrid solverfilter:target:confidence:output:commandBuffer:];
-[LLVBilateralGrid solverfilterWithGuide:target:confidence:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:commandBuffer:];
-[LLVBilateralGrid solverfilterWithGuide:target:confidence:output:commandBuffer:];
-[LLVBilateralGrid upsample:grid_tex:conf_tex:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:commandBuffer:];
```
