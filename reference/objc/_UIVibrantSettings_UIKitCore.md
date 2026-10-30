# `_UIVibrantSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 21 instance methods, 1 class methods

## Instance variables

```
q _style;
@"UIColor" _referenceColor;
@"_UILegibilitySettings" _legibilitySettings;
d _referenceContrast;
@"UIColor" _tintColor;
@"UIColor" _shimmerColor;
@"UIColor" _chevronShimmerColor;
@"UIColor" _highlightColor;
@"UIColor" _highlightLimitingColor;
```

## Properties

```
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (T@"UIColor",&,N,V_highlightLimitingColor) highlightLimitingColor;
@property (T@"UIColor",&,N,V_shimmerColor) shimmerColor;
@property (T@"UIColor",&,N,V_chevronShimmerColor) chevronShimmerColor;
@property (T@"UIColor",&,N,V_highlightColor) highlightColor;
@property (T@"UIColor",R,N,V_referenceColor) referenceColor;
@property (Td,R,N,V_referenceContrast) referenceContrast;
@property (T@"_UILegibilitySettings",R,N,V_legibilitySettings) legibilitySettings;
@property (Tq,R,N,V_style) style;
```

## Class methods

```
+[_UIVibrantSettings vibrantSettingsWithReferenceColor:referenceContrast:legibilitySettings:];
```

## Instance methods

```
-[_UIVibrantSettings setShimmerColor:];
-[_UIVibrantSettings shimmerColor];
-[_UIVibrantSettings setHighlightColor:];
-[_UIVibrantSettings style];
-[_UIVibrantSettings setTintColor:];
-[_UIVibrantSettings hash];
-[_UIVibrantSettings highlightColor];
-[_UIVibrantSettings _style];
-[_UIVibrantSettings legibilitySettings];
-[_UIVibrantSettings tintColor];
-[_UIVibrantSettings isEqual:];
-[_UIVibrantSettings highlightLimitingViewWithFrame:];
-[_UIVibrantSettings _computeSourceColorDodgeColorForDestinationColor:producingLuminanceChange:];
-[_UIVibrantSettings chevronShimmerColor];
-[_UIVibrantSettings highlightLimitingColor];
-[_UIVibrantSettings initWithReferenceColor:referenceContrast:legibilitySettings:];
-[_UIVibrantSettings referenceColor];
-[_UIVibrantSettings referenceContrast];
-[_UIVibrantSettings setChevronShimmerColor:];
-[_UIVibrantSettings setHighlightLimitingColor:];
-[_UIVibrantSettings tintViewWithFrame:];
```
