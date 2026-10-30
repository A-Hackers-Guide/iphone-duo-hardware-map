# `CUIShapeEffectPreset`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 39 instance methods, 8 class methods

## Instance variables

```
[125{?="effectType"I"effectParameter"I"effectValue"(?="floatValue"d"intValue"Q"colorValue"{_rgbcolor="r"C"g"C"b"C}"angleValue"s"enumValue"I)}] _parameterList;
[26I] _effectIndex;
d _scaleFactor;
f _minimumShadowSpread;
```

## Properties

```
@property (Tf,V_minimumShadowSpread) minimumShadowSpread;
```

## Class methods

```
+[CUIShapeEffectPreset caFilterFromCUIEffectBlendMode:];
+[CUIShapeEffectPreset cgBlendModeFromCUIEffectBlendMode:];
+[CUIShapeEffectPreset configureVibrantColorMatrixFilter:withOptions:];
+[CUIShapeEffectPreset cuiEffectBlendModeFromCGBlendMode:];
+[CUIShapeEffectPreset monochromeVibrantColorMatrixOptions];
+[CUIShapeEffectPreset requiredEffectParametersForEffectType:];
+[CUIShapeEffectPreset standardVibrantColorMatrixOptionsForColor:];
+[CUIShapeEffectPreset vibrantColorMatrixOptionsWithColor:saturation:brightness:];
```

## Instance methods

```
-[CUIShapeEffectPreset debugDescription];
-[CUIShapeEffectPreset init];
-[CUIShapeEffectPreset effectScale];
-[CUIShapeEffectPreset CUIEffectDataRepresentation];
-[CUIShapeEffectPreset _parameterCount];
-[CUIShapeEffectPreset _insertEffectTuple:atEffectIndex:];
-[CUIShapeEffectPreset addBevelEmbossWithHighlightColorRed:green:blue:opacity:shadowColorRed:green:blue:opacity:blur:soften:bevelStyle:];
-[CUIShapeEffectPreset addColorFillWithRed:green:blue:opacity:blendMode:tintable:];
-[CUIShapeEffectPreset addColorValueRed:green:blue:forParameter:withNewEffectType:];
-[CUIShapeEffectPreset addDropShadowWithColorRed:green:blue:opacity:blur:spread:offset:angle:];
-[CUIShapeEffectPreset addEffectsFromPreset:];
-[CUIShapeEffectPreset addEnumValue:forParameter:withNewEffectType:];
-[CUIShapeEffectPreset addExtraShadowWithColorRed:green:blue:opacity:blur:spread:offset:angle:];
-[CUIShapeEffectPreset addFloatValue:forParameter:withNewEffectType:];
-[CUIShapeEffectPreset addGradientFillWithTopColorRed:green:blue:bottomColorRed:green:blue:opacity:blendMode:];
-[CUIShapeEffectPreset addHueSaturationWithColorRed:green:blue:angle:width:tintable:];
-[CUIShapeEffectPreset addInnerGlowWithColorRed:green:blue:opacity:blur:blendMode:];
-[CUIShapeEffectPreset addInnerShadowWithColorRed:green:blue:opacity:blur:offset:angle:blendMode:];
-[CUIShapeEffectPreset addIntValue:forParameter:withNewEffectType:];
-[CUIShapeEffectPreset addOuterGlowWithColorRed:green:blue:opacity:blur:spread:];
-[CUIShapeEffectPreset addOutputOpacityWithOpacity:];
-[CUIShapeEffectPreset addShapeOpacityWithOpacity:];
-[CUIShapeEffectPreset addValue:forParameter:withEffectType:atEffectIndex:];
-[CUIShapeEffectPreset addValue:forParameter:withNewEffectType:];
-[CUIShapeEffectPreset appendAngleValue:forParameter:withEffectType:];
-[CUIShapeEffectPreset appendColorValueRed:green:blue:forParameter:withEffectType:];
-[CUIShapeEffectPreset appendEnumValue:forParameter:withEffectType:];
-[CUIShapeEffectPreset appendFloatValue:forParameter:withEffectType:];
-[CUIShapeEffectPreset appendIntValue:forParameter:withEffectType:];
-[CUIShapeEffectPreset appendValue:forParameter:withEffectType:];
-[CUIShapeEffectPreset effectCount];
-[CUIShapeEffectPreset effectTypeAtIndex:];
-[CUIShapeEffectPreset getEffectTuples:count:atEffectIndex:];
-[CUIShapeEffectPreset initWithConstantPreset:];
-[CUIShapeEffectPreset initWithEffectScale:];
-[CUIShapeEffectPreset layerEffectsRepresentation];
-[CUIShapeEffectPreset minimumShadowSpread];
-[CUIShapeEffectPreset setMinimumShadowSpread:];
-[CUIShapeEffectPreset valueForParameter:inEffectAtIndex:];
```
