# `tBBRNet`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 0 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"<MTLDevice>" device_;
@"<MTLResidencySet>" residencySet_;
{BBRNetDescriptor="version"i"image_width"I"image_height"I"tDesc"{tBBRNetDescriptor="input_width"I"input_height"I"input_channels"I"output_width"I"output_height"I"output_channels"I"weight_file"@"NSString""weight_file_nq"@"NSString""weight_layout"i"inputIsQuantized"B"inputIsNCHW"B"outputNCHW"B"outputIsQuantized"B"headProducesTextures"B}"sDesc"{sBBRNetDescriptor="input_width"I"input_height"I"input_channels"I"output_width"I"output_height"I"output_channels"I"weight_file"@"NSString""weight_layout"i"inputIsFP16"B"inputIsNCHW"B"outputIsFP16"B"outputIsNCHW"B"NmatsHW"S"nsimd_per_tg"S"fp16Intermediate"B}} desc_;
@"<MTL4ArgumentTable>" sharedArgTable_;
@"Conv3x3Stride1" conv3x3s1_step1_;
@"Conv3x3Stride2" conv3x3s2_step2_;
@"Conv3x3Stride2" conv3x3s2_step3_;
@"Conv3x3Stride2" conv3x3s2_step4_;
@"Conv3x3Stride1" conv3x3s1_step5_;
@"Conv3x3Stride1" conv3x3s1_step6_;
@"Conv3x3Stride1" conv3x3s1_step7_;
@"Conv3x3Stride1" conv3x3s1_step8_;
@"Conv3x3Stride1" conv3x3s1_step9_;
@"Conv3x3Stride1" conv3x3s1_step10_;
@"Conv3x3Stride1" conv3x3s1_step11_;
@"<MTLBuffer>" buf0_;
@"<MTLBuffer>" buf1_;
@"<MTLBuffer>" skipEnc0_;
@"<MTLBuffer>" skipEnc1_;
@"<MTLBuffer>" skipEnc2_;
@"<MTLTexture>" texDec1_;
@"<MTLTexture>" texDec2_;
@"<MTLTexture>" texDec3_;
B useTextureIntermediate_;
B useSplitInput_;
{IntermediateStorage="buffer"@"<MTLBuffer>""texture"@"<MTLTexture>"} dec1Storage_;
{IntermediateStorage="buffer"@"<MTLBuffer>""texture"@"<MTLTexture>"} dec2Storage_;
{IntermediateStorage="buffer"@"<MTLBuffer>""texture"@"<MTLTexture>"} dec3Storage_;
```

## Class methods

```
+[tBBRNet intermediateBufferSizesForDescriptor:];
```

## Instance methods

```
-[tBBRNet initWithDevice:descriptor:];
-[tBBRNet printDescriptor];
-[tBBRNet executeWithCommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:];
-[tBBRNet executeWithCommandBuffer:feed:target:];
-[tBBRNet executeWithCommandBuffer:feed:target:intermediates:];
-[tBBRNet executeWithCommandBuffer:feed:target:temporalTex:rnnTex:];
-[tBBRNet executeWithCommandBuffer:feedU8:feedF16:target:intermediates:];
-[tBBRNet executeWithCommandBuffer:feedU8:feedF16:target:temporalTex:rnnTex:intermediates:];
-[tBBRNet executeWithMTL4CommandBuffer:feed:feedU8:feedF16:target:temporalTex:rnnTex:fence:];
-[tBBRNet executeWithMTL4CommandBuffer:feed:target:fence:];
-[tBBRNet executeWithMTL4CommandBuffer:feed:target:temporalTex:rnnTex:fence:];
-[tBBRNet executeWithMTL4CommandBuffer:feedU8:feedF16:target:fence:];
-[tBBRNet executeWithMTL4CommandBuffer:feedU8:feedF16:target:temporalTex:rnnTex:fence:];
-[tBBRNet initWithDevice:library:descriptor:];
-[tBBRNet initWithDevice:library:descriptor:residencySet:];
-[tBBRNet setupBuffers];
-[tBBRNet setupModelWithLibrary:];
```
