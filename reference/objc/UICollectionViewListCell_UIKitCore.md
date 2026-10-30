# `UICollectionViewListCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- Protocols: `_UICollectionViewListCellReorderControlDelegate`, `UITableConstantsCellProviding`
- 25 instance variables, 23 properties, 133 instance methods, 3 class methods

## Instance variables

```
{?="style"b3"isStyledAsHeaderOrFooter"b1"isFooter"b1"forceHeaderStylingDueToSPIOutlineDisclosureAccessory"b1"selectionStyle"b1"expanded"b1"needsUpdateAccessories"b1"hasCustomIndentationLevel"b1"hasCustomIndentationWidth"b1"cellSelectionTogglesExpansionState"b1"indentsAccessories"b1"indentationMarginIsBasedOnCustomMargin"b1"isNextSelectionUpdateUserInitiated"b1"edgesAbuttingAccessoriesWhenNotEditing"b4"edgesAbuttingAccessoriesWhenEditing"b4"separatorLayoutGuideLeadingReferencesPrimaryText"b1"subclassOverridesSeparatorInsetsSPI"b1} _listCellFlags;
@"_UICollectionViewListCellVisualProvider" _visualProvider;
@"NSDictionary" _accessoriesByIdentifier;
d _extraLeadingLayoutMarginForIndentation;
@"NSArray" _contentViewConstraints;
@"NSLayoutConstraint" _separatorLayoutGuideHeightConstraint;
@"NSLayoutConstraint" _separatorLayoutGuideLeadingConstraint;
@"NSLayoutConstraint" _separatorLayoutGuideTrailingConstraint;
@"UILayoutGuide" _separatorLayoutGuide;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _sectionSeparatorInsets;
d _lastPreferredLeadingSeparatorInsetFromContentView;
d _lastPreferredTrailingSeparatorInsetFromContentView;
@"NSArray" _accessories;
@"NSArray" _leadingAccessoryConfigurations;
@"NSArray" _trailingAccessoryConfigurations;
@"NSArray" _leadingEditingAccessoryConfigurations;
@"NSArray" _trailingEditingAccessoryConfigurations;
q _indentationLevel;
d _indentationWidth;
@"<UITableConstants>" _constants;
@? __disclosureActionHandler;
@"<UIFocusItem>" __parentFocusItem;
@"UICellAccessoryManager" _accessoryManager;
q _defaultIndentationLevel;
@ _itemIdentifier;
```

## Properties

```
@property (T@"NSArray",C,N,V_leadingAccessoryConfigurations) leadingAccessoryConfigurations;
@property (T@"NSArray",C,N,V_trailingAccessoryConfigurations) trailingAccessoryConfigurations;
@property (T@"NSArray",C,N,V_leadingEditingAccessoryConfigurations) leadingEditingAccessoryConfigurations;
@property (T@"NSArray",C,N,V_trailingEditingAccessoryConfigurations) trailingEditingAccessoryConfigurations;
@property (T@"UIView",R,N,G_owningViewForSeparatorLayoutGuide) owningViewForSeparatorLayoutGuide;
@property (T@"<UITableConstants>",R,N,G_constants,V_constants) constants;
@property (TB,N,G_expanded,S_setExpanded:) _expanded;
@property (T@?,C,N,S_setDisclosureActionHandler:,V__disclosureActionHandler) _disclosureActionHandler;
@property (T@"<UIFocusItem>",W,N,S_setParentFocusItem:,V__parentFocusItem) _parentFocusItem;
@property (T@"UICellAccessoryManager",R,N,G_accessoryManager,V_accessoryManager) accessoryManager;
@property (Tq,N,G_defaultIndentationLevel,S_setDefaultIndentationLevel:,V_defaultIndentationLevel) defaultIndentationLevel;
@property (T@,&,N,G_itemIdentifier,S_setItemIdentifier:,V_itemIdentifier) itemIdentifier;
@property (Tq,N,V_indentationLevel) indentationLevel;
@property (Td,N,V_indentationWidth) indentationWidth;
@property (TB,N) indentsAccessories;
@property (T@"NSArray",C,N,V_accessories) accessories;
@property (T@"UILayoutGuide",R,N) separatorLayoutGuide;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N,G_minimumCellAccessoryMargin) minimumCellAccessoryMargin;
@property (Tq,R,N,G_cellStyle) cellStyle;
```

## Class methods

```
+[UICollectionViewListCell _contentViewClass];
+[UICollectionViewListCell _createDefaultContentViewWithFrame:];
+[UICollectionViewListCell _createVisualProviderForCell:];
```

## Instance methods

