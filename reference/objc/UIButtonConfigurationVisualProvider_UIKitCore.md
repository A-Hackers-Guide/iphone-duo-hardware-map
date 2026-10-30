# `UIButtonConfigurationVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIButtonConfigurationUpdateExecuting`, `UIButtonModernVisualProvider`
- 16 instance variables, 13 properties, 113 instance methods, 4 class methods

## Instance variables

```
@"UIImageView" _indicatorView;
@"UIActivityIndicatorView" _progressIndicatorView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
{?="buttonBounds"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"idealSize"{CGSize="width"d"height"d}"imageFrame"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"indicatorFrame"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"titleFrame"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"subtitleFrame"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"baselineOffsets"{?="firstFromTop"d"lastFromBottom"d}"flags"{?="isValid"b1"hasImage"b1"hasIndicator"b1"hasProgressIndicator"b1"hasTitle"b1"hasSubtitle"b1}} _layoutData;
Q _accessibilityButtonShapesChangedToken;
@"UIView" _contentView;
{?="needsUpdateConfiguration"b1"fadeInAnimated"b1} _flags;
@"UIImageView" _imageView;
@"_UISystemBackgroundView" _backgroundView;
B _vendsBaselineInformationToAutoLayout;
B _avoidDefaultTitleAndImageLayout;
@"UIButton" _button;
d _widthForMultilineTextLayout;
d _previousFirstBaselineOffsetForAttributeLowering;
d _previousLastBaselineOffsetForAttributeLowering;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,V_widthForMultilineTextLayout) widthForMultilineTextLayout;
@property (TB,R,N) hasMultilineText;
@property (TB,R,N) hasBaseline;
@property (TB,N,V_vendsBaselineInformationToAutoLayout) vendsBaselineInformationToAutoLayout;
@property (Td,N,V_previousFirstBaselineOffsetForAttributeLowering) previousFirstBaselineOffsetForAttributeLowering;
@property (Td,N,V_previousLastBaselineOffsetForAttributeLowering) previousLastBaselineOffsetForAttributeLowering;
@property (Td,N) focusSizeIncrease;
@property (T@"UIButton",?,N,V_button) button;
@property (TB,?,N,V_avoidDefaultTitleAndImageLayout) avoidDefaultTitleAndImageLayout;
```

## Class methods

```
+[UIButtonConfigurationVisualProvider requiresNewVisualProviderForChanges];
+[UIButtonConfigurationVisualProvider wantsConfigurationUpdateForButtonShapes];
+[UIButtonConfigurationVisualProvider visualProviderForButton:];
+[UIButtonConfigurationVisualProvider shouldUpdateContextMenuEnabledOnMenuChanges];
```

## Instance methods

