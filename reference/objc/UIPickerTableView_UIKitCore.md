# `UIPickerTableView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableView`
- Protocols: `UITableViewDelegate`
- 11 instance variables, 10 properties, 52 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _selectionBarRect;
q _selectionBarRow;
@"NSMutableIndexSet" _checkedRows;
d _lastClickedOffset;
q _lastSelectedRow;
@"UIColor" _textColor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleRect;
@"NSMutableArray" _referencingCells;
{?="allowsMultipleSelection"b1"scrollingDirection"b2"didSelectDisabled"b1"skipRowChangeNotifications"b1"scrollingForSelection"b1"cancellingAnimation"b1"updatingContentInset"b1} _pickerTableFlags;
B _playsFeedback;
B _generatorActivated;
```

## Properties

```
@property (Tq,N,S_setSelectionBarRow:,V_selectionBarRow) selectionBarRow;
@property (TB,N,V_generatorActivated) generatorActivated;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_selectionBarRect) selectionBarRect;
@property (Tq,N,V_lastSelectedRow) lastSelectedRow;
@property (TB,G_playsFeedback,S_setPlaysFeedback:,V_playsFeedback) playsFeedback;
@property (T@"UIColor",&,N,G_textColor,S_setTextColor:) _textColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPickerTableView _isInternalTableView];
```

## Instance methods

```
-[UIPickerTableView _scrollViewAnimationEnded:finished:];
-[UIPickerTableView _visibleBounds];
-[UIPickerTableView _setContentOffset:notify:];
-[UIPickerTableView _setTextColor:];
-[UIPickerTableView lastSelectedRow];
-[UIPickerTableView _playsFeedback];
-[UIPickerTableView _scrollingFinished];
-[UIPickerTableView _textColor];
-[UIPickerTableView _anyDateLabel];
-[UIPickerTableView _scrollViewDidInterruptDecelerating:];
-[UIPickerTableView _checkedRows];
-[UIPickerTableView selectionBarRow];
-[UIPickerTableView scrollViewShouldScrollToTop:];
-[UIPickerTableView setGeneratorActivated:];
-[UIPickerTableView setContentOffset:];
-[UIPickerTableView dealloc];
-[UIPickerTableView _updateContentInsets];
-[UIPickerTableView layoutSubviews];
-[UIPickerTableView _transformForCellAtY:];
-[UIPickerTableView tableView:willDisplayCell:forRowAtIndexPath:];
-[UIPickerTableView didSelectDisabled:];
-[UIPickerTableView _rectChangedWithNewSize:oldSize:];
-[UIPickerTableView setBounds:];
-[UIPickerTableView selectRow:animated:notify:];
-[UIPickerTableView contentOffsetForRowAtIndexPath:];
-[UIPickerTableView _contentInsetAdjustmentBehavior];
-[UIPickerTableView scrollViewWillEndDragging:withVelocity:targetContentOffset:];
-[UIPickerTableView _playClickIfNecessary];
-[UIPickerTableView _scrollRowAtIndexPathToSelectionBar:animated:];
-[UIPickerTableView selectionBarRect];
-[UIPickerTableView _beginTrackingWithEvent:];
-[UIPickerTableView isRowChecked:];
-[UIPickerTableView _setPlaysFeedback:];
-[UIPickerTableView tableView:willSelectRowAtIndexPath:];
-[UIPickerTableView scrollViewDidEndScrollingAnimation:];
-[UIPickerTableView generatorActivated];
-[UIPickerTableView scrollViewWillBeginDragging:];
-[UIPickerTableView _shouldWrapCells];
-[UIPickerTableView _containerView];
-[UIPickerTableView tableView:didSelectRowAtIndexPath:];
-[UIPickerTableView setFrame:];
-[UIPickerTableView setSelectionBarRect:];
-[UIPickerTableView _pickerView];
-[UIPickerTableView initWithFrame:style:visibleRect:];
-[UIPickerTableView scrollViewDidEndDragging:willDecelerate:];
-[UIPickerTableView selectRow:animated:notify:updateChecked:];
-[UIPickerTableView scrollViewDidEndDecelerating:];
-[UIPickerTableView _notifyContentOffsetChange];
-[UIPickerTableView _setSelectionBarRow:];
-[UIPickerTableView _deactivateFeedbackGeneratorIfNeeded];
-[UIPickerTableView _selectionBarRectForBounds:];
-[UIPickerTableView setLastSelectedRow:];
```
