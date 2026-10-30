# `CUIRenditionLayerReference`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 19 properties, 41 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
@"NSString" _layerName;
d _opacity;
i _blendMode;
B _fixedFrame;
B _makeOpaqueIfPossible;
B _hasLightingEffects;
B _gathersSpecularByElement;
q _shadowStyle;
d _shadowOpacity;
B _hasSpecular;
f _blurStrength;
d _refractionStrength;
d _refractionHeight;
q _specularPlacement;
@"NSString" _gradientOrColorName;
@"CUIRenditionKey" _referenceKey;
d _translucency;
```

## Properties

```
@property (T@"CUIRenditionKey",&,N,V_referenceKey) referenceKey;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T@"NSString",C,N,V_layerName) layerName;
@property (Td,N,V_opacity) opacity;
@property (Ti,N,V_blendMode) blendMode;
@property (TB,N,V_fixedFrame) fixedFrame;
@property (TB,N,V_makeOpaqueIfPossible) makeOpaqueIfPossible;
@property (Tf,N,V_blurStrength) blurStrength;
@property (T@"NSString",C,N,V_gradientOrColorName) gradientOrColorName;
@property (T@"NSString",C,N) colorName;
@property (TB,N,V_hasLightingEffects) hasLightingEffects;
@property (TB,N,V_gathersSpecularByElement) gathersSpecularByElement;
@property (Tq,N,V_shadowStyle) shadowStyle;
@property (Td,N,V_shadowOpacity) shadowOpacity;
@property (TB,N,V_hasSpecular) hasSpecular;
@property (Td,N,V_translucency) translucency;
@property (Td,N,V_refractionStrength) refractionStrength;
@property (Td,N,V_refractionHeight) refractionHeight;
@property (Tq,N,V_specularPlacement) specularPlacement;
```

## Instance methods

```
-[CUIRenditionLayerReference shadowStyle];
-[CUIRenditionLayerReference setShadowStyle:];
-[CUIRenditionLayerReference referenceKey];
-[CUIRenditionLayerReference colorName];
-[CUIRenditionLayerReference init];
-[CUIRenditionLayerReference setRefractionStrength:];
-[CUIRenditionLayerReference dealloc];
-[CUIRenditionLayerReference refractionHeight];
-[CUIRenditionLayerReference opacity];
-[CUIRenditionLayerReference setGathersSpecularByElement:];
-[CUIRenditionLayerReference setOpacity:];
-[CUIRenditionLayerReference setTranslucency:];
-[CUIRenditionLayerReference layerName];
-[CUIRenditionLayerReference setSpecularPlacement:];
-[CUIRenditionLayerReference setBlurStrength:];
-[CUIRenditionLayerReference setMakeOpaqueIfPossible:];
-[CUIRenditionLayerReference specularPlacement];
-[CUIRenditionLayerReference blurStrength];
-[CUIRenditionLayerReference setColorName:];
-[CUIRenditionLayerReference hasSpecular];
-[CUIRenditionLayerReference setFrame:];
-[CUIRenditionLayerReference makeOpaqueIfPossible];
-[CUIRenditionLayerReference refractionStrength];
-[CUIRenditionLayerReference description];
-[CUIRenditionLayerReference hasLightingEffects];
-[CUIRenditionLayerReference shadowOpacity];
-[CUIRenditionLayerReference gathersSpecularByElement];
-[CUIRenditionLayerReference setGradientOrColorName:];
-[CUIRenditionLayerReference setHasLightingEffects:];
-[CUIRenditionLayerReference setReferenceKey:];
-[CUIRenditionLayerReference setFixedFrame:];
-[CUIRenditionLayerReference blendMode];
-[CUIRenditionLayerReference setHasSpecular:];
-[CUIRenditionLayerReference setRefractionHeight:];
-[CUIRenditionLayerReference setLayerName:];
-[CUIRenditionLayerReference fixedFrame];
-[CUIRenditionLayerReference gradientOrColorName];
-[CUIRenditionLayerReference setBlendMode:];
-[CUIRenditionLayerReference translucency];
-[CUIRenditionLayerReference setShadowOpacity:];
-[CUIRenditionLayerReference frame];
```
