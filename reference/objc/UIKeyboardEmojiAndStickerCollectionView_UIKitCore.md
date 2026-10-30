# `UIKeyboardEmojiAndStickerCollectionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionView`
- Protocols: `UIKeyboardEmojiCollectionInputViewDelegate`
- 7 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIKeyboardEmojiGraphicsTraits" _emojiGraphicsTraits;
@"UIKeyboardEmojiCollectionViewCell" _lastTouchedEmojiCell;
@"NSMutableArray" _gestureRecognizersToEnable;
B _touchDidMove;
@"NSIndexPath" _rearrangingPath;
B _isInSearchPopover;
@"UIResponder" _hitTestResponder;
```

## Properties

```
@property (T@"UIResponder",W,N,V_hitTestResponder) hitTestResponder;
@property (T@"UIKeyboardEmojiGraphicsTraits",R,V_emojiGraphicsTraits) emojiGraphicsTraits;
@property (TB,N,V_isInSearchPopover) isInSearchPopover;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardEmojiAndStickerCollectionView touchesEnded:withEvent:];
-[UIKeyboardEmojiAndStickerCollectionView touchesCancelled:withEvent:];
-[UIKeyboardEmojiAndStickerCollectionView layoutSubviews];
-[UIKeyboardEmojiAndStickerCollectionView hitTest:withEvent:];
-[UIKeyboardEmojiAndStickerCollectionView touchesBegan:withEvent:];
-[UIKeyboardEmojiAndStickerCollectionView touchesMoved:withEvent:];
-[UIKeyboardEmojiAndStickerCollectionView accessibilityIdentifier];
-[UIKeyboardEmojiAndStickerCollectionView backgroundColor];
-[UIKeyboardEmojiAndStickerCollectionView _currentScreenScale];
-[UIKeyboardEmojiAndStickerCollectionView closestCellForPoint:];
-[UIKeyboardEmojiAndStickerCollectionView disableConflictingGestureRecognizers];
-[UIKeyboardEmojiAndStickerCollectionView emojiGraphicsTraits];
-[UIKeyboardEmojiAndStickerCollectionView enableConflictingGestureRecognizers];
-[UIKeyboardEmojiAndStickerCollectionView hitTestResponder];
-[UIKeyboardEmojiAndStickerCollectionView initWithFrame:collectionViewLayout:emojiGraphicsTraits:];
-[UIKeyboardEmojiAndStickerCollectionView isInSearchPopover];
-[UIKeyboardEmojiAndStickerCollectionView setHitTestResponder:];
-[UIKeyboardEmojiAndStickerCollectionView setIsInSearchPopover:];
-[UIKeyboardEmojiAndStickerCollectionView willCancelVariants:];
```
