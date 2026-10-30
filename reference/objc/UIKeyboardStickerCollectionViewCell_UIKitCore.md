# `UIKeyboardStickerCollectionViewCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardEmojiStickerBaseCollectionViewCell`
- Protocols: `UIKeyboardEmojiCollectionInputViewDelegate`
- 15 instance variables, 19 properties, 62 instance methods, 0 class methods

## Instance variables

```
B _rearrangeMode;
B _isRestrictedContent;
B _allowsDistribution;
@"STKImageGlyph" _imageGlyph;
@"NSString" _usageSource;
@"<UIKeyboardEmojiAndStickerCollectionViewCellDelegate>" _delegate;
@"<UIKeyboardEmojiAndStickerCollectionViewDelegate>" _cellDelegate;
@"UIView" _stickerView;
@"UIView" _rearrangingView;
@"UIKeyboardStickerRestrictedContentView" _restrictedContentView;
@"UIButton" _deleteButton;
@"UITapGestureRecognizer" _rearrangeViewTapGR;
@"UILongPressGestureRecognizer" _longPressGR;
@"UIEditMenuInteraction" _editMenuInteraction;
@"UIView" _navigationHighlightView;
```

## Properties

```
@property (T@"UIView",&,N,V_stickerView) stickerView;
@property (T@"UIView",&,N,V_rearrangingView) rearrangingView;
@property (T@"UIKeyboardStickerRestrictedContentView",&,N,V_restrictedContentView) restrictedContentView;
@property (T@"UIButton",&,N,V_deleteButton) deleteButton;
@property (T@"UITapGestureRecognizer",&,N,V_rearrangeViewTapGR) rearrangeViewTapGR;
@property (T@"UILongPressGestureRecognizer",&,N,V_longPressGR) longPressGR;
@property (T@"UIEditMenuInteraction",&,N,V_editMenuInteraction) editMenuInteraction;
@property (T@"UIView",&,N,V_navigationHighlightView) navigationHighlightView;
@property (T@"STKImageGlyph",C,N,V_imageGlyph) imageGlyph;
@property (TB,N,V_rearrangeMode) rearrangeMode;
@property (TB,N,V_isRestrictedContent) isRestrictedContent;
@property (TB,N,V_allowsDistribution) allowsDistribution;
@property (T@"NSString",C,N,V_usageSource) usageSource;
@property (T@"<UIKeyboardEmojiAndStickerCollectionViewCellDelegate>",W,N,V_delegate) delegate;
@property (T@"<UIKeyboardEmojiAndStickerCollectionViewDelegate>",W,N,V_cellDelegate) cellDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKeyboardStickerCollectionViewCell setDeleteButton:];
-[UIKeyboardStickerCollectionViewCell setSelected:];
-[UIKeyboardStickerCollectionViewCell deleteButton];
-[UIKeyboardStickerCollectionViewCell layoutSubviews];
-[UIKeyboardStickerCollectionViewCell hitTest:withEvent:];
-[UIKeyboardStickerCollectionViewCell setDelegate:];
-[UIKeyboardStickerCollectionViewCell didLongPress:];
-[UIKeyboardStickerCollectionViewCell accessibilityIdentifier];
-[UIKeyboardStickerCollectionViewCell editMenuInteraction];
-[UIKeyboardStickerCollectionViewCell prepareForReuse];
-[UIKeyboardStickerCollectionViewCell accessibilityLabel];
-[UIKeyboardStickerCollectionViewCell delegate];
-[UIKeyboardStickerCollectionViewCell isAccessibilityElement];
-[UIKeyboardStickerCollectionViewCell editMenuInteraction:menuForConfiguration:suggestedActions:];
-[UIKeyboardStickerCollectionViewCell initWithFrame:];
-[UIKeyboardStickerCollectionViewCell allowsRearrange];
-[UIKeyboardStickerCollectionViewCell rearrangingView];
-[UIKeyboardStickerCollectionViewCell tappedNewEmoji:];
-[UIKeyboardStickerCollectionViewCell _startRearrange];
-[UIKeyboardStickerCollectionViewCell setLongPressGR:];
-[UIKeyboardStickerCollectionViewCell setStickerView:];
-[UIKeyboardStickerCollectionViewCell setUsageSource:];
-[UIKeyboardStickerCollectionViewCell _didTapDuringRearrange:];
-[UIKeyboardStickerCollectionViewCell _endJiggle];
-[UIKeyboardStickerCollectionViewCell _endRearrange];
-[UIKeyboardStickerCollectionViewCell _jiggleAnimationWithVariation:keyPath:duration:];
-[UIKeyboardStickerCollectionViewCell _jiggleTranslationAnimationTranslation:];
-[UIKeyboardStickerCollectionViewCell _performDeleteAction];
-[UIKeyboardStickerCollectionViewCell _reportRearrangeStateChanged:];
-[UIKeyboardStickerCollectionViewCell _showRearrangeViewIfNecessary:];
-[UIKeyboardStickerCollectionViewCell _startJiggle];
-[UIKeyboardStickerCollectionViewCell allowsDistribution];
-[UIKeyboardStickerCollectionViewCell cellDelegate];
-[UIKeyboardStickerCollectionViewCell didEndDisplaying];
-[UIKeyboardStickerCollectionViewCell imageGlyph];
-[UIKeyboardStickerCollectionViewCell isEmptyCell];
-[UIKeyboardStickerCollectionViewCell isRestrictedContent];
-[UIKeyboardStickerCollectionViewCell longPressGR];
-[UIKeyboardStickerCollectionViewCell navigationHighlightView];
-[UIKeyboardStickerCollectionViewCell performDeleteWithCompletionHandler:];
-[UIKeyboardStickerCollectionViewCell rearrangeMode];
-[UIKeyboardStickerCollectionViewCell rearrangeStateChanged:];
-[UIKeyboardStickerCollectionViewCell rearrangeViewTapGR];
-[UIKeyboardStickerCollectionViewCell resetRestrictedContent];
-[UIKeyboardStickerCollectionViewCell restrictedContentView];
-[UIKeyboardStickerCollectionViewCell setAllowsDistribution:];
-[UIKeyboardStickerCollectionViewCell setCellDelegate:];
-[UIKeyboardStickerCollectionViewCell setEditMenuInteraction:];
-[UIKeyboardStickerCollectionViewCell setImageGlyph:];
-[UIKeyboardStickerCollectionViewCell setIsRestrictedContent:];
-[UIKeyboardStickerCollectionViewCell setNavigationHighlightView:];
-[UIKeyboardStickerCollectionViewCell setRearrangeMode:];
-[UIKeyboardStickerCollectionViewCell setRearrangeViewTapGR:];
-[UIKeyboardStickerCollectionViewCell setRearrangingView:];
-[UIKeyboardStickerCollectionViewCell setRestrictedContentView:];
-[UIKeyboardStickerCollectionViewCell stickerView];
-[UIKeyboardStickerCollectionViewCell tappedAddEffect:];
-[UIKeyboardStickerCollectionViewCell tappedDelete:];
-[UIKeyboardStickerCollectionViewCell tappedRearrange:];
-[UIKeyboardStickerCollectionViewCell updateDistributionPermissions];
-[UIKeyboardStickerCollectionViewCell usageSource];
-[UIKeyboardStickerCollectionViewCell willDisplay];
```
