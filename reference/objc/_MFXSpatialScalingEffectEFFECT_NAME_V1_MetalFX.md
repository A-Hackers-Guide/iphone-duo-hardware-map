# `_MFXSpatialScalingEffectEFFECT_NAME_V1`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLFXSpatialScaler`
- Protocols: `MTLFXSpatialScalerSPI`
- 33 instance variables, 19 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<MTLDeviceSPI>" _device;
@"<MTLTexture>" _inputTexture;
@"<MTLTexture>" _outputTexture;
@"<MTLTexture>" _debugTexture;
B _inputOutputNormalized;
B _inputLinear;
@"<MTLRenderPipelineState>" _mfxNormPerceptPSO;
@"<MTLRenderPipelineState>" _mfxUpscalePSO;
@"<MTLRenderPipelineState>" _mfxSharpenPSO;
@"<MTLComputePipelineState>" _mfxUpscaleKernel;
@"<MTLComputePipelineState>" _mfxSharpenKernel;
@"MTLRenderPassDescriptor" _mfxPassDescriptor;
@"<MTLTexture>" _mfxNormPerceptTex;
@"<MTLTexture>" _mfxUpscaledTex;
@"MTLTextureDescriptor" _texDesc;
Q _inputFormat;
Q _outputFormat;
B _inputSRGB;
B _outputSRGB;
B _use3DPipeline;
Q _intermediatePixelFormat;
q _colorProcessingMode;
Q _inputContentWidth;
Q _inputContentHeight;
Q _colorTextureUsage;
Q _outputTextureUsage;
@"<MTLFence>" _fence;
Q _colorTextureFormat;
Q _outputTextureFormat;
Q _inputWidth;
Q _inputHeight;
Q _outputWidth;
Q _outputHeight;
```

## Properties

```
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
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 outputHeight];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 initWithDevice:descriptor:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setOutputTexture:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 inputTexture];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 outputTexture];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 outputWidth];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setInputTexture:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 inputHeight];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 encodeToCommandQueue:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 inputWidth];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 encodeToCommandBuffer:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setColorTexture:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 colorTexture];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 debugTexture];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 colorProcessingMode];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 colorTextureFormat];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 colorTextureUsage];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 fence];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 inputContentHeight];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 inputContentWidth];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 outputTextureFormat];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 outputTextureUsage];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setDebugTexture:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setFence:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setInputContentHeight:];
-[_MFXSpatialScalingEffectEFFECT_NAME_V1 setInputContentWidth:];
```
