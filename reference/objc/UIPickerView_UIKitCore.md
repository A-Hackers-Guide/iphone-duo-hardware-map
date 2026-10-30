# `UIPickerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPickerViewScrollTesting`, `UITableViewDelegate`, `UIPickerTableViewContainerDelegate`, `UITableViewDataSource`, `NSCoding`
- 19 instance variables, 19 properties, 119 instance methods, 11 class methods

## Instance variables

```
@"NSMutableArray" _tables;
@"<UIPickerViewDataSource>" _dataSource;
@"<UIPickerViewDelegate>" _delegate;
q _numberOfComponents;
@"UIView" _foregroundView;
@"CALayer" _maskGradientLayer;
@"CALayer" _maskMagnifierLayer;
@"UIView" _topLineOrFillView;
@"UIView" _bottomLineView;
{?="needsLayout"b1"delegateRespondsToNumberOfComponentsInPickerView"b1"delegateRespondsToNumberOfRowsInComponent"b1"delegateRespondsToDidSelectRow"b1"delegateRespondsToViewForRow"b1"delegateRespondsToTitleForRow"b1"delegateRespondsToAttributedTitleForRow"b1"delegateRespondsToWidthForComponent"b1"delegateRespondsToRowHeightForComponent"b1"showsSelectionBar"b1"allowsMultipleSelection"b1"allowSelectingCells"b1"soundsDisabled"b1"usesCheckedSelection"b1"skipsBackground"b1"isInLayoutSubviews"b1"usesDynamicRowHeight"b1"selectionBarIgnoresInset"b1} _pickerViewFlags;
@"UIColor" _textColor;
@"UIColor" _textShadowColor;
@"_UIPickerViewStyle" _style;
@"_UIPickerViewTestParameters" _currentTestParameters;
B _magnifierEnabled;
B _enabled;
q _magnifierStyle;
@"UISelectionFeedbackGenerator" _selectionFeedbackGenerator;
@"UIColor" _magnifierLineColor;
```

## Properties

```
@property (TB,N,G_enabled,S_setEnabled:,V_enabled) enabled;
@property (Tq,N,G_magnifierStyle,S_setMagnifierStyle:,V_magnifierStyle) magnifierStyle;
@property (T@"_UIPickerViewStyle",R,N,G_style) style;
@property (TB,N,S_setMagnifierEnabled:,V_magnifierEnabled) _magnifierEnabled;
@property (T@"UISelectionFeedbackGenerator",&,N,G_selectionFeedbackGenerator,S_setSelectionFeedbackGenerator:,V_selectionFeedbackGenerator) selectionFeedbackGenerator;
@property (T@"UIColor",&,N,G_highlightColor,S_setHighlightColor:) highlightColor;
@property (T@"UIColor",&,N,G_textColor,S_setTextColor:) textColor;
@property (T@"UIColor",&,N,G_textShadowColor,S_setTextShadowColor:) textShadowColor;
@property (T@"UIColor",&,N,G_magnifierLineColor,S_setMagnifierLineColor:,V_magnifierLineColor) magnifierLineColor;
@property (TB,G_usesDynamicRowHeight,S_setUsesDynamicRowHeight:) usesDynamicRowHeight;
@property (TB,N,S_setSelectionBarIgnoresInset:) _selectionBarIgnoresInset;
@property (T@"<UIPickerViewDataSource>",W,N,V_dataSource) dataSource;
@property (T@"<UIPickerViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N) showsSelectionIndicator;
@property (Tq,R,N,V_numberOfComponents) numberOfComponents;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPickerView initialize];
+[UIPickerView _setAllowsUnsupportedMacIdiomBehavior:];
+[UIPickerView _allowsUnsupportedMacIdiomBehavior];
+[UIPickerView _prepareStyleStorageIfNecessary];
+[UIPickerView _styleForIdiom:];
+[UIPickerView _registerStyle:forIdiom:];
+[UIPickerView defaultSizeForCurrentOrientation];
+[UIPickerView defaultSizeForMainScreenTraits];
+[UIPickerView defaultSizeForTraits:];
+[UIPickerView sizeForMainScreenTraitsThatFits:];
+[UIPickerView sizeThatFits:forTraits:];
```

## Instance methods

