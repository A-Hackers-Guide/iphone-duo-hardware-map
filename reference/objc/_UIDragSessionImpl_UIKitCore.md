# `_UIDragSessionImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDraggingSessionDelegate`, `UIDragSession`, `_UIDragSetDownAnimationTarget`, `_UIDragDropSessionInternal`
- 10 instance variables, 15 properties, 40 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _allItems;
@"NSMapTable" _dragSourceInteractionByItem;
@"NSHashTable" _allInteractions;
B _didHandOffDragImage;
@"NSMutableSet" _addedDraggingItemsWaitingForHandOffOfDragImage;
@"NSMutableSet" _addedDragItemsPendingUpdate;
B _sentSessionDidBegin;
@ _localContext;
@"_UIInternalDraggingSessionSource" _internalDragSession;
@"UIDragInteraction" _primaryInteraction;
```

## Properties

```
@property (T@"_UIInternalDraggingSessionSource",&,N,G_internalDragSession,S_setInternalDragSession:,V_internalDragSession) internalDragSession;
@property (T@"UIDragInteraction",R,W,N,V_primaryInteraction) primaryInteraction;
@property (T@"NSSet",R,N) trackedInteractions;
@property (TB,N,G_sentSessionDidBegin,S_setSentSessionDidBegin:,V_sentSessionDidBegin) sentSessionDidBegin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@,&,N,V_localContext) localContext;
@property (T@"NSArray",R,N) items;
@property (TB,R,N) allowsMoveOperation;
@property (TB,R,N,GisRestrictedToDraggingApplication) restrictedToDraggingApplication;
@property (TB,R,N,G_allowsItemsToUpdate) _allowsItemsToUpdate;
@property (Tq,R,N) _dataOwner;
@property (TI,R,N) _sessionIdentifier;
```

## Class methods

```
+[_UIDragSessionImpl activeSessions];
+[_UIDragSessionImpl _localDragSessionForSessionDestination:];
```

## Instance methods

```
-[_UIDragSessionImpl _cancelDrag];
-[_UIDragSessionImpl _isActive];
-[_UIDragSessionImpl _setDownAnimation:prepareForSetDownOfDragItem:visibleDroppedItem:];
-[_UIDragSessionImpl _setDownAnimation:willAnimateSetDownOfDragItem:withAnimator:preview:];
-[_UIDragSessionImpl initWithInteraction:];
-[_UIDragSessionImpl items];
-[_UIDragSessionImpl locationInView:];
-[_UIDragSessionImpl localContext];
-[_UIDragSessionImpl _windowForSetDownOfDragItem:];
-[_UIDragSessionImpl _setDownAnimation:customSpringAnimationBehaviorForSetDownOfDragItem:];
-[_UIDragSessionImpl _sessionIdentifier];
-[_UIDragSessionImpl _allowsItemsToUpdate];
-[_UIDragSessionImpl _canAddItems];
-[_UIDragSessionImpl _dataOwner];
-[_UIDragSessionImpl _draggingSession:handedOffDragImageForItem:];
-[_UIDragSessionImpl _draggingSessionHandedOffDragImage:];
-[_UIDragSessionImpl _internalDragSession];
-[_UIDragSessionImpl _internalSession];
-[_UIDragSessionImpl _itemsNeedUpdate:];
-[_UIDragSessionImpl _sentSessionDidBegin];
-[_UIDragSessionImpl _setInternalDragSession:];
-[_UIDragSessionImpl _setSentSessionDidBegin:];
-[_UIDragSessionImpl addItems:forDragSourceInteraction:];
-[_UIDragSessionImpl allowsMoveOperation];
-[_UIDragSessionImpl canLoadObjectsOfClass:];
-[_UIDragSessionImpl dragSourceInteractionForDragItem:];
-[_UIDragSessionImpl draggingSession:sourceOperationMaskForDraggingWithinApp:];
-[_UIDragSessionImpl draggingSession:willAddItems:];
-[_UIDragSessionImpl draggingSessionDidEnd:withOperation:];
-[_UIDragSessionImpl draggingSessionDidMove:];
-[_UIDragSessionImpl draggingSessionDidTransferItems:];
-[_UIDragSessionImpl draggingSessionDynamicallyUpdatesPrefersFullSizePreviews:];
-[_UIDragSessionImpl draggingSessionPrefersFullSizePreviews:];
-[_UIDragSessionImpl draggingSessionWillBegin:];
-[_UIDragSessionImpl draggingSessionWillEnd:withOperation:];
-[_UIDragSessionImpl hasItemsConformingToTypeIdentifiers:];
-[_UIDragSessionImpl isRestrictedToDraggingApplication];
-[_UIDragSessionImpl primaryInteraction];
-[_UIDragSessionImpl setLocalContext:];
-[_UIDragSessionImpl trackedInteractions];
```
