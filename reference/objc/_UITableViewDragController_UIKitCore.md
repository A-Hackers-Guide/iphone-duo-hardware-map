# `_UITableViewDragController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionDelegate_Internal`
- 12 instance variables, 19 properties, 56 instance methods, 1 class methods

## Instance variables

```
B _forceEnabledForReordering;
q _clientEnabledState;
@"<UIDragSession>" _dragSession;
@"NSMutableOrderedSet" _indexPaths;
@"UIDragInteraction" _dragInteraction;
@"UITableView<_UITableViewDragControllerDelegate>" _tableView;
@"UITableViewCell" _initiatingCell;
@"NSIndexPath" _initiatingIndexPath;
@"UITableViewCell" _tentativeInitiatingCell;
@"NSIndexPath" _tentativeInitiatingIndexPath;
@"NSMutableOrderedSet" _tentativeIndexPaths;
@"NSMapTable" _cellsAnimatingCancel;
```

## Properties

```
@property (T@"UIDragInteraction",&,N,V_dragInteraction) dragInteraction;
@property (T@"UITableView<_UITableViewDragControllerDelegate>",W,N,V_tableView) tableView;
@property (T@"UITableViewCell",&,N,V_initiatingCell) initiatingCell;
@property (T@"NSIndexPath",&,N,V_initiatingIndexPath) initiatingIndexPath;
@property (T@"NSMutableOrderedSet",&,N,V_indexPaths) indexPaths;
@property (T@"UITableViewCell",&,N,V_tentativeInitiatingCell) tentativeInitiatingCell;
@property (T@"NSIndexPath",&,N,V_tentativeInitiatingIndexPath) tentativeInitiatingIndexPath;
@property (T@"NSMutableOrderedSet",&,N,V_tentativeIndexPaths) tentativeIndexPaths;
@property (T@"<UIDragSession>",&,N,V_dragSession) dragSession;
@property (T@"NSMapTable",&,N,V_cellsAnimatingCancel) cellsAnimatingCancel;
@property (Tq,N,V_clientEnabledState) clientEnabledState;
@property (TB,N,V_forceEnabledForReordering) forceEnabledForReordering;
@property (TB,R,N,GisActive) active;
@property (T@"UITableViewCell",R,N) draggedCell;
@property (T@"NSIndexPath",R,N) draggedIndexPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITableViewDragController isEnabledByDefault];
```

## Instance methods

```
-[_UITableViewDragController dragInteraction:previewForLiftingItem:session:];
-[_UITableViewDragController tableView];
-[_UITableViewDragController dragInteraction:itemsForBeginningSession:];
-[_UITableViewDragController dragInteraction:previewForCancellingItem:withDefault:];
-[_UITableViewDragController dragInteraction:item:willAnimateCancelWithAnimator:];
-[_UITableViewDragController dragInteraction:session:didEndWithOperation:];
-[_UITableViewDragController dragInteraction:sessionWillBegin:];
-[_UITableViewDragController dragInteraction:prefersFullSizePreviewsForSession:];
-[_UITableViewDragController draggedCell];
-[_UITableViewDragController dragInteraction:sessionForAddingItems:withTouchAtPoint:];
-[_UITableViewDragController dragInteraction];
-[_UITableViewDragController dragInteraction:sessionAllowsMoveOperation:];
-[_UITableViewDragController setCellsAnimatingCancel:];
-[_UITableViewDragController initiatingCell];
-[_UITableViewDragController setTentativeIndexPaths:];
-[_UITableViewDragController tentativeInitiatingCell];
-[_UITableViewDragController setClientEnabledState:];
-[_UITableViewDragController dragInteraction:sessionIsRestrictedToDraggingApplication:];
-[_UITableViewDragController _dragInteraction:dataOwnerForSession:];
-[_UITableViewDragController setupDragInteraction];
-[_UITableViewDragController setInitiatingIndexPath:];
-[_UITableViewDragController setDragSession:];
-[_UITableViewDragController dragInteraction:session:willAddItems:forInteraction:];
-[_UITableViewDragController forceReset];
-[_UITableViewDragController _dragInteraction:sessionPropertiesForSession:];
-[_UITableViewDragController uninstallFromTableView];
-[_UITableViewDragController setTentativeInitiatingCell:];
-[_UITableViewDragController updateDragInteractionEnabledState];
-[_UITableViewDragController tentativeInitiatingIndexPath];
-[_UITableViewDragController _dragInteraction:dataOwnerForAddingToSession:withTouchAtPoint:];
-[_UITableViewDragController setTableView:];
-[_UITableViewDragController initWithTableView:];
-[_UITableViewDragController _dragInteractionDynamicallyUpdatesPrefersFullSizePreviews:];
-[_UITableViewDragController forceEnabledForReordering];
-[_UITableViewDragController dragSession];
-[_UITableViewDragController setInitiatingCell:];
-[_UITableViewDragController beginDragForTentativeRows];
-[_UITableViewDragController draggedIndexPath];
-[_UITableViewDragController cellsAnimatingCancel];
-[_UITableViewDragController clearTentativeRows];
-[_UITableViewDragController immediatelyBeginDragWithTouch:];
-[_UITableViewDragController dragInteraction:itemsForAddingToSession:withTouchAtPoint:];
-[_UITableViewDragController indexPaths];
-[_UITableViewDragController setForceEnabledForReordering:];
-[_UITableViewDragController dragInteraction:willAnimateLiftWithAnimator:session:];
-[_UITableViewDragController isActive];
-[_UITableViewDragController initiatingIndexPath];
-[_UITableViewDragController setDragInteraction:];
-[_UITableViewDragController setIndexPaths:];
-[_UITableViewDragController beginDragOfRowsForSession:notifyDelegate:];
-[_UITableViewDragController clientEnabledState];
-[_UITableViewDragController addTentativeRowAtIndexPath:];
-[_UITableViewDragController setTentativeInitiatingIndexPath:];
-[_UITableViewDragController canProvideItemsForDragAtPoint:];
-[_UITableViewDragController tentativeIndexPaths];
-[_UITableViewDragController resetDragState];
```
