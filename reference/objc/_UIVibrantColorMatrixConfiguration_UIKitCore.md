# `_UIVibrantColorMatrixConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _preservesHue;
d _maxColorComponent;
{CAColorMatrix="m11"f"m12"f"m13"f"m14"f"m15"f"m21"f"m22"f"m23"f"m24"f"m25"f"m31"f"m32"f"m33"f"m34"f"m35"f"m41"f"m42"f"m43"f"m44"f"m45"f} _colorMatrix;
```

## Properties

```
@property (T{CAColorMatrix=ffffffffffffffffffff},N,V_colorMatrix) colorMatrix;
@property (Td,N,V_maxColorComponent) maxColorComponent;
@property (TB,N,V_preservesHue) preservesHue;
```

## Class methods

```
+[_UIVibrantColorMatrixConfiguration _vibrantColorMatrixConfigurationWithColorMatrix:maxColorComponent:preservesHue:];
```

## Instance methods

```
-[_UIVibrantColorMatrixConfiguration setColorMatrix:];
-[_UIVibrantColorMatrixConfiguration preservesHue];
-[_UIVibrantColorMatrixConfiguration setPreservesHue:];
-[_UIVibrantColorMatrixConfiguration maxColorComponent];
-[_UIVibrantColorMatrixConfiguration setMaxColorComponent:];
-[_UIVibrantColorMatrixConfiguration colorMatrix];
-[_UIVibrantColorMatrixConfiguration hash];
-[_UIVibrantColorMatrixConfiguration isEqual:];
```
