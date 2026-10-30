# `_M4FXTemporalScalingEffectBBR`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MFXTemporalScalingEffectBase`
- Protocols: `MTL4FXTemporalScalerSPI`, `MTL4FXEffectTracing`
- 2 instance variables, 58 properties, 12 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<BBRNet_Filter<MFXDevice4>, std::default_delete<BBRNet_Filter<MFXDevice4>>>=""{?="__ptr_"^v}} _filter;
@"<MTL4FXEffectTracingDelegate>" _tracingDelegate;
```

## Properties

```
@property (TQ,N) colorTextureBarrierStages;
@property (TQ,R,N) outputTextureBarrierStages;
@property (T{CGPoint=dd},N) previousJitterOffset;
@property (T{?=[4]},N) currentWorldToViewMatrix;
@property (T{?=[4]},N) currentViewToClipMatrix;
@property (T{?=[4]},N) previousWorldToViewMatrix;
@property (T{?=[4]},N) previousViewToClipMatrix;
@property (T@"<MTLTexture>",R,N) dilatedMotionVectors;
@property (T@"<MTLTexture>",&,N) debugTexture;
@property (TQ,R,N) executionMode;
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<MTL4FXEffectTracingDelegate>",W,V_tracingDelegate) tracingDelegate;
```

## Instance methods

```
-[_M4FXTemporalScalingEffectBBR encodeToCommandBuffer:];
-[_M4FXTemporalScalingEffectBBR tracingDelegate];
-[_M4FXTemporalScalingEffectBBR _didCreateComputeCommandEncoder:forEncode:];
-[_M4FXTemporalScalingEffectBBR _didCreateRenderCommandEncoder:forEncode:];
-[_M4FXTemporalScalingEffectBBR colorTextureBarrierStages];
-[_M4FXTemporalScalingEffectBBR dilatedMotionVectors];
-[_M4FXTemporalScalingEffectBBR executionMode];
-[_M4FXTemporalScalingEffectBBR initWithDevice:descriptor:compiler:history:];
-[_M4FXTemporalScalingEffectBBR outputTextureBarrierStages];
-[_M4FXTemporalScalingEffectBBR setColorTextureBarrierStages:];
-[_M4FXTemporalScalingEffectBBR setOutputTextureBarrierStages:];
-[_M4FXTemporalScalingEffectBBR setTracingDelegate:];
```
