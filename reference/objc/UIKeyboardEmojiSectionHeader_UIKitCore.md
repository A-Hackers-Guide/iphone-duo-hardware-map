# `UIKeyboardEmojiSectionHeader`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionReusableView`
- 3 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _emojiSectionHeader;
@"UIVisualEffectView" _backdropView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _insets;
```

## Properties

```
@property (T@"NSString",C,N) headerName;
@property (T@"UIColor",C,N) headerTextColor;
@property (Td,N) headerFontSize;
@property (Td,N) headerOpacity;
@property (TB,N) useVibrantBlend;
@property (T{UIEdgeInsets=dddd},N,V_insets) insets;
@property (T@"UIVisualEffect",C,N) effect;
```

## Instance methods

```
-[UIKeyboardEmojiSectionHeader layoutSubviews];
-[UIKeyboardEmojiSectionHeader effect];
-[UIKeyboardEmojiSectionHeader setEffect:];
-[UIKeyboardEmojiSectionHeader headerOpacity];
-[UIKeyboardEmojiSectionHeader initWithFrame:];
-[UIKeyboardEmojiSectionHeader headerTextColor];
-[UIKeyboardEmojiSectionHeader useVibrantBlend];
-[UIKeyboardEmojiSectionHeader headerFontSize];
-[UIKeyboardEmojiSectionHeader headerName];
-[UIKeyboardEmojiSectionHeader insets];
-[UIKeyboardEmojiSectionHeader setHeaderFontSize:];
-[UIKeyboardEmojiSectionHeader setHeaderName:];
-[UIKeyboardEmojiSectionHeader setHeaderOpacity:];
-[UIKeyboardEmojiSectionHeader setHeaderTextColor:];
-[UIKeyboardEmojiSectionHeader setInsets:];
-[UIKeyboardEmojiSectionHeader setUseVibrantBlend:];
```