```
-[UIButtonConfigurationVisualProvider useTitleForSelectedIndicatorBounds];
-[UIButtonConfigurationVisualProvider setPreviousFirstBaselineOffsetForAttributeLowering:];
-[UIButtonConfigurationVisualProvider setContentVerticalAlignment:];
-[UIButtonConfigurationVisualProvider focusSizeIncrease];
-[UIButtonConfigurationVisualProvider setFocusSizeIncrease:];
-[UIButtonConfigurationVisualProvider setSelected:];
-[UIButtonConfigurationVisualProvider adjustsFontForContentSizeCategory];
-[UIButtonConfigurationVisualProvider contentBackdropView];
-[UIButtonConfigurationVisualProvider contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[UIButtonConfigurationVisualProvider avoidDefaultTitleAndImageLayout];
-[UIButtonConfigurationVisualProvider intrinsicContentSize];
-[UIButtonConfigurationVisualProvider selectionIndicatorView];
-[UIButtonConfigurationVisualProvider pointerEffectPreviewParameters];
-[UIButtonConfigurationVisualProvider pointerWillExit:];
-[UIButtonConfigurationVisualProvider cleanupForVisualProvider:];
-[UIButtonConfigurationVisualProvider hasBaseline];
-[UIButtonConfigurationVisualProvider contextMenuInteraction:configurationForMenuAtLocation:];
-[UIButtonConfigurationVisualProvider defaultFocusEffect];
-[UIButtonConfigurationVisualProvider setButton:];
-[UIButtonConfigurationVisualProvider init];
-[UIButtonConfigurationVisualProvider effectiveContentView];
-[UIButtonConfigurationVisualProvider didUpdateFocusInContext:withAnimationCoordinator:];
-[UIButtonConfigurationVisualProvider alignmentRectInsets];
-[UIButtonConfigurationVisualProvider setShowsTouchWhenHighlighted:];
-[UIButtonConfigurationVisualProvider _accessibilityButtonShapesChangedNotification:];
-[UIButtonConfigurationVisualProvider setContextMenuIsPrimary:];
-[UIButtonConfigurationVisualProvider setHighlighted:animated:];
-[UIButtonConfigurationVisualProvider previousFirstBaselineOffsetForAttributeLowering];
-[UIButtonConfigurationVisualProvider dealloc];
-[UIButtonConfigurationVisualProvider contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[UIButtonConfigurationVisualProvider imageRectForContentRect:];
-[UIButtonConfigurationVisualProvider _transitionContentIfNeededOn:WithBlock:];
-[UIButtonConfigurationVisualProvider button];
-[UIButtonConfigurationVisualProvider menuAttachmentPointForConfiguration:];
-[UIButtonConfigurationVisualProvider viewForLastBaselineLayout];
-[UIButtonConfigurationVisualProvider layoutSubviews];
-[UIButtonConfigurationVisualProvider _updateImageViewWithConfiguration:];
-[UIButtonConfigurationVisualProvider imageViewCreateIfNeeded:];
-[UIButtonConfigurationVisualProvider setPreferredSymbolConfiguration:forImageInState:];
-[UIButtonConfigurationVisualProvider vendsBaselineInformationToAutoLayout];
-[UIButtonConfigurationVisualProvider baselineOffsetsAtSize:];
-[UIButtonConfigurationVisualProvider setPreviousLastBaselineOffsetForAttributeLowering:];
-[UIButtonConfigurationVisualProvider updateProperties];
-[UIButtonConfigurationVisualProvider updateConfigurationIfNecessary];
-[UIButtonConfigurationVisualProvider _updateTitleLabelWithConfiguration:];
-[UIButtonConfigurationVisualProvider canBecomeFocused];
-[UIButtonConfigurationVisualProvider visualBoundsWithCornerRadius:];
-[UIButtonConfigurationVisualProvider intrinsicContentSizeInvalidatedForChildView:];
-[UIButtonConfigurationVisualProvider setSemanticContentAttribute:];
-[UIButtonConfigurationVisualProvider pointerWillEnter:];
-[UIButtonConfigurationVisualProvider pointerEffectWithPreview:];
-[UIButtonConfigurationVisualProvider _updateProgressIndicatorWithConfiguration:];
-[UIButtonConfigurationVisualProvider setMenuProvider:];
-[UIButtonConfigurationVisualProvider _updateSubtitleLabelWithConfiguration:];
-[UIButtonConfigurationVisualProvider tintColorDidChange];
-[UIButtonConfigurationVisualProvider _updateBackgroundViewWithConfiguration:];
-[UIButtonConfigurationVisualProvider _layoutBounds];
-[UIButtonConfigurationVisualProvider willMoveToWindow:];
-[UIButtonConfigurationVisualProvider subtitleViewCreateIfNeeded:];
-[UIButtonConfigurationVisualProvider preferredConfigurationForFocusAnimation:inContext:];
-[UIButtonConfigurationVisualProvider imageEffectContainerView];
-[UIButtonConfigurationVisualProvider automaticallyUpdateConfigurationIfNecessary:];
-[UIButtonConfigurationVisualProvider hasMultilineText];
-[UIButtonConfigurationVisualProvider setEnabled:];
-[UIButtonConfigurationVisualProvider viewForFirstBaselineLayout];
-[UIButtonConfigurationVisualProvider setAttributedTitle:forState:];
-[UIButtonConfigurationVisualProvider updatedAppliedCornerRadius:];
-[UIButtonConfigurationVisualProvider alignmentRectInsetsHaveChangedForChildImageView:];
-[UIButtonConfigurationVisualProvider titleViewCreateIfNeeded:];
-[UIButtonConfigurationVisualProvider updatedAppliedCornersAreContinuous:];
-[UIButtonConfigurationVisualProvider setTitle:forState:];
-[UIButtonConfigurationVisualProvider setImage:forState:];
-[UIButtonConfigurationVisualProvider setOn:];
-[UIButtonConfigurationVisualProvider _layoutDataInBounds:forConfiguration:];
-[UIButtonConfigurationVisualProvider setRole:];
-[UIButtonConfigurationVisualProvider backgroundViewCreateIfNeeded:];
-[UIButtonConfigurationVisualProvider _executeConfigurationUpdate];
-[UIButtonConfigurationVisualProvider preferredHoverEffect];
-[UIButtonConfigurationVisualProvider _layoutContent];
-[UIButtonConfigurationVisualProvider _applyButtonValuesToConfiguration:];
-[UIButtonConfigurationVisualProvider updateConstraints];
-[UIButtonConfigurationVisualProvider updateBaselineInformationDependentOnBounds];
-[UIButtonConfigurationVisualProvider traitCollectionDidChange:];
-[UIButtonConfigurationVisualProvider isOn];
-[UIButtonConfigurationVisualProvider intrinsicSizeWithinSize:];
-[UIButtonConfigurationVisualProvider pointerShapeInContainer:proposal:];
-[UIButtonConfigurationVisualProvider touchesBegan];
-[UIButtonConfigurationVisualProvider setReversesTitleShadowWhenHighlighted:];
-[UIButtonConfigurationVisualProvider preferredHoverShape];
-[UIButtonConfigurationVisualProvider touchesEnded];
-[UIButtonConfigurationVisualProvider previousLastBaselineOffsetForAttributeLowering];
-[UIButtonConfigurationVisualProvider didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UIButtonConfigurationVisualProvider _layoutDataInBounds:];
-[UIButtonConfigurationVisualProvider titleRectForContentRect:];
-[UIButtonConfigurationVisualProvider setControlEvent:];
-[UIButtonConfigurationVisualProvider _animateContentIfNeededWithBlock:];
-[UIButtonConfigurationVisualProvider widthForMultilineTextLayout];
-[UIButtonConfigurationVisualProvider invalidateLayoutData];
-[UIButtonConfigurationVisualProvider setContentHorizontalAlignment:];
-[UIButtonConfigurationVisualProvider systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[UIButtonConfigurationVisualProvider setAvoidDefaultTitleAndImageLayout:];
-[UIButtonConfigurationVisualProvider _debugLayoutData];
-[UIButtonConfigurationVisualProvider contentRectForBounds:];
-[UIButtonConfigurationVisualProvider setContentHuggingPriorities:];
-[UIButtonConfigurationVisualProvider _updateIndicatorWithConfiguration:];
-[UIButtonConfigurationVisualProvider contextMenuInteraction:updateStyleForMenuWithConfiguration:style:];
-[UIButtonConfigurationVisualProvider setVendsBaselineInformationToAutoLayout:];
-[UIButtonConfigurationVisualProvider _layoutDataUpdatingIfNecessary];
-[UIButtonConfigurationVisualProvider updateAccessibilityUnderline];
-[UIButtonConfigurationVisualProvider applyConfiguration];
-[UIButtonConfigurationVisualProvider setNeedsUpdateConfiguration];
-[UIButtonConfigurationVisualProvider setWidthForMultilineTextLayout:];
-[UIButtonConfigurationVisualProvider setMenu:];
```
