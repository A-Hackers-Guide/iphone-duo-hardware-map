# `LUTFactory`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MTLTextureDescriptor" _textureDescriptor;
q _gammaCountHalf;
q _gammaCount;
d _gammaBias;
d _gammaScale;
```

## Properties

```
@property (T@"MTLTextureDescriptor",&,N,V_textureDescriptor) textureDescriptor;
@property (Tq,N,V_gammaCountHalf) gammaCountHalf;
@property (Tq,N,V_gammaCount) gammaCount;
@property (Td,N,V_gammaBias) gammaBias;
@property (Td,N,V_gammaScale) gammaScale;
```

## Instance methods

```
-[LUTFactory init];
-[LUTFactory gammaBias];
-[LUTFactory gammaCount];
-[LUTFactory gammaCountHalf];
-[LUTFactory gammaScale];
-[LUTFactory initWithGammaScale:gammaBias:gammaCount:];
-[LUTFactory initializeGammaLUTWithGammaTexture:degammaTexture:];
-[LUTFactory initializeRec709LUTWithGammaTexture:degammaTexture:];
-[LUTFactory initializecGammaLUTWithGammaTexture:degammaTexture:];
-[LUTFactory initializesRGBLUTWithGammaTexture:degammaTexture:];
-[LUTFactory setGammaBias:];
-[LUTFactory setGammaCount:];
-[LUTFactory setGammaCountHalf:];
-[LUTFactory setGammaScale:];
-[LUTFactory setTextureDescriptor:];
-[LUTFactory textureDescriptor];
```
