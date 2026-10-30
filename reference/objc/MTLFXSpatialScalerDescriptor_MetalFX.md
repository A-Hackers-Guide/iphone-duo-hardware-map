# `MTLFXSpatialScalerDescriptor`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 21 instance methods, 5 class methods

## Instance variables

```
Q outputTextureFormat;
Q inputWidth;
Q inputHeight;
Q outputWidth;
Q outputHeight;
Q version;
q colorProcessingMode;
Q _colorTextureFormat;
```

## Properties

```
@property (TQ,Vversion) version;
@property (TQ,N,V_colorTextureFormat) colorTextureFormat;
@property (TQ,N,VoutputTextureFormat) outputTextureFormat;
@property (TQ,N,VinputWidth) inputWidth;
@property (TQ,N,VinputHeight) inputHeight;
@property (TQ,N,VoutputWidth) outputWidth;
@property (TQ,N,VoutputHeight) outputHeight;
@property (Tq,N,VcolorProcessingMode) colorProcessingMode;
```

## Class methods

```
+[MTLFXSpatialScalerDescriptor supportsDevice:];
+[MTLFXSpatialScalerDescriptor colorTextureUsage];
+[MTLFXSpatialScalerDescriptor inputTextureUsage];
+[MTLFXSpatialScalerDescriptor outputTextureUsage];
+[MTLFXSpatialScalerDescriptor supportsMetal4FX:];
```

## Instance methods

```
-[MTLFXSpatialScalerDescriptor outputHeight];
-[MTLFXSpatialScalerDescriptor setInputHeight:];
-[MTLFXSpatialScalerDescriptor version];
-[MTLFXSpatialScalerDescriptor setOutputWidth:];
-[MTLFXSpatialScalerDescriptor setOutputHeight:];
-[MTLFXSpatialScalerDescriptor outputWidth];
-[MTLFXSpatialScalerDescriptor setVersion:];
-[MTLFXSpatialScalerDescriptor copyWithZone:];
-[MTLFXSpatialScalerDescriptor inputHeight];
-[MTLFXSpatialScalerDescriptor inputWidth];
-[MTLFXSpatialScalerDescriptor setInputWidth:];
-[MTLFXSpatialScalerDescriptor setColorTextureFormat:];
-[MTLFXSpatialScalerDescriptor setOutputTextureFormat:];
-[MTLFXSpatialScalerDescriptor colorProcessingMode];
-[MTLFXSpatialScalerDescriptor colorTextureFormat];
-[MTLFXSpatialScalerDescriptor getInputTextureFormat];
-[MTLFXSpatialScalerDescriptor newSpatialScalerWithDevice:];
-[MTLFXSpatialScalerDescriptor newSpatialScalerWithDevice:compiler:];
-[MTLFXSpatialScalerDescriptor outputTextureFormat];
-[MTLFXSpatialScalerDescriptor setColorProcessingMode:];
-[MTLFXSpatialScalerDescriptor setInputTextureFormat:];
```
