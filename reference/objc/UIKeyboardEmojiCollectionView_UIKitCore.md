# `UIKeyboardEmojiCollectionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionView`
- 6 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIKeyboardEmojiGraphicsTraits" _emojiGraphicsTraits;
@"UIKeyboardEmojiCollectionViewCell" _lastTouchedEmojiCell;
@"NSMutableArray" _gestureRecognizersToEnable;
B _touchDidMove;
B _isInSearchPopover;
@"UIResponder" _hitTestResponder;
```

## Properties

```
@property (TB,N,V_isInSearchPopover) isInSearchPopover;
@property (T@"UIResponder",W,N,V_hitTestResponder) hitTestResponder;
@property (T@"UIKeyboardEmojiGraphicsTraits",R,V_emojiGraphicsTraits) emojiGraphicsTraits;
```

## Instance methods

```
-[UIKeyboardEmojiCollectionView touchesEnded:withEvent:];
-[UIKeyboardEmojiCollectionView touchesCancelled:withEvent:];
-[UIKeyboardEmojiCollectionView layoutSubviews];
-[UIKeyboardEmojiCollectionView touchesBegan:withEvent:];
-[UIKeyboardEmojiCollectionView touchesMoved:withEvent:];
-[UIKeyboardEmojiCollectionView backgroundColor];
-[UIKeyboardEmojiCollectionView _currentScreenScale];
-[UIKeyboardEmojiCollectionView closestCellForPoint:];
-[UIKeyboardEmojiCollectionView disableConflictingGestureRecognizers];
-[UIKeyboardEmojiCollectionView emojiGraphicsTraits];
-[UIKeyboardEmojiCollectionView enableConflictingGestureRecognizers];
-[UIKeyboardEmojiCollectionView hitTestResponder];
-[UIKeyboardEmojiCollectionView initWithFrame:collectionViewLayout:emojiGraphicsTraits:];
-[UIKeyboardEmojiCollectionView isInSearchPopover];
-[UIKeyboardEmojiCollectionView setHitTestResponder:];
-[UIKeyboardEmojiCollectionView setIsInSearchPopover:];
-[UIKeyboardEmojiCollectionView willCancelVariants:];
```
