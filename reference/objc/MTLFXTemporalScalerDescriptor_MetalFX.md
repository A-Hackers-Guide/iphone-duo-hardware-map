# `MTLFXTemporalScalerDescriptor`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 18 instance variables, 18 properties, 43 instance methods, 4 class methods

## Instance variables

```
B inputContentPropertiesEnabled;
B outputResolutionMotionVectorsEnabled;
B jitteredMotionVectorsEnabled;
B reactiveMaskTextureEnabled;
B autoExposureEnabled;
B requiresSynchronousInitialization;
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
Q reactiveMaskTextureFormat;
Q _outputTextureFormat;
```

## Properties

```
@property (TQ,Vversion) version;
@property (TQ,N,VcolorTextureFormat) colorTextureFormat;
@property (TQ,N,VdepthTextureFormat) depthTextureFormat;
@property (TQ,N,VmotionTextureFormat) motionTextureFormat;
@property (TQ,N,V_outputTextureFormat) outputTextureFormat;
@property (TQ,N,VinputWidth) inputWidth;
@property (TQ,N,VinputHeight) inputHeight;
@property (TQ,N,VoutputWidth) outputWidth;
@property (TQ,N,VoutputHeight) outputHeight;
@property (TB,N,GisAutoExposureEnabled,VautoExposureEnabled) autoExposureEnabled;
@property (TB,N,VrequiresSynchronousInitialization) requiresSynchronousInitialization;
@property (TB,N,GisInputContentPropertiesEnabled,VinputContentPropertiesEnabled) inputContentPropertiesEnabled;
@property (Tf,N,VinputContentMinScale) inputContentMinScale;
@property (Tf,N,VinputContentMaxScale) inputContentMaxScale;
@property (TB,N,GisOutputResolutionMotionVectorsEnabled,VoutputResolutionMotionVectorsEnabled) outputResolutionMotionVectorsEnabled;
@property (TB,N,GisJitteredMotionVectorsEnabled,VjitteredMotionVectorsEnabled) jitteredMotionVectorsEnabled;
@property (TB,N,GisReactiveMaskTextureEnabled,VreactiveMaskTextureEnabled) reactiveMaskTextureEnabled;
@property (TQ,N,VreactiveMaskTextureFormat) reactiveMaskTextureFormat;
```

## Class methods

```
+[MTLFXTemporalScalerDescriptor supportsDevice:];
+[MTLFXTemporalScalerDescriptor supportedInputContentMaxScaleForDevice:];
+[MTLFXTemporalScalerDescriptor supportedInputContentMinScaleForDevice:];
+[MTLFXTemporalScalerDescriptor supportsMetal4FX:];
```

## Instance methods

```
-[MTLFXTemporalScalerDescriptor outputHeight];
-[MTLFXTemporalScalerDescriptor setInputHeight:];
-[MTLFXTemporalScalerDescriptor version];
-[MTLFXTemporalScalerDescriptor setOutputWidth:];
-[MTLFXTemporalScalerDescriptor setOutputHeight:];
-[MTLFXTemporalScalerDescriptor outputWidth];
-[MTLFXTemporalScalerDescriptor setVersion:];
-[MTLFXTemporalScalerDescriptor copyWithZone:];
-[MTLFXTemporalScalerDescriptor inputHeight];
-[MTLFXTemporalScalerDescriptor inputWidth];
-[MTLFXTemporalScalerDescriptor setInputWidth:];
-[MTLFXTemporalScalerDescriptor newTemporalScalerWithDevice:];
-[MTLFXTemporalScalerDescriptor setAutoExposureEnabled:];
-[MTLFXTemporalScalerDescriptor setColorTextureFormat:];
-[MTLFXTemporalScalerDescriptor setDepthTextureFormat:];
-[MTLFXTemporalScalerDescriptor setMotionTextureFormat:];
-[MTLFXTemporalScalerDescriptor setOutputTextureFormat:];
-[MTLFXTemporalScalerDescriptor setReactiveMaskTextureEnabled:];
-[MTLFXTemporalScalerDescriptor isInputContentPropertiesEnabled];
-[MTLFXTemporalScalerDescriptor colorTextureFormat];
-[MTLFXTemporalScalerDescriptor depthTextureFormat];
-[MTLFXTemporalScalerDescriptor enableInputContentProperties];
-[MTLFXTemporalScalerDescriptor inputContentMaxScale];
-[MTLFXTemporalScalerDescriptor inputContentMinScale];
-[MTLFXTemporalScalerDescriptor isAutoExposureEnabled];
-[MTLFXTemporalScalerDescriptor isJitteredMotionVectorsEnabled];
-[MTLFXTemporalScalerDescriptor isOutputResolutionMotionVectorsEnabled];
-[MTLFXTemporalScalerDescriptor isReactiveMaskTextureEnabled];
-[MTLFXTemporalScalerDescriptor motionTextureFormat];
-[MTLFXTemporalScalerDescriptor newTemporalScalerWithDevice:compiler:];
-[MTLFXTemporalScalerDescriptor newTemporalScalerWithHistoryTexture:];
-[MTLFXTemporalScalerDescriptor newTemporalScalerWithHistoryTexture:compiler:];
-[MTLFXTemporalScalerDescriptor outputTextureFormat];
-[MTLFXTemporalScalerDescriptor reactiveMaskTextureFormat];
-[MTLFXTemporalScalerDescriptor requiresSynchronousInitialization];
-[MTLFXTemporalScalerDescriptor setEnableInputContentProperties:];
-[MTLFXTemporalScalerDescriptor setInputContentMaxScale:];
-[MTLFXTemporalScalerDescriptor setInputContentMinScale:];
-[MTLFXTemporalScalerDescriptor setInputContentPropertiesEnabled:];
-[MTLFXTemporalScalerDescriptor setJitteredMotionVectorsEnabled:];
-[MTLFXTemporalScalerDescriptor setOutputResolutionMotionVectorsEnabled:];
-[MTLFXTemporalScalerDescriptor setReactiveMaskTextureFormat:];
-[MTLFXTemporalScalerDescriptor setRequiresSynchronousInitialization:];
```
