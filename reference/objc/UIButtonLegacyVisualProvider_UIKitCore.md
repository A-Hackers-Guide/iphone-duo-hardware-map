# `UIButtonLegacyVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFloatingContentViewDelegate`, `_UIButtonMaskAnimationViewDelegate`, `UIButtonVisualProvider`, `UIButtonArchivingVisualProvider`, `UIButtonVisualEffectSupportingVisualProvider`, `UIButtonDeprecatedAPISupportingVisualProvider`, `UIButtonDeprecatedSPISupportingVisualProvider`
- 12 instance variables, 8 properties, 147 instance methods, 5 class methods

## Instance variables

```
@"UIButton" _button;
@"UIImageView" _backgroundView;
@"_UIFloatingContentView" _floatingContentView;
@"UIVisualEffectView" _contentBackdropView;
@"UIImageView" _imageView;
@"UILabel" _titleView;
@"UIView" _selectionView;
@"CALayer" _highlightLayer;
@"_UIButtonMaskAnimationView" _maskAnimationView;
@"UIView" _effectiveContentView;
B _avoidDefaultTitleAndImageLayout;
@"NSArray" _contentConstraints;
```

## Properties

```
@property (T@"NSArray",C,N,S_setContentConstraints:,V_contentConstraints) _contentConstraints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N) focusSizeIncrease;
@property (T@"UIButton",?,N,V_button) button;
@property (TB,?,N,V_avoidDefaultTitleAndImageLayout) avoidDefaultTitleAndImageLayout;
```

## Class methods

```
+[UIButtonLegacyVisualProvider requiresNewVisualProviderForChanges];
+[UIButtonLegacyVisualProvider _NSTextAlignmentForUIControlContentHorizontalAlignment:];
+[UIButtonLegacyVisualProvider _selectedIndicatorImage];
+[UIButtonLegacyVisualProvider visualProviderForButton:];
+[UIButtonLegacyVisualProvider shouldUpdateContextMenuEnabledOnMenuChanges];
```

## Instance methods

