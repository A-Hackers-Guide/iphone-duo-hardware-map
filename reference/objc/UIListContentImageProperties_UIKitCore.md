# `UIListContentImageProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 14 properties, 38 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedPreferredSymbolConfiguration"b1"hasCustomizedTintColor"b1"hasCustomizedTintColorTransformer"b1"hasCustomizedCornerRadius"b1"hasCustomizedReservedLayoutSize"b1"hasCustomizedMaximumSize"b1"hasCustomizedAccessibilityIgnoresInvertColors"b1"hasCustomizedStrokeColor"b1"hasCustomizedStrokeColorTransformer"b1"hasCustomizedStrokeWidth"b1"hasCustomizedMonochromaticTreatment"b1} _imageFlags;
B _accessibilityIgnoresInvertColors;
@"UIImage" _image;
@"UIImageSymbolConfiguration" _preferredSymbolConfiguration;
@"UIColor" _tintColor;
@? _tintColorTransformer;
d _cornerRadius;
@"UIColor" _strokeColor;
@? _strokeColorTransformer;
d _strokeWidth;
q _tintColorTransformerIdentifier;
q _strokeColorTransformerIdentifier;
q __monochromaticTreatment;
{CGSize="width"d"height"d} _reservedLayoutSize;
{CGSize="width"d"height"d} _maximumSize;
```

## Properties

```
@property (T@"UIColor",&,N,S_setStrokeColor:) _strokeColor;
@property (T@?,C,N,S_setStrokeColorTransformer:) _strokeColorTransformer;
@property (Td,N,S_setStrokeWidth:) _strokeWidth;
@property (Tq,N,S_setMonochromaticTreatment:) _monochromaticTreatment;
@property (T@"UIImageSymbolConfiguration",C,N) preferredSymbolConfiguration;
@property (T@"UIColor",&,N) tintColor;
@property (T@?,C,N) tintColorTransformer;
@property (Td,N) cornerRadius;
@property (T{CGSize=dd},N) maximumSize;
@property (T{CGSize=dd},N) reservedLayoutSize;
@property (TB,N) accessibilityIgnoresInvertColors;
@property (Td,N) strokeWidth;
@property (T@"UIColor",&,N) strokeColor;
@property (T@?,C,N) strokeColorTransformer;
```

## Class methods

```
+[UIListContentImageProperties supportsSecureCoding];
```

## Instance methods

```
-[UIListContentImageProperties setAccessibilityIgnoresInvertColors:];
-[UIListContentImageProperties setStrokeColorTransformer:];
-[UIListContentImageProperties strokeColorTransformer];
-[UIListContentImageProperties resolvedStrokeColorForTintColor:];
-[UIListContentImageProperties setMaximumSize:];
-[UIListContentImageProperties _setStrokeColor:];
-[UIListContentImageProperties maximumSize];
-[UIListContentImageProperties preferredSymbolConfiguration];
-[UIListContentImageProperties setStrokeWidth:];
-[UIListContentImageProperties init];
-[UIListContentImageProperties accessibilityIgnoresInvertColors];
-[UIListContentImageProperties reservedLayoutSize];
-[UIListContentImageProperties strokeWidth];
-[UIListContentImageProperties _strokeWidth];
-[UIListContentImageProperties setPreferredSymbolConfiguration:];
-[UIListContentImageProperties setStrokeColor:];
-[UIListContentImageProperties strokeColor];
-[UIListContentImageProperties setCornerRadius:];
-[UIListContentImageProperties resolvedTintColorForTintColor:];
-[UIListContentImageProperties setTintColor:];
-[UIListContentImageProperties _strokeColorTransformer];
-[UIListContentImageProperties setTintColorTransformer:];
-[UIListContentImageProperties cornerRadius];
-[UIListContentImageProperties encodeWithCoder:];
-[UIListContentImageProperties _setMonochromaticTreatment:];
-[UIListContentImageProperties setReservedLayoutSize:];
-[UIListContentImageProperties hash];
-[UIListContentImageProperties description];
-[UIListContentImageProperties _setStrokeColorTransformer:];
-[UIListContentImageProperties tintColor];
-[UIListContentImageProperties initWithCoder:];
-[UIListContentImageProperties copyWithZone:];
-[UIListContentImageProperties tintColorTransformer];
-[UIListContentImageProperties _strokeColor];
-[UIListContentImageProperties _resolvedStrokeColorForTintColor:];
-[UIListContentImageProperties _setStrokeWidth:];
-[UIListContentImageProperties isEqual:];
-[UIListContentImageProperties _monochromaticTreatment];
```
