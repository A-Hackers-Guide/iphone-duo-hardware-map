# `BRNet4_1`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"<MTLDevice>" device_;
{BRNetDescriptor="version"i"image_width"I"image_height"I"input_width"I"input_height"I"input_channels"I"input_unshuffle_ratio"I"unshuffle_width"I"unshuffle_height"I"unshuffle_channels"I"output_shuffle_ratio"I"output_width"I"output_height"I"output_channels"I"tensorDataLayout"Q"weight_file"@"NSString"} desc_;
@"Conv12x12Stride4" conv12x12_;
@"ConvKxKStride2" conv3x3Stride2_1_;
@"ConvKxKStride2" conv3x3Stride2_2_;
@"ConvKxKStride2" conv3x3Stride2_3_;
@"Conv1x1FusedBilinear" conv1x1Fused_1_;
@"Conv1x1FusedBilinear" conv1x1Fused_2_;
@"Conv1x1FusedBilinear" conv1x1Fused_3_;
@"Conv1x1FusedBilinear" conv1x1Fused_4_;
@"Conv3x3Stride1" conv3x3Sigmoid_;
@"<MTLBuffer>" bufSkip0_;
@"<MTLBuffer>" bufSkip1_;
@"<MTLBuffer>" bufSkip2_;
@"<MTLBuffer>" bufInterm0_;
@"<MTLBuffer>" bufInterm1_;
@"<MTL4ArgumentTable>" mtl4ArgTable_;
```

## Class methods

```
+[BRNet4_1 intermediateBufferSizesForDescriptor:];
```

## Instance methods

```
-[BRNet4_1 initWithDevice:descriptor:];
-[BRNet4_1 printDescriptor];
-[BRNet4_1 executeWithCommandBuffer:feed:target:];
-[BRNet4_1 executeWithCommandBuffer:feed:target:intermediates:];
-[BRNet4_1 executeWithMTL4CommandBuffer:feed:target:];
-[BRNet4_1 initWithDevice:library:descriptor:];
-[BRNet4_1 setupBuffersAndTensors];
-[BRNet4_1 setupModelWithLibrary:];
```
