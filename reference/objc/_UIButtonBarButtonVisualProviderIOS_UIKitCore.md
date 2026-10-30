# `_UIButtonBarButtonVisualProviderIOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIButtonBarButtonVisualProvider`
- 17 instance variables, 0 properties, 89 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _currentConstraints;
@"NSMutableDictionary" _oldConstraints;
@"_UIModernBarButton" _backIndicatorButton;
@"_UIBackButtonMaskView" _backButtonMask;
@"_UIModernBarButton" _titleButton;
@"_UIModernBarButton" _imageButton;
@"UIImageView" _backgroundView;
@"<_UIButtonBarAppearanceDelegate>" _appearanceDelegate;
@"NSArray" _barButtonTitleAttributes;
@"NSArray" _finalTitleAttributes;
@"NSMutableDictionary" _backgroundImages;
@"NSArray" _titleContent;
@"NSMutableDictionary" _titleLookup;
@"NSLayoutConstraint" _backButtonTitleMaxWidthConstraint;
@? _menuProvider;
q _systemItem;
{?="imageHasBaseline"b1"backButtonMaskEnabled"b1"style"b3"isSystemItem"b1} _flags;
```

## Instance methods

```
-[_UIButtonBarButtonVisualProviderIOS buttonSelectionState:forRequestedState:];
-[_UIButtonBarButtonVisualProviderIOS buttonDidUpdateBoundsSize];
-[_UIButtonBarButtonVisualProviderIOS buttonContextMenuStyleFromDefaultStyle:];
-[_UIButtonBarButtonVisualProviderIOS accessoryViewAlignmentRect];
-[_UIButtonBarButtonVisualProviderIOS _imageInsetsForBarButtonItem:compact:isBackButton:];
-[_UIButtonBarButtonVisualProviderIOS buttonControlClass];
-[_UIButtonBarButtonVisualProviderIOS _backIndicatorMaskForCompact:];
-[_UIButtonBarButtonVisualProviderIOS updateButton:forSelectedState:];
-[_UIButtonBarButtonVisualProviderIOS updateButton:forHighlightedState:];
-[_UIButtonBarButtonVisualProviderIOS updateButton:appearance:];
-[_UIButtonBarButtonVisualProviderIOS updateButton:forEnabledState:];
-[_UIButtonBarButtonVisualProviderIOS updateMenu];
-[_UIButtonBarButtonVisualProviderIOS activateHeightMinimizer];
-[_UIButtonBarButtonVisualProviderIOS buttonImageViewSize:];
-[_UIButtonBarButtonVisualProviderIOS canUpdateMenuInPlace];
-[_UIButtonBarButtonVisualProviderIOS updateButton:forHeldState:];
-[_UIButtonBarButtonVisualProviderIOS pointerShapeInContainer:];
-[_UIButtonBarButtonVisualProviderIOS buttonContextMenuTargetedPreview];
-[_UIButtonBarButtonVisualProviderIOS symbolImageView];
-[_UIButtonBarButtonVisualProviderIOS resetButtonHasHighlighted];
-[_UIButtonBarButtonVisualProviderIOS textButton];
-[_UIButtonBarButtonVisualProviderIOS buttonLayoutSubviews:baseImplementation:];
-[_UIButtonBarButtonVisualProviderIOS _configureImageWithInsets:paddingEdges:additionalPadding:];
-[_UIButtonBarButtonVisualProviderIOS updateImage];
-[_UIButtonBarButtonVisualProviderIOS matchingPointerShapeForView:rect:inContainer:];
-[_UIButtonBarButtonVisualProviderIOS alignmentViewForStaticNavBarButtonLeading];
-[_UIButtonBarButtonVisualProviderIOS supportsBackButtons];
-[_UIButtonBarButtonVisualProviderIOS configureButton:fromBarButtonItem:];
-[_UIButtonBarButtonVisualProviderIOS shouldLift];
-[_UIButtonBarButtonVisualProviderIOS setBackButtonMaskEnabled:];
-[_UIButtonBarButtonVisualProviderIOS buttonContextMenuInteractionConfiguration];
-[_UIButtonBarButtonVisualProviderIOS alignmentViewForStaticNavBarButtonTrailing];
-[_UIButtonBarButtonVisualProviderIOS menuAnchorPoint];
-[_UIButtonBarButtonVisualProviderIOS symbolConfigurationCompact:];
-[_UIButtonBarButtonVisualProviderIOS configureButton:withAppearanceDelegate:fromBarItem:];
-[_UIButtonBarButtonVisualProviderIOS backButtonSystemLayoutSizeFittingSize:horizontalFittingPriority:verticalFittingPriority:];
-[_UIButtonBarButtonVisualProviderIOS buttonSpringLoadedInteractionEffect];
-[_UIButtonBarButtonVisualProviderIOS backIndicatorView];
-[_UIButtonBarButtonVisualProviderIOS backButtonBackgroundVerticalAdjustmentForCompact:];
-[_UIButtonBarButtonVisualProviderIOS traitDependenciesUpdated];
-[_UIButtonBarButtonVisualProviderIOS _effectiveEdgeSpacing];
-[_UIButtonBarButtonVisualProviderIOS backButtonMaskEnabled];
-[_UIButtonBarButtonVisualProviderIOS pointerPreviewParameters];
-[_UIButtonBarButtonVisualProviderIOS _configureTextWithOffset:additionalPadding:];
-[_UIButtonBarButtonVisualProviderIOS updateButton:toUseButtonShapes:];
-[_UIButtonBarButtonVisualProviderIOS backgroundVerticalAdjustmentForCompact:];
-[_UIButtonBarButtonVisualProviderIOS _defaultBackIndicatorBaselineInsetCompact:];
-[_UIButtonBarButtonVisualProviderIOS _configureBackButtonWithBackButtonLayoutInsets:useBaselineAlignment:];
-[_UIButtonBarButtonVisualProviderIOS _configureBackButtonMask];
-[_UIButtonBarButtonVisualProviderIOS _prepareBackgroundViewFromBarButtonItem:isBackButton:];
-[_UIButtonBarButtonVisualProviderIOS reload];
-[_UIButtonBarButtonVisualProviderIOS contentButtonTrailingOffset:];
-[_UIButtonBarButtonVisualProviderIOS _removeTitleButton];
-[_UIButtonBarButtonVisualProviderIOS _addConstraintsForBackgroundViewWithOffset:isBackButton:resizesImage:];
-[_UIButtonBarButtonVisualProviderIOS _updateTextContent];
-[_UIButtonBarButtonVisualProviderIOS activateWidthMinimizer];
-[_UIButtonBarButtonVisualProviderIOS _addVerticalConstraintsForImageWithInsets:];
-[_UIButtonBarButtonVisualProviderIOS prefersCapsularPointerShape];
-[_UIButtonBarButtonVisualProviderIOS _configureTextBackButtonWithTitlePositionAdjustment:backButtonLayoutInsets:useBaselineAlignment:];
-[_UIButtonBarButtonVisualProviderIOS addActiveConstraint:named:];
-[_UIButtonBarButtonVisualProviderIOS _titleContentForTitle:];
-[_UIButtonBarButtonVisualProviderIOS updateActiveConstraints:];
-[_UIButtonBarButtonVisualProviderIOS backButtonTitlePositionOffsetForCompact:];
-[_UIButtonBarButtonVisualProviderIOS imageButton];
-[_UIButtonBarButtonVisualProviderIOS _defaultHeightFromDelegate];
-[_UIButtonBarButtonVisualProviderIOS _updateMonochromaticTreatment];
-[_UIButtonBarButtonVisualProviderIOS _configureImageOrTitleCompact:];
-[_UIButtonBarButtonVisualProviderIOS contentView];
-[_UIButtonBarButtonVisualProviderIOS _addHorizontalConstraintsForTextWithOffset:additionalPadding:];
-[_UIButtonBarButtonVisualProviderIOS _computeTextAttributes];
-[_UIButtonBarButtonVisualProviderIOS backButtonBackgroundImageForState:compact:];
-[_UIButtonBarButtonVisualProviderIOS titlePositionOffsetForCompact:];
-[_UIButtonBarButtonVisualProviderIOS tintColor];
-[_UIButtonBarButtonVisualProviderIOS _updateViewsForMaskingEnabled];
-[_UIButtonBarButtonVisualProviderIOS _setupAlternateTitles];
-[_UIButtonBarButtonVisualProviderIOS backgroundImageView];
-[_UIButtonBarButtonVisualProviderIOS _computeTextAttributesForBarButtonItem:];
-[_UIButtonBarButtonVisualProviderIOS _backIndicatorMaskSymbolConfigurationForCompact:];
-[_UIButtonBarButtonVisualProviderIOS _setTitle:];
-[_UIButtonBarButtonVisualProviderIOS _insetsForCompact:];
-[_UIButtonBarButtonVisualProviderIOS _defaultPaddingForInsets:];
-[_UIButtonBarButtonVisualProviderIOS _addHorizontalConstraintsForImageWithInsets:paddingEdges:additionalPadding:];
-[_UIButtonBarButtonVisualProviderIOS _addVerticalConstraintsForBackIndicatorWithTitleOffset:bottomOffset:useBaselineAlignment:];
-[_UIButtonBarButtonVisualProviderIOS _backIndicatorSymbolConfigurationForCompact:];
-[_UIButtonBarButtonVisualProviderIOS backgroundImageForState:compact:];
-[_UIButtonBarButtonVisualProviderIOS _addVerticalConstraintsForTextWithOffset:];
-[_UIButtonBarButtonVisualProviderIOS _backIndicatorImageForCompact:];
-[_UIButtonBarButtonVisualProviderIOS _addHorizontalConstraintsForContentButton:titleOffset:backButtonLayoutInsets:];
-[_UIButtonBarButtonVisualProviderIOS _configureImageBackButtonWithImageInsets:backButtonLayoutInsets:useBaselineAlignment:];
```
