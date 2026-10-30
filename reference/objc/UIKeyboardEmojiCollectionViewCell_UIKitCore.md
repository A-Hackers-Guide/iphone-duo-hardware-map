# `UIKeyboardEmojiCollectionViewCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardEmojiStickerBaseCollectionViewCell`
- Protocols: `UIKeyboardEmojiDraggableViewDelegate`
- 11 instance variables, 16 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _unreleasedHighlight;
B _noResultsCell;
@"UILabel" _unreleasedBanner;
@"UIKeyboardEmoji" _emoji;
d _highlightPadding;
@"NSString" _usageSource;
@"NSString" _bundleID;
@"UIKeyboardEmojiDraggableView" _emojiLabel;
@"UIView" _navigationHighlightView;
@"UILabel" _noResultsLabel;
q _desiredFontSize;
```

## Properties

```
@property (T@"UILabel",&,N,V_unreleasedBanner) unreleasedBanner;
@property (T@"UIView",&,N,V_navigationHighlightView) navigationHighlightView;
@property (T@"UILabel",&,N,V_noResultsLabel) noResultsLabel;
@property (Tq,N,V_desiredFontSize) desiredFontSize;
@property (T@"UIKeyboardEmoji",C,N,V_emoji) emoji;
@property (Tq,N) emojiFontSize;
@property (Td,N,V_highlightPadding) highlightPadding;
@property (T@"NSString",C,N,V_usageSource) usageSource;
@property (T@"NSString",C,N,V_bundleID) bundleID;
@property (T@"UIKeyboardEmojiDraggableView",R,N,V_emojiLabel) emojiLabel;
@property (TB,N,V_unreleasedHighlight) unreleasedHighlight;
@property (TB,N,V_noResultsCell) noResultsCell;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardEmojiCollectionViewCell setSelected:];
-[UIKeyboardEmojiCollectionViewCell debugDescription];
-[UIKeyboardEmojiCollectionViewCell setBundleID:];
-[UIKeyboardEmojiCollectionViewCell layoutSubviews];
-[UIKeyboardEmojiCollectionViewCell accessibilityIdentifier];
-[UIKeyboardEmojiCollectionViewCell bundleID];
-[UIKeyboardEmojiCollectionViewCell initWithFrame:];
-[UIKeyboardEmojiCollectionViewCell desiredFontSize];
-[UIKeyboardEmojiCollectionViewCell setUsageSource:];
-[UIKeyboardEmojiCollectionViewCell _dragAllowed];
-[UIKeyboardEmojiCollectionViewCell emoji];
-[UIKeyboardEmojiCollectionViewCell emojiFontSize];
-[UIKeyboardEmojiCollectionViewCell emojiLabel];
-[UIKeyboardEmojiCollectionViewCell highlightPadding];
-[UIKeyboardEmojiCollectionViewCell navigationHighlightView];
-[UIKeyboardEmojiCollectionViewCell noResultsCell];
-[UIKeyboardEmojiCollectionViewCell noResultsLabel];
-[UIKeyboardEmojiCollectionViewCell setCurrentEmojiFontSize:];
-[UIKeyboardEmojiCollectionViewCell setDesiredFontSize:];
-[UIKeyboardEmojiCollectionViewCell setEmoji:];
-[UIKeyboardEmojiCollectionViewCell setEmojiFontSize:];
-[UIKeyboardEmojiCollectionViewCell setHighlightPadding:];
-[UIKeyboardEmojiCollectionViewCell setNavigationHighlightView:];
-[UIKeyboardEmojiCollectionViewCell setNoResultsCell:];
-[UIKeyboardEmojiCollectionViewCell setNoResultsLabel:];
-[UIKeyboardEmojiCollectionViewCell setUnreleasedBanner:];
-[UIKeyboardEmojiCollectionViewCell setUnreleasedHighlight:];
-[UIKeyboardEmojiCollectionViewCell triggerUsageSignal:payload:];
-[UIKeyboardEmojiCollectionViewCell unreleasedBanner];
-[UIKeyboardEmojiCollectionViewCell unreleasedHighlight];
-[UIKeyboardEmojiCollectionViewCell usageSource];
```
