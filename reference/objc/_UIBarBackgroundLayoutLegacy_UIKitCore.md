# `_UIBarBackgroundLayoutLegacy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarBackgroundLayout`
- 9 instance variables, 4 properties, 31 instance methods, 0 class methods

## Instance variables

```
q _translucence;
@"UIImage" _backgroundImage;
@"UIColor" _backgroundTintColor;
@"NSArray" _backgroundEffects;
@"UIImage" _shadowImage;
@"UIColor" _shadowColor;
@"UIVibrancyEffect" _shadowEffect;
B _hasShadow;
d _topInset;
```

## Properties

```
@property (T@"UIImage",R,N) shadowImage;
@property (TB,D,N) disableTinting;
@property (Td,N,V_topInset) topInset;
@property (TB,R,N) hasBackgroundEffect;
```

## Instance methods

```
-[_UIBarBackgroundLayoutLegacy describeInto:];
-[_UIBarBackgroundLayoutLegacy bg1Color];
-[_UIBarBackgroundLayoutLegacy configureShadowForBarStyle:];
-[_UIBarBackgroundLayoutLegacy configureEffectForStyle:backgroundTintColor:forceOpaque:];
-[_UIBarBackgroundLayoutLegacy shadowImage];
-[_UIBarBackgroundLayoutLegacy configureAsTransparent];
-[_UIBarBackgroundLayoutLegacy _blurWithStyle:tint:];
-[_UIBarBackgroundLayoutLegacy configureWithEffects:];
-[_UIBarBackgroundLayoutLegacy bg1HasShadow];
-[_UIBarBackgroundLayoutLegacy bg1Image];
-[_UIBarBackgroundLayoutLegacy bg1Effects];
-[_UIBarBackgroundLayoutLegacy bg1Alpha];
-[_UIBarBackgroundLayoutLegacy bg1ShadowAlpha];
-[_UIBarBackgroundLayoutLegacy shouldUseExplicitGeometry];
-[_UIBarBackgroundLayoutLegacy initWithLayout:];
-[_UIBarBackgroundLayoutLegacy bgInset];
-[_UIBarBackgroundLayoutLegacy configureBackgroundColor:barStyle:translucent:];
-[_UIBarBackgroundLayoutLegacy configureWithoutShadow];
-[_UIBarBackgroundLayoutLegacy configureImage:forceOpaque:barStyle:];
-[_UIBarBackgroundLayoutLegacy setTopInset:];
-[_UIBarBackgroundLayoutLegacy bg1ShadowColor];
-[_UIBarBackgroundLayoutLegacy bg1ImageAlpha];
-[_UIBarBackgroundLayoutLegacy bg1ShadowEffect];
-[_UIBarBackgroundLayoutLegacy configureImage:forceOpaque:backgroundTintColor:];
-[_UIBarBackgroundLayoutLegacy configureShadowImage:];
-[_UIBarBackgroundLayoutLegacy setUseExplicitGeometry:];
-[_UIBarBackgroundLayoutLegacy _colorForStyle:];
-[_UIBarBackgroundLayoutLegacy topInset];
-[_UIBarBackgroundLayoutLegacy bg1ShadowImage];
-[_UIBarBackgroundLayoutLegacy hasBackgroundEffect];
-[_UIBarBackgroundLayoutLegacy configureImage:forceTranslucent:];
```
