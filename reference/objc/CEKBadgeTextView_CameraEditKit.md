# `CEKBadgeTextView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CEKBadgeView`
- 10 instance variables, 10 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _supportsMultilineText;
B _wantsLargerBadge;
B __symbolTrailing;
@"NSString" _contentSizeCategory;
Q _fontStyle;
@"NSDictionary" __textAttributes;
@"NSAttributedString" __symbolText;
@"NSString" __text;
@"NSString" __symbol;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __textInsets;
```

## Properties

```
@property (T@"NSDictionary",&,N,S_setTextAttributes:,V__textAttributes) _textAttributes;
@property (T@"NSAttributedString",&,N,S_setSymbolText:,V__symbolText) _symbolText;
@property (T@"NSString",C,N,S_setText:,V__text) _text;
@property (T@"NSString",C,N,S_setSymbol:,V__symbol) _symbol;
@property (T{UIEdgeInsets=dddd},N,S_setTextInsets:,V__textInsets) _textInsets;
@property (TB,N,S_setSymbolTrailing:,V__symbolTrailing) _symbolTrailing;
@property (T@"NSString",C,N,V_contentSizeCategory) contentSizeCategory;
@property (TQ,N,V_fontStyle) fontStyle;
@property (TB,N,V_supportsMultilineText) supportsMultilineText;
@property (TB,N,V_wantsLargerBadge) wantsLargerBadge;
```

## Class methods

```
+[CEKBadgeTextView _defaultTextInsets];
```

## Instance methods

```
-[CEKBadgeTextView setFontStyle:];
-[CEKBadgeTextView fontStyle];
-[CEKBadgeTextView intrinsicContentSize];
-[CEKBadgeTextView _textInsets];
-[CEKBadgeTextView setContentSizeCategory:];
-[CEKBadgeTextView _preferredContentSizeCategoryChanged];
-[CEKBadgeTextView wantsLargerBadge];
-[CEKBadgeTextView setWantsLargerBadge:];
-[CEKBadgeTextView initWithFrame:];
-[CEKBadgeTextView contentSizeCategory];
-[CEKBadgeTextView _maskImage];
-[CEKBadgeTextView _text];
-[CEKBadgeTextView _textSize];
-[CEKBadgeTextView _setText:];
-[CEKBadgeTextView _textAttributes];
-[CEKBadgeTextView _setTextInsets:];
-[CEKBadgeTextView _updateAttributedString];
-[CEKBadgeTextView _setSymbol:];
-[CEKBadgeTextView _setSymbolTrailing:];
-[CEKBadgeTextView setSupportsMultilineText:];
-[CEKBadgeTextView _symbol];
-[CEKBadgeTextView _setSymbolText:];
-[CEKBadgeTextView _symbolTrailing];
-[CEKBadgeTextView _didUpdateContents];
-[CEKBadgeTextView _fontForContentSize:];
-[CEKBadgeTextView _setTextAttributes:];
-[CEKBadgeTextView _symbolText];
-[CEKBadgeTextView _textAttributesForContentSize:];
-[CEKBadgeTextView supportsMultilineText];
```