```
-[UICollectionViewListCell _layoutMarginsDidChangeFromOldMargins:];
-[UICollectionViewListCell setSelectionStyle:];
-[UICollectionViewListCell _constants];
-[UICollectionViewListCell _listCellProminence];
-[UICollectionViewListCell _configureFocusedFloatingContentView:];
-[UICollectionViewListCell _safeAreaInsetsDidChangeFromOldInsets:];
-[UICollectionViewListCell layoutSubviews];
-[UICollectionViewListCell selectionStyle];
-[UICollectionViewListCell accessories];
-[UICollectionViewListCell setEditing:];
-[UICollectionViewListCell prepareForReuse];
-[UICollectionViewListCell encodeWithCoder:];
-[UICollectionViewListCell setAccessories:];
-[UICollectionViewListCell _edgesAbuttingAccessories];
-[UICollectionViewListCell _listCellStyle];
-[UICollectionViewListCell _updateSystemTypeAccessoryView:withCellAccessory:orConfiguration:usingState:isUserInitiated:];
-[UICollectionViewListCell initWithCoder:];
-[UICollectionViewListCell traitCollectionDidChange:];
-[UICollectionViewListCell _accessoryManager];
-[UICollectionViewListCell initWithFrame:];
-[UICollectionViewListCell indentationLevel];
-[UICollectionViewListCell _itemIdentifier];
-[UICollectionViewListCell _separatorInsetsFromLayoutGuide];
-[UICollectionViewListCell _setContentView:addToHierarchy:];
-[UICollectionViewListCell _updateConfigurationUsingState:];
-[UICollectionViewListCell _defaultBackgroundConfiguration];
-[UICollectionViewListCell _updateEdgesAbuttingAccessories];
-[UICollectionViewListCell trailingAccessoryConfigurations];
-[UICollectionViewListCell _adjustedRawLayoutMargins:withLeadingLayoutMarginAdjustment:];
-[UICollectionViewListCell _applyCellAccessoriesToNormalConfiguration:editingConfiguration:];
-[UICollectionViewListCell _canFocusProgrammatically];
-[UICollectionViewListCell _canPerformActionForKey:];
-[UICollectionViewListCell _cellAccessoriesForConfigurations:isLeadingEdge:];
-[UICollectionViewListCell _cellAccessoryForConfiguration:isLeadingEdge:usingState:];
-[UICollectionViewListCell _cellSelectionTogglesExpansionState];
-[UICollectionViewListCell _cellStyle];
-[UICollectionViewListCell _clearChangeHandlersForOldContentView:];
-[UICollectionViewListCell _computeAccessoryLayoutWidthWithTraitUsageTrackingForSelector:performing:];
-[UICollectionViewListCell _computeDisclosureAccessoryLayoutWidth];
-[UICollectionViewListCell _computeStandardAccessoryLayoutWidth];
-[UICollectionViewListCell _configurationState];
-[UICollectionViewListCell _constantsDidChange];
-[UICollectionViewListCell _contentView:inset:convertedToCellInsetOnEdge:];
-[UICollectionViewListCell _contentViewInset];
-[UICollectionViewListCell _contentViewShouldBeIndented];
-[UICollectionViewListCell _createAccessoryManager];
-[UICollectionViewListCell _createCustomAccessoryViewWithCellAccessory:updatedForState:];
-[UICollectionViewListCell _createSystemTypeAccessoryViewWithCellAccessory:orConfiguration:updatedForState:];
-[UICollectionViewListCell _defaultBackgroundConfigurationUsingSpecificStyling];
-[UICollectionViewListCell _defaultBackgroundView];
-[UICollectionViewListCell _defaultContentConfigurationUsingSpecificStyling];
-[UICollectionViewListCell _defaultFocusStyle];
-[UICollectionViewListCell _defaultIndentationLevel];
-[UICollectionViewListCell _defaultSelectedBackgroundView];
-[UICollectionViewListCell _deleteAccessoryTriggered];
-[UICollectionViewListCell _didPerformConfigurationStateUpdate];
-[UICollectionViewListCell _disclosureActionHandler];
-[UICollectionViewListCell _editingControlTintColorForStyle:];
-[UICollectionViewListCell _expanded];
-[UICollectionViewListCell _hasCustomSelectionAction];
-[UICollectionViewListCell _internalAccessoriesForCellAccessories:usingState:];
-[UICollectionViewListCell _invalidatePreferredSeparatorInsetsFromContentView];
-[UICollectionViewListCell _isAccompaniedSidebar];
-[UICollectionViewListCell _isFocusableWhenStyledAsHeader];
-[UICollectionViewListCell _layoutAccessoriesAndContentView];
-[UICollectionViewListCell _leadingIndentation];
-[UICollectionViewListCell _listStyle];
-[UICollectionViewListCell _minimumCellAccessoryMargin];
-[UICollectionViewListCell _owningViewForSeparatorLayoutGuide];
-[UICollectionViewListCell _parentFocusItem];
-[UICollectionViewListCell _performActionForKey:];
-[UICollectionViewListCell _performCustomSelectionAction];
-[UICollectionViewListCell _popUpMenuAccessory];
-[UICollectionViewListCell _popUpMenuAccessoryForCustomSelectionAction];
-[UICollectionViewListCell _preferredLayoutAttributesFittingAttributes:isAnimatingExistingView:];
-[UICollectionViewListCell _preferredSeparatorInsetsForProposedInsets:];
-[UICollectionViewListCell _preferredSeparatorInsetsFromContentViewWithDefaultInsets:];
-[UICollectionViewListCell _presentPopUpMenuForAccessory:];
-[UICollectionViewListCell _removesHighlightedAndSelectedStatesForBackground];
-[UICollectionViewListCell _reorderControl:didReceiveTouchesBegan:];
-[UICollectionViewListCell _reorderControl:didUpdateWithOffset:];
-[UICollectionViewListCell _reorderControlDidBeginReordering:];
-[UICollectionViewListCell _reorderControlDidEndReordering:cancelled:];
-[UICollectionViewListCell _reorderControlShouldBeginReordering:];
-[UICollectionViewListCell _resetRawLayoutMargins];
-[UICollectionViewListCell _separatorInsetsFromPrimaryTextLayoutFrameWithDefaultInsets:];
-[UICollectionViewListCell _setDefaultIndentationLevel:];
-[UICollectionViewListCell _setDisclosureActionHandler:];
-[UICollectionViewListCell _setExpanded:];
-[UICollectionViewListCell _setIndentationLevel:];
-[UICollectionViewListCell _setIndentationWidth:];
-[UICollectionViewListCell _setItemIdentifier:];
-[UICollectionViewListCell _setLayoutAttributes:];
-[UICollectionViewListCell _setNeedsUpdateAccessories];
-[UICollectionViewListCell _setParentFocusItem:];
-[UICollectionViewListCell _setRawLayoutMargins:];
-[UICollectionViewListCell _setSelected:animated:isUserInitiated:];
-[UICollectionViewListCell _setupChangeHandlersForNewContentView:];
-[UICollectionViewListCell _shouldIncreaseCellLeadingLayoutMarginForIndentation];
-[UICollectionViewListCell _shouldUseMonochromaticTreatmentForCellAccessory:orConfiguration:sidebarStyle:cellConfigurationState:traitCollection:];
-[UICollectionViewListCell _systemAccessoriesChanged];
-[UICollectionViewListCell _tableStyle];
-[UICollectionViewListCell _toggleExpansionState];
-[UICollectionViewListCell _updateAccessoriesIfNeeded];
-[UICollectionViewListCell _updateAccessoryLayoutMetrics];
-[UICollectionViewListCell _updateCellSelectionTogglesExpansionState];
-[UICollectionViewListCell _updateConstants];
-[UICollectionViewListCell _updateContentViewConstraintsIfNeeded];
-[UICollectionViewListCell _updateCurrentSystemTypeAccessoryViewsUsingState:];
-[UICollectionViewListCell _updateCustomAccessoryView:withCellAccessory:orConfiguration:usingState:isUserInitiated:];
-[UICollectionViewListCell _updateDefaultIndentationWidth];
-[UICollectionViewListCell _updateLeadingLayoutMarginForIndentation];
-[UICollectionViewListCell _updateSeparatorConfigurationForPreferredAttributes:bounds:isAnimatingExistingView:];
-[UICollectionViewListCell _updateSeparatorLayoutGuideForSectionSeparatorInsets:];
-[UICollectionViewListCell _updateSeparatorLayoutGuideHeight];
-[UICollectionViewListCell _validatedDisclosureActionForKey:];
-[UICollectionViewListCell _viewForMultiSelectAccessory];
-[UICollectionViewListCell canBeEdited];
-[UICollectionViewListCell defaultBackgroundConfiguration];
-[UICollectionViewListCell defaultContentConfiguration];
-[UICollectionViewListCell indentationWidth];
-[UICollectionViewListCell indentsAccessories];
-[UICollectionViewListCell leadingAccessoryConfigurations];
-[UICollectionViewListCell leadingEditingAccessoryConfigurations];
-[UICollectionViewListCell separatorLayoutGuide];
-[UICollectionViewListCell setIndentationLevel:];
-[UICollectionViewListCell setIndentationWidth:];
-[UICollectionViewListCell setIndentsAccessories:];
-[UICollectionViewListCell setLeadingAccessoryConfigurations:];
-[UICollectionViewListCell setLeadingEditingAccessoryConfigurations:];
-[UICollectionViewListCell setTrailingAccessoryConfigurations:];
-[UICollectionViewListCell setTrailingEditingAccessoryConfigurations:];
-[UICollectionViewListCell trailingEditingAccessoryConfigurations];
```
