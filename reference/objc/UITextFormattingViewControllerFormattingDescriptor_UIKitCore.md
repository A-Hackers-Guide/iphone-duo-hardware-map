# `UITextFormattingViewControllerFormattingDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 19 instance variables, 18 properties, 48 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _attributes;
B _underlinePresent;
B _strikethroughPresent;
B __canToggleBold;
B __canToggleItalic;
q _underline;
q _strikethrough;
q _listStyle;
@"NSArray" _fonts;
@"NSArray" _textColors;
d _lineHeight;
@"NSSet" _textAlignments;
@"NSSet" _textLists;
@"NSSet" _highlights;
@"NSString" _formattingStyleKey;
@"NSParagraphStyle" __paragraphStyle;
@"NSSet" __customComponentKeys;
@"NSString" __emphasisStyleKey;
q __blockquote;
```

## Properties

```
@property (T@"NSParagraphStyle",C,N,V__paragraphStyle) _paragraphStyle;
@property (T@"NSSet",C,N,V__customComponentKeys) _customComponentKeys;
@property (T@"NSString",C,N,V__emphasisStyleKey) _emphasisStyleKey;
@property (Tq,N,V__blockquote) _blockquote;
@property (TB,N,V__canToggleBold) _canToggleBold;
@property (TB,N,V__canToggleItalic) _canToggleItalic;
@property (Tq,N,V_underline) underline;
@property (Tq,N,V_strikethrough) strikethrough;
@property (Tq,N,V_listStyle) listStyle;
@property (T@"NSArray",C,N,V_fonts) fonts;
@property (T@"NSArray",C,N,V_textColors) textColors;
@property (Td,N,V_lineHeight) lineHeight;
@property (TB,N,V_underlinePresent) underlinePresent;
@property (TB,N,V_strikethroughPresent) strikethroughPresent;
@property (T@"NSSet",C,N,V_textAlignments) textAlignments;
@property (T@"NSSet",C,N,V_textLists) textLists;
@property (T@"NSSet",C,N,V_highlights) highlights;
@property (T@"NSString",C,N,V_formattingStyleKey) formattingStyleKey;
```

## Class methods

```
+[UITextFormattingViewControllerFormattingDescriptor supportsSecureCoding];
+[UITextFormattingViewControllerFormattingDescriptor _canToggleTrait:forFont:inText:];
+[UITextFormattingViewControllerFormattingDescriptor _canToggleTrait:forFont:];
```

## Instance methods

```
-[UITextFormattingViewControllerFormattingDescriptor _setAttributes:];
-[UITextFormattingViewControllerFormattingDescriptor initWithAttributes:];
-[UITextFormattingViewControllerFormattingDescriptor _attributes];
-[UITextFormattingViewControllerFormattingDescriptor init];
-[UITextFormattingViewControllerFormattingDescriptor highlights];
-[UITextFormattingViewControllerFormattingDescriptor _paragraphStyle];
-[UITextFormattingViewControllerFormattingDescriptor encodeWithCoder:];
-[UITextFormattingViewControllerFormattingDescriptor hash];
-[UITextFormattingViewControllerFormattingDescriptor initWithCoder:];
-[UITextFormattingViewControllerFormattingDescriptor setFonts:];
-[UITextFormattingViewControllerFormattingDescriptor copyWithZone:];
-[UITextFormattingViewControllerFormattingDescriptor isEqual:];
-[UITextFormattingViewControllerFormattingDescriptor fonts];
-[UITextFormattingViewControllerFormattingDescriptor setHighlights:];
-[UITextFormattingViewControllerFormattingDescriptor set_blockquote:];
-[UITextFormattingViewControllerFormattingDescriptor _blockquote];
-[UITextFormattingViewControllerFormattingDescriptor _canToggleBold];
-[UITextFormattingViewControllerFormattingDescriptor _canToggleItalic];
-[UITextFormattingViewControllerFormattingDescriptor _customComponentKeys];
-[UITextFormattingViewControllerFormattingDescriptor _emphasisStyleKey];
-[UITextFormattingViewControllerFormattingDescriptor _updateWithMatchingStyleIn:];
-[UITextFormattingViewControllerFormattingDescriptor formattingStyleKey];
-[UITextFormattingViewControllerFormattingDescriptor initWithString:range:];
-[UITextFormattingViewControllerFormattingDescriptor lineHeight];
-[UITextFormattingViewControllerFormattingDescriptor listStyle];
-[UITextFormattingViewControllerFormattingDescriptor matches:in:];
-[UITextFormattingViewControllerFormattingDescriptor setFormattingStyleKey:];
-[UITextFormattingViewControllerFormattingDescriptor setLineHeight:];
-[UITextFormattingViewControllerFormattingDescriptor setListStyle:];
-[UITextFormattingViewControllerFormattingDescriptor setStrikethrough:];
-[UITextFormattingViewControllerFormattingDescriptor setStrikethroughPresent:];
-[UITextFormattingViewControllerFormattingDescriptor setTextAlignments:];
-[UITextFormattingViewControllerFormattingDescriptor setTextColors:];
-[UITextFormattingViewControllerFormattingDescriptor setTextLists:];
-[UITextFormattingViewControllerFormattingDescriptor setUnderline:];
-[UITextFormattingViewControllerFormattingDescriptor setUnderlinePresent:];
-[UITextFormattingViewControllerFormattingDescriptor set_canToggleBold:];
-[UITextFormattingViewControllerFormattingDescriptor set_canToggleItalic:];
-[UITextFormattingViewControllerFormattingDescriptor set_customComponentKeys:];
-[UITextFormattingViewControllerFormattingDescriptor set_emphasisStyleKey:];
-[UITextFormattingViewControllerFormattingDescriptor set_paragraphStyle:];
-[UITextFormattingViewControllerFormattingDescriptor strikethrough];
-[UITextFormattingViewControllerFormattingDescriptor strikethroughPresent];
-[UITextFormattingViewControllerFormattingDescriptor textAlignments];
-[UITextFormattingViewControllerFormattingDescriptor textColors];
-[UITextFormattingViewControllerFormattingDescriptor textLists];
-[UITextFormattingViewControllerFormattingDescriptor underline];
-[UITextFormattingViewControllerFormattingDescriptor underlinePresent];
```
