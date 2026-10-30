# `UITable_UITableViewCellDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UITable`
- 0 instance variables, 8 properties, 39 instance methods, 0 class methods

## Properties

```
@property (Td,R,N,G_rowSpacing) rowSpacing;
@property (T{UIEdgeInsets=dddd},R,N,G_rawSeparatorInset) rawSeparatorInset;
@property (Tq,R,N,G_popoverControllerStyle) popoverControllerStyle;
@property (TB,R,N,G_isInModalViewController) inModalViewController;
@property (TB,R,N,G_wasEditing) wasEditing;
@property (TB,R,N,G_isEditingForSwipeDeletion) editingForSwipeDeletion;
@property (T@"UITableViewCell",&,N,G_swipeToDeleteCell,S_setSwipeToDeleteCell:) swipeToDeleteCell;
@property (TB,R,N) selectionFollowsFocus;
```

## Instance methods

```
-[UITable_UITableViewCellDelegate setEditing:animated:];
-[UITable_UITableViewCellDelegate _endReorderingForCell:wasCancelled:animated:];
-[UITable_UITableViewCellDelegate _cellDidShowSelectedBackground:];
-[UITable_UITableViewCellDelegate _cellDidHideSelectedBackground:];
-[UITable_UITableViewCellDelegate _isReorderControlActiveForCell:];
-[UITable_UITableViewCellDelegate _reorderingCell];
-[UITable_UITableViewCellDelegate _accessoryButtonAction:];
-[UITable_UITableViewCellDelegate _animateDeletionOfRowAtIndexPath:];
-[UITable_UITableViewCellDelegate _animateDeletionOfRowWithCell:];
-[UITable_UITableViewCellDelegate _beginReorderingForCell:touch:];
-[UITable_UITableViewCellDelegate _calloutTargetRectForCell:];
-[UITable_UITableViewCellDelegate _canFocusCell:];
-[UITable_UITableViewCellDelegate _canPerformAction:forCell:sender:];
-[UITable_UITableViewCellDelegate _cellDidBecomeFocused:];
-[UITable_UITableViewCellDelegate _cellDidBecomeUnfocused:];
-[UITable_UITableViewCellDelegate _cellDidInvalidateIntrinsicContentSize:];
-[UITable_UITableViewCellDelegate _cellFocusItemDeferral:];
-[UITable_UITableViewCellDelegate _didInsertRowForTableCell:];
-[UITable_UITableViewCellDelegate _draggingReorderingCell:yDelta:touch:];
-[UITable_UITableViewCellDelegate _effectiveDefaultAllowsFocus];
-[UITable_UITableViewCellDelegate _highlightCell:animated:scrollPosition:highlight:];
-[UITable_UITableViewCellDelegate _highlightDidEndForCell:withInteraction:];
-[UITable_UITableViewCellDelegate _isCellReorderable:];
-[UITable_UITableViewCellDelegate _isEditingForSwipeDeletion];
-[UITable_UITableViewCellDelegate _isInModalViewController];
-[UITable_UITableViewCellDelegate _performAction:forCell:sender:];
-[UITable_UITableViewCellDelegate _popoverControllerStyle];
-[UITable_UITableViewCellDelegate _prepareHighlightForCell:withInteraction:];
-[UITable_UITableViewCellDelegate _rawSeparatorInset];
-[UITable_UITableViewCellDelegate _rowSpacing];
-[UITable_UITableViewCellDelegate _setSwipeToDeleteCell:];
-[UITable_UITableViewCellDelegate _shouldShowMenuForCell:];
-[UITable_UITableViewCellDelegate _swipeToDeleteCell];
-[UITable_UITableViewCellDelegate _swipeToDeleteCell:];
-[UITable_UITableViewCellDelegate _titleForDeleteConfirmationButton:];
-[UITable_UITableViewCellDelegate _updateCell:withValue:];
-[UITable_UITableViewCellDelegate _userSelectCell:];
-[UITable_UITableViewCellDelegate _wasEditing];
-[UITable_UITableViewCellDelegate selectionFollowsFocus];
```
