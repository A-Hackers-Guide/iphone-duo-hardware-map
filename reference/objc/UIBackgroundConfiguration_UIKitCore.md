# `UIBackgroundConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIBackgroundConfigurationInternal`, `NSCopying`, `NSSecureCoding`
- 25 instance variables, 37 properties, 72 instance methods, 14 class methods

## Instance variables

```
{?="hasCustomizedCustomView"b1"hasCustomizedCornerRadius"b1"hasCustomizedBackgroundInsets"b1"hasCustomizedEdgesAddingLayoutMarginsToBackgroundInsets"b1"hasCustomizedBackgroundColor"b1"hasCustomizedBackgroundColorTransformer"b1"hasCustomizedVisualEffect"b1"hasCustomizedVisualEffectGroupName"b1"hasCustomizedVisualEffectblurClippingMode"b1"hasCustomizedImage"b1"hasCustomizedImageContentMode"b1"hasCustomizedStrokeColor"b1"hasCustomizedStrokeColorTransformer"b1"hasCustomizedStrokeWidth"b1"hasCustomizedStrokeOutset"b1"hasCustomizedMaskedCorners"b1"hasCustomizedMaterial"b1} _configurationFlags;
B _contentViewIgnoresBackgroundInsets;
@"UIView" _customView;
d _cornerRadius;
Q _edgesAddingLayoutMarginsToBackgroundInsets;
@"UIColor" _backgroundColor;
@? _backgroundColorTransformer;
@"UIVisualEffect" _visualEffect;
@"NSString" _visualEffectGroupName;
@"UIImage" _image;
q _imageContentMode;
@"UIColor" _strokeColor;
@? _strokeColorTransformer;
d _strokeWidth;
d _strokeOutset;
@"UIShadowProperties" _shadowProperties;
Q _maskedCorners;
Q _visualEffectblurClippingMode;
q _defaultStyle;
q _backgroundColorTransformerIdentifier;
q _strokeColorTransformerIdentifier;
q _strokeLocation;
@"UIView" _contentView;
@"<_UIViewMaterial>" _material;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _backgroundInsets;
```

## Properties

```
@property (T@"UIShadowProperties",&,N,S_setShadowProperties:,V_shadowProperties) _shadowProperties;
@property (TQ,N,S_setMaskedCorners:) _maskedCorners;
@property (T@"NSString",C,N,S_setVisualEffectGroupName:) _visualEffectGroupName;
@property (TB,N,S_setVisualEffectAllowsTransparentBlurring:) _visualEffectAllowsTransparentBlurring;
@property (TQ,N,S_setVisualEffectblurClippingMode:) _visualEffectblurClippingMode;
@property (T@"UIView",&,N) customView;
@property (Td,N) cornerRadius;
@property (T{NSDirectionalEdgeInsets=dddd},N) backgroundInsets;
@property (TQ,N) edgesAddingLayoutMarginsToBackgroundInsets;
@property (T@"UIColor",&,N) backgroundColor;
@property (T@?,C,N) backgroundColorTransformer;
@property (T@"UIVisualEffect",C,N) visualEffect;
@property (T@"UIImage",&,N) image;
@property (Tq,N) imageContentMode;
@property (T@"UIColor",&,N) strokeColor;
@property (T@?,C,N) strokeColorTransformer;
@property (Td,N) strokeWidth;
@property (Td,N) strokeOutset;
@property (T@"UIShadowProperties",R,N) shadowProperties;
@property (TB,R,N) isTintBackgroundColor;
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
@property (T@"UIView",&,N,S_setContentView:,V_contentView) _contentView;
@property (TB,N,S_setContentViewIgnoresBackgroundInsets:,V_contentViewIgnoresBackgroundInsets) _contentViewIgnoresBackgroundInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIBackgroundConfiguration supportsSecureCoding];
+[UIBackgroundConfiguration listPlainCellConfiguration];
+[UIBackgroundConfiguration _listInsetGroupedHeaderFooterConfiguration];
+[UIBackgroundConfiguration _listInsetGroupedCellConfiguration];
+[UIBackgroundConfiguration listSidebarCellConfiguration];
+[UIBackgroundConfiguration clearConfiguration];
+[UIBackgroundConfiguration listFooterConfiguration];
+[UIBackgroundConfiguration listHeaderConfiguration];
+[UIBackgroundConfiguration listSidebarHeaderConfiguration];
+[UIBackgroundConfiguration listCellConfiguration];
+[UIBackgroundConfiguration listGroupedCellConfiguration];
+[UIBackgroundConfiguration listAccompaniedSidebarCellConfiguration];
+[UIBackgroundConfiguration listGroupedHeaderFooterConfiguration];
+[UIBackgroundConfiguration listPlainHeaderFooterConfiguration];
```

