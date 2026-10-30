# `UIVibrancyEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- 1 instance variables, 1 properties, 21 instance methods, 20 class methods

## Instance variables

```
@"_UIVibrancyEffectImpl" _impl;
```

## Properties

```
@property (Tq,R,N,G_vibrancyStyle) _vibrancyStyle;
```

## Class methods

```
+[UIVibrancyEffect supportsSecureCoding];
+[UIVibrancyEffect _darkVibrantEffectWithLightenColor:dodgeColor:compositingColor:];
+[UIVibrancyEffect _effectForBlurEffect:vibrancyStyle:];
+[UIVibrancyEffect _effectWithStyle:ignoreSimpleVibrancy:];
+[UIVibrancyEffect _lightVibrantEffectWithDarkenColor:burnColor:compositingColor:];
+[UIVibrancyEffect _vibrancyEntryWithType:inputColor1:inputColor2:inputReversed:];
+[UIVibrancyEffect _vibrantEffectForLightMaterial:darkMaterial:vibrancyStyle:];
+[UIVibrancyEffect _vibrantEffectWithCAColorMatrix:alpha:];
+[UIVibrancyEffect _vibrantEffectWithLightCAColorMatrix:darkCAColorMatrix:alpha:];
+[UIVibrancyEffect _vibrantEffectWithLightCAColorMatrix:darkCAColorMatrix:tintColor:];
+[UIVibrancyEffect _vibrantEffectWithLightVibrantColorMatrix:darkVibrantColorMatrix:alpha:];
+[UIVibrancyEffect _vibrantShadowEffect];
+[UIVibrancyEffect darkVibrantEffectWithDodgeColor:lightenColor:compositingColor:];
+[UIVibrancyEffect effectForBlurEffect:];
+[UIVibrancyEffect effectForBlurEffect:style:];
+[UIVibrancyEffect lightVibrantEffectWithBurnColor:darkenColor:compositingColor:];
+[UIVibrancyEffect vibrantChromeShadowEffect];
+[UIVibrancyEffect vibrantEffectWithCompositingMode:compositingColor:];
+[UIVibrancyEffect vibrantHeavyShadowEffect];
+[UIVibrancyEffect vibrantMediumShadowEffect];
```

## Instance methods

```
-[UIVibrancyEffect _expectedUsage];
-[UIVibrancyEffect effectForUserInterfaceStyle:];
-[UIVibrancyEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[UIVibrancyEffect init];
-[UIVibrancyEffect _initWithImplementation:];
-[UIVibrancyEffect _isAutomaticStyle];
-[UIVibrancyEffect effectConfig];
-[UIVibrancyEffect _blurStyle];
-[UIVibrancyEffect _isATVStyle];
-[UIVibrancyEffect _updateEffectDescriptor:forEnvironment:usage:];
-[UIVibrancyEffect _reduceTransparencyEffectConfig];
-[UIVibrancyEffect effectConfigForQuality:];
-[UIVibrancyEffect encodeWithCoder:];
-[UIVibrancyEffect hash];
-[UIVibrancyEffect effectConfigForReducedTransperancy:];
-[UIVibrancyEffect description];
-[UIVibrancyEffect initWithCoder:];
-[UIVibrancyEffect copyWithZone:];
-[UIVibrancyEffect _vibrancyStyle];
-[UIVibrancyEffect isEqual:];
-[UIVibrancyEffect _effectReplacingTintColor:];
```
