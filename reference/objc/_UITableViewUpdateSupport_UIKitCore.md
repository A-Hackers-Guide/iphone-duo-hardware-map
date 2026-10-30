# `_UITableViewUpdateSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
q oldSection;
q newSection;
q oldGlobalRow;
q newGlobalRow;
@"UITableView" tableView;
{_NSRange="location"Q"length"Q} visibleRows;
@"NSArray" updateItems;
@"UITableViewRowData" oldRowData;
@"UITableViewRowData" newRowData;
{_NSRange="location"Q"length"Q} oldRowRange;
{_NSRange="location"Q"length"Q} newRowRange;
@"NSMutableIndexSet" movedRows;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} oldTableViewVisibleBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} newTableViewVisibleBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} tableViewVisibleBoundsUnion;
d tableViewVisibleBoundsOffset;
q oldSectionCount;
q newSectionCount;
q oldGlobalRowCount;
q newGlobalRowCount;
^@ animatedCells;
^@ animatedHeaders;
^@ animatedFooters;
q globalReorderingRow;
@ _context;
@"<_UITableViewIgnoreDragsToken>" _ignoringDragsToken;
B _updateItemUsedAutomaticRowAnimation;
@"NSMutableArray" viewAnimations;
@"NSMutableArray" deletedSections;
@"NSMutableArray" insertedSections;
{_UIDataSourceUpdateMaps="oldSectionCount"I"newSectionCount"I"oldGlobalItemCount"I"newGlobalItemCount"I"oldSectionMap"^I"newSectionMap"^I"oldGlobalItemMap"^I"newGlobalItemMap"^I"updatesAreInvalid"B} _updateMaps;
@"NSString" _invalidUpdatesErrorMessage;
```

## Instance methods

```
-[_UITableViewUpdateSupport dealloc];
```
