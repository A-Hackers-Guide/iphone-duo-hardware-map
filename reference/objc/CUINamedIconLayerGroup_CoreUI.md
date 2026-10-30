# `CUINamedIconLayerGroup`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CUINamedLookup`
- 15 instance variables, 16 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _layers;
d _opacity;
i _blendMode;
d _blurStrength;
@"NSString" _gradientOrColorName;
B _hasLightingEffects;
B _gathersSpecularByElement;
q _shadowStyle;
d _shadowOpacity;
B _hasSpecular;
@ _gradientOrColor;
d _translucency;
d _refractionStrength;
d _refractionHeight;
q _specularPlacement;
```

## Properties

```
@property (T@"NSArray",&,N,V_layers) layers;
@property (Td,N,V_opacity) opacity;
@property (Ti,N,V_blendMode) blendMode;
@property (Td,N,V_blurStrength) blurStrength;
@property (TB,N,V_hasLightingEffects) hasLightingEffects;
@property (TB,N,V_gathersSpecularByElement) gathersSpecularByElement;
@property (Tq,N,V_shadowStyle) shadowStyle;
@property (Td,N,V_shadowOpacity) shadowOpacity;
@property (TB,N,V_hasSpecular) hasSpecular;
@property (Td,N,V_translucency) translucency;
@property (Td,N,V_refractionStrength) refractionStrength;
@property (Td,N,V_refractionHeight) refractionHeight;
@property (Tq,N,V_specularPlacement) specularPlacement;
@property (T@"NSString",C,N,V_gradientOrColorName) gradientOrColorName;
@property (T^{CGColor=},R,N) color;
@property (T@"CUINamedGradient",R,N) gradient;
```

## Instance methods

```
-[CUINamedIconLayerGroup shadowStyle];
-[CUINamedIconLayerGroup gradient];
-[CUINamedIconLayerGroup setShadowStyle:];
-[CUINamedIconLayerGroup _removeLayerAtIndex:];
-[CUINamedIconLayerGroup _setBlurStrength:];
-[CUINamedIconLayerGroup layers];
-[CUINamedIconLayerGroup _setShadowOpacity:];
-[CUINamedIconLayerGroup _addLayer:];
-[CUINamedIconLayerGroup _setSpecularPlacement:];
-[CUINamedIconLayerGroup _setGathersSpecularByElement:];
-[CUINamedIconLayerGroup setRefractionStrength:];
-[CUINamedIconLayerGroup dealloc];
-[CUINamedIconLayerGroup refractionHeight];
-[CUINamedIconLayerGroup _setRefractionHeight:];
-[CUINamedIconLayerGroup opacity];
-[CUINamedIconLayerGroup _setBlendMode:];
-[CUINamedIconLayerGroup _gradientOrColor];
-[CUINamedIconLayerGroup setGathersSpecularByElement:];
-[CUINamedIconLayerGroup setOpacity:];
-[CUINamedIconLayerGroup color];
-[CUINamedIconLayerGroup _setShadowStyle:];
-[CUINamedIconLayerGroup setTranslucency:];
-[CUINamedIconLayerGroup _setRefractionStrength:];
-[CUINamedIconLayerGroup setSpecularPlacement:];
-[CUINamedIconLayerGroup setBlurStrength:];
-[CUINamedIconLayerGroup _setHasSpecular:];
-[CUINamedIconLayerGroup specularPlacement];
-[CUINamedIconLayerGroup blurStrength];
-[CUINamedIconLayerGroup initWithName:usingRenditionKey:fromTheme:resolvingWithBlock:];
-[CUINamedIconLayerGroup hasSpecular];
-[CUINamedIconLayerGroup _setHasLightingEffects:];
-[CUINamedIconLayerGroup _setGradientOrColorName:];
-[CUINamedIconLayerGroup refractionStrength];
-[CUINamedIconLayerGroup hasLightingEffects];
-[CUINamedIconLayerGroup shadowOpacity];
-[CUINamedIconLayerGroup gathersSpecularByElement];
-[CUINamedIconLayerGroup setLayers:];
-[CUINamedIconLayerGroup setGradientOrColorName:];
-[CUINamedIconLayerGroup setHasLightingEffects:];
-[CUINamedIconLayerGroup _setGradientOrColor:];
-[CUINamedIconLayerGroup blendMode];
-[CUINamedIconLayerGroup mutableCopy];
-[CUINamedIconLayerGroup setHasSpecular:];
-[CUINamedIconLayerGroup _updateFromCatalog:displayGamut:deviceIdiom:appearanceName:];
-[CUINamedIconLayerGroup setRefractionHeight:];
-[CUINamedIconLayerGroup _setOpacity:];
-[CUINamedIconLayerGroup gradientOrColorName];
-[CUINamedIconLayerGroup setBlendMode:];
-[CUINamedIconLayerGroup translucency];
-[CUINamedIconLayerGroup setShadowOpacity:];
-[CUINamedIconLayerGroup _setTranslucency:];
```