```
-[UIButtonLegacyVisualProvider _setupTitleView];
-[UIButtonLegacyVisualProvider _updateImageView];
-[UIButtonLegacyVisualProvider useTitleForSelectedIndicatorBounds];
-[UIButtonLegacyVisualProvider titleShadowOffset];
-[UIButtonLegacyVisualProvider setImageContentMode:];
-[UIButtonLegacyVisualProvider setContentVerticalAlignment:];
-[UIButtonLegacyVisualProvider _shouldDefaultToTemplatesForImageViewBackground:];
-[UIButtonLegacyVisualProvider focusSizeIncrease];
-[UIButtonLegacyVisualProvider setFocusSizeIncrease:];
-[UIButtonLegacyVisualProvider setSelected:];
-[UIButtonLegacyVisualProvider adjustsFontForContentSizeCategory];
-[UIButtonLegacyVisualProvider _visualBoundsWithCornerRadius:hasProposal:shouldUseProposal:];
-[UIButtonLegacyVisualProvider contentBackdropView];
-[UIButtonLegacyVisualProvider contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[UIButtonLegacyVisualProvider _setupTitleViewRequestingLayout:];
-[UIButtonLegacyVisualProvider avoidDefaultTitleAndImageLayout];
-[UIButtonLegacyVisualProvider selectionIndicatorView];
-[UIButtonLegacyVisualProvider pointerEffectPreviewParameters];
-[UIButtonLegacyVisualProvider _applyAppropriateTouchInsetsForButton];
-[UIButtonLegacyVisualProvider pointerWillExit:];
-[UIButtonLegacyVisualProvider _isExternalRoundedRectButtonWithPressednessState];
-[UIButtonLegacyVisualProvider cleanupForVisualProvider:];
-[UIButtonLegacyVisualProvider setTitleShadowOffset:];
-[UIButtonLegacyVisualProvider contextMenuInteraction:configurationForMenuAtLocation:];
-[UIButtonLegacyVisualProvider _layoutContentBackdropView];
-[UIButtonLegacyVisualProvider defaultFocusEffect];
-[UIButtonLegacyVisualProvider setButton:];
-[UIButtonLegacyVisualProvider _beginTitleAnimation];
-[UIButtonLegacyVisualProvider effectiveContentView];
-[UIButtonLegacyVisualProvider didUpdateFocusInContext:withAnimationCoordinator:];
-[UIButtonLegacyVisualProvider alignmentRectInsets];
-[UIButtonLegacyVisualProvider _updateTitleView];
-[UIButtonLegacyVisualProvider deferToLazyTitleFont];
-[UIButtonLegacyVisualProvider setShowsTouchWhenHighlighted:];
-[UIButtonLegacyVisualProvider _highlightsBackgroundImage];
-[UIButtonLegacyVisualProvider setContextMenuIsPrimary:];
-[UIButtonLegacyVisualProvider setHighlighted:animated:];
-[UIButtonLegacyVisualProvider _setupPressednessForState:];
-[UIButtonLegacyVisualProvider _transitionAnimationWithKeyPath:];
-[UIButtonLegacyVisualProvider _fadeOutAnimationWithKeyPath:];
-[UIButtonLegacyVisualProvider _highlightRectForImageRect:];
-[UIButtonLegacyVisualProvider dealloc];
-[UIButtonLegacyVisualProvider _setContentConstraints:];
-[UIButtonLegacyVisualProvider _prepareMaskAnimationViewIfNecessary];
-[UIButtonLegacyVisualProvider currentImageWithResolvedConfiguration];
-[UIButtonLegacyVisualProvider contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[UIButtonLegacyVisualProvider imageRectForContentRect:];
-[UIButtonLegacyVisualProvider _setupDrawingStyleForState:];
-[UIButtonLegacyVisualProvider _contentConstraints];
-[UIButtonLegacyVisualProvider button];
-[UIButtonLegacyVisualProvider menuAttachmentPointForConfiguration:];
-[UIButtonLegacyVisualProvider backgroundRectForBounds:];
-[UIButtonLegacyVisualProvider viewForLastBaselineLayout];
-[UIButtonLegacyVisualProvider _newImageViewWithFrame:];
-[UIButtonLegacyVisualProvider layoutSubviews];
-[UIButtonLegacyVisualProvider _wantsContentBackdropView];
-[UIButtonLegacyVisualProvider _updateBackgroundImageView];
-[UIButtonLegacyVisualProvider imageViewCreateIfNeeded:];
-[UIButtonLegacyVisualProvider setPreferredSymbolConfiguration:forImageInState:];
-[UIButtonLegacyVisualProvider _selectedIndicatorBounds];
-[UIButtonLegacyVisualProvider baselineOffsetsAtSize:];
-[UIButtonLegacyVisualProvider _imageNeedsCompositingModeWhenSelected];
-[UIButtonLegacyVisualProvider _borderWidthForState:bounds:];
-[UIButtonLegacyVisualProvider updateProperties];
-[UIButtonLegacyVisualProvider canBecomeFocused];
-[UIButtonLegacyVisualProvider visualBoundsWithCornerRadius:];
-[UIButtonLegacyVisualProvider intrinsicContentSizeInvalidatedForChildView:];
-[UIButtonLegacyVisualProvider setSemanticContentAttribute:];
-[UIButtonLegacyVisualProvider pointerWillEnter:];
-[UIButtonLegacyVisualProvider pointerEffectWithPreview:];
-[UIButtonLegacyVisualProvider setExternalFlatEdge:];
-[UIButtonLegacyVisualProvider setMenuProvider:];
-[UIButtonLegacyVisualProvider sizeThatFits:];
-[UIButtonLegacyVisualProvider _floatingContentView];
-[UIButtonLegacyVisualProvider _contentHuggingDefault_isUsuallyFixedHeight];
-[UIButtonLegacyVisualProvider setFont:isDefaultForIdiom:];
-[UIButtonLegacyVisualProvider tintColorDidChange];
-[UIButtonLegacyVisualProvider _intrinsicWidthForAttributedTitle:];
-[UIButtonLegacyVisualProvider _intrinsicSizeForTitle:attributedTitle:image:backgroundImage:titlePaddingInsets:];
-[UIButtonLegacyVisualProvider _layoutBackgroundImageView];
-[UIButtonLegacyVisualProvider willMoveToWindow:];
-[UIButtonLegacyVisualProvider _updateTitleViewStyleEffectConfiguration];
-[UIButtonLegacyVisualProvider preferredConfigurationForFocusAnimation:inContext:];
-[UIButtonLegacyVisualProvider _setupBackgroundView];
-[UIButtonLegacyVisualProvider _layoutImageAndTitleViews];
-[UIButtonLegacyVisualProvider imageEffectContainerView];
-[UIButtonLegacyVisualProvider setEnabled:];
-[UIButtonLegacyVisualProvider viewForFirstBaselineLayout];
-[UIButtonLegacyVisualProvider setAttributedTitle:forState:];
-[UIButtonLegacyVisualProvider updatedAppliedCornerRadius:];
-[UIButtonLegacyVisualProvider titleViewCreateIfNeeded:];
-[UIButtonLegacyVisualProvider encodableSubviews];
-[UIButtonLegacyVisualProvider _updateMaskState];
-[UIButtonLegacyVisualProvider _createPreparedImageViewWithFrame:];
-[UIButtonLegacyVisualProvider updatedAppliedCornersAreContinuous:];
-[UIButtonLegacyVisualProvider setTitle:forState:];
-[UIButtonLegacyVisualProvider setImage:forState:];
-[UIButtonLegacyVisualProvider setOn:];
-[UIButtonLegacyVisualProvider _updateSelectionViewForState:];
-[UIButtonLegacyVisualProvider highlightBounds];
-[UIButtonLegacyVisualProvider _newLabelWithFrame:];
-[UIButtonLegacyVisualProvider _updateEffectsForImageView:background:];
-[UIButtonLegacyVisualProvider _removeContentBackdropView];
-[UIButtonLegacyVisualProvider setRole:];
-[UIButtonLegacyVisualProvider backgroundViewCreateIfNeeded:];
-[UIButtonLegacyVisualProvider setDrawingStroke:forState:];
-[UIButtonLegacyVisualProvider setVisualEffectViewEnabled:backgroundColor:];
-[UIButtonLegacyVisualProvider preferredHoverEffect];
-[UIButtonLegacyVisualProvider _deriveTitleRect:imageRect:fromContentRect:calculatePositionForEmptyTitle:];
-[UIButtonLegacyVisualProvider _layoutHighlightLayer];
-[UIButtonLegacyVisualProvider _reducedTransparencyDidChange:];
-[UIButtonLegacyVisualProvider updateConstraints];
-[UIButtonLegacyVisualProvider traitCollectionDidChange:];
-[UIButtonLegacyVisualProvider isOn];
-[UIButtonLegacyVisualProvider intrinsicSizeWithinSize:];
-[UIButtonLegacyVisualProvider pointerShapeInContainer:proposal:];
-[UIButtonLegacyVisualProvider _shouldUpdatePressedness];
-[UIButtonLegacyVisualProvider _textNeedsCompositingModeWhenSelected];
-[UIButtonLegacyVisualProvider touchesBegan];
-[UIButtonLegacyVisualProvider setReversesTitleShadowWhenHighlighted:];
-[UIButtonLegacyVisualProvider preferredHoverShape];
-[UIButtonLegacyVisualProvider touchesEnded];
-[UIButtonLegacyVisualProvider font];
-[UIButtonLegacyVisualProvider floatingContentView:isTransitioningFromState:toState:];
-[UIButtonLegacyVisualProvider didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UIButtonLegacyVisualProvider _titleOrImageViewForBaselineLayout];
-[UIButtonLegacyVisualProvider titleRectForContentRect:];
-[UIButtonLegacyVisualProvider _viewForBaselineLayout];
-[UIButtonLegacyVisualProvider _setupImageView];
-[UIButtonLegacyVisualProvider _highlightRectForTextRect:];
-[UIButtonLegacyVisualProvider setControlEvent:];
-[UIButtonLegacyVisualProvider populateArchivedSubviews:];
-[UIButtonLegacyVisualProvider setContentHorizontalAlignment:];
-[UIButtonLegacyVisualProvider setAvoidDefaultTitleAndImageLayout:];
-[UIButtonLegacyVisualProvider _updateContentBackdropView];
-[UIButtonLegacyVisualProvider fontIsDefaultForIdiom];
-[UIButtonLegacyVisualProvider _titleRectForContentRect:calculatePositionForEmptyTitle:];
-[UIButtonLegacyVisualProvider setLineBreakMode:];
-[UIButtonLegacyVisualProvider _invalidateContentConstraints];
-[UIButtonLegacyVisualProvider contentRectForBounds:];
-[UIButtonLegacyVisualProvider setContentHuggingPriorities:];
-[UIButtonLegacyVisualProvider _highlightBoundsForDrawingStyle];
-[UIButtonLegacyVisualProvider contextMenuInteraction:updateStyleForMenuWithConfiguration:style:];
-[UIButtonLegacyVisualProvider setBlurEnabled:];
-[UIButtonLegacyVisualProvider lineBreakMode];
-[UIButtonLegacyVisualProvider _contentHuggingDefault_isUsuallyFixedWidth];
-[UIButtonLegacyVisualProvider setMenu:];
```
