# `UIKeyboardEmojiDraggableView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIDragInteractionDelegate_Private`
- 15 instance variables, 9 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _fixedLabel;
@"UIView" _liftContainerView;
@"UILabel" _previewLabel;
@"UIImageView" _upscaledImageView;
d _liftScale;
@"_MSStickerDragPreviewContainerView" _container;
@"UIDragInteraction" _dragInteraction;
B _shouldLiftFromLastTouchLocation;
{CGPoint="x"d"y"d} _lastTouchLocation;
B _lifted;
B _dragEnabled;
@"<UIKeyboardEmojiDraggableViewDelegate>" _delegate;
@"NSString" _text;
@"NSAttributedString" _attributedText;
@"UIFont" _font;
```

## Properties

```
@property (T@"<UIKeyboardEmojiDraggableViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",&,N,V_text) text;
@property (T@"NSAttributedString",&,N,V_attributedText) attributedText;
@property (T@"UIFont",&,N,V_font) font;
@property (TB,N,V_dragEnabled) dragEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardEmojiDraggableView dragInteraction:previewForLiftingItem:session:];
-[UIKeyboardEmojiDraggableView dragInteraction:itemsForBeginningSession:];
-[UIKeyboardEmojiDraggableView dragInteraction:item:willAnimateCancelWithAnimator:];
-[UIKeyboardEmojiDraggableView dragInteraction:session:didEndWithOperation:];
-[UIKeyboardEmojiDraggableView dragInteraction:sessionWillBegin:];
-[UIKeyboardEmojiDraggableView intrinsicContentSize];
-[UIKeyboardEmojiDraggableView text];
-[UIKeyboardEmojiDraggableView setAttributedText:];
-[UIKeyboardEmojiDraggableView reset];
-[UIKeyboardEmojiDraggableView layoutSubviews];
-[UIKeyboardEmojiDraggableView _dragInteraction:sessionPropertiesForSession:];
-[UIKeyboardEmojiDraggableView touchesBegan:withEvent:];
-[UIKeyboardEmojiDraggableView setDelegate:];
-[UIKeyboardEmojiDraggableView attributedText];
-[UIKeyboardEmojiDraggableView delegate];
-[UIKeyboardEmojiDraggableView setText:];
-[UIKeyboardEmojiDraggableView dragInteraction:willAnimateLiftWithAnimator:session:];
-[UIKeyboardEmojiDraggableView font];
-[UIKeyboardEmojiDraggableView initWithFrame:];
-[UIKeyboardEmojiDraggableView dragInteraction:sessionDidTransferItems:];
-[UIKeyboardEmojiDraggableView setFont:];
-[UIKeyboardEmojiDraggableView setDragEnabled:];
-[UIKeyboardEmojiDraggableView updateLiftScale];
-[UIKeyboardEmojiDraggableView _dragInteractionDidCancelLiftWithoutDragging:];
-[UIKeyboardEmojiDraggableView addSilhouetteFiltersToView:];
-[UIKeyboardEmojiDraggableView createLabel];
-[UIKeyboardEmojiDraggableView dragEnabled];
-[UIKeyboardEmojiDraggableView generateEmoji:withCompletion:];
-[UIKeyboardEmojiDraggableView newLiftContainerView];
-[UIKeyboardEmojiDraggableView registerPlainText:toItemProvider:];
-[UIKeyboardEmojiDraggableView sendPeelAndStickAnalytics:];
-[UIKeyboardEmojiDraggableView setEmojiPopoverBackgroundHitTestingEnabled:];
-[UIKeyboardEmojiDraggableView updateDragInteraction];
-[UIKeyboardEmojiDraggableView willCancelVariantsWithTouch:];
```
