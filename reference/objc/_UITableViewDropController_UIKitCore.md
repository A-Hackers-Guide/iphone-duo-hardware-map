# `_UITableViewDropController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDropInteractionDelegate_Private`, `_UITableViewDropCoordinatorDelegate`
- 9 instance variables, 16 properties, 46 instance methods, 0 class methods

## Instance variables

```
B _canOnlyHandleReordering;
@"UIDropInteraction" _dropInteraction;
@"UITableView<_UITableViewDropControllerDelegate>" _tableView;
Q _defaultDropOperation;
@"NSIndexPath" _targetIndexPath;
@"UITableViewDropProposal" _dropProposal;
@"<UIDropSession>" _dropSession;
q _ignoringDragsCount;
@"NSMapTable" _dragItemDropAnimations;
```

## Properties

```
@property (T@"UIDropInteraction",&,N,V_dropInteraction) dropInteraction;
@property (T@"UITableView<_UITableViewDropControllerDelegate>",W,N,V_tableView) tableView;
@property (TQ,N,V_defaultDropOperation) defaultDropOperation;
@property (TB,R,N,GisTrackingDrag) trackingDrag;
@property (T@"NSIndexPath",&,N,V_targetIndexPath) targetIndexPath;
@property (T@"UITableViewDropProposal",&,N,V_dropProposal) dropProposal;
@property (T@"<UIDropSession>",&,N,V_dropSession) dropSession;
@property (TB,R,N) shouldIgnoreDrags;
@property (Tq,N,V_ignoringDragsCount) ignoringDragsCount;
@property (T@"NSMapTable",&,N,V_dragItemDropAnimations) dragItemDropAnimations;
@property (TB,N,V_canOnlyHandleReordering) canOnlyHandleReordering;
@property (TB,R,N,GisActive) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITableViewDropController dropSession];
-[_UITableViewDropController tableView];
-[_UITableViewDropController dropInteraction:sessionDidEnter:];
-[_UITableViewDropController dropInteraction:sessionDidUpdate:];
-[_UITableViewDropController _dropInteraction:dataOwnerForSession:];
-[_UITableViewDropController dropInteraction:concludeDrop:];
-[_UITableViewDropController dropInteraction:performDrop:];
-[_UITableViewDropController dropInteraction];
-[_UITableViewDropController setupDragInteraction];
-[_UITableViewDropController uninstallFromTableView];
-[_UITableViewDropController dropInteraction:item:willAnimateDropWithAnimator:];
-[_UITableViewDropController setTableView:];
-[_UITableViewDropController initWithTableView:];
-[_UITableViewDropController dropInteraction:sessionDidExit:];
-[_UITableViewDropController isActive];
-[_UITableViewDropController dropInteraction:sessionDidEnd:];
-[_UITableViewDropController dropProposal];
-[_UITableViewDropController dropInteraction:previewForDroppingItem:withDefault:];
-[_UITableViewDropController targetIndexPath];
-[_UITableViewDropController setDropSession:];
-[_UITableViewDropController animateDragItem:intoRowAtIndexPath:rect:];
-[_UITableViewDropController animateDragItem:toCell:withPreviewParameters:];
-[_UITableViewDropController animateDragItem:toRowAtIndexPath:];
-[_UITableViewDropController animateDragItem:toTarget:];
-[_UITableViewDropController beginIgnoringDrags];
-[_UITableViewDropController canOnlyHandleReordering];
-[_UITableViewDropController commitPlaceholderInsertionWithContext:dataSourceUpdates:];
-[_UITableViewDropController defaultAnimatorForDragItem:];
-[_UITableViewDropController defaultDropOperation];
-[_UITableViewDropController deletePlaceholder:];
-[_UITableViewDropController dragItemDropAnimations];
-[_UITableViewDropController endIgnoringDrags];
-[_UITableViewDropController ignoringDragsCount];
-[_UITableViewDropController insertPlaceholderAtIndexPath:withContext:previewParametersProvider:];
-[_UITableViewDropController isTrackingDrag];
-[_UITableViewDropController resetAllDragState];
-[_UITableViewDropController resetTrackingState];
-[_UITableViewDropController setCanOnlyHandleReordering:];
-[_UITableViewDropController setDefaultDropOperation:];
-[_UITableViewDropController setDragItemDropAnimations:];
-[_UITableViewDropController setDropInteraction:];
-[_UITableViewDropController setDropProposal:];
-[_UITableViewDropController setIgnoringDragsCount:];
-[_UITableViewDropController setTargetIndexPath:];
-[_UITableViewDropController shouldIgnoreDrags];
-[_UITableViewDropController updateTargetIndexPathAndDropProposalForSession:];
```
