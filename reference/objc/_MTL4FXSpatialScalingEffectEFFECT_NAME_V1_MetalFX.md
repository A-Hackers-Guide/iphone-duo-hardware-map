# `_MTL4FXSpatialScalingEffectEFFECT_NAME_V1`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4FXSpatialScaler`
- Protocols: `MTL4FXSpatialScalerSPI`
- 44 instance variables, 21 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<MTLDeviceSPI>" _device;
@"<MTLTexture>" _inputTexture;
@"<MTLTexture>" _outputTexture;
@"<MTLTexture>" _debugTexture;
@"<MTLRenderPipelineState>" _mfxNormPerceptPSO;
@"<MTLRenderPipelineState>" _mfxUpscalePSO;
@"<MTLRenderPipelineState>" _mfxSharpenPSO;
@"MTL4RenderPassDescriptor" _mfxPassDescriptor;
@"<MTLTexture>" _mfxNormPerceptTex;
@"<MTLTexture>" _mfxUpscaledTex;
@"MTLTextureDescriptor" _texDesc;
Q _inputFormat;
Q _outputFormat;
B _inputSRGB;
B _outputSRGB;
Q _intermediatePixelFormat;
Q _inputContentWidth;
Q _inputContentHeight;
Q _colorTextureUsage;
Q _outputTextureUsage;
@"<MTLFence>" _fence;
Q _colorTextureBarrierStages;
Q _outputTextureBarrierStages;
q _colorProcessingMode;
@"<MTL4ArgumentTable>" _normPerceptFragInputs;
@"<MTLBuffer>" _normalizeBuffer;
@"<MTL4ArgumentTable>" _scaleFragInputs;
@"NSMutableArray" _fxrUpscaleBuffer;
@"<MTLBuffer>" _scaleBuffer;
@"<MTL4ArgumentTable>" _sharpenFragInputs;
@"<MTLBuffer>" _fxrSharpenBuffer;
@"<MTLBuffer>" _sharpenBuffer;
B _needNormPercept;
@"<MTLResidencySet>" _residencySetGlobal;
@"<MTLResidencySet>" _residencySetPercept;
Q _frame;
Q _framesInFlight;
@"<MTLFence>" _internalFence;
Q _colorTextureFormat;
Q _outputTextureFormat;
Q _inputWidth;
Q _inputHeight;
Q _outputWidth;
Q _outputHeight;
```

## Properties

```
@property (TQ,N,V_colorTextureBarrierStages) colorTextureBarrierStages;
@property (TQ,R,N,V_outputTextureBarrierStages) outputTextureBarrierStages;
@property (T@"<MTLTexture>",&,N,V_debugTexture) debugTexture;
@property (TQ,R,N,V_colorTextureUsage) colorTextureUsage;
@property (TQ,R,N,V_outputTextureUsage) outputTextureUsage;
@property (TQ,N,V_inputContentWidth) inputContentWidth;
@property (TQ,N,V_inputContentHeight) inputContentHeight;
@property (T@"<MTLTexture>",&,N,V_inputTexture) colorTexture;
@property (T@"<MTLTexture>",&,N,V_outputTexture) outputTexture;
@property (TQ,R,N,V_colorTextureFormat) colorTextureFormat;
@property (TQ,R,N,V_outputTextureFormat) outputTextureFormat;
@property (TQ,R,N,V_inputWidth) inputWidth;
@property (TQ,R,N,V_inputHeight) inputHeight;
@property (TQ,R,N,V_outputWidth) outputWidth;
@property (TQ,R,N,V_outputHeight) outputHeight;
@property (Tq,R,N,V_colorProcessingMode) colorProcessingMode;
@property (T@"<MTLFence>",&,N,V_fence) fence;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputHeight];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setOutputTexture:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTexture];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputWidth];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputHeight];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputWidth];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 encodeToCommandBuffer:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setColorTexture:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTexture];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 debugTexture];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorProcessingMode];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTextureBarrierStages];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTextureFormat];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 colorTextureUsage];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 fence];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 initWithDevice:compiler:descriptor:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputContentHeight];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 inputContentWidth];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTextureBarrierStages];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTextureFormat];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 outputTextureUsage];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setColorTextureBarrierStages:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setDebugTexture:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setFence:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setInputContentHeight:];
-[_MTL4FXSpatialScalingEffectEFFECT_NAME_V1 setInputContentWidth:];
```
