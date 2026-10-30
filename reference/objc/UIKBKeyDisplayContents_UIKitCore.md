# `UIKBKeyDisplayContents`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _fillPath;
B _force1xImages;
B _stringKeycapOverImage;
B _flipImageHorizontally;
B _forceImageKeycap;
@"NSString" _displayString;
@"NSString" _displayStringImage;
@"NSArray" _secondaryDisplayStrings;
@"NSArray" _secondaryDisplayStringImages;
@"NSArray" _variantDisplayContents;
@"NSArray" _highlightedVariantsList;
q _displayPathType;
@"UIKBKeyDisplayContents" _fallbackContents;
@"NSString" _bundlePathOverride;
@"UIImage" _displayImage;
```

## Properties

```
@property (T@"NSString",&,N,V_displayString) displayString;
@property (T@"NSString",&,N,V_displayStringImage) displayStringImage;
@property (T@"NSArray",&,N,V_secondaryDisplayStrings) secondaryDisplayStrings;
@property (T@"NSArray",&,N,V_secondaryDisplayStringImages) secondaryDisplayStringImages;
@property (T@"UIImage",&,N,V_displayImage) displayImage;
@property (T@"NSString",&,N,V_bundlePathOverride) bundlePathOverride;
@property (T@"NSArray",&,N,V_variantDisplayContents) variantDisplayContents;
@property (T@"NSArray",&,N,V_highlightedVariantsList) highlightedVariantsList;
@property (Tq,N,V_displayPathType) displayPathType;
@property (TB,N,V_fillPath) fillPath;
@property (TB,N,V_force1xImages) force1xImages;
@property (TB,N,V_stringKeycapOverImage) stringKeycapOverImage;
@property (TB,N,V_flipImageHorizontally) flipImageHorizontally;
@property (TB,N,V_forceImageKeycap) forceImageKeycap;
@property (T@"UIKBKeyDisplayContents",&,N,V_fallbackContents) fallbackContents;
```

## Class methods

```
+[UIKBKeyDisplayContents displayContents];
```

## Instance methods

```
-[UIKBKeyDisplayContents displayImage];
-[UIKBKeyDisplayContents setForceImageKeycap:];
-[UIKBKeyDisplayContents setFallbackContents:];
-[UIKBKeyDisplayContents displayPathType];
-[UIKBKeyDisplayContents setSecondaryDisplayStrings:];
-[UIKBKeyDisplayContents setBundlePathOverride:];
-[UIKBKeyDisplayContents setDisplayImage:];
-[UIKBKeyDisplayContents setFillPath:];
-[UIKBKeyDisplayContents secondaryDisplayStringImages];
-[UIKBKeyDisplayContents setStringKeycapOverImage:];
-[UIKBKeyDisplayContents setFlipImageHorizontally:];
-[UIKBKeyDisplayContents setSecondaryDisplayStringImages:];
-[UIKBKeyDisplayContents highlightedVariantsList];
-[UIKBKeyDisplayContents setDisplayPathType:];
-[UIKBKeyDisplayContents displayString];
-[UIKBKeyDisplayContents setDisplayString:];
-[UIKBKeyDisplayContents setForce1xImages:];
-[UIKBKeyDisplayContents fallbackContents];
-[UIKBKeyDisplayContents setVariantDisplayContents:];
-[UIKBKeyDisplayContents setDisplayStringImage:];
-[UIKBKeyDisplayContents fillPath];
-[UIKBKeyDisplayContents stringKeycapOverImage];
-[UIKBKeyDisplayContents displayStringImage];
-[UIKBKeyDisplayContents flipImageHorizontally];
-[UIKBKeyDisplayContents secondaryDisplayStrings];
-[UIKBKeyDisplayContents description];
-[UIKBKeyDisplayContents setHighlightedVariantsList:];
-[UIKBKeyDisplayContents force1xImages];
-[UIKBKeyDisplayContents variantDisplayContents];
-[UIKBKeyDisplayContents bundlePathOverride];
-[UIKBKeyDisplayContents forceImageKeycap];
```