```
-[UIPickerView setNeedsLayout];
-[UIPickerView numberOfColumns];
-[UIPickerView tableView:numberOfRowsInSection:];
-[UIPickerView tableView:cellForRowAtIndexPath:];
-[UIPickerView _usesCheckSelection];
-[UIPickerView _setTextColor:];
-[UIPickerView didMoveToWindow];
-[UIPickerView _systemDefaultFocusGroupIdentifier];
-[UIPickerView _selectRow:inComponent:animated:notify:];
-[UIPickerView _textColor];
-[UIPickerView setAllowsMultipleSelection:];
-[UIPickerView _setEnabled:];
-[UIPickerView _intrinsicSizeWithinSize:];
-[UIPickerView init];
-[UIPickerView dealloc];
-[UIPickerView _contentView];
-[UIPickerView layoutSubviews];
-[UIPickerView setDataSource:];
-[UIPickerView hitTest:withEvent:];
-[UIPickerView reload];
-[UIPickerView setBounds:];
-[UIPickerView setBackgroundColor:];
-[UIPickerView reloadData];
-[UIPickerView sizeThatFits:];
-[UIPickerView _contentHuggingDefault_isUsuallyFixedHeight];
-[UIPickerView setDelegate:];
-[UIPickerView dataSource];
-[UIPickerView _resetSelectionOfTables];
-[UIPickerView _highlightColor];
-[UIPickerView encodeWithCoder:];
-[UIPickerView delegate];
-[UIPickerView setFrame:];
-[UIPickerView _sendCheckedRow:inTableView:checked:];
-[UIPickerView _style];
-[UIPickerView _perspectiveTransform];
-[UIPickerView _tableRowHeight];
-[UIPickerView initWithCoder:];
-[UIPickerView traitCollectionDidChange:];
-[UIPickerView _populateArchivedSubviews:];
-[UIPickerView initWithFrame:];
-[UIPickerView _soundsEnabled];
-[UIPickerView numberOfComponents];
-[UIPickerView _contentHuggingDefault_isUsuallyFixedWidth];
-[UIPickerView _addMagnifierLinesForRowHeight:];
-[UIPickerView _contentSizeForRow:inComponent:];
-[UIPickerView _delegateRowHeightForComponent:];
-[UIPickerView selectRow:inComponent:animated:];
-[UIPickerView _magnifierStyle];
-[UIPickerView _setSelectionFeedbackGenerator:];
-[UIPickerView isAccessibilityElementByDefault];
-[UIPickerView _addHighlightRectForRowHeight:];
-[UIPickerView _addMagnifierForRowHeight:];
-[UIPickerView _canHostViewControllerContentScrollView];
-[UIPickerView _completeCurrentTest];
-[UIPickerView _createColumnWithTableFrame:rowHeight:paddingAroundWheels:];
-[UIPickerView _createTableWithFrame:forComponent:];
-[UIPickerView _delegateAttributedTitleForRow:forComponent:];
-[UIPickerView _delegateNumberOfComponents];
-[UIPickerView _delegateNumberOfRowsInComponent:];
-[UIPickerView _delegateTitleForRow:forComponent:];
-[UIPickerView _delegateWidthForComponent:ofCount:withSizeLeft:];
-[UIPickerView _drawsBackground];
-[UIPickerView _effectiveTableViewFrameForColumn:];
-[UIPickerView _enabled];
-[UIPickerView _forceTextAlignmentCentered];
-[UIPickerView _increaseContrastSettingDidChange:];
-[UIPickerView _iterateOnCurrentTest];
-[UIPickerView _magnifierEnabled];
-[UIPickerView _magnifierLineColor];
-[UIPickerView _needsLayout];
-[UIPickerView _noteScrollingFinishedForComponent:];
-[UIPickerView _performScrollTest:withIterations:rowsToScroll:inComponent:];
-[UIPickerView _rowHeightForDefaultFont];
-[UIPickerView _scalarStatisticsForUserValueChangedEvent];
-[UIPickerView _selectionBarIgnoresInset];
-[UIPickerView _selectionBarRectForHeight:];
-[UIPickerView _selectionBarSideInset];
-[UIPickerView _selectionBarSuffix];
-[UIPickerView _selectionFeedbackGenerator];
-[UIPickerView _sendSelectionChangedForComponent:notify:];
-[UIPickerView _sendSelectionChangedFromTable:notify:];
-[UIPickerView _setColumnView:enabled:];
-[UIPickerView _setDrawsBackground:];
-[UIPickerView _setHighlightColor:];
-[UIPickerView _setMagnifierEnabled:];
-[UIPickerView _setMagnifierLineColor:];
-[UIPickerView _setMagnifierStyle:];
-[UIPickerView _setSelectionBarIgnoresInset:];
-[UIPickerView _setTextShadowColor:];
-[UIPickerView _setUsesCheckedSelection:];
-[UIPickerView _setUsesDynamicRowHeight:];
-[UIPickerView _sizeThatFits:];
-[UIPickerView _textShadowColor];
-[UIPickerView _updateSelectedRows];
-[UIPickerView _updateWithOldSize:newSize:];
-[UIPickerView _usesCheckedSelection];
-[UIPickerView _usesDynamicRowHeight];
-[UIPickerView _wheelShift];
-[UIPickerView _willPlayClickSound];
-[UIPickerView allowsMultipleSelection];
-[UIPickerView columnForTableView:];
-[UIPickerView defaultSize];
-[UIPickerView numberOfRowsInColumn:];
-[UIPickerView numberOfRowsInComponent:];
-[UIPickerView reloadAllComponents];
-[UIPickerView reloadAllPickerPieces];
-[UIPickerView reloadComponent:];
-[UIPickerView reloadDataForColumn:];
-[UIPickerView rowSizeForComponent:];
-[UIPickerView scrollAnimationDuration];
-[UIPickerView selectRow:inColumn:animated:];
-[UIPickerView selectedRowForColumn:];
-[UIPickerView selectedRowInComponent:];
-[UIPickerView setShowsSelectionIndicator:];
-[UIPickerView setSoundsEnabled:];
-[UIPickerView showsSelectionIndicator];
-[UIPickerView tableViewForColumn:];
-[UIPickerView viewForRow:forComponent:];
-[UIPickerView visibleRowsForColumn:];
```
