# `sBBRNet`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" device_;
{BBRNetDescriptor="version"i"image_width"I"image_height"I"tDesc"{tBBRNetDescriptor="input_width"I"input_height"I"input_channels"I"output_width"I"output_height"I"output_channels"I"weight_file"@"NSString""weight_file_nq"@"NSString""weight_layout"i"inputIsQuantized"B"inputIsNCHW"B"outputNCHW"B"outputIsQuantized"B"headProducesTextures"B}"sDesc"{sBBRNetDescriptor="input_width"I"input_height"I"input_channels"I"output_width"I"output_height"I"output_channels"I"weight_file"@"NSString""weight_layout"i"inputIsFP16"B"inputIsNCHW"B"outputIsFP16"B"outputIsNCHW"B"NmatsHW"S"nsimd_per_tg"S"fp16Intermediate"B}} desc_;
@"SBBRNet_MLP" mlpOp_;
```

## Instance methods

```
-[sBBRNet initWithDevice:descriptor:];
-[sBBRNet executeWithCommandBuffer:feed:target:];
-[sBBRNet executeWithMTL4CommandBuffer:feed:target:fence:];
-[sBBRNet initWithDevice:library:descriptor:];
-[sBBRNet initWithDevice:library:descriptor:residencySet:];
```
