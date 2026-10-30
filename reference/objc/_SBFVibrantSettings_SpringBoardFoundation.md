# `_SBFVibrantSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
@property (T@"UIColor",&,N,V_highlightLimitingColor) highlightLimitingColor;
@property (T@"UIColor",&,N,V_shimmerColor) shimmerColor;
@property (T@"UIColor",&,N,V_chevronShimmerColor) chevronShimmerColor;
@property (T@"UIColor",&,N,V_highlightColor) highlightColor;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (T@"UIColor",R,N,V_referenceColor) referenceColor;
@property (Td,R,N,V_referenceContrast) referenceContrast;
@property (T@"_UILegibilitySettings",R,N,V_legibilitySettings) legibilitySettings;
@property (Tq,R,N,V_style) style;
```

## Class methods

```
+[_SBFVibrantSettings vibrantSettingsWithReferenceColor:referenceContrast:legibilitySettings:];
```

## Instance methods

```
-[_SBFVibrantSettings setShimmerColor:];
-[_SBFVibrantSettings shimmerColor];
-[_SBFVibrantSettings setHighlightColor:];
-[_SBFVibrantSettings style];
-[_SBFVibrantSettings setTintColor:];
-[_SBFVibrantSettings hash];
-[_SBFVibrantSettings highlightColor];
-[_SBFVibrantSettings _style];
-[_SBFVibrantSettings legibilitySettings];
-[_SBFVibrantSettings tintColor];
-[_SBFVibrantSettings isEqual:];
-[_SBFVibrantSettings highlightLimitingViewWithFrame:];
-[_SBFVibrantSettings _computeSourceColorDodgeColorForDestinationColor:producingLuminanceChange:];
-[_SBFVibrantSettings chevronShimmerColor];
-[_SBFVibrantSettings highlightLimitingColor];
-[_SBFVibrantSettings initWithReferenceColor:referenceContrast:legibilitySettings:];
-[_SBFVibrantSettings referenceColor];
-[_SBFVibrantSettings referenceContrast];
-[_SBFVibrantSettings setChevronShimmerColor:];
-[_SBFVibrantSettings setHighlightLimitingColor:];
-[_SBFVibrantSettings tintViewWithFrame:];
```
