# `UIPickerColumnView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIPickerColumn`, `UIPickerTableViewContainerDelegate`, `UITableViewDataSource`
- 16 instance variables, 14 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"UIPickerTableView" _topTable;
@"UIPickerTableView" _middleTable;
@"UIPickerTableView" _bottomTable;
@"UIView" _topContainerView;
@"UIView" _middleContainerView;
@"UIView" _bottomContainerView;
d _middleBarHeight;
d _rowHeight;
d _paddingAroundWheels;
@"UIPickerView" _pickerView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _tableFrame;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _perspectiveTransform;
B _isNoLongerInUse;
@"UIColor" __textColor;
d _leftHitTestExtension;
d _rightHitTestExtension;
```

## Properties

```
@property (TB,N,V_isNoLongerInUse) isNoLongerInUse;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) selectionBarRect;
@property (Tq,R,N) selectionBarRow;
@property (T@"UIColor",&,N,G_textColor,S_setTextColor:,V__textColor) _textColor;
@property (Td,N,V_rowHeight) rowHeight;
@property (T{CATransform3D=dddddddddddddddd},N,V_perspectiveTransform) perspectiveTransform;
@property (Td,N,V_leftHitTestExtension) leftHitTestExtension;
@property (Td,N,V_rightHitTestExtension) rightHitTestExtension;
@property (T@"UIView",R,N) view;
@property (T@"UIView",R,N) highlightedRegion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPickerColumnView tableView:numberOfRowsInSection:];
-[UIPickerColumnView tableView:cellForRowAtIndexPath:];
-[UIPickerColumnView _pointLiesWithinEffectiveTableBounds:];
-[UIPickerColumnView endUpdates];
-[UIPickerColumnView accessibilityFrame];
-[UIPickerColumnView _usesCheckSelection];
-[UIPickerColumnView isNoLongerInUse];
-[UIPickerColumnView _setTextColor:];
-[UIPickerColumnView _systemDefaultFocusGroupIdentifier];
-[UIPickerColumnView _horizontalBiasForEndTables];
-[UIPickerColumnView _textColor];
-[UIPickerColumnView markAsNoLongerInUse];
-[UIPickerColumnView setAllowsMultipleSelection:];
-[UIPickerColumnView _moveTableViewIfNecessary:toContentOffset:];
-[UIPickerColumnView setRowHeight:];
-[UIPickerColumnView selectionBarRow];
-[UIPickerColumnView _containerViewForLegacyFocusRing];
-[UIPickerColumnView setPerspectiveTransform:];
-[UIPickerColumnView setRightHitTestExtension:];
-[UIPickerColumnView _visibleGlobalRows];
-[UIPickerColumnView _defaultFocusRegionFrame];
-[UIPickerColumnView _transformForTableWithTranslationX:];
-[UIPickerColumnView cellForRowAtIndexPath:];
-[UIPickerColumnView rightHitTestExtension];
-[UIPickerColumnView selectRow:animated:notify:];
-[UIPickerColumnView canBecomeFocused];
-[UIPickerColumnView _centerTableInContainer:];
-[UIPickerColumnView _transformForTableWithPerspectiveTranslationX:];
-[UIPickerColumnView _allVisibleCells];
-[UIPickerColumnView reloadData];
-[UIPickerColumnView _createContainerViewWithFrame:];
-[UIPickerColumnView _containsTable:];
-[UIPickerColumnView view];
-[UIPickerColumnView _defaultFocusEffect];
-[UIPickerColumnView highlightedRegion];
-[UIPickerColumnView _scrollRowAtIndexPathToSelectionBar:animated:];
-[UIPickerColumnView selectionBarRect];
-[UIPickerColumnView isRowChecked:];
-[UIPickerColumnView initWithFrame:tableFrame:middleBarHeight:rowHeight:paddingAroundWheels:pickerView:transform:];
-[UIPickerColumnView setIsNoLongerInUse:];
-[UIPickerColumnView numberOfRowsInSection:];
-[UIPickerColumnView _createTableViewWithFrame:containingFrame:];
-[UIPickerColumnView rowHeight];
-[UIPickerColumnView setSelectionBarRect:];
-[UIPickerColumnView _tableFrame];
-[UIPickerColumnView _sendCheckedRow:inTableView:checked:];
-[UIPickerColumnView beginUpdates];
-[UIPickerColumnView _visibleCellClosestToPoint:inView:];
-[UIPickerColumnView setLeftHitTestExtension:];
-[UIPickerColumnView selectRow:animated:notify:updateChecked:];
-[UIPickerColumnView leftHitTestExtension];
-[UIPickerColumnView perspectiveTransform];
-[UIPickerColumnView pickerTableView:didChangeSelectionBarRowFrom:to:];
-[UIPickerColumnView _preferredTable];
-[UIPickerColumnView _soundsEnabled];
-[UIPickerColumnView _pickerTableViewDidChangeContentOffset:];
```
