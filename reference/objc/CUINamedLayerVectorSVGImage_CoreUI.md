# `CUINamedLayerVectorSVGImage`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedVectorSVGImage`
- 6 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
d _opacity;
i _blendMode;
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
```

## Instance methods

```
-[CUINamedLayerVectorSVGImage gradient];
-[CUINamedLayerVectorSVGImage _setBlurStrength:];
-[CUINamedLayerVectorSVGImage dealloc];
-[CUINamedLayerVectorSVGImage _setFrame:];
-[CUINamedLayerVectorSVGImage opacity];
-[CUINamedLayerVectorSVGImage _setBlendMode:];
-[CUINamedLayerVectorSVGImage _gradientOrColor];
-[CUINamedLayerVectorSVGImage initWithName:usingRenditionKey:fromTheme:];
-[CUINamedLayerVectorSVGImage setOpacity:];
-[CUINamedLayerVectorSVGImage color];
-[CUINamedLayerVectorSVGImage setBlurStrength:];
-[CUINamedLayerVectorSVGImage blurStrength];
-[CUINamedLayerVectorSVGImage _setHasLightingEffects:];
-[CUINamedLayerVectorSVGImage setFrame:];
-[CUINamedLayerVectorSVGImage _setGradientOrColorName:];
-[CUINamedLayerVectorSVGImage hasLightingEffects];
-[CUINamedLayerVectorSVGImage setGradientOrColorName:];
-[CUINamedLayerVectorSVGImage setHasLightingEffects:];
-[CUINamedLayerVectorSVGImage _setGradientOrColor:];
-[CUINamedLayerVectorSVGImage blendMode];
-[CUINamedLayerVectorSVGImage mutableCopy];
-[CUINamedLayerVectorSVGImage _updateFromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedLayerVectorSVGImage gradientOrColorName];
-[CUINamedLayerVectorSVGImage setBlendMode:];
-[CUINamedLayerVectorSVGImage frame];
```
