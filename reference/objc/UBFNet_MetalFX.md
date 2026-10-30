# `UBFNet`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<MTLDevice>" device_;
@"<MTLResidencySet>" residencySet_;
{UBFNetDescriptor="version"i"image_width"I"image_height"I"input_width"I"input_height"I"input_channels"I"input_unshuffle_ratio"I"unshuffle_width"I"unshuffle_height"I"unshuffle_channels"I"output_shuffle_ratio"I"output_width"I"output_height"I"output_channels"I"up_channels"I"layers_channels"[4I]} desc_;
@"<MTL4ArgumentTable>" sharedArgTable_;
@"ConvKxKStride2" e0_;
@"ConvKxKStride2" e1_;
@"ConvKxKStride2" e2_;
@"ConvKxKStride2" e3_;
@"ConvKxKStride2" e4_;
@"MaxPoolConv" bottleneck_;
@"MaxPoolConv" u1_;
@"MaxPoolConv" u2_;
@"MaxPoolConv" u3ab_;
@"MaxPoolConv" u3c_;
@"Conv3x3Stride1" head_;
@"<MTLBuffer>" buf0_;
@"<MTLBuffer>" buf1_;
@"<MTLBuffer>" skipA_;
@"<MTLBuffer>" skipB_;
@"<MTLBuffer>" skipC_;
```

## Class methods

```
+[UBFNet intermediateBufferSizesForDescriptor:];
```

## Instance methods

```
-[UBFNet initWithDevice:descriptor:];
-[UBFNet printDescriptor];
-[UBFNet executeWithCommandBuffer:feed:target:];
-[UBFNet executeWithCommandBuffer:feed:target:intermediates:];
-[UBFNet executeWithMTL4CommandBuffer:feed:target:fence:];
-[UBFNet initWithDevice:library:descriptor:];
-[UBFNet initWithDevice:library:descriptor:residencySet:];
-[UBFNet setupBuffers];
-[UBFNet setupModelWithLibrary:];
```
