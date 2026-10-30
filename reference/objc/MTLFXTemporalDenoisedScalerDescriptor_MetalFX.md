# `MTLFXTemporalDenoisedScalerDescriptor`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 26 instance variables, 26 properties, 58 instance methods, 4 class methods

## Instance variables

```
B inputContentPropertiesEnabled;
B autoExposureEnabled;
B requiresSynchronousInitialization;
B _reactiveMaskTextureEnabled;
B _specularHitDistanceTextureEnabled;
B _denoiseStrengthMaskTextureEnabled;
B _transparencyOverlayTextureEnabled;
f inputContentMinScale;
f inputContentMaxScale;
Q colorTextureFormat;
Q depthTextureFormat;
Q motionTextureFormat;
Q inputWidth;
Q inputHeight;
Q outputWidth;
Q outputHeight;
Q version;
Q _diffuseAlbedoTextureFormat;
Q _specularAlbedoTextureFormat;
Q _normalTextureFormat;
Q _roughnessTextureFormat;
Q _specularHitDistanceTextureFormat;
Q _denoiseStrengthMaskTextureFormat;
Q _transparencyOverlayTextureFormat;
Q _outputTextureFormat;
Q _reactiveMaskTextureFormat;
```

## Properties

```
@property (TB,N,GisInputContentPropertiesEnabled,VinputContentPropertiesEnabled) inputContentPropertiesEnabled;
@property (Tf,N,VinputContentMinScale) inputContentMinScale;
@property (Tf,N,VinputContentMaxScale) inputContentMaxScale;
@property (TQ,Vversion) version;
@property (TQ,N,VcolorTextureFormat) colorTextureFormat;
@property (TQ,N,VdepthTextureFormat) depthTextureFormat;
@property (TQ,N,VmotionTextureFormat) motionTextureFormat;
@property (TQ,N,V_diffuseAlbedoTextureFormat) diffuseAlbedoTextureFormat;
@property (TQ,N,V_specularAlbedoTextureFormat) specularAlbedoTextureFormat;
@property (TQ,N,V_normalTextureFormat) normalTextureFormat;
@property (TQ,N,V_roughnessTextureFormat) roughnessTextureFormat;
@property (TQ,N,V_specularHitDistanceTextureFormat) specularHitDistanceTextureFormat;
@property (TQ,N,V_denoiseStrengthMaskTextureFormat) denoiseStrengthMaskTextureFormat;
@property (TQ,N,V_transparencyOverlayTextureFormat) transparencyOverlayTextureFormat;
@property (TQ,N,V_outputTextureFormat) outputTextureFormat;
@property (TQ,N,VinputWidth) inputWidth;
@property (TQ,N,VinputHeight) inputHeight;
@property (TQ,N,VoutputWidth) outputWidth;
@property (TQ,N,VoutputHeight) outputHeight;
@property (TB,N,VrequiresSynchronousInitialization) requiresSynchronousInitialization;
@property (TB,N,GisAutoExposureEnabled,VautoExposureEnabled) autoExposureEnabled;
@property (TB,N,GisReactiveMaskTextureEnabled,V_reactiveMaskTextureEnabled) reactiveMaskTextureEnabled;
@property (TQ,N,V_reactiveMaskTextureFormat) reactiveMaskTextureFormat;
@property (TB,N,GisSpecularHitDistanceTextureEnabled,V_specularHitDistanceTextureEnabled) specularHitDistanceTextureEnabled;
@property (TB,N,GisDenoiseStrengthMaskTextureEnabled,V_denoiseStrengthMaskTextureEnabled) denoiseStrengthMaskTextureEnabled;
@property (TB,N,GisTransparencyOverlayTextureEnabled,V_transparencyOverlayTextureEnabled) transparencyOverlayTextureEnabled;
```

## Class methods

```
+[MTLFXTemporalDenoisedScalerDescriptor supportsDevice:];
+[MTLFXTemporalDenoisedScalerDescriptor supportedInputContentMaxScaleForDevice:];
+[MTLFXTemporalDenoisedScalerDescriptor supportedInputContentMinScaleForDevice:];
+[MTLFXTemporalDenoisedScalerDescriptor supportsMetal4FX:];
```

