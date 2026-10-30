# `UIListContentTextProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIListContentTextPropertiesInternal`, `NSCopying`, `NSSecureCoding`
- 18 instance variables, 17 properties, 43 instance methods, 1 class methods

## Instance variables

```
{?="hasCustomizedFont"b1"hasCustomizedColor"b1"hasCustomizedColorTransformer"b1"hasCustomizedAlignment"b1"hasCustomizedLineBreakMode"b1"hasCustomizedNumberOfLines"b1"hasCustomizedAdjustsFontSizeToFitWidth"b1"hasCustomizedMinimumScaleFactor"b1"hasCustomizedAllowsDefaultTighteningForTruncation"b1"hasCustomizedAdjustsFontForContentSizeCategory"b1"hasCustomizedShowsExpansionTextWhenTruncated"b1"hasCustomizedTransform"b1"hasCustomizedMarqueeWhenAncestorFocused"b1"hasCustomizedMonochromaticTreatment"b1} _textFlags;
B _adjustsFontSizeToFitWidth;
B _allowsDefaultTighteningForTruncation;
B _adjustsFontForContentSizeCategory;
B _showsExpansionTextWhenTruncated;
B __enablesMarqueeWhenAncestorFocused;
@"NSString" _text;
@"UIFont" _font;
@"UIColor" _color;
@? _colorTransformer;
q _alignment;
q _lineBreakMode;
@"NSAttributedString" _attributedText;
q _numberOfLines;
d _minimumScaleFactor;
q _transform;
q __monochromaticTreatment;
q _colorTransformerIdentifier;
```

## Properties

```
@property (T@"NSString",C,N) text;
@property (TB,N,S_setEnablesMarqueeWhenAncestorFocused:) _enablesMarqueeWhenAncestorFocused;
@property (Tq,N,S_setMonochromaticTreatment:) _monochromaticTreatment;
@property (T@"UIFont",&,N) font;
@property (T@"UIColor",&,N) color;
@property (T@?,C,N) colorTransformer;
@property (Tq,N) alignment;
@property (Tq,N) lineBreakMode;
@property (Tq,N) numberOfLines;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (Td,N) minimumScaleFactor;
@property (TB,N) allowsDefaultTighteningForTruncation;
@property (TB,N) adjustsFontForContentSizeCategory;
@property (TB,N) showsExpansionTextWhenTruncated;
@property (Tq,N) transform;
@property (Tq,R,N) _effectiveTextAlignment;
@property (TB,R,N) _hasNonEmptyPlainTextOnly;
```

## Class methods

```
+[UIListContentTextProperties supportsSecureCoding];
```

## Instance methods

```
-[UIListContentTextProperties setColor:];
-[UIListContentTextProperties adjustsFontForContentSizeCategory];
-[UIListContentTextProperties setAdjustsFontForContentSizeCategory:];
-[UIListContentTextProperties setShowsExpansionTextWhenTruncated:];
-[UIListContentTextProperties debugDescription];
-[UIListContentTextProperties text];
-[UIListContentTextProperties init];
-[UIListContentTextProperties allowsDefaultTighteningForTruncation];
-[UIListContentTextProperties numberOfLines];
-[UIListContentTextProperties setAdjustsFontSizeToFitWidth:];
-[UIListContentTextProperties setAlignment:];
-[UIListContentTextProperties setTransform:];
-[UIListContentTextProperties transform];
-[UIListContentTextProperties alignment];
-[UIListContentTextProperties color];
-[UIListContentTextProperties _effectiveTextAlignment];
-[UIListContentTextProperties _enablesMarqueeWhenAncestorFocused];
-[UIListContentTextProperties _hasText];
-[UIListContentTextProperties minimumScaleFactor];
-[UIListContentTextProperties _setEnablesMarqueeWhenAncestorFocused:];
-[UIListContentTextProperties adjustsFontSizeToFitWidth];
-[UIListContentTextProperties encodeWithCoder:];
-[UIListContentTextProperties _setMonochromaticTreatment:];
-[UIListContentTextProperties setNumberOfLines:];
-[UIListContentTextProperties hash];
-[UIListContentTextProperties colorTransformer];
-[UIListContentTextProperties description];
-[UIListContentTextProperties initWithCoder:];
-[UIListContentTextProperties _applyToTextField:];
-[UIListContentTextProperties setText:];
-[UIListContentTextProperties resolvedColor];
-[UIListContentTextProperties font];
-[UIListContentTextProperties setAllowsDefaultTighteningForTruncation:];
-[UIListContentTextProperties copyWithZone:];
-[UIListContentTextProperties _hasNonEmptyPlainTextOnly];
-[UIListContentTextProperties showsExpansionTextWhenTruncated];
-[UIListContentTextProperties isEqual:];
-[UIListContentTextProperties setMinimumScaleFactor:];
-[UIListContentTextProperties setLineBreakMode:];
-[UIListContentTextProperties _monochromaticTreatment];
-[UIListContentTextProperties setColorTransformer:];
-[UIListContentTextProperties lineBreakMode];
-[UIListContentTextProperties setFont:];
```
