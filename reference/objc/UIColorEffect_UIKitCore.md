# `UIColorEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- 7 instance variables, 0 properties, 13 instance methods, 19 class methods

## Instance variables

```
@"NSString" _filterType;
@"UIColor" _backgroundColor;
@"NSDictionary" _configurationValues;
@"NSDictionary" _identityValues;
@"NSDictionary" _requestedValues;
@? _sourceColorUpdater;
B _disableInPlaceFiltering;
```

## Class methods

```
+[UIColorEffect supportsSecureCoding];
+[UIColorEffect colorEffectAdd:];
+[UIColorEffect _colorEffectCAMatrix:];
+[UIColorEffect _colorEffectSourceOver:];
+[UIColorEffect colorEffectBlendColor:];
+[UIColorEffect colorEffectBrightness:];
+[UIColorEffect colorEffectColor:];
+[UIColorEffect colorEffectContrast:];
+[UIColorEffect colorEffectCurvesRed:green:blue:alpha:];
+[UIColorEffect colorEffectInvert];
+[UIColorEffect colorEffectLightMatrix:darkMatrix:];
+[UIColorEffect colorEffectLuminanceCurveMap:blendingAmount:];
+[UIColorEffect colorEffectLuminanceMap:blendingAmount:];
+[UIColorEffect colorEffectMatrix:];
+[UIColorEffect colorEffectMonochromeTint:blendingAmount:brightnessAdjustment:];
+[UIColorEffect colorEffectMultiply:];
+[UIColorEffect colorEffectSaturate:];
+[UIColorEffect colorEffectSubtract:];
+[UIColorEffect effectWithColor:];
```

## Instance methods

```
-[UIColorEffect _expectedUsage];
-[UIColorEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[UIColorEffect init];
-[UIColorEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:changedTraits:usage:];
-[UIColorEffect _filterEntryForTraitCollection:];
-[UIColorEffect _updateEffectDescriptor:forEnvironment:usage:];
-[UIColorEffect encodeWithCoder:];
-[UIColorEffect hash];
-[UIColorEffect description];
-[UIColorEffect initWithCoder:];
-[UIColorEffect copyWithZone:];
-[UIColorEffect isEqual:];
-[UIColorEffect _filterEntry];
```
