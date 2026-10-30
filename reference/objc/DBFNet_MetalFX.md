# `DBFNet`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<MTLDevice>" device_;
@"<MTLResidencySet>" residencySet_;
{DBFNetDescriptor="version"i"image_width"I"image_height"I"input_width"I"input_height"I"input_channels"I"output_width"I"output_height"I"output_channels"I"input_padding"I} desc_;
@"<MTL4ArgumentTable>" sharedArgTable_;
@"MaxPoolConv" cellE1_;
@"MaxPoolConv" cellE2_;
@"MaxPoolConv" cellE3_;
@"MaxPoolConv" cellE4_;
@"MaxPoolConv" cellD1_;
@"MaxPoolConv" cellD2_;
@"MaxPoolConv" cellD3_;
@"<MTLBuffer>" buf0_;
@"<MTLBuffer>" buf1_;
@"<MTLBuffer>" skipL2_;
@"<MTLBuffer>" skipL4_;
@"<MTLBuffer>" skipL6_;
```

## Class methods

```
+[DBFNet intermediateBufferSizesForDescriptor:];
```

## Instance methods

```
-[DBFNet initWithDevice:descriptor:];
-[DBFNet printDescriptor];
-[DBFNet executeWithCommandBuffer:feed:target:];
-[DBFNet executeWithCommandBuffer:feed:target:intermediates:];
-[DBFNet executeWithMTL4CommandBuffer:feed:target:fence:];
-[DBFNet initWithDevice:library:descriptor:];
-[DBFNet initWithDevice:library:descriptor:residencySet:];
-[DBFNet setupBuffers];
-[DBFNet setupModelWithLibrary:];
```