## Instance methods

```
-[MTLFXTemporalDenoisedScalerDescriptor outputHeight];
-[MTLFXTemporalDenoisedScalerDescriptor setInputHeight:];
-[MTLFXTemporalDenoisedScalerDescriptor version];
-[MTLFXTemporalDenoisedScalerDescriptor setOutputWidth:];
-[MTLFXTemporalDenoisedScalerDescriptor setOutputHeight:];
-[MTLFXTemporalDenoisedScalerDescriptor outputWidth];
-[MTLFXTemporalDenoisedScalerDescriptor setVersion:];
-[MTLFXTemporalDenoisedScalerDescriptor copyWithZone:];
-[MTLFXTemporalDenoisedScalerDescriptor inputHeight];
-[MTLFXTemporalDenoisedScalerDescriptor inputWidth];
-[MTLFXTemporalDenoisedScalerDescriptor setInputWidth:];
-[MTLFXTemporalDenoisedScalerDescriptor setSpecularAlbedoTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithDevice:];
-[MTLFXTemporalDenoisedScalerDescriptor setAutoExposureEnabled:];
-[MTLFXTemporalDenoisedScalerDescriptor setColorTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setDenoiseStrengthMaskTextureEnabled:];
-[MTLFXTemporalDenoisedScalerDescriptor setDepthTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setDiffuseAlbedoTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setMotionTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setNormalTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setOutputTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setReactiveMaskTextureEnabled:];
-[MTLFXTemporalDenoisedScalerDescriptor setRoughnessTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setSpecularHitDistanceTextureEnabled:];
-[MTLFXTemporalDenoisedScalerDescriptor setSpecularHitDistanceTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setTransparencyOverlayTextureEnabled:];
-[MTLFXTemporalDenoisedScalerDescriptor isInputContentPropertiesEnabled];
-[MTLFXTemporalDenoisedScalerDescriptor colorTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor denoiseStrengthMaskTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor depthTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor diffuseAlbedoTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor enableInputContentProperties];
-[MTLFXTemporalDenoisedScalerDescriptor inputContentMaxScale];
-[MTLFXTemporalDenoisedScalerDescriptor inputContentMinScale];
-[MTLFXTemporalDenoisedScalerDescriptor isAutoExposureEnabled];
-[MTLFXTemporalDenoisedScalerDescriptor isDenoiseStrengthMaskTextureEnabled];
-[MTLFXTemporalDenoisedScalerDescriptor isReactiveMaskTextureEnabled];
-[MTLFXTemporalDenoisedScalerDescriptor isSpecularHitDistanceTextureEnabled];
-[MTLFXTemporalDenoisedScalerDescriptor isTransparencyOverlayTextureEnabled];
-[MTLFXTemporalDenoisedScalerDescriptor motionTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithDevice:compiler:];
-[MTLFXTemporalDenoisedScalerDescriptor newTemporalDenoisedScalerWithHistoryTexture:];
-[MTLFXTemporalDenoisedScalerDescriptor normalTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor outputTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor reactiveMaskTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor requiresSynchronousInitialization];
-[MTLFXTemporalDenoisedScalerDescriptor roughnessTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor setDenoiseStrengthMaskTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setEnableInputContentProperties:];
-[MTLFXTemporalDenoisedScalerDescriptor setInputContentMaxScale:];
-[MTLFXTemporalDenoisedScalerDescriptor setInputContentMinScale:];
-[MTLFXTemporalDenoisedScalerDescriptor setInputContentPropertiesEnabled:];
-[MTLFXTemporalDenoisedScalerDescriptor setReactiveMaskTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor setRequiresSynchronousInitialization:];
-[MTLFXTemporalDenoisedScalerDescriptor setTransparencyOverlayTextureFormat:];
-[MTLFXTemporalDenoisedScalerDescriptor specularAlbedoTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor specularHitDistanceTextureFormat];
-[MTLFXTemporalDenoisedScalerDescriptor transparencyOverlayTextureFormat];
```
