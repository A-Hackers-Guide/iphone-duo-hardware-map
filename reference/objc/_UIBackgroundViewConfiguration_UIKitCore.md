# `_UIBackgroundViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIBackgroundConfigurationInternal`, `NSCopying`, `NSSecureCoding`
- 18 instance variables, 32 properties, 65 instance methods, 17 class methods

## Instance variables

```
{?="hasCustomizedCustomView"b1"hasCustomizedCornerRadius"b1"hasCustomizedBackgroundInsets"b1"hasCustomizedEdgesAddingLayoutMarginsToBackgroundInsets"b1"hasCustomizedBackgroundColorOrMode"b1"hasCustomizedVisualEffect"b1"hasCustomizedStrokeColorOrMode"b1"hasCustomizedStrokeWidth"b1"hasCustomizedStrokeOutset"b1} _configurationFlags;
@"UIView" _customView;
d _cornerRadius;
Q _edgesAddingLayoutMarginsToBackgroundInsets;
q _backgroundColorMode;
@"UIColor" _backgroundColor;
@"UIVisualEffect" _visualEffect;
q _strokeColorMode;
@"UIColor" _strokeColor;
d _strokeWidth;
d _strokeOutset;
@"UIShadowProperties" _shadowProperties;
q _defaultStyle;
q _strokeLocation;
Q _maskedCorners;
@"NSString" _visualEffectGroupName;
Q _visualEffectblurClippingMode;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _backgroundInsets;
```

## Properties

```
@property (T@"UIShadowProperties",&,N,S_setShadowProperties:,V_shadowProperties) _shadowProperties;
@property (T@"UIView",&,N) customView;
@property (Td,N) cornerRadius;
@property (T{NSDirectionalEdgeInsets=dddd},N) backgroundInsets;
@property (TQ,N) edgesAddingLayoutMarginsToBackgroundInsets;
@property (Tq,N) backgroundColorMode;
@property (T@"UIColor",&,N) backgroundColor;
@property (T@"UIVisualEffect",C,N) visualEffect;
@property (Tq,N) strokeColorMode;
@property (T@"UIColor",&,N) strokeColor;
@property (Td,N) strokeWidth;
@property (Td,N) strokeOutset;
@property (TB,R,N) isTintBackgroundColor;
@property (T@"UIImage",&,N) image;
@property (Tq,N) imageContentMode;
@property (Tq,N,G_strokeLocation,S_setStrokeLocation:,V_strokeLocation) strokeLocation;
@property (TQ,N,S__setMaskedCorners:,V_maskedCorners) __maskedCorners;
@property (T@"NSString",C,N,S__setVisualEffectGroupName:,V_visualEffectGroupName) __visualEffectGroupName;
@property (Td,N,S_setCornerRadius:,V_cornerRadius) _cornerRadius;
@property (TB,R,N,G_hasBackgroundColor) hasBackgroundColor;
@property (TB,R,N,G_hasStroke) hasStroke;
@property (TB,R,N,G_hasBackgroundFill) hasBackgroundFill;
@property (TQ,N,S__setVisualEffectblurClippingMode:,V_visualEffectblurClippingMode) __visualEffectblurClippingMode;
@property (TB,R,N,G_hasMaterial) hasMaterial;
@property (T@"<_UIViewMaterial>",&,N,S_setMaterial:) _material;
@property (TB,R,N,G_hasContentView) hasContentView;
@property (T@"UIView",&,N,S_setContentView:) _contentView;
@property (TB,N,S_setContentViewIgnoresBackgroundInsets:) _contentViewIgnoresBackgroundInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBackgroundViewConfiguration supportsSecureCoding];
+[_UIBackgroundViewConfiguration defaultGroupedListCellConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultGroupedListHeaderFooterConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultInsetGroupedListCellConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultInsetGroupedListHeaderFooterConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultOutlineCellConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultOutlineParentCellConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultPlainListCellConfigurationForState:];
+[_UIBackgroundViewConfiguration defaultPlainListHeaderFooterConfigurationForState:];
+[_UIBackgroundViewConfiguration groupedListCellConfiguration];
+[_UIBackgroundViewConfiguration groupedListHeaderFooterConfiguration];
+[_UIBackgroundViewConfiguration insetGroupedListCellConfiguration];
+[_UIBackgroundViewConfiguration insetGroupedListHeaderFooterConfiguration];
+[_UIBackgroundViewConfiguration outlineCellConfiguration];
+[_UIBackgroundViewConfiguration outlineRootParentCellConfiguration];
+[_UIBackgroundViewConfiguration plainListCellConfiguration];
+[_UIBackgroundViewConfiguration plainListHeaderFooterConfiguration];
```

