# `MTLFXTemporalDenoisedScalerBase` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLFXFrameInterpolatableScaler`
- 0 instance variables, 54 properties, 77 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) colorTextureUsage;
@property (TQ,R,N) depthTextureUsage;
@property (TQ,R,N) motionTextureUsage;
@property (TQ,R,N) reactiveMaskTextureUsage;
@property (TQ,R,N) reactiveTextureUsage;
@property (TQ,R,N) diffuseAlbedoTextureUsage;
@property (TQ,R,N) specularAlbedoTextureUsage;
@property (TQ,R,N) normalTextureUsage;
@property (TQ,R,N) roughnessTextureUsage;
@property (TQ,R,N) specularHitDistanceTextureUsage;
@property (TQ,R,N) denoiseStrengthMaskTextureUsage;
@property (TQ,R,N) transparencyOverlayTextureUsage;
@property (TQ,R,N) outputTextureUsage;
@property (T@"<MTLTexture>",&,N) colorTexture;
@property (T@"<MTLTexture>",&,N) depthTexture;
@property (T@"<MTLTexture>",&,N) motionTexture;
@property (T@"<MTLTexture>",&,N) diffuseAlbedoTexture;
@property (T@"<MTLTexture>",&,N) specularAlbedoTexture;
@property (T@"<MTLTexture>",&,N) normalTexture;
@property (T@"<MTLTexture>",&,N) roughnessTexture;
@property (T@"<MTLTexture>",&,N) specularHitDistanceTexture;
@property (T@"<MTLTexture>",&,N) denoiseStrengthMaskTexture;
@property (T@"<MTLTexture>",&,N) transparencyOverlayTexture;
@property (T@"<MTLTexture>",&,N) outputTexture;
@property (T@"<MTLTexture>",&,N) exposureTexture;
@property (Tf,N) preExposure;
@property (T@"<MTLTexture>",&,N) reactiveMaskTexture;
@property (Tf,N) jitterOffsetX;
@property (Tf,N) jitterOffsetY;
@property (Tf,N) motionVectorScaleX;
@property (Tf,N) motionVectorScaleY;
@property (TB,N) shouldResetHistory;
@property (TB,N,GisDepthReversed) depthReversed;
@property (TQ,R,N) colorTextureFormat;
@property (TQ,R,N) depthTextureFormat;
@property (TQ,R,N) motionTextureFormat;
@property (TQ,R,N) diffuseAlbedoTextureFormat;
@property (TQ,R,N) specularAlbedoTextureFormat;
@property (TQ,R,N) normalTextureFormat;
@property (TQ,R,N) roughnessTextureFormat;
@property (TQ,R,N) specularHitDistanceTextureFormat;
@property (TQ,R,N) denoiseStrengthMaskTextureFormat;
@property (TQ,R,N) transparencyOverlayTextureFormat;
@property (TQ,R,N) reactiveMaskTextureFormat;
@property (TQ,R,N) outputTextureFormat;
@property (TQ,R,N) inputWidth;
@property (TQ,R,N) inputHeight;
@property (TQ,R,N) outputWidth;
@property (TQ,R,N) outputHeight;
@property (Tf,R,N) inputContentMinScale;
@property (Tf,R,N) inputContentMaxScale;
@property (T{?=[4]},N) worldToViewMatrix;
@property (T{?=[4]},N) viewToClipMatrix;
@property (T@"<MTLFence>",&,N) fence;
```

## Instance methods

```
-[MTLFXTemporalDenoisedScalerBase outputHeight];
-[MTLFXTemporalDenoisedScalerBase setOutputTexture:];
-[MTLFXTemporalDenoisedScalerBase outputTexture];
-[MTLFXTemporalDenoisedScalerBase outputWidth];
-[MTLFXTemporalDenoisedScalerBase inputHeight];
-[MTLFXTemporalDenoisedScalerBase inputWidth];
-[MTLFXTemporalDenoisedScalerBase depthTexture];
-[MTLFXTemporalDenoisedScalerBase setColorTexture:];
-[MTLFXTemporalDenoisedScalerBase setDepthReversed:];
-[MTLFXTemporalDenoisedScalerBase setDepthTexture:];
-[MTLFXTemporalDenoisedScalerBase setDiffuseAlbedoTexture:];
-[MTLFXTemporalDenoisedScalerBase setJitterOffsetX:];
-[MTLFXTemporalDenoisedScalerBase setJitterOffsetY:];
-[MTLFXTemporalDenoisedScalerBase setMotionTexture:];
-[MTLFXTemporalDenoisedScalerBase setMotionVectorScaleX:];
-[MTLFXTemporalDenoisedScalerBase setMotionVectorScaleY:];
-[MTLFXTemporalDenoisedScalerBase setNormalTexture:];
-[MTLFXTemporalDenoisedScalerBase setRoughnessTexture:];
-[MTLFXTemporalDenoisedScalerBase setSpecularAlbedoTexture:];
-[MTLFXTemporalDenoisedScalerBase setSpecularHitDistanceTexture:];
-[MTLFXTemporalDenoisedScalerBase setViewToClipMatrix:];
-[MTLFXTemporalDenoisedScalerBase setWorldToViewMatrix:];
-[MTLFXTemporalDenoisedScalerBase colorTexture];
-[MTLFXTemporalDenoisedScalerBase setPreExposure:];
-[MTLFXTemporalDenoisedScalerBase specularHitDistanceTextureUsage];
-[MTLFXTemporalDenoisedScalerBase transparencyOverlayTextureUsage];
-[MTLFXTemporalDenoisedScalerBase denoiseStrengthMaskTextureUsage];
-[MTLFXTemporalDenoisedScalerBase exposureTexture];
-[MTLFXTemporalDenoisedScalerBase isDepthReversed];
-[MTLFXTemporalDenoisedScalerBase colorTextureFormat];
-[MTLFXTemporalDenoisedScalerBase colorTextureUsage];
-[MTLFXTemporalDenoisedScalerBase denoiseStrengthMaskTexture];
-[MTLFXTemporalDenoisedScalerBase denoiseStrengthMaskTextureFormat];
-[MTLFXTemporalDenoisedScalerBase depthTextureFormat];
-[MTLFXTemporalDenoisedScalerBase depthTextureUsage];
-[MTLFXTemporalDenoisedScalerBase diffuseAlbedoTexture];
-[MTLFXTemporalDenoisedScalerBase diffuseAlbedoTextureFormat];
-[MTLFXTemporalDenoisedScalerBase diffuseAlbedoTextureUsage];
-[MTLFXTemporalDenoisedScalerBase fence];
-[MTLFXTemporalDenoisedScalerBase inputContentMaxScale];
-[MTLFXTemporalDenoisedScalerBase inputContentMinScale];
-[MTLFXTemporalDenoisedScalerBase jitterOffsetX];
-[MTLFXTemporalDenoisedScalerBase jitterOffsetY];
-[MTLFXTemporalDenoisedScalerBase motionTexture];
-[MTLFXTemporalDenoisedScalerBase motionTextureFormat];
-[MTLFXTemporalDenoisedScalerBase motionTextureUsage];
-[MTLFXTemporalDenoisedScalerBase motionVectorScaleX];
-[MTLFXTemporalDenoisedScalerBase motionVectorScaleY];
-[MTLFXTemporalDenoisedScalerBase normalTexture];
-[MTLFXTemporalDenoisedScalerBase normalTextureFormat];
-[MTLFXTemporalDenoisedScalerBase normalTextureUsage];
-[MTLFXTemporalDenoisedScalerBase outputTextureFormat];
-[MTLFXTemporalDenoisedScalerBase outputTextureUsage];
-[MTLFXTemporalDenoisedScalerBase preExposure];
-[MTLFXTemporalDenoisedScalerBase reactiveMaskTexture];
-[MTLFXTemporalDenoisedScalerBase reactiveMaskTextureFormat];
-[MTLFXTemporalDenoisedScalerBase reactiveMaskTextureUsage];
-[MTLFXTemporalDenoisedScalerBase reactiveTextureUsage];
-[MTLFXTemporalDenoisedScalerBase roughnessTexture];
-[MTLFXTemporalDenoisedScalerBase roughnessTextureFormat];
-[MTLFXTemporalDenoisedScalerBase roughnessTextureUsage];
-[MTLFXTemporalDenoisedScalerBase setDenoiseStrengthMaskTexture:];
-[MTLFXTemporalDenoisedScalerBase setExposureTexture:];
-[MTLFXTemporalDenoisedScalerBase setFence:];
-[MTLFXTemporalDenoisedScalerBase setReactiveMaskTexture:];
-[MTLFXTemporalDenoisedScalerBase setShouldResetHistory:];
-[MTLFXTemporalDenoisedScalerBase setTransparencyOverlayTexture:];
-[MTLFXTemporalDenoisedScalerBase shouldResetHistory];
-[MTLFXTemporalDenoisedScalerBase specularAlbedoTexture];
-[MTLFXTemporalDenoisedScalerBase specularAlbedoTextureFormat];
-[MTLFXTemporalDenoisedScalerBase specularAlbedoTextureUsage];
-[MTLFXTemporalDenoisedScalerBase specularHitDistanceTexture];
-[MTLFXTemporalDenoisedScalerBase specularHitDistanceTextureFormat];
-[MTLFXTemporalDenoisedScalerBase transparencyOverlayTexture];
-[MTLFXTemporalDenoisedScalerBase transparencyOverlayTextureFormat];
-[MTLFXTemporalDenoisedScalerBase viewToClipMatrix];
-[MTLFXTemporalDenoisedScalerBase worldToViewMatrix];
```
