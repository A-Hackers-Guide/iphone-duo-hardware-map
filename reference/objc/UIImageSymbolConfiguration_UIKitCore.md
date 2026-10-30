# `UIImageSymbolConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIImageConfiguration`
- 8 instance variables, 10 properties, 37 instance methods, 24 class methods

## Instance variables

```
d _pointSize;
{?="hasFixedPointSize"b1"usesHierarchicalColors"b1"prefersMulticolor"b1"specifiedPrefersMulticolor"b1"prefersMonochrome"b1"specifiedPrefersMonochrome"b1"variableValueMode"b2"colorRenderingMode"b2"suppressesMaterialRendering"b1} _configFlags;
@"NSDictionary" _namedColorStyles;
@"NSArray" _colors;
q _scale;
q _weight;
@"NSString" _textStyle;
d _customFontPointSizeMultiplier;
```

## Properties

```
@property (Tq,R,N,V_scale) scale;
@property (Tq,R,N,V_weight) weight;
@property (T@"NSString",R,C,N,V_textStyle) textStyle;
@property (Td,R,N,V_customFontPointSizeMultiplier) customFontPointSizeMultiplier;
@property (Td,R,N) pointSizeForScalingWithTextStyle;
@property (T@"NSDictionary",R,N,V_namedColorStyles) _namedColorStyles;
@property (T@"NSArray",R,N,V_colors) _colors;
@property (Tq,R,N) variableValueMode;
@property (Tq,R,N) colorRenderingMode;
@property (TB,R,N) _suppressesMaterialRendering;
```

## Class methods

```
+[UIImageSymbolConfiguration supportsSecureCoding];
+[UIImageSymbolConfiguration unspecifiedConfiguration];
+[UIImageSymbolConfiguration defaultConfiguration];
+[UIImageSymbolConfiguration configurationWithPaletteColors:];
+[UIImageSymbolConfiguration _configurationWithColorRenderingMode:];
+[UIImageSymbolConfiguration _configurationWithHierarchicalColors:];
+[UIImageSymbolConfiguration _configurationWithNamedColorStyles:];
+[UIImageSymbolConfiguration _configurationWithVariableValueMode:];
+[UIImageSymbolConfiguration _defaultConfiguration];
+[UIImageSymbolConfiguration _unspecifiedConfiguration];
+[UIImageSymbolConfiguration configurationPreferringMonochrome];
+[UIImageSymbolConfiguration configurationPreferringMulticolor];
+[UIImageSymbolConfiguration configurationWithColorRenderingMode:];
+[UIImageSymbolConfiguration configurationWithFont:];
+[UIImageSymbolConfiguration configurationWithFont:scale:];
+[UIImageSymbolConfiguration configurationWithHierarchicalColor:];
+[UIImageSymbolConfiguration configurationWithPointSize:];
+[UIImageSymbolConfiguration configurationWithPointSize:weight:];
+[UIImageSymbolConfiguration configurationWithPointSize:weight:scale:];
+[UIImageSymbolConfiguration configurationWithScale:];
+[UIImageSymbolConfiguration configurationWithTextStyle:];
+[UIImageSymbolConfiguration configurationWithTextStyle:scale:];
+[UIImageSymbolConfiguration configurationWithVariableValueMode:];
+[UIImageSymbolConfiguration configurationWithWeight:];
```

## Instance methods

```
-[UIImageSymbolConfiguration _shouldApplyConfiguration:];
-[UIImageSymbolConfiguration isEqualToConfiguration:];
-[UIImageSymbolConfiguration _isEquivalentToConfiguration:];
-[UIImageSymbolConfiguration _initWithTraitCollection:];
-[UIImageSymbolConfiguration _isUnspecified];
-[UIImageSymbolConfiguration variableValueMode];
-[UIImageSymbolConfiguration configurationWithoutScale];
-[UIImageSymbolConfiguration _colorForNamedStyle:renditionContext:resolveDynamicColors:];
-[UIImageSymbolConfiguration _suppressesMaterialRendering];
-[UIImageSymbolConfiguration weight];
-[UIImageSymbolConfiguration _applyConfigurationValuesTo:];
-[UIImageSymbolConfiguration scale];
-[UIImageSymbolConfiguration customFontPointSizeMultiplier];
-[UIImageSymbolConfiguration _deriveGlyphSize:weight:pointSize:];
-[UIImageSymbolConfiguration _hasSpecifiedPaletteColors];
-[UIImageSymbolConfiguration _hasSpecifiedScale];
-[UIImageSymbolConfiguration _paletteColorsWithRenditionContext:resolveDynamicColors:];
-[UIImageSymbolConfiguration configurationWithoutWeight];
-[UIImageSymbolConfiguration _hasColorConfigurationWithTintColor];
-[UIImageSymbolConfiguration encodeWithCoder:];
-[UIImageSymbolConfiguration _namedColorStyles];
-[UIImageSymbolConfiguration hash];
-[UIImageSymbolConfiguration description];
-[UIImageSymbolConfiguration initWithCoder:];
-[UIImageSymbolConfiguration pointSizeForScalingWithTextStyle];
-[UIImageSymbolConfiguration configurationWithoutPointSizeAndWeight];
-[UIImageSymbolConfiguration _configurationSuppressingMaterialRendering];
-[UIImageSymbolConfiguration _configurationByReplacingColors:];
-[UIImageSymbolConfiguration copyWithZone:];
-[UIImageSymbolConfiguration textStyle];
-[UIImageSymbolConfiguration isEqual:];
-[UIImageSymbolConfiguration configurationWithoutTextStyle];
-[UIImageSymbolConfiguration _colors];
-[UIImageSymbolConfiguration _hasSpecifiedHierarchicalColors];
-[UIImageSymbolConfiguration _prefersMulticolor];
-[UIImageSymbolConfiguration _prefersMonochrome];
-[UIImageSymbolConfiguration colorRenderingMode];
```
