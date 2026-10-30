# `_UIBadgeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _label;
@"NSMutableDictionary" _mergedTextAttributes;
@"NSString" _text;
@"NSDictionary" _textAttributes;
@"UIColor" _badgeColor;
@"_UIBadgeVisualStyle" _style;
{UIOffset="horizontal"d"vertical"d} _textOffset;
```

## Properties

```
@property (T@"NSString",C,N,V_text) text;
@property (T@"NSDictionary",C,N,V_textAttributes) textAttributes;
@property (T@"UIColor",C,N,V_badgeColor) badgeColor;
@property (T{UIOffset=dd},N,V_textOffset) textOffset;
@property (T@"_UIBadgeVisualStyle",&,N,V_style) style;
```

## Instance methods

```
-[_UIBadgeView text];
-[_UIBadgeView badgeColor];
-[_UIBadgeView initWithText:];
-[_UIBadgeView layoutSubviews];
-[_UIBadgeView style];
-[_UIBadgeView setStyle:];
-[_UIBadgeView sizeThatFits:];
-[_UIBadgeView setTextOffset:];
-[_UIBadgeView textOffset];
-[_UIBadgeView setText:];
-[_UIBadgeView setBadgeColor:];
-[_UIBadgeView _applyTextToLabel];
-[_UIBadgeView _setUpLabelIfNecessary];
-[_UIBadgeView setTextAttributes:];
-[_UIBadgeView textAttributes];
```
