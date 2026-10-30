# `UITable_RowDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UITable`
- 0 instance variables, 28 properties, 51 instance methods, 0 class methods

## Properties

```
@property (T@"<UITableConstants>",R,N,G_constants) constants;
@property (T@"UITableMetricsAdapter",R,N,G_metricsAdapter) metricsAdapter;
@property (Td,R,N,G_headerFooterTrailingMarginWidth) headerFooterTrailingMarginWidth;
@property (Td,R,N,G_defaultSectionHeaderHeight) defaultSectionHeaderHeight;
@property (Td,R,N,G_defaultSectionFooterHeight) defaultSectionFooterHeight;
@property (Td,R,N,G_sidePadding) sidePadding;
@property (T{UIEdgeInsets=dddd},R,N,G_contentInset) _contentInset;
@property (T{UIEdgeInsets=dddd},R,N,G_tableContentInset) tableContentInset;
@property (Td,R,N,G_paddingAboveFirstSectionHeader) paddingAboveFirstSectionHeader;
@property (Td,R,N,G_paddingAboveSectionHeaders) paddingAboveSectionHeaders;
@property (Td,R,N,G_sectionHeaderToFirstRowPadding) sectionHeaderToFirstRowPadding;
@property (Td,R,N,G_sectionFooterToLastRowPadding) sectionFooterToLastRowPadding;
@property (Tq,R,N,G_headerFooterPinningBehavior) headerFooterPinningBehavior;
@property (T{UIEdgeInsets=dddd},R,N,G_sectionHeaderContentInsets) _sectionHeaderContentInsets;
@property (T{UIEdgeInsets=dddd},R,N,G_sectionFooterContentInsets) _sectionFooterContentInsets;
@property (Td,R,N,G_rowSpacing) rowSpacing;
@property (TB,R,N,G_isTableHeaderAutohiding) isTableHeaderAutohiding;
@property (Td,R,N,G_heightForTableHeader) heightForTableHeader;
@property (Td,R,N,G_heightForTableFooter) heightForTableFooter;
@property (TB,R,N,G_providesRowHeights) providesRowHeights;
@property (TB,R,N,G_estimatesHeights) estimatesHeights;
@property (TB,R,N,G_estimatesRowHeights) estimatesRowHeights;
@property (TB,R,N,G_estimatesSectionHeaderHeights) estimatesSectionHeaderHeights;
@property (TB,R,N,G_estimatesSectionFooterHeights) estimatesSectionFooterHeights;
@property (T@"UIView",R,N,G_tableHeaderView) tableHeaderView;
@property (T@"UIView",R,N,G_tableFooterView) tableFooterView;
@property (TB,R,N,G_shouldUseSearchBarHeaderBehavior) shouldUseSearchBarHeaderBehavior;
@property (TB,R,N,G_shouldUseNewHeaderFooterBehavior) shouldUseNewHeaderFooterBehavior;
```

## Instance methods

```
-[UITable_RowDataSource _constants];
-[UITable_RowDataSource _defaultSectionHeaderHeight];
-[UITable_RowDataSource _defaultSectionFooterHeight];
-[UITable_RowDataSource _headerFooterPinningBehavior];
-[UITable_RowDataSource _paddingAboveFirstSectionHeader];
-[UITable_RowDataSource _sectionHeaderToFirstRowPadding];
-[UITable_RowDataSource _metricsAdapter];
-[UITable_RowDataSource _applyContentSizeDeltaImmediately:];
-[UITable_RowDataSource _coalesceContentSizeUpdateWithDelta:];
-[UITable_RowDataSource _contentInset];
-[UITable_RowDataSource _dataSourceHeightForFooterInSection:];
-[UITable_RowDataSource _dataSourceHeightForHeaderInSection:];
-[UITable_RowDataSource _dataSourceHeightForRowAtIndexPath:];
-[UITable_RowDataSource _detailTextForHeaderInSection:];
-[UITable_RowDataSource _estimatedHeightForFooterInSection:];
-[UITable_RowDataSource _estimatedHeightForHeaderInSection:];
-[UITable_RowDataSource _estimatedHeightForRowAtIndexPath:];
-[UITable_RowDataSource _estimatesHeights];
-[UITable_RowDataSource _estimatesRowHeights];
-[UITable_RowDataSource _estimatesSectionFooterHeights];
-[UITable_RowDataSource _estimatesSectionHeaderHeights];
-[UITable_RowDataSource _headerFooterLeadingMarginWidthIsHeader:isFirstSection:];
-[UITable_RowDataSource _headerFooterTrailingMarginWidth];
-[UITable_RowDataSource _heightForFooterInSection:];
-[UITable_RowDataSource _heightForRowAtIndexPath:];
-[UITable_RowDataSource _heightForTableFooter];
-[UITable_RowDataSource _heightForTableHeader];
-[UITable_RowDataSource _isTableHeaderAutohiding];
-[UITable_RowDataSource _maxTitleWidthForFooterInSection:];
-[UITable_RowDataSource _maxTitleWidthForHeaderInSection:];
-[UITable_RowDataSource _paddingAboveSectionHeaders];
-[UITable_RowDataSource _prepareForRowDataHeaderFooterSizing];
-[UITable_RowDataSource _providesRowHeights];
-[UITable_RowDataSource _rowSpacing];
-[UITable_RowDataSource _sectionFooterContentInsets];
-[UITable_RowDataSource _sectionFooterToLastRowPadding];
-[UITable_RowDataSource _sectionHeaderContentInsets];
-[UITable_RowDataSource _setHeight:forRowAtIndexPath:usingPresentationValues:];
-[UITable_RowDataSource _shouldStripHeaderTopPaddingForSection:];
-[UITable_RowDataSource _shouldUseNewHeaderFooterBehavior];
-[UITable_RowDataSource _shouldUseSearchBarHeaderBehavior];
-[UITable_RowDataSource _sidePadding];
-[UITable_RowDataSource _sizeForHeaderInSection:];
-[UITable_RowDataSource _tableContentInset];
-[UITable_RowDataSource _tableFooterView];
-[UITable_RowDataSource _tableHeaderView];
-[UITable_RowDataSource _titleAlignmentForFooterInSection:];
-[UITable_RowDataSource _titleAlignmentForHeaderInSection:];
-[UITable_RowDataSource _titleForFooterInSection:];
-[UITable_RowDataSource _titleForHeaderInSection:];
-[UITable_RowDataSource _configureTableHeaderFooterView:forHeader:section:floating:withTitle:detailText:textAlignment:fromClient:];
```
