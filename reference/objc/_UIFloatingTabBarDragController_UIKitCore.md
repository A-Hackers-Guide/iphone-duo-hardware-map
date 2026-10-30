# `_UIFloatingTabBarDragController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionDelegate_Internal`, `UIDropInteractionDelegate`
- 13 instance variables, 16 properties, 47 instance methods, 0 class methods

## Instance variables

```
B _needsFavoriteOrderUpdate;
B _editing;
B _pendingDropTabHasValidTarget;
@"<_UIFloatingTabBarDragControllerDelegate>" _delegate;
@"UITab" _pendingDropTab;
@"UIDragItem" _activeDropItem;
@"UIDragInteraction" _dragInteraction;
@"UIDropInteraction" _dropInteraction;
@"UITab" _currentDragTab;
q _currentDragTabOriginalIndex;
@"<UIDropSession>" _activeDropSession;
@"NSMutableOrderedSet" _pendingFavoriteOrder;
@"NSMutableSet" _pendingExcludedItems;
```

## Properties

```
@property (T@"UIDragInteraction",R,N,V_dragInteraction) dragInteraction;
@property (T@"UIDropInteraction",R,N,V_dropInteraction) dropInteraction;
@property (T@"UITab",&,N,V_currentDragTab) currentDragTab;
@property (Tq,N,V_currentDragTabOriginalIndex) currentDragTabOriginalIndex;
@property (T@"UITab",&,N,V_pendingDropTab) pendingDropTab;
@property (T@"<UIDropSession>",W,N,V_activeDropSession) activeDropSession;
@property (TB,N,V_pendingDropTabHasValidTarget) pendingDropTabHasValidTarget;
@property (T@"NSMutableOrderedSet",&,N,V_pendingFavoriteOrder) pendingFavoriteOrder;
@property (T@"NSMutableSet",&,N,V_pendingExcludedItems) pendingExcludedItems;
@property (T@"<_UIFloatingTabBarDragControllerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,R,N,GisEditing,V_editing) editing;
@property (T@"UIDragItem",R,W,N,V_activeDropItem) activeDropItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFloatingTabBarDragController dragInteraction:previewForLiftingItem:session:];
-[_UIFloatingTabBarDragController dragInteraction:itemsForBeginningSession:];
-[_UIFloatingTabBarDragController dragInteraction:previewForCancellingItem:withDefault:];
-[_UIFloatingTabBarDragController dropInteraction:sessionDidEnter:];
-[_UIFloatingTabBarDragController dropInteraction:sessionDidUpdate:];
-[_UIFloatingTabBarDragController dragInteraction:session:didEndWithOperation:];
-[_UIFloatingTabBarDragController endEditing];
-[_UIFloatingTabBarDragController dragInteraction:session:willEndWithOperation:];
-[_UIFloatingTabBarDragController dropInteraction:performDrop:];
-[_UIFloatingTabBarDragController dropInteraction];
-[_UIFloatingTabBarDragController dragInteraction];
-[_UIFloatingTabBarDragController dragInteraction:sessionAllowsMoveOperation:];
-[_UIFloatingTabBarDragController dropInteraction:canHandleSession:];
-[_UIFloatingTabBarDragController dropInteraction:item:willAnimateDropWithAnimator:];
-[_UIFloatingTabBarDragController delegate];
-[_UIFloatingTabBarDragController dropInteraction:sessionDidExit:];
-[_UIFloatingTabBarDragController dragInteraction:willAnimateLiftWithAnimator:session:];
-[_UIFloatingTabBarDragController dropInteraction:sessionDidEnd:];
-[_UIFloatingTabBarDragController isEditing];
-[_UIFloatingTabBarDragController dropInteraction:previewForDroppingItem:withDefault:];
-[_UIFloatingTabBarDragController setCurrentDragTabOriginalIndex:];
-[_UIFloatingTabBarDragController _dragInteraction:delayForLiftBeginningAtLocation:];
-[_UIFloatingTabBarDragController _insertPlaceholderAtIndex:];
-[_UIFloatingTabBarDragController _removePlaceholder];
-[_UIFloatingTabBarDragController _shouldAddPlaceholderForPendingDrop];
-[_UIFloatingTabBarDragController _updateFavoriteOrderAnimated:];
-[_UIFloatingTabBarDragController activeDropItem];
-[_UIFloatingTabBarDragController activeDropSession];
-[_UIFloatingTabBarDragController beginEditingWithFavoriteOrder:excludedItems:];
-[_UIFloatingTabBarDragController currentDragTab];
-[_UIFloatingTabBarDragController currentDragTabOriginalIndex];
-[_UIFloatingTabBarDragController excludedItems];
-[_UIFloatingTabBarDragController hasActiveDrag];
-[_UIFloatingTabBarDragController initWithDelegate:view:];
-[_UIFloatingTabBarDragController insertTabForIdentifier:];
-[_UIFloatingTabBarDragController pendingDropTab];
-[_UIFloatingTabBarDragController pendingDropTabHasValidTarget];
-[_UIFloatingTabBarDragController pendingExcludedItems];
-[_UIFloatingTabBarDragController pendingFavoriteOrder];
-[_UIFloatingTabBarDragController removeTabForIdentifier:];
-[_UIFloatingTabBarDragController resetFavoriteOrderWithDefaultOrder:];
-[_UIFloatingTabBarDragController setActiveDropSession:];
-[_UIFloatingTabBarDragController setCurrentDragTab:];
-[_UIFloatingTabBarDragController setPendingDropTab:];
-[_UIFloatingTabBarDragController setPendingDropTabHasValidTarget:];
-[_UIFloatingTabBarDragController setPendingExcludedItems:];
-[_UIFloatingTabBarDragController setPendingFavoriteOrder:];
```
