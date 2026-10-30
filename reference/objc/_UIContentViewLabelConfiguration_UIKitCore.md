# `_UIContentViewLabelConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIListContentTextPropertiesInternal`, `NSCopying`, `NSSecureCoding`
- 13 instance variables, 14 properties, 36 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedFont"b1"hasCustomizedTextColor"b1"hasCustomizedTextAlignment"b1"hasCustomizedLineBreakMode"b1"hasCustomizedNumberOfLines"b1"hasCustomizedAdjustsFontSizeToFitWidth"b1"hasCustomizedMinimumScaleFactor"b1"hasCustomizedAllowsDefaultTighteningForTruncation"b1"hasCustomizedAdjustsFontForContentSizeCategory"b1} _configurationFlags;
B _adjustsFontSizeToFitWidth;
B _allowsDefaultTighteningForTruncation;
B _adjustsFontForContentSizeCategory;
@"NSString" _text;
@"UIFont" _font;
@"UIColor" _textColor;
q _textAlignment;
q _lineBreakMode;
@"NSAttributedString" _attributedText;
q _numberOfLines;
d _minimumScaleFactor;
@"UIColor" _highlightedTextColor;
```

## Properties

```
@property (T@"NSString",C,N) text;
@property (T@"UIFont",&,N) font;
@property (T@"UIColor",&,N) textColor;
@property (Tq,N) textAlignment;
@property (Tq,N) lineBreakMode;
@property (T@"NSAttributedString",C,N) attributedText;
@property (Tq,N) numberOfLines;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (Td,N) minimumScaleFactor;
@property (TB,N) allowsDefaultTighteningForTruncation;
@property (TB,N) adjustsFontForContentSizeCategory;
@property (T@"UIColor",&,N,V_highlightedTextColor) highlightedTextColor;
@property (Tq,R,N) _effectiveTextAlignment;
@property (TB,R,N) _hasNonEmptyPlainTextOnly;
```

## Class methods

```
+[_UIContentViewLabelConfiguration supportsSecureCoding];
```

## Instance methods

```
-[_UIContentViewLabelConfiguration setTextAlignment:];
-[_UIContentViewLabelConfiguration adjustsFontForContentSizeCategory];
-[_UIContentViewLabelConfiguration setHighlightedTextColor:];
-[_UIContentViewLabelConfiguration setAdjustsFontForContentSizeCategory:];
-[_UIContentViewLabelConfiguration textAlignment];
-[_UIContentViewLabelConfiguration text];
-[_UIContentViewLabelConfiguration textColor];
-[_UIContentViewLabelConfiguration init];
-[_UIContentViewLabelConfiguration allowsDefaultTighteningForTruncation];
-[_UIContentViewLabelConfiguration numberOfLines];
-[_UIContentViewLabelConfiguration setAttributedText:];
-[_UIContentViewLabelConfiguration setTextColor:];
-[_UIContentViewLabelConfiguration setAdjustsFontSizeToFitWidth:];
-[_UIContentViewLabelConfiguration _effectiveTextAlignment];
-[_UIContentViewLabelConfiguration _hasText];
-[_UIContentViewLabelConfiguration minimumScaleFactor];
-[_UIContentViewLabelConfiguration adjustsFontSizeToFitWidth];
-[_UIContentViewLabelConfiguration attributedText];
-[_UIContentViewLabelConfiguration encodeWithCoder:];
-[_UIContentViewLabelConfiguration setNumberOfLines:];
-[_UIContentViewLabelConfiguration hash];
-[_UIContentViewLabelConfiguration description];
-[_UIContentViewLabelConfiguration initWithCoder:];
-[_UIContentViewLabelConfiguration _applyToTextField:];
-[_UIContentViewLabelConfiguration setText:];
-[_UIContentViewLabelConfiguration font];
-[_UIContentViewLabelConfiguration setAllowsDefaultTighteningForTruncation:];
-[_UIContentViewLabelConfiguration copyWithZone:];
-[_UIContentViewLabelConfiguration _hasNonEmptyPlainTextOnly];
-[_UIContentViewLabelConfiguration isEqual:];
-[_UIContentViewLabelConfiguration highlightedTextColor];
-[_UIContentViewLabelConfiguration setMinimumScaleFactor:];
-[_UIContentViewLabelConfiguration setLineBreakMode:];
-[_UIContentViewLabelConfiguration lineBreakMode];
-[_UIContentViewLabelConfiguration setFont:];
-[_UIContentViewLabelConfiguration applyToLabel:];
```
