# `UIKeyboardEmojiCategoryBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardEmojiKeyView`
- 6 instance variables, 4 properties, 29 instance methods, 1 class methods

## Instance variables

```
Q _selectedIndex;
@"UIView" _scrubView;
@"UIKeyboardEmojiGraphicsTraits" _emojiGraphicsTraits;
B _isScrubbing;
d _scrubStartXLocation;
@"UIResponder<UIKBEmojiHitTestResponder>" _hitTestResponder;
```

## Properties

```
@property (T@"UIView",&,N,V_scrubView) scrubView;
@property (T@"UIKeyboardEmojiGraphicsTraits",&,N,V_emojiGraphicsTraits) emojiGraphicsTraits;
@property (T@"UIResponder<UIKBEmojiHitTestResponder>",N,V_hitTestResponder) hitTestResponder;
@property (TQ,V_selectedIndex) selectedIndex;
```

## Class methods

```
+[UIKeyboardEmojiCategoryBar wantsScreenTraits];
```

## Instance methods

```
-[UIKeyboardEmojiCategoryBar paddedFrame];
-[UIKeyboardEmojiCategoryBar touchesEnded:withEvent:];
-[UIKeyboardEmojiCategoryBar didMoveToWindow];
-[UIKeyboardEmojiCategoryBar dimKeys:];
-[UIKeyboardEmojiCategoryBar prepareForDisplay];
-[UIKeyboardEmojiCategoryBar initWithFrame:keyplane:key:];
-[UIKeyboardEmojiCategoryBar touchesCancelled:withEvent:];
-[UIKeyboardEmojiCategoryBar selectedIndex];
-[UIKeyboardEmojiCategoryBar dealloc];
-[UIKeyboardEmojiCategoryBar layoutSubviews];
-[UIKeyboardEmojiCategoryBar touchesBegan:withEvent:];
-[UIKeyboardEmojiCategoryBar touchesMoved:withEvent:];
-[UIKeyboardEmojiCategoryBar removeFromSuperview];
-[UIKeyboardEmojiCategoryBar setSelectedIndex:];
-[UIKeyboardEmojiCategoryBar animateScrubberToRect:];
-[UIKeyboardEmojiCategoryBar categorySelectedCircleRect:];
-[UIKeyboardEmojiCategoryBar emojiGraphicsTraits];
-[UIKeyboardEmojiCategoryBar flippedIndexForIndex:];
-[UIKeyboardEmojiCategoryBar frameForDivider:];
-[UIKeyboardEmojiCategoryBar hitTestResponder];
-[UIKeyboardEmojiCategoryBar initWithFrame:keyplane:key:screenTraits:];
-[UIKeyboardEmojiCategoryBar scrubView];
-[UIKeyboardEmojiCategoryBar selectedIndexForTouches:];
-[UIKeyboardEmojiCategoryBar setEmojiGraphicsTraits:];
-[UIKeyboardEmojiCategoryBar setHitTestResponder:];
-[UIKeyboardEmojiCategoryBar setScrubView:];
-[UIKeyboardEmojiCategoryBar updateCategory];
-[UIKeyboardEmojiCategoryBar updateCategoryOnBar:];
-[UIKeyboardEmojiCategoryBar updateToCategory:];
```
