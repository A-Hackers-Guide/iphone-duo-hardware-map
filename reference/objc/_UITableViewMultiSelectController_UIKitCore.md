# `_UITableViewMultiSelectController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIMultiSelectInteractionDelegate`
- 3 instance variables, 8 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"UITableView" _tableView;
@"UIMultiSelectInteraction" _multiSelectInteraction;
@"UIMultiSelectInteractionState" _currentSelectionState;
```

## Properties

```
@property (T@"UITableView",W,N,V_tableView) tableView;
@property (T@"UIMultiSelectInteraction",&,N,V_multiSelectInteraction) multiSelectInteraction;
@property (T@"UIMultiSelectInteractionState",&,N,V_currentSelectionState) currentSelectionState;
@property (TB,R,N,GisInMultiselectInteraction) inMultiselectInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITableViewMultiSelectController shouldAllowSelectionExtensionAtPoint:];
-[_UITableViewMultiSelectController multiSelectInteraction:extendSelectionInDirection:];
-[_UITableViewMultiSelectController supportsMultiSelectInteraction:];
-[_UITableViewMultiSelectController tableView];
-[_UITableViewMultiSelectController didCancelMultiSelectInteraction:atPoint:];
-[_UITableViewMultiSelectController keyCommandsForSelectionExtension];
-[_UITableViewMultiSelectController isInMultiSelectMode];
-[_UITableViewMultiSelectController _adjustSelectionRangeToIndexPath:isDeselecting:];
-[_UITableViewMultiSelectController _shouldBeginInteractionAtIndexPath:];
-[_UITableViewMultiSelectController multiSelectInteraction:toggleSelectionStateUpToPoint:];
-[_UITableViewMultiSelectController targetForKeyCommands];
-[_UITableViewMultiSelectController multiSelectInteraction];
-[_UITableViewMultiSelectController shouldAllowSelectionExtensionAtIndexPath:];
-[_UITableViewMultiSelectController _updateSelectedIndexPaths:];
-[_UITableViewMultiSelectController interaction:shouldAutomaticallyTransitionToMultiSelectModeAtPoint:withVelocity:];
-[_UITableViewMultiSelectController multiSelectInteraction:appendSelectionAtPoint:];
-[_UITableViewMultiSelectController toggleSelectionStateUpToIndexPath:];
-[_UITableViewMultiSelectController setCurrentSelectionState:];
-[_UITableViewMultiSelectController _updateSelectedIndexPathsForCurrentSelection];
-[_UITableViewMultiSelectController noteProgrammaticSelectionChangeAtIndexPath:];
-[_UITableViewMultiSelectController _selectIndexPaths:];
-[_UITableViewMultiSelectController willBeginMultiSelectInteraction:atPoint:keepCurrentSelection:];
-[_UITableViewMultiSelectController didEndMultiSelectInteraction:atPoint:];
-[_UITableViewMultiSelectController shouldAllowSelectionAppendageAtPoint:];
-[_UITableViewMultiSelectController uninstallFromTableView];
-[_UITableViewMultiSelectController isInMultiselectInteraction];
-[_UITableViewMultiSelectController _deselectIndexPaths:];
-[_UITableViewMultiSelectController setTableView:];
-[_UITableViewMultiSelectController initWithTableView:];
-[_UITableViewMultiSelectController supportsKeyboardSelectionExtension];
-[_UITableViewMultiSelectController _isPointInsideEditControl:];
-[_UITableViewMultiSelectController clearSelectionState];
-[_UITableViewMultiSelectController setMultiSelectInteraction:];
-[_UITableViewMultiSelectController currentSelectionState];
-[_UITableViewMultiSelectController _tableViewDelegate];
-[_UITableViewMultiSelectController shouldBeginMultiSelectInteraction:ofType:atPoint:withVelocity:];
-[_UITableViewMultiSelectController _shouldBeginInteractionAtPoint:];
-[_UITableViewMultiSelectController automaticallyTransitionToMultiSelectModeKeepingCurrentSelection:];
-[_UITableViewMultiSelectController _endAutoScroll];
-[_UITableViewMultiSelectController willBeginExtendingSelectionAtIndexPath:keepingSelection:];
-[_UITableViewMultiSelectController selectedIndexPathsChanged:];
-[_UITableViewMultiSelectController _handleAutoScrollFromPoint:];
-[_UITableViewMultiSelectController multiSelectInteractionGestureShouldPreventDragLiftGesture:];
```
