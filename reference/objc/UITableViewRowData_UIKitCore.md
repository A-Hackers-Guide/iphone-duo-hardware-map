# `UITableViewRowData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 25 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"<UITable_RowDataSource>" _tableView;
@"UITableViewHeaderFooterView" _headerFooterViewUsedForMeasurements;
d _tableViewWidth;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _sectionContentInset;
q _numSections;
B _estimatesHeights;
q _sectionRowDataCapacity;
^@ _sectionRowData;
d _tableHeaderHeight;
d _tableFooterHeight;
d _heightForTableHeaderViewHiding;
q _headerFooterPinningBehavior;
{?="tableHeaderHeightValid"b1"tableFooterHeightValid"b1"tableSidePaddingValid"b1"usesVariableMargins"b1"pinsTableHeaderView"b1} _rowDataFlags;
d _minimumRowHeight;
d _rowSpacing;
d _tableTopPadding;
d _tableBottomPadding;
d _tableSidePadding;
@"NSIndexPath" _gapIndexPath;
@"NSIndexPath" _reorderedIndexPath;
@"NSIndexPath" _draggedIndexPath;
d _defaultSectionHeaderHeight;
d _defaultSectionFooterHeight;
d _gapRowHeight;
d _draggedRowHeight;
```

## Class methods

```
+[UITableViewRowData sectionLocationForRow:inSection:numRows:gapIndexPath:rowSpacing:];
```

## Instance methods

```
-[UITableViewRowData dealloc];
-[UITableViewRowData description];
-[UITableViewRowData copyWithZone:];
```
