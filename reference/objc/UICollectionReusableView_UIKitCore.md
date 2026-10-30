# `UICollectionReusableView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIEditable`
- 9 instance variables, 18 properties, 64 instance methods, 0 class methods

## Instance variables

```
@"UICollectionViewLayoutAttributes" _layoutAttributes;
@"UICollectionView" _collectionView;
q _updateAnimationCount;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _defaultLayoutMargins;
{?="wasDequeued"b1"hasBeenReused"b1"preferredAttributesValid"b1"generatingPreferredAttributes"b1"didSetMasksToBounds"b1"didSetMaskedCorners"b1"didSetCornerRadius"b1"didSetMaskView"b1"hasBlocksToPerformWhenReused"b1"isBeingReused"b1"isDisplayed"b1"collectionViewHasBeenExplicitlySet"b1"shouldConstrainWidth"b1"shouldConstrainHeight"b1"hasDefaultLayoutMargins"b1"automaticIntrinsicContentSizeInvalidationEnabled"b1} _reusableViewFlags;
B _preferredAttributesValid;
@"NSString" _reuseIdentifier;
@"_UIScrollPocketContainerInteraction" __scrollPocketContainerInteraction;
@"NSString" _elementKind;
```

## Properties

```
@property (T@"UICollectionViewLayoutAttributes",C,N,G_layoutAttributes,S_setLayoutAttributes:) layoutAttributes;
@property (T@"NSString",C,N,S_setReuseIdentifier:,V_reuseIdentifier) reuseIdentifier;
@property (T@"NSString",C,N,G_elementKind,S_setElementKind:,V_elementKind) elementKind;
@property (T@"UICollectionView",W,N,G_collectionView,S_setCollectionView:) collectionView;
@property (TB,R,N,G_isInUpdateAnimation) inUpdateAnimation;
@property (TB,N,S_setAutomaticIntrinsicContentSizeInvalidationEnabled:) _automaticIntrinsicContentSizeInvalidationEnabled;
@property (TB,N,G_shouldConstrainWidth,S_setShouldConstrainWidth:) shouldConstrainWidth;
@property (TB,N,G_shouldConstrainHeight,S_setShouldConstrainHeight:) shouldConstrainHeight;
@property (TB,N,G_isBeingReused,S_setIsBeingReused:) isBeingReused;
@property (TB,R,N,G_hasBeenReused) hasBeenReused;
@property (TB,N,G_isHiddenForReordering,S_setHiddenForReordering:) _hiddenForReordering;
@property (TB,N,G_arePreferredAttributesValid,V_preferredAttributesValid) preferredAttributesValid;
@property (TB,R,N) canBeEdited;
@property (TB,N,GisEditing) editing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UICollectionReusableView invalidateIntrinsicContentSize];
-[UICollectionReusableView _concreteDefaultLayoutMargins];
-[UICollectionReusableView applyLayoutAttributes:];
-[UICollectionReusableView setTranslatesAutoresizingMaskIntoConstraints:];
-[UICollectionReusableView _disableRasterizeInAnimations];
-[UICollectionReusableView setEditing:];
-[UICollectionReusableView prepareForReuse];
-[UICollectionReusableView encodeWithCoder:];
-[UICollectionReusableView reuseIdentifier];
-[UICollectionReusableView initWithCoder:];
-[UICollectionReusableView _collectionView];
-[UICollectionReusableView didMoveToSuperview];
-[UICollectionReusableView isEditing];
-[UICollectionReusableView initWithFrame:];
-[UICollectionReusableView _markAsDequeued];
-[UICollectionReusableView _updateMaskViewUsingAttributes:];
-[UICollectionReusableView _addBackdropViewForMaskingIfNeeded];
-[UICollectionReusableView _addUpdateAnimation];
-[UICollectionReusableView _appliesLayoutAttributesMaskingToReusableView];
-[UICollectionReusableView _applyListEnvironmentTraitOverridesUsingNewListAttributes:previousListAttributes:];
-[UICollectionReusableView _arePreferredAttributesValid];
-[UICollectionReusableView _automaticIntrinsicContentSizeInvalidationEnabled];
-[UICollectionReusableView _clearUpdateAnimation];
-[UICollectionReusableView _disableGroupOpacityInAnimations];
-[UICollectionReusableView _elementKind];
-[UICollectionReusableView _hasBeenReused];
-[UICollectionReusableView _hasNotifiedIsDisplaying];
-[UICollectionReusableView _invalidatePreferredAttributes];
-[UICollectionReusableView _isBeingReused];
-[UICollectionReusableView _isEffectivelyHidden];
-[UICollectionReusableView _isFocusableWhenStyledAsHeader];
-[UICollectionReusableView _isHiddenForReordering];
-[UICollectionReusableView _isInUpdateAnimation];
-[UICollectionReusableView _isStyledAsHeaderOrFooterFromLayoutAttributes:];
-[UICollectionReusableView _layoutAttributes];
-[UICollectionReusableView _notifyIsDisplaying:];
-[UICollectionReusableView _preferredLayoutAttributesFittingAttributes:isAnimatingExistingView:];
-[UICollectionReusableView _removeExistingBackdropViewForMasking];
-[UICollectionReusableView _setAutomaticIntrinsicContentSizeInvalidationEnabled:];
-[UICollectionReusableView _setBaseLayoutAttributes:];
-[UICollectionReusableView _setCollectionView:];
-[UICollectionReusableView _setElementKind:];
-[UICollectionReusableView _setHiddenForReordering:];
-[UICollectionReusableView _setHiddenForReuse:];
-[UICollectionReusableView _setIsBeingReused:];
-[UICollectionReusableView _setLayoutAttributes:];
-[UICollectionReusableView _setLayoutAttributes:force:];
-[UICollectionReusableView _setMaskView:];
-[UICollectionReusableView _setReuseIdentifier:];
-[UICollectionReusableView _setShouldConstrainHeight:];
-[UICollectionReusableView _setShouldConstrainWidth:];
-[UICollectionReusableView _shouldConstrainHeight];
-[UICollectionReusableView _shouldConstrainWidth];
-[UICollectionReusableView _styleFromLayoutAttributes:];
-[UICollectionReusableView _updateDefaultLayoutMarginsUsingAttributes:];
-[UICollectionReusableView _updateMaskingUsingAttributes:];
-[UICollectionReusableView _updateScrollPocketContainerInteractionUsingAttributes:];
-[UICollectionReusableView _wasDequeued];
-[UICollectionReusableView _willRevealWithLayoutAttributes:];
-[UICollectionReusableView canBeEdited];
-[UICollectionReusableView didTransitionFromLayout:toLayout:];
-[UICollectionReusableView preferredLayoutAttributesFittingAttributes:];
-[UICollectionReusableView setPreferredAttributesValid:];
-[UICollectionReusableView willTransitionFromLayout:toLayout:];
```
