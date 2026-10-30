# `_UIContentViewImageViewConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedImage"b1"hasCustomizedPreferredSymbolConfiguration"b1"hasCustomizedTintColor"b1"hasCustomizedCornerRadius"b1"hasCustomizedReservedLayoutSize"b1"hasCustomizedMaximumSize"b1} _configurationFlags;
@"UIImage" _image;
@"UIImageSymbolConfiguration" _preferredSymbolConfiguration;
@"UIColor" _tintColor;
d _cornerRadius;
@"UIImage" _highlightedImage;
{CGSize="width"d"height"d} _reservedLayoutSize;
{CGSize="width"d"height"d} _maximumSize;
```

## Properties

```
@property (T@"UIImage",&,N) image;
@property (T@"UIImageSymbolConfiguration",C,N) preferredSymbolConfiguration;
@property (T@"UIColor",&,N) tintColor;
@property (Td,N) cornerRadius;
@property (T{CGSize=dd},N) reservedLayoutSize;
@property (T{CGSize=dd},N) maximumSize;
@property (Td,N) horizontalCenteringWidth;
@property (T@"UIImage",&,N,V_highlightedImage) highlightedImage;
```

## Class methods

```
+[_UIContentViewImageViewConfiguration supportsSecureCoding];
```

## Instance methods

```
-[_UIContentViewImageViewConfiguration setMaximumSize:];
-[_UIContentViewImageViewConfiguration setHighlightedImage:];
-[_UIContentViewImageViewConfiguration maximumSize];
-[_UIContentViewImageViewConfiguration preferredSymbolConfiguration];
-[_UIContentViewImageViewConfiguration init];
-[_UIContentViewImageViewConfiguration reservedLayoutSize];
-[_UIContentViewImageViewConfiguration setPreferredSymbolConfiguration:];
-[_UIContentViewImageViewConfiguration setCornerRadius:];
-[_UIContentViewImageViewConfiguration setTintColor:];
-[_UIContentViewImageViewConfiguration cornerRadius];
-[_UIContentViewImageViewConfiguration encodeWithCoder:];
-[_UIContentViewImageViewConfiguration setReservedLayoutSize:];
-[_UIContentViewImageViewConfiguration hash];
-[_UIContentViewImageViewConfiguration description];
-[_UIContentViewImageViewConfiguration highlightedImage];
-[_UIContentViewImageViewConfiguration tintColor];
-[_UIContentViewImageViewConfiguration initWithCoder:];
-[_UIContentViewImageViewConfiguration image];
-[_UIContentViewImageViewConfiguration copyWithZone:];
-[_UIContentViewImageViewConfiguration isEqual:];
-[_UIContentViewImageViewConfiguration setImage:];
-[_UIContentViewImageViewConfiguration applyToImageView:];
-[_UIContentViewImageViewConfiguration horizontalCenteringWidth];
-[_UIContentViewImageViewConfiguration setHorizontalCenteringWidth:];
```
