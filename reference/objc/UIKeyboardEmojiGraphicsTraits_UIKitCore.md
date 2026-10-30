# `UIKeyboardEmojiGraphicsTraits`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 20 properties, 21 instance methods, 2 class methods

## Instance variables

```
B _isFirstPartyStickers;
d _emojiKeyWidth;
d _minimumLineSpacing;
d _minimumInteritemSpacing;
d _columnOffset;
d _sectionOffset;
d _bottomPadding;
d _categoryHeaderHeight;
d _categoryHeaderLeftPadding;
d _categorySelectedCirWidth;
d _categoryHeaderFontSize;
q _prepolulatedRecentCount;
d _inputViewLeftMostPadding;
d _inputViewRightMostPadding;
d _rightBiasPercentage;
d _scrollSnapOffset;
d _screenToNativeScaleRatio;
d _topPadding;
d _categoryHeaderBottomInset;
d _alertTextWidth;
{CGSize="width"d"height"d} _fakeEmojiKeySize;
```

## Properties

```
@property (Td,R,N,V_emojiKeyWidth) emojiKeyWidth;
@property (Td,R,N,V_minimumLineSpacing) minimumLineSpacing;
@property (Td,R,N,V_minimumInteritemSpacing) minimumInteritemSpacing;
@property (Td,R,N,V_columnOffset) columnOffset;
@property (Td,R,N,V_sectionOffset) sectionOffset;
@property (Td,R,N,V_topPadding) topPadding;
@property (Td,R,N,V_bottomPadding) bottomPadding;
@property (Td,R,N,V_categoryHeaderHeight) categoryHeaderHeight;
@property (Td,R,N,V_categoryHeaderBottomInset) categoryHeaderBottomInset;
@property (Td,R,N,V_categoryHeaderLeftPadding) categoryHeaderLeftPadding;
@property (Td,R,N,V_categorySelectedCirWidth) categorySelectedCirWidth;
@property (T{CGSize=dd},R,N,V_fakeEmojiKeySize) fakeEmojiKeySize;
@property (Td,R,N,V_categoryHeaderFontSize) categoryHeaderFontSize;
@property (Tq,R,N,V_prepolulatedRecentCount) prepolulatedRecentCount;
@property (Td,R,N,V_inputViewLeftMostPadding) inputViewLeftMostPadding;
@property (Td,R,N,V_inputViewRightMostPadding) inputViewRightMostPadding;
@property (Td,R,N,V_rightBiasPercentage) rightBiasPercentage;
@property (Td,R,N,V_alertTextWidth) alertTextWidth;
@property (Td,R,N,V_scrollSnapOffset) scrollSnapOffset;
@property (Td,R,N,V_screenToNativeScaleRatio) screenToNativeScaleRatio;
```

## Class methods

```
+[UIKeyboardEmojiGraphicsTraits emojiGraphicsTraitsForCurrentScreenTraits];
+[UIKeyboardEmojiGraphicsTraits emojiGraphicsTraitsWithScreenTraits:];
```

## Instance methods

```
-[UIKeyboardEmojiGraphicsTraits bottomPadding];
-[UIKeyboardEmojiGraphicsTraits topPadding];
-[UIKeyboardEmojiGraphicsTraits columnOffset];
-[UIKeyboardEmojiGraphicsTraits screenToNativeScaleRatio];
-[UIKeyboardEmojiGraphicsTraits alertTextWidth];
-[UIKeyboardEmojiGraphicsTraits categoryHeaderBottomInset];
-[UIKeyboardEmojiGraphicsTraits categoryHeaderFontSize];
-[UIKeyboardEmojiGraphicsTraits categoryHeaderHeight];
-[UIKeyboardEmojiGraphicsTraits categoryHeaderLeftPadding];
-[UIKeyboardEmojiGraphicsTraits categorySelectedCirWidth];
-[UIKeyboardEmojiGraphicsTraits emojiKeyWidth];
-[UIKeyboardEmojiGraphicsTraits fakeEmojiKeySize];
-[UIKeyboardEmojiGraphicsTraits initWithScreenTrait:];
-[UIKeyboardEmojiGraphicsTraits inputViewLeftMostPadding];
-[UIKeyboardEmojiGraphicsTraits inputViewRightMostPadding];
-[UIKeyboardEmojiGraphicsTraits minimumInteritemSpacing];
-[UIKeyboardEmojiGraphicsTraits minimumLineSpacing];
-[UIKeyboardEmojiGraphicsTraits prepolulatedRecentCount];
-[UIKeyboardEmojiGraphicsTraits rightBiasPercentage];
-[UIKeyboardEmojiGraphicsTraits scrollSnapOffset];
-[UIKeyboardEmojiGraphicsTraits sectionOffset];
```
