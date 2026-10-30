# `UIContentUnavailableTextProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedText"b1"hasCustomizedFont"b1"hasCustomizedColor"b1"hasCustomizedLineBreakMode"b1"hasCustomizedAttributedText"b1"hasCustomizedNumberOfLines"b1"hasCustomizedAdjustsFontSizeToFitWidth"b1"hasCustomizedMinimumScaleFactor"b1"hasCustomizedAllowsDefaultTighteningForTruncation"b1"hasCustomizedWidthFraction"b1} _textFlags;
B _adjustsFontSizeToFitWidth;
B _allowsDefaultTighteningForTruncation;
@"NSString" _text;
@"UIFont" _font;
@"UIColor" _color;
q _lineBreakMode;
@"NSAttributedString" _attributedText;
q _numberOfLines;
d _minimumScaleFactor;
d _widthFraction;
q _alignment;
```

## Properties

```
@property (T@"UIFont",&,N) font;
@property (T@"UIColor",&,N) color;
@property (Tq,N) lineBreakMode;
@property (Tq,N) numberOfLines;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (Td,N) minimumScaleFactor;
@property (TB,N) allowsDefaultTighteningForTruncation;
```

## Class methods

```
+[UIContentUnavailableTextProperties supportsSecureCoding];
```

## Instance methods

```
-[UIContentUnavailableTextProperties setColor:];
-[UIContentUnavailableTextProperties init];
-[UIContentUnavailableTextProperties allowsDefaultTighteningForTruncation];
-[UIContentUnavailableTextProperties numberOfLines];
-[UIContentUnavailableTextProperties setAdjustsFontSizeToFitWidth:];
-[UIContentUnavailableTextProperties color];
-[UIContentUnavailableTextProperties minimumScaleFactor];
-[UIContentUnavailableTextProperties adjustsFontSizeToFitWidth];
-[UIContentUnavailableTextProperties encodeWithCoder:];
-[UIContentUnavailableTextProperties setNumberOfLines:];
-[UIContentUnavailableTextProperties hash];
-[UIContentUnavailableTextProperties description];
-[UIContentUnavailableTextProperties initWithCoder:];
-[UIContentUnavailableTextProperties font];
-[UIContentUnavailableTextProperties setAllowsDefaultTighteningForTruncation:];
-[UIContentUnavailableTextProperties copyWithZone:];
-[UIContentUnavailableTextProperties isEqual:];
-[UIContentUnavailableTextProperties setMinimumScaleFactor:];
-[UIContentUnavailableTextProperties setLineBreakMode:];
-[UIContentUnavailableTextProperties lineBreakMode];
-[UIContentUnavailableTextProperties setFont:];
```
