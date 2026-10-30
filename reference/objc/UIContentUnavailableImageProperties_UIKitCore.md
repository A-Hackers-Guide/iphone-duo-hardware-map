# `UIContentUnavailableImageProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedPreferredSymbolConfiguration"b1"hasCustomizedTintColor"b1"hasCustomizedCornerRadius"b1"hasCustomizedMaximumSize"b1"hasCustomizedAccessibilityIgnoresInvertColors"b1} _imageFlags;
B _accessibilityIgnoresInvertColors;
@"UIImage" _image;
@"UIImageSymbolConfiguration" _preferredSymbolConfiguration;
@"UIColor" _tintColor;
d _cornerRadius;
{CGSize="width"d"height"d} _maximumSize;
```

## Properties

```
@property (T@"UIImageSymbolConfiguration",C,N) preferredSymbolConfiguration;
@property (T@"UIColor",&,N) tintColor;
@property (Td,N) cornerRadius;
@property (T{CGSize=dd},N) maximumSize;
@property (TB,N) accessibilityIgnoresInvertColors;
```

## Class methods

```
+[UIContentUnavailableImageProperties supportsSecureCoding];
```

## Instance methods

```
-[UIContentUnavailableImageProperties setAccessibilityIgnoresInvertColors:];
-[UIContentUnavailableImageProperties setMaximumSize:];
-[UIContentUnavailableImageProperties maximumSize];
-[UIContentUnavailableImageProperties preferredSymbolConfiguration];
-[UIContentUnavailableImageProperties init];
-[UIContentUnavailableImageProperties accessibilityIgnoresInvertColors];
-[UIContentUnavailableImageProperties setPreferredSymbolConfiguration:];
-[UIContentUnavailableImageProperties setCornerRadius:];
-[UIContentUnavailableImageProperties setTintColor:];
-[UIContentUnavailableImageProperties cornerRadius];
-[UIContentUnavailableImageProperties encodeWithCoder:];
-[UIContentUnavailableImageProperties hash];
-[UIContentUnavailableImageProperties description];
-[UIContentUnavailableImageProperties tintColor];
-[UIContentUnavailableImageProperties initWithCoder:];
-[UIContentUnavailableImageProperties copyWithZone:];
-[UIContentUnavailableImageProperties isEqual:];
```
