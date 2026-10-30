# `UIKBRenderTraits`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 28 instance variables, 27 properties, 61 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _renderEffects;
@"NSMutableArray" _foregroundRenderEffects;
B _honorControlOpacity;
B _controlOpacities;
B _blurBlending;
B _renderSecondarySymbolsSeparately;
B _usesDarkAppearance;
@"UIKBRenderGeometry" _geometry;
@"UIKBGradient" _backgroundGradient;
@"UIKBGradient" _layeredBackgroundGradient;
@"UIKBGradient" _layeredForegroundGradient;
@"UIKBTextStyle" _symbolStyle;
@"UIKBTextStyle" _fallbackSymbolStyle;
@"NSArray" _secondarySymbolStyles;
@"NSArray" _variantGeometries;
@"UIKBRenderTraits" _variantTraits;
@"UIKBRenderTraits" _highlightedVariantTraits;
q _blendForm;
@"NSArray" _renderFlags;
q _renderFlagsForAboveEffects;
@"NSString" _hashString;
d _floatingContentViewCornerRadius;
d _floatingContentViewControlFocusedIncreaseSize;
d _floatingContentViewShadowVerticalOffset;
d _floatingContentViewShadowRadius;
d _floatingContentViewShadowOpacity;
{CGSize="width"d"height"d} _floatingContentViewFocusedIncreaseSize;
{CGSize="width"d"height"d} _floatingContentViewControlFocusedBaseSize;
```

## Properties

```
@property (T@"UIKBRenderGeometry",&,N,V_geometry) geometry;
@property (T@"UIKBGradient",&,N,V_backgroundGradient) backgroundGradient;
@property (T@"UIKBGradient",&,N,V_layeredBackgroundGradient) layeredBackgroundGradient;
@property (T@"UIKBGradient",&,N,V_layeredForegroundGradient) layeredForegroundGradient;
@property (T@"UIKBTextStyle",&,N,V_symbolStyle) symbolStyle;
@property (T@"UIKBTextStyle",&,N,V_fallbackSymbolStyle) fallbackSymbolStyle;
@property (T@"NSArray",&,N,V_secondarySymbolStyles) secondarySymbolStyles;
@property (T@"NSArray",R,N,V_renderEffects) renderEffects;
@property (T@"NSArray",R,N,V_foregroundRenderEffects) foregroundRenderEffects;
@property (T@"NSArray",&,N,V_variantGeometries) variantGeometries;
@property (T@"UIKBRenderTraits",&,N,V_variantTraits) variantTraits;
@property (T@"UIKBRenderTraits",&,N,V_highlightedVariantTraits) highlightedVariantTraits;
@property (TB,N,V_controlOpacities) controlOpacities;
@property (TB,N,V_blurBlending) blurBlending;
@property (Tq,N,V_blendForm) blendForm;
@property (T@"NSArray",&,N,V_renderFlags) renderFlags;
@property (TB,N,V_renderSecondarySymbolsSeparately) renderSecondarySymbolsSeparately;
@property (Tq,N,V_renderFlagsForAboveEffects) renderFlagsForAboveEffects;
@property (T@"NSString",&,N,V_hashString) hashString;
@property (TB,N,V_usesDarkAppearance) usesDarkAppearance;
@property (Td,N,V_floatingContentViewCornerRadius) floatingContentViewCornerRadius;
@property (T{CGSize=dd},N,V_floatingContentViewFocusedIncreaseSize) floatingContentViewFocusedIncreaseSize;
@property (T{CGSize=dd},N,V_floatingContentViewControlFocusedBaseSize) floatingContentViewControlFocusedBaseSize;
@property (Td,N,V_floatingContentViewControlFocusedIncreaseSize) floatingContentViewControlFocusedIncreaseSize;
@property (Td,N,V_floatingContentViewShadowVerticalOffset) floatingContentViewShadowVerticalOffset;
@property (Td,N,V_floatingContentViewShadowRadius) floatingContentViewShadowRadius;
@property (Td,N,V_floatingContentViewShadowOpacity) floatingContentViewShadowOpacity;
```

## Class methods

```
+[UIKBRenderTraits emptyTraits];
+[UIKBRenderTraits traitsWithGeometry:];
+[UIKBRenderTraits traitsWithSymbolStyle:];
```

## Instance methods

```
-[UIKBRenderTraits floatingContentViewCornerRadius];
-[UIKBRenderTraits addForegroundRenderEffect:];
-[UIKBRenderTraits overlayWithTraits:];
-[UIKBRenderTraits floatingContentViewShadowRadius];
-[UIKBRenderTraits setRenderFlagsForAboveEffects:];
-[UIKBRenderTraits renderFlagsForAboveEffects];
-[UIKBRenderTraits foregroundRenderEffects];
-[UIKBRenderTraits floatingContentViewShadowVerticalOffset];
-[UIKBRenderTraits setFloatingContentViewShadowVerticalOffset:];
-[UIKBRenderTraits floatingContentViewFocusedIncreaseSize];
-[UIKBRenderTraits setSecondarySymbolStyles:];
-[UIKBRenderTraits setControlOpacities:];
-[UIKBRenderTraits usesDarkAppearance];
-[UIKBRenderTraits addRenderEffect:];
-[UIKBRenderTraits renderFlags];
-[UIKBRenderTraits symbolStyle];
-[UIKBRenderTraits secondarySymbolStyles];
-[UIKBRenderTraits setUsesDarkAppearance:];
-[UIKBRenderTraits setBlurBlending:];
-[UIKBRenderTraits setFallbackSymbolStyle:];
-[UIKBRenderTraits renderSecondarySymbolsSeparately];
-[UIKBRenderTraits setFloatingContentViewShadowRadius:];
-[UIKBRenderTraits floatingContentViewShadowOpacity];
-[UIKBRenderTraits layeredForegroundGradient];
-[UIKBRenderTraits geometry];
-[UIKBRenderTraits setHighlightedVariantTraits:];
-[UIKBRenderTraits setVariantTraits:];
-[UIKBRenderTraits setGeometry:];
-[UIKBRenderTraits setRenderSecondarySymbolsSeparately:];
-[UIKBRenderTraits setFloatingContentViewFocusedIncreaseSize:];
-[UIKBRenderTraits setVariantGeometries:];
-[UIKBRenderTraits hashString];
-[UIKBRenderTraits setBackgroundGradient:];
-[UIKBRenderTraits floatingContentViewControlFocusedIncreaseSize];
-[UIKBRenderTraits blendForm];
-[UIKBRenderTraits fallbackSymbolStyle];
-[UIKBRenderTraits variantGeometries];
-[UIKBRenderTraits variantTraits];
-[UIKBRenderTraits setLayeredBackgroundGradient:];
-[UIKBRenderTraits backgroundGradient];
-[UIKBRenderTraits setLayeredForegroundGradient:];
-[UIKBRenderTraits setFloatingContentViewControlFocusedBaseSize:];
-[UIKBRenderTraits description];
-[UIKBRenderTraits floatingContentViewControlFocusedBaseSize];
-[UIKBRenderTraits setFloatingContentViewControlFocusedIncreaseSize:];
-[UIKBRenderTraits removeAllRenderEffects];
-[UIKBRenderTraits copyWithZone:];
-[UIKBRenderTraits modifyForMasking];
-[UIKBRenderTraits extraFiltersForType:];
-[UIKBRenderTraits controlOpacities];
-[UIKBRenderTraits isEqual:];
-[UIKBRenderTraits blurBlending];
-[UIKBRenderTraits setRenderFlags:];
-[UIKBRenderTraits setFloatingContentViewShadowOpacity:];
-[UIKBRenderTraits renderEffects];
-[UIKBRenderTraits setHashString:];
-[UIKBRenderTraits setBlendForm:];
-[UIKBRenderTraits layeredBackgroundGradient];
-[UIKBRenderTraits setSymbolStyle:];
-[UIKBRenderTraits highlightedVariantTraits];
-[UIKBRenderTraits setFloatingContentViewCornerRadius:];
```
