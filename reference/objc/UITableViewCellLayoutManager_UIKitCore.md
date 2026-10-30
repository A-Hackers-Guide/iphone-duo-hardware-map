# `UITableViewCellLayoutManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 87 instance methods, 6 class methods

## Class methods

```
+[UITableViewCellLayoutManager initialize];
+[UITableViewCellLayoutManager _externalDetailTextColor];
+[UITableViewCellLayoutManager _externalTextColor];
+[UITableViewCellLayoutManager layoutManagerForTableViewCellStyle:];
+[UITableViewCellLayoutManager requiresLegacyLayout];
+[UITableViewCellLayoutManager sharedLayoutManager];
```

## Instance methods

```
-[UITableViewCellLayoutManager defaultImageViewForCell:];
-[UITableViewCellLayoutManager standardLayoutImageViewFrameForCell:forSizing:];
-[UITableViewCellLayoutManager defaultDetailTextLabelFontSizeForCell:];
-[UITableViewCellLayoutManager defaultDetailTextLabelFontForCell:];
-[UITableViewCellLayoutManager getTextLabelRect:detailTextLabelRect:forCell:rowWidth:forSizing:];
-[UITableViewCellLayoutManager layoutSubviewsOfCell:];
-[UITableViewCellLayoutManager detailTextLabelForCell:];
-[UITableViewCellLayoutManager textRectForCell:rowWidth:forSizing:];
-[UITableViewCellLayoutManager textLabelForCell:];
-[UITableViewCellLayoutManager defaultTextLabelFontSizeForCell:];
-[UITableViewCellLayoutManager intrinsicContentSizeForCell:rowWidth:];
-[UITableViewCellLayoutManager imageViewForCell:];
-[UITableViewCellLayoutManager _adjustedBackgroundRectForCell:];
-[UITableViewCellLayoutManager editControlShouldAppearForCell:];
-[UITableViewCellLayoutManager _accessoryRectForCell:offscreen:];
-[UITableViewCellLayoutManager _accessoryRectForCell:offscreen:rowWidth:];
-[UITableViewCellLayoutManager _adjustedBackgroundContentRectForCell:];
-[UITableViewCellLayoutManager _adjustedBackgroundContentRectForCell:rowWidth:];
-[UITableViewCellLayoutManager _adjustedBackgroundRectForCell:rowWidth:];
-[UITableViewCellLayoutManager _backgroundRectForCell:];
-[UITableViewCellLayoutManager _backgroundRectForCell:rowWidth:];
-[UITableViewCellLayoutManager _contentRectForCell:forEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager _contentRectForCell:forEditingState:showingDeleteConfirmation:rowWidth:];
-[UITableViewCellLayoutManager _contentRectLeadingOffsetForCell:editingState:rowWidth:];
-[UITableViewCellLayoutManager _editControlOnSameSideAsReorderControlForCell:];
-[UITableViewCellLayoutManager _editControlRectForCell:offscreen:];
-[UITableViewCellLayoutManager _editingAccessoryRectForCell:offscreen:];
-[UITableViewCellLayoutManager _layoutFocusGuidesForCell:];
-[UITableViewCellLayoutManager _legacy_cell:didTransitionToState:];
-[UITableViewCellLayoutManager _legacy_cell:willTransitionToState:];
-[UITableViewCellLayoutManager _legacy_contentRectForCell:forEditingState:showingDeleteConfirmation:rowWidth:];
-[UITableViewCellLayoutManager _legacy_layoutSubviewsOfCell:];
-[UITableViewCellLayoutManager _modern_cell:didTransitionToState:];
-[UITableViewCellLayoutManager _modern_layoutSubviewsOfCell:];
-[UITableViewCellLayoutManager _reconfigureCell:];
-[UITableViewCellLayoutManager _reorderControlRectForCell:offscreen:];
-[UITableViewCellLayoutManager _reorderSeparatorRectForCell:offscreen:];
-[UITableViewCellLayoutManager _resetTextLabelDefaultFontInCell:];
-[UITableViewCellLayoutManager _updateFocusGuidesForCell:editing:];
-[UITableViewCellLayoutManager accessoryEndingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager accessoryShouldAppearForCell:];
-[UITableViewCellLayoutManager accessoryShouldFadeForCell:];
-[UITableViewCellLayoutManager accessoryStartingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager backgroundEndingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager backgroundStartingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager badgeForCell:];
-[UITableViewCellLayoutManager cell:didTransitionToState:];
-[UITableViewCellLayoutManager cell:willTransitionToState:];
-[UITableViewCellLayoutManager contentEndingRectForCell:forDisplayOfDeleteConfirmation:];
-[UITableViewCellLayoutManager contentEndingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager contentIndentationForCell:];
-[UITableViewCellLayoutManager contentRectForCell:forState:];
-[UITableViewCellLayoutManager contentRectForCell:forState:rowWidth:];
-[UITableViewCellLayoutManager contentStartingRectForCell:forDisplayOfDeleteConfirmation:];
-[UITableViewCellLayoutManager contentStartingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager customAccessoryViewForCell:editing:];
-[UITableViewCellLayoutManager defaultBadgeForCell:];
-[UITableViewCellLayoutManager defaultEditableTextFieldForCell:];
-[UITableViewCellLayoutManager defaultLabelForCell:];
-[UITableViewCellLayoutManager defaultLabelForCell:ofClass:];
-[UITableViewCellLayoutManager defaultTextLabelFontForCell:];
-[UITableViewCellLayoutManager editControlEndingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager editControlShouldFadeForCell:];
-[UITableViewCellLayoutManager editControlStartingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager editableTextFieldForCell:];
-[UITableViewCellLayoutManager editingAccessoryEndingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager editingAccessoryShouldAppearForCell:];
-[UITableViewCellLayoutManager editingAccessoryShouldFadeForCell:];
-[UITableViewCellLayoutManager editingAccessoryStartingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager optimumSizeForLabel:inTotalTextRect:minimizeWidthOnVerticalOverflow:preferSingleLineWidth:];
-[UITableViewCellLayoutManager prepareCellForReuse:];
-[UITableViewCellLayoutManager reorderControlEndingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager reorderControlShouldAppearForCell:];
-[UITableViewCellLayoutManager reorderControlShouldFadeForCell:];
-[UITableViewCellLayoutManager reorderControlStartingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager reorderSeparatorEndingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager reorderSeparatorShouldAppearForCell:];
-[UITableViewCellLayoutManager reorderSeparatorShouldFadeForCell:];
-[UITableViewCellLayoutManager reorderSeparatorStartingRectForCell:forNewEditingState:showingDeleteConfirmation:];
-[UITableViewCellLayoutManager requiredIndentationForFirstLineOfCell:rowWidth:];
-[UITableViewCellLayoutManager requiredIndentationForFirstLineOfCell:rowWidth:forSizing:];
-[UITableViewCellLayoutManager selectedBackgroundEndingRectForCell:forNewEditingState:];
-[UITableViewCellLayoutManager shouldApplyAccessibilityLargeTextLayoutForCell:];
-[UITableViewCellLayoutManager shouldIncreaseMarginForImageViewInCell:];
-[UITableViewCellLayoutManager shouldStackAccessoryViewVerticallyForCell:editing:];
-[UITableViewCellLayoutManager textRectForCell:];
-[UITableViewCellLayoutManager textRectForCell:rowWidth:];
```
