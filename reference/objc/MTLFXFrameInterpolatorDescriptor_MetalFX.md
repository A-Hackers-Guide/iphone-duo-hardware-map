# `MTLFXFrameInterpolatorDescriptor`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 17 instance variables, 17 properties, 37 instance methods, 2 class methods

## Instance variables

```
B depthInverted;
B distortionTextureEnabled;
B requiresPrevColorTexture;
Q colorTextureFormat;
Q outputTextureFormat;
Q motionTextureFormat;
Q depthTextureFormat;
Q inputWidth;
Q inputHeight;
Q outputWidth;
Q outputHeight;
Q maskTextureFormat;
Q width;
Q height;
Q _uiTextureFormat;
@"<MTLFXFrameInterpolatableScaler>" _scaler;
Q _version;
```

## Properties

```
@property (TQ,N,VmaskTextureFormat) maskTextureFormat;
@property (TQ,N,Vwidth) width;
@property (TQ,N,Vheight) height;
@property (TB,N,VdepthInverted) depthInverted;
@property (TQ,V_version) version;
@property (TQ,N,VcolorTextureFormat) colorTextureFormat;
@property (TQ,N,VoutputTextureFormat) outputTextureFormat;
@property (TQ,N,VdepthTextureFormat) depthTextureFormat;
@property (TQ,N,VmotionTextureFormat) motionTextureFormat;
@property (TQ,N,SsetUITextureFormat:,V_uiTextureFormat) uiTextureFormat;
@property (T@"<MTLFXFrameInterpolatableScaler>",&,N,V_scaler) scaler;
@property (TQ,N,VinputWidth) inputWidth;
@property (TQ,N,VinputHeight) inputHeight;
@property (TQ,N,VoutputWidth) outputWidth;
@property (TQ,N,VoutputHeight) outputHeight;
@property (TB,N,GisDistortionTextureEnabled,VdistortionTextureEnabled) distortionTextureEnabled;
@property (TB,N,VrequiresPrevColorTexture) requiresPrevColorTexture;
```

## Class methods

```
+[MTLFXFrameInterpolatorDescriptor supportsDevice:];
+[MTLFXFrameInterpolatorDescriptor supportsMetal4FX:];
```

## Instance methods

```
-[MTLFXFrameInterpolatorDescriptor outputHeight];
-[MTLFXFrameInterpolatorDescriptor setInputHeight:];
-[MTLFXFrameInterpolatorDescriptor version];
-[MTLFXFrameInterpolatorDescriptor setOutputWidth:];
-[MTLFXFrameInterpolatorDescriptor setHeight:];
-[MTLFXFrameInterpolatorDescriptor setOutputHeight:];
-[MTLFXFrameInterpolatorDescriptor outputWidth];
-[MTLFXFrameInterpolatorDescriptor setVersion:];
-[MTLFXFrameInterpolatorDescriptor setWidth:];
-[MTLFXFrameInterpolatorDescriptor width];
-[MTLFXFrameInterpolatorDescriptor copyWithZone:];
-[MTLFXFrameInterpolatorDescriptor inputHeight];
-[MTLFXFrameInterpolatorDescriptor height];
-[MTLFXFrameInterpolatorDescriptor inputWidth];
-[MTLFXFrameInterpolatorDescriptor setInputWidth:];
-[MTLFXFrameInterpolatorDescriptor setColorTextureFormat:];
-[MTLFXFrameInterpolatorDescriptor setDepthTextureFormat:];
-[MTLFXFrameInterpolatorDescriptor setMotionTextureFormat:];
-[MTLFXFrameInterpolatorDescriptor setOutputTextureFormat:];
-[MTLFXFrameInterpolatorDescriptor newFrameInterpolatorWithDevice:];
-[MTLFXFrameInterpolatorDescriptor uiTextureFormat];
-[MTLFXFrameInterpolatorDescriptor colorTextureFormat];
-[MTLFXFrameInterpolatorDescriptor depthInverted];
-[MTLFXFrameInterpolatorDescriptor depthTextureFormat];
-[MTLFXFrameInterpolatorDescriptor isDistortionTextureEnabled];
-[MTLFXFrameInterpolatorDescriptor maskTextureFormat];
-[MTLFXFrameInterpolatorDescriptor motionTextureFormat];
-[MTLFXFrameInterpolatorDescriptor newFrameInterpolatorWithDevice:compiler:];
-[MTLFXFrameInterpolatorDescriptor outputTextureFormat];
-[MTLFXFrameInterpolatorDescriptor requiresPrevColorTexture];
-[MTLFXFrameInterpolatorDescriptor scaler];
-[MTLFXFrameInterpolatorDescriptor setDepthInverted:];
-[MTLFXFrameInterpolatorDescriptor setDistortionTextureEnabled:];
-[MTLFXFrameInterpolatorDescriptor setMaskTextureFormat:];
-[MTLFXFrameInterpolatorDescriptor setRequiresPrevColorTexture:];
-[MTLFXFrameInterpolatorDescriptor setScaler:];
-[MTLFXFrameInterpolatorDescriptor setUITextureFormat:];
```
