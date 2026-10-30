# `CUINamedLayerImage`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedImage`
- Protocols: `CUINamedLayerImageProtocol`
- 7 instance variables, 15 properties, 32 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
d _opacity;
i _blendMode;
B _fixedFrame;
d _blurStrength;
@"NSString" _gradientOrColorName;
B _hasLightingEffects;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (Td,N,V_opacity) opacity;
@property (Ti,N,V_blendMode) blendMode;
@property (Td,N,V_blurStrength) blurStrength;
@property (TB,N,V_hasLightingEffects) hasLightingEffects;
@property (T@"NSString",C,N,V_gradientOrColorName) gradientOrColorName;
@property (T^{CGColor=},R,N) color;
@property (T@"CUINamedGradient",R,N) gradient;
@property (TB,N,V_fixedFrame) fixedFrame;
@property (T^{CGImage=},R,N) image;
@property (Td,R,N) scale;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CUINamedLayerImage gradient];
-[CUINamedLayerImage _setBlurStrength:];
-[CUINamedLayerImage _setBlurStrength:];
-[CUINamedLayerImage dealloc];
-[CUINamedLayerImage _setFrame:];
-[CUINamedLayerImage opacity];
-[CUINamedLayerImage _setBlendMode:];
-[CUINamedLayerImage _gradientOrColor];
-[CUINamedLayerImage initWithName:usingRenditionKey:fromTheme:];
-[CUINamedLayerImage setOpacity:];
-[CUINamedLayerImage color];
-[CUINamedLayerImage setBlurStrength:];
-[CUINamedLayerImage blurStrength];
-[CUINamedLayerImage _setHasLightingEffects:];
-[CUINamedLayerImage setFrame:];
-[CUINamedLayerImage _setGradientOrColorName:];
-[CUINamedLayerImage _setGradientOrColorName:];
-[CUINamedLayerImage hasLightingEffects];
-[CUINamedLayerImage setGradientOrColorName:];
-[CUINamedLayerImage setHasLightingEffects:];
-[CUINamedLayerImage _setGradientOrColor:];
-[CUINamedLayerImage setFixedFrame:];
-[CUINamedLayerImage blendMode];
-[CUINamedLayerImage _updateFromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedLayerImage fixedFrame];
-[CUINamedLayerImage _setOpacity:];
-[CUINamedLayerImage gradientOrColorName];
-[CUINamedLayerImage setBlendMode:];
-[CUINamedLayerImage frame];
-[CUINamedLayerImage _opacity];
-[CUINamedLayerImage _blendMode];
-[CUINamedLayerImage sdfTextureWithBufferAllocator:];
```
