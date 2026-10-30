# `MTLFXSpatialScalerBase` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 19 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) colorTextureUsage;
@property (TQ,R,N) outputTextureUsage;
@property (TQ,N) inputContentWidth;
@property (TQ,N) inputContentHeight;
@property (T@"<MTLTexture>",&,N) colorTexture;
@property (T@"<MTLTexture>",&,N) outputTexture;
@property (TQ,R,N) colorTextureFormat;
@property (TQ,R,N) outputTextureFormat;
@property (TQ,R,N) inputWidth;
@property (TQ,R,N) inputHeight;
@property (TQ,R,N) outputWidth;
@property (TQ,R,N) outputHeight;
@property (Tq,R,N) colorProcessingMode;
@property (T@"<MTLFence>",&,N) fence;
```

## Instance methods

```
-[MTLFXSpatialScalerBase outputHeight];
-[MTLFXSpatialScalerBase setOutputTexture:];
-[MTLFXSpatialScalerBase outputTexture];
-[MTLFXSpatialScalerBase outputWidth];
-[MTLFXSpatialScalerBase inputHeight];
-[MTLFXSpatialScalerBase inputWidth];
-[MTLFXSpatialScalerBase setColorTexture:];
-[MTLFXSpatialScalerBase colorTexture];
-[MTLFXSpatialScalerBase colorProcessingMode];
-[MTLFXSpatialScalerBase colorTextureFormat];
-[MTLFXSpatialScalerBase colorTextureUsage];
-[MTLFXSpatialScalerBase fence];
-[MTLFXSpatialScalerBase inputContentHeight];
-[MTLFXSpatialScalerBase inputContentWidth];
-[MTLFXSpatialScalerBase outputTextureFormat];
-[MTLFXSpatialScalerBase outputTextureUsage];
-[MTLFXSpatialScalerBase setFence:];
-[MTLFXSpatialScalerBase setInputContentHeight:];
-[MTLFXSpatialScalerBase setInputContentWidth:];
```
