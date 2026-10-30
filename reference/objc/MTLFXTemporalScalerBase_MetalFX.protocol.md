# `MTLFXTemporalScalerBase` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLFXFrameInterpolatableScaler`
- 0 instance variables, 43 properties, 69 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) colorTextureUsage;
@property (TQ,R,N) depthTextureUsage;
@property (TQ,R,N) motionTextureUsage;
@property (TQ,R,N) reactiveMaskTextureUsage;
@property (TQ,R,N) reactiveTextureUsage;
@property (TQ,R,N) outputTextureUsage;
@property (TQ,N) inputContentWidth;
@property (TQ,N) inputContentHeight;
@property (TQ,N) colorContentOffsetX;
@property (TQ,N) colorContentOffsetY;
@property (TQ,N) depthContentOffsetX;
@property (TQ,N) depthContentOffsetY;
@property (TQ,N) motionContentOffsetX;
@property (TQ,N) motionContentOffsetY;
@property (TQ,N) reactiveMaskContentOffsetX;
@property (TQ,N) reactiveMaskContentOffsetY;
@property (TQ,N) outputOffsetX;
@property (TQ,N) outputOffsetY;
@property (T@"<MTLTexture>",&,N) colorTexture;
@property (T@"<MTLTexture>",&,N) depthTexture;
@property (T@"<MTLTexture>",&,N) motionTexture;
@property (T@"<MTLTexture>",&,N) outputTexture;
@property (T@"<MTLTexture>",&,N) exposureTexture;
@property (T@"<MTLTexture>",&,N) reactiveMaskTexture;
@property (Tf,N) preExposure;
@property (Tf,N) jitterOffsetX;
@property (Tf,N) jitterOffsetY;
@property (Tf,N) motionVectorScaleX;
@property (Tf,N) motionVectorScaleY;
@property (TB,N) reset;
@property (TB,N,GisDepthReversed) depthReversed;
@property (TQ,R,N) colorTextureFormat;
@property (TQ,R,N) depthTextureFormat;
@property (TQ,R,N) motionTextureFormat;
@property (TQ,R,N) reactiveMaskTextureFormat;
@property (TQ,R,N) outputTextureFormat;
@property (TQ,R,N) inputWidth;
@property (TQ,R,N) inputHeight;
@property (TQ,R,N) outputWidth;
@property (TQ,R,N) outputHeight;
@property (Tf,R,N) inputContentMinScale;
@property (Tf,R,N) inputContentMaxScale;
@property (T@"<MTLFence>",&,N) fence;
```

## Instance methods

```
-[MTLFXTemporalScalerBase outputHeight];
-[MTLFXTemporalScalerBase setReset:];
-[MTLFXTemporalScalerBase reset];
-[MTLFXTemporalScalerBase setOutputTexture:];
-[MTLFXTemporalScalerBase outputTexture];
-[MTLFXTemporalScalerBase outputWidth];
-[MTLFXTemporalScalerBase inputHeight];
-[MTLFXTemporalScalerBase inputWidth];
-[MTLFXTemporalScalerBase depthTexture];
-[MTLFXTemporalScalerBase setColorTexture:];
-[MTLFXTemporalScalerBase setDepthReversed:];
-[MTLFXTemporalScalerBase setDepthTexture:];
-[MTLFXTemporalScalerBase setJitterOffsetX:];
-[MTLFXTemporalScalerBase setJitterOffsetY:];
-[MTLFXTemporalScalerBase setMotionTexture:];
-[MTLFXTemporalScalerBase setMotionVectorScaleX:];
-[MTLFXTemporalScalerBase setMotionVectorScaleY:];
-[MTLFXTemporalScalerBase colorTexture];
-[MTLFXTemporalScalerBase setPreExposure:];
-[MTLFXTemporalScalerBase exposureTexture];
-[MTLFXTemporalScalerBase isDepthReversed];
-[MTLFXTemporalScalerBase colorContentOffsetX];
-[MTLFXTemporalScalerBase colorContentOffsetY];
-[MTLFXTemporalScalerBase colorTextureFormat];
-[MTLFXTemporalScalerBase colorTextureUsage];
-[MTLFXTemporalScalerBase depthContentOffsetX];
-[MTLFXTemporalScalerBase depthContentOffsetY];
-[MTLFXTemporalScalerBase depthTextureFormat];
-[MTLFXTemporalScalerBase depthTextureUsage];
-[MTLFXTemporalScalerBase fence];
-[MTLFXTemporalScalerBase inputContentHeight];
-[MTLFXTemporalScalerBase inputContentMaxScale];
-[MTLFXTemporalScalerBase inputContentMinScale];
-[MTLFXTemporalScalerBase inputContentWidth];
-[MTLFXTemporalScalerBase jitterOffsetX];
-[MTLFXTemporalScalerBase jitterOffsetY];
-[MTLFXTemporalScalerBase motionContentOffsetX];
-[MTLFXTemporalScalerBase motionContentOffsetY];
-[MTLFXTemporalScalerBase motionTexture];
-[MTLFXTemporalScalerBase motionTextureFormat];
-[MTLFXTemporalScalerBase motionTextureUsage];
-[MTLFXTemporalScalerBase motionVectorScaleX];
-[MTLFXTemporalScalerBase motionVectorScaleY];
-[MTLFXTemporalScalerBase outputOffsetX];
-[MTLFXTemporalScalerBase outputOffsetY];
-[MTLFXTemporalScalerBase outputTextureFormat];
-[MTLFXTemporalScalerBase outputTextureUsage];
-[MTLFXTemporalScalerBase preExposure];
-[MTLFXTemporalScalerBase reactiveMaskContentOffsetX];
-[MTLFXTemporalScalerBase reactiveMaskContentOffsetY];
-[MTLFXTemporalScalerBase reactiveMaskTexture];
-[MTLFXTemporalScalerBase reactiveMaskTextureFormat];
-[MTLFXTemporalScalerBase reactiveMaskTextureUsage];
-[MTLFXTemporalScalerBase reactiveTextureUsage];
-[MTLFXTemporalScalerBase setColorContentOffsetX:];
-[MTLFXTemporalScalerBase setColorContentOffsetY:];
-[MTLFXTemporalScalerBase setDepthContentOffsetX:];
-[MTLFXTemporalScalerBase setDepthContentOffsetY:];
-[MTLFXTemporalScalerBase setExposureTexture:];
-[MTLFXTemporalScalerBase setFence:];
-[MTLFXTemporalScalerBase setInputContentHeight:];
-[MTLFXTemporalScalerBase setInputContentWidth:];
-[MTLFXTemporalScalerBase setMotionContentOffsetX:];
-[MTLFXTemporalScalerBase setMotionContentOffsetY:];
-[MTLFXTemporalScalerBase setOutputOffsetX:];
-[MTLFXTemporalScalerBase setOutputOffsetY:];
-[MTLFXTemporalScalerBase setReactiveMaskContentOffsetX:];
-[MTLFXTemporalScalerBase setReactiveMaskContentOffsetY:];
-[MTLFXTemporalScalerBase setReactiveMaskTexture:];
```