## Instance methods

```
-[UIBackgroundConfiguration imageContentMode];
-[UIBackgroundConfiguration setStrokeColorTransformer:];
-[UIBackgroundConfiguration strokeColorTransformer];
-[UIBackgroundConfiguration setImageContentMode:];
-[UIBackgroundConfiguration resolvedStrokeColorForTintColor:];
-[UIBackgroundConfiguration customView];
-[UIBackgroundConfiguration _setCornerRadius:];
-[UIBackgroundConfiguration _setShadowProperties:];
-[UIBackgroundConfiguration _hasBackgroundFill];
-[UIBackgroundConfiguration _setMaterial:];
-[UIBackgroundConfiguration shadowProperties];
-[UIBackgroundConfiguration _hasBackgroundColor];
-[UIBackgroundConfiguration _setContentView:];
-[UIBackgroundConfiguration setStrokeWidth:];
-[UIBackgroundConfiguration _setVisualEffectGroupName:];
-[UIBackgroundConfiguration _setStrokeLocation:];
-[UIBackgroundConfiguration _cornerRadius];
-[UIBackgroundConfiguration _hasMaterial];
-[UIBackgroundConfiguration strokeWidth];
-[UIBackgroundConfiguration strokeOutset];
-[UIBackgroundConfiguration _contentViewIgnoresBackgroundInsets];
-[UIBackgroundConfiguration setStrokeColor:];
-[UIBackgroundConfiguration _contentView];
-[UIBackgroundConfiguration setEdgesAddingLayoutMarginsToBackgroundInsets:];
-[UIBackgroundConfiguration __setVisualEffectblurClippingMode:];
-[UIBackgroundConfiguration visualEffect];
-[UIBackgroundConfiguration _strokeLocation];
-[UIBackgroundConfiguration strokeColor];
-[UIBackgroundConfiguration setCornerRadius:];
-[UIBackgroundConfiguration _backgroundFillIsEqual:withTintColor:];
-[UIBackgroundConfiguration __setVisualEffectGroupName:];
-[UIBackgroundConfiguration _updatedConfigurationForState:];
-[UIBackgroundConfiguration setBackgroundColor:];
-[UIBackgroundConfiguration _material];
-[UIBackgroundConfiguration updatedConfigurationForState:];
-[UIBackgroundConfiguration __maskedCorners];
-[UIBackgroundConfiguration __visualEffectblurClippingMode];
-[UIBackgroundConfiguration setStrokeOutset:];
-[UIBackgroundConfiguration _visualEffectblurClippingMode];
-[UIBackgroundConfiguration _maskedCorners];
-[UIBackgroundConfiguration setBackgroundColorTransformer:];
-[UIBackgroundConfiguration _isEqualToInternalConfigurationLayoutOnly:];
-[UIBackgroundConfiguration cornerRadius];
-[UIBackgroundConfiguration encodeWithCoder:];
-[UIBackgroundConfiguration setCustomView:];
-[UIBackgroundConfiguration __setMaskedCorners:];
-[UIBackgroundConfiguration hash];
-[UIBackgroundConfiguration backgroundColor];
-[UIBackgroundConfiguration description];
-[UIBackgroundConfiguration _setContentViewIgnoresBackgroundInsets:];
-[UIBackgroundConfiguration __visualEffectGroupName];
-[UIBackgroundConfiguration initWithCoder:];
-[UIBackgroundConfiguration _hasContentView];
-[UIBackgroundConfiguration setBackgroundInsets:];
-[UIBackgroundConfiguration _visualEffectAllowsTransparentBlurring];
-[UIBackgroundConfiguration backgroundColorTransformer];
-[UIBackgroundConfiguration _isEqualToInternalConfigurationQuick:];
-[UIBackgroundConfiguration _shadowProperties];
-[UIBackgroundConfiguration isTintBackgroundColor];
-[UIBackgroundConfiguration image];
-[UIBackgroundConfiguration _visualEffectGroupName];
-[UIBackgroundConfiguration copyWithZone:];
-[UIBackgroundConfiguration isEqual:];
-[UIBackgroundConfiguration _hasStroke];
-[UIBackgroundConfiguration edgesAddingLayoutMarginsToBackgroundInsets];
-[UIBackgroundConfiguration backgroundInsets];
-[UIBackgroundConfiguration _setMaskedCorners:];
-[UIBackgroundConfiguration _setVisualEffectblurClippingMode:];
-[UIBackgroundConfiguration resolvedBackgroundColorForTintColor:];
-[UIBackgroundConfiguration _setVisualEffectAllowsTransparentBlurring:];
-[UIBackgroundConfiguration setVisualEffect:];
-[UIBackgroundConfiguration setImage:];
```