## Instance methods

```
-[_UIBackgroundViewConfiguration imageContentMode];
-[_UIBackgroundViewConfiguration setImageContentMode:];
-[_UIBackgroundViewConfiguration resolvedStrokeColorForTintColor:];
-[_UIBackgroundViewConfiguration customView];
-[_UIBackgroundViewConfiguration _setCornerRadius:];
-[_UIBackgroundViewConfiguration _setShadowProperties:];
-[_UIBackgroundViewConfiguration _hasBackgroundFill];
-[_UIBackgroundViewConfiguration _setMaterial:];
-[_UIBackgroundViewConfiguration _hasBackgroundColor];
-[_UIBackgroundViewConfiguration _setContentView:];
-[_UIBackgroundViewConfiguration setStrokeWidth:];
-[_UIBackgroundViewConfiguration _setStrokeLocation:];
-[_UIBackgroundViewConfiguration _cornerRadius];
-[_UIBackgroundViewConfiguration init];
-[_UIBackgroundViewConfiguration _hasMaterial];
-[_UIBackgroundViewConfiguration strokeWidth];
-[_UIBackgroundViewConfiguration strokeOutset];
-[_UIBackgroundViewConfiguration _contentViewIgnoresBackgroundInsets];
-[_UIBackgroundViewConfiguration setStrokeColor:];
-[_UIBackgroundViewConfiguration _contentView];
-[_UIBackgroundViewConfiguration setEdgesAddingLayoutMarginsToBackgroundInsets:];
-[_UIBackgroundViewConfiguration __setVisualEffectblurClippingMode:];
-[_UIBackgroundViewConfiguration visualEffect];
-[_UIBackgroundViewConfiguration _strokeLocation];
-[_UIBackgroundViewConfiguration strokeColor];
-[_UIBackgroundViewConfiguration setCornerRadius:];
-[_UIBackgroundViewConfiguration _backgroundFillIsEqual:withTintColor:];
-[_UIBackgroundViewConfiguration __setVisualEffectGroupName:];
-[_UIBackgroundViewConfiguration _updatedConfigurationForState:];
-[_UIBackgroundViewConfiguration setBackgroundColor:];
-[_UIBackgroundViewConfiguration _material];
-[_UIBackgroundViewConfiguration updatedConfigurationForState:];
-[_UIBackgroundViewConfiguration __maskedCorners];
-[_UIBackgroundViewConfiguration __visualEffectblurClippingMode];
-[_UIBackgroundViewConfiguration setStrokeOutset:];
-[_UIBackgroundViewConfiguration _isEqualToInternalConfigurationLayoutOnly:];
-[_UIBackgroundViewConfiguration cornerRadius];
-[_UIBackgroundViewConfiguration encodeWithCoder:];
-[_UIBackgroundViewConfiguration setCustomView:];
-[_UIBackgroundViewConfiguration __setMaskedCorners:];
-[_UIBackgroundViewConfiguration hash];
-[_UIBackgroundViewConfiguration backgroundColor];
-[_UIBackgroundViewConfiguration description];
-[_UIBackgroundViewConfiguration _setContentViewIgnoresBackgroundInsets:];
-[_UIBackgroundViewConfiguration __visualEffectGroupName];
-[_UIBackgroundViewConfiguration initWithCoder:];
-[_UIBackgroundViewConfiguration _hasContentView];
-[_UIBackgroundViewConfiguration setBackgroundInsets:];
-[_UIBackgroundViewConfiguration _isEqualToInternalConfigurationQuick:];
-[_UIBackgroundViewConfiguration _shadowProperties];
-[_UIBackgroundViewConfiguration isTintBackgroundColor];
-[_UIBackgroundViewConfiguration image];
-[_UIBackgroundViewConfiguration copyWithZone:];
-[_UIBackgroundViewConfiguration isEqual:];
-[_UIBackgroundViewConfiguration _hasStroke];
-[_UIBackgroundViewConfiguration edgesAddingLayoutMarginsToBackgroundInsets];
-[_UIBackgroundViewConfiguration backgroundInsets];
-[_UIBackgroundViewConfiguration resolvedBackgroundColorForTintColor:];
-[_UIBackgroundViewConfiguration setVisualEffect:];
-[_UIBackgroundViewConfiguration setImage:];
-[_UIBackgroundViewConfiguration strokeColorMode];
-[_UIBackgroundViewConfiguration backgroundColorMode];
-[_UIBackgroundViewConfiguration setBackgroundColorMode:];
-[_UIBackgroundViewConfiguration setStrokeColorMode:];
-[_UIBackgroundViewConfiguration updatedConfigurationForState:traitCollection:];
```
