# `_UIVibrancyEffectVibrantColorMatrixImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIVibrancyEffectImpl`
- 6 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
q _systemName;
@"_UIVibrantColorMatrixConfiguration" _lightConfiguration;
@"_UIVibrantColorMatrixConfiguration" _darkConfiguration;
@"UIColor" _reducedTransperancyColor;
@"UIColor" _tintColor;
B _hasDarkVariant;
```

## Instance methods

```
-[_UIVibrancyEffectVibrantColorMatrixImpl appendDescriptionTo:];
-[_UIVibrancyEffectVibrantColorMatrixImpl implementationReplacingTintColor:];
-[_UIVibrancyEffectVibrantColorMatrixImpl initWithLightConfiguration:darkConfiguration:alpha:];
-[_UIVibrancyEffectVibrantColorMatrixImpl initWithLightCAColorMatrix:darkCAColorMatrix:alpha:];
-[_UIVibrancyEffectVibrantColorMatrixImpl _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[_UIVibrancyEffectVibrantColorMatrixImpl initWithLightConfiguration:darkConfiguration:tintColor:];
-[_UIVibrancyEffectVibrantColorMatrixImpl initWithSystemName:];
-[_UIVibrancyEffectVibrantColorMatrixImpl initWithLightCAColorMatrix:darkCAColorMatrix:tintColor:];
-[_UIVibrancyEffectVibrantColorMatrixImpl _updateEffectDescriptor:forEnvironment:usage:];
-[_UIVibrancyEffectVibrantColorMatrixImpl encodeWithCoder:];
-[_UIVibrancyEffectVibrantColorMatrixImpl hash];
-[_UIVibrancyEffectVibrantColorMatrixImpl initWithCAColorMatrix:alpha:];
-[_UIVibrancyEffectVibrantColorMatrixImpl isEqual:];
```
