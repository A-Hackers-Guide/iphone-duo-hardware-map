# `PKInkParticleDescriptor`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 16 properties, 39 instance methods, 3 class methods

## Instance variables

```
d _dynamicStep;
{unique_ptr<PKFunction, std::default_delete<PKFunction>>=""{?="__ptr_"^{PKFunction}}} _particleSpacingFunction;
B _initialRandomRotation;
B _maskInitialRandomOffset;
B _adjustEndCapParticleAlpha;
@"NSString" _textureName;
^{CGImage=} _textureImage;
@"NSString" _maskTextureName;
^{CGImage=} _maskTextureImage;
d _particleSpacing;
q _particleCount;
Q _particleRotation;
d _maskScale;
d _maskScaleConstant;
d _maskMovement;
d _maskDepth;
Q _particleBlendMode;
{CGSize="width"d"height"d} _particleSize;
```

## Properties

```
@property (T@"NSString",C,N,V_textureName) textureName;
@property (T^{CGImage=},&,N,V_textureImage) textureImage;
@property (T@"NSString",C,N,V_maskTextureName) maskTextureName;
@property (T^{CGImage=},&,N,V_maskTextureImage) maskTextureImage;
@property (Td,N,V_particleSpacing) particleSpacing;
@property (Tq,N,V_particleCount) particleCount;
@property (T{CGSize=dd},N,V_particleSize) particleSize;
@property (Td,N,V_maskScale) maskScale;
@property (Td,N,V_maskScaleConstant) maskScaleConstant;
@property (Td,N,V_maskMovement) maskMovement;
@property (TQ,N,V_particleRotation) particleRotation;
@property (TB,N,V_initialRandomRotation) initialRandomRotation;
@property (TQ,N,V_particleBlendMode) particleBlendMode;
@property (Td,N,V_maskDepth) maskDepth;
@property (TB,N,V_maskInitialRandomOffset) maskInitialRandomOffset;
@property (TB,N,GadjustEndCapParticleAlpha,SsetAdjustEndCapParticleAlpha:,V_adjustEndCapParticleAlpha) adjustEndCapParticleAlpha;
```

## Class methods

```
+[PKInkParticleDescriptor arrayFromVector:];
+[PKInkParticleDescriptor particleDescriptorWithName:particleSpacing:particleCount:particleSize:particleRotation:];
+[PKInkParticleDescriptor particleDescriptorWithName:texture:particleSpacing:particleCount:particleSize:particleRotation:];
```

## Instance methods

```
-[PKInkParticleDescriptor particleCount];
-[PKInkParticleDescriptor particleRotation];
-[PKInkParticleDescriptor mutableCopy];
-[PKInkParticleDescriptor setTextureImage:];
-[PKInkParticleDescriptor textureImage];
-[PKInkParticleDescriptor particleSize];
-[PKInkParticleDescriptor setParticleSize:];
-[PKInkParticleDescriptor setMaskScale:];
-[PKInkParticleDescriptor setTextureName:];
-[PKInkParticleDescriptor textureName];
-[PKInkParticleDescriptor particleSpacing];
-[PKInkParticleDescriptor maskTextureName];
-[PKInkParticleDescriptor setDynamicStep:];
-[PKInkParticleDescriptor adjustEndCapParticleAlpha];
-[PKInkParticleDescriptor dynamicStep];
-[PKInkParticleDescriptor initWithTextureName:textureImage:maskTextureName:maskTextureImage:particleSpacing:particleCount:particleSize:particleRotation:maskScale:maskScaleConstant:maskMovement:maskDepth:initialRandomRotation:maskInitialRandomOffset:adjustEndCapParticleAlpha:particleBlendMode:];
-[PKInkParticleDescriptor initialRandomRotation];
-[PKInkParticleDescriptor maskDepth];
-[PKInkParticleDescriptor maskInitialRandomOffset];
-[PKInkParticleDescriptor maskMovement];
-[PKInkParticleDescriptor maskScale];
-[PKInkParticleDescriptor maskScaleConstant];
-[PKInkParticleDescriptor maskTextureImage];
-[PKInkParticleDescriptor particleBlendMode];
-[PKInkParticleDescriptor particleSpacingForRadius:];
-[PKInkParticleDescriptor particleSpacingFunction];
-[PKInkParticleDescriptor setAdjustEndCapParticleAlpha:];
-[PKInkParticleDescriptor setInitialRandomRotation:];
-[PKInkParticleDescriptor setMaskDepth:];
-[PKInkParticleDescriptor setMaskInitialRandomOffset:];
-[PKInkParticleDescriptor setMaskMovement:];
-[PKInkParticleDescriptor setMaskScaleConstant:];
-[PKInkParticleDescriptor setMaskTextureImage:];
-[PKInkParticleDescriptor setMaskTextureName:];
-[PKInkParticleDescriptor setParticleBlendMode:];
-[PKInkParticleDescriptor setParticleCount:];
-[PKInkParticleDescriptor setParticleRotation:];
-[PKInkParticleDescriptor setParticleSpacing:];
-[PKInkParticleDescriptor setParticleSpacingFunction:];
```
