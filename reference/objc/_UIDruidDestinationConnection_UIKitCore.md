# `_UIDruidDestinationConnection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_DUIClientDestination`, `_DUIClientSessionDestination`, `_UIDruidDestinationConnection`
- 13 instance variables, 14 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"<_DUIServerSessionDestination>" _serverSession;
@"_DUIPotentialDrop" _lastPotentialDrop;
@"NSXPCConnection" _connection;
B _systemPolicy;
I _sessionIdentifier;
@? _connectionBlock;
@? _dragEndBlock;
@? _dropPerformBlock;
@? _handOffDroppedItemsBlock;
@? _dragPreviewProviderBlock;
@? _itemsAddedBlock;
@? _updatedPresentationBlock;
q _state;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (TB,N,GisSystemPolicy,V_systemPolicy) systemPolicy;
@property (TI,R,N,V_sessionIdentifier) sessionIdentifier;
@property (T@?,C,N,V_connectionBlock) connectionBlock;
@property (T@?,C,N,V_dragPreviewProviderBlock) dragPreviewProviderBlock;
@property (T@?,C,N,V_itemsAddedBlock) itemsAddedBlock;
@property (T@?,C,N,V_dropPerformBlock) dropPerformBlock;
@property (T@?,C,N,V_handOffDroppedItemsBlock) handOffDroppedItemsBlock;
@property (T@?,C,N,V_dragEndBlock) dragEndBlock;
@property (T@?,C,N,V_updatedPresentationBlock) updatedPresentationBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDruidDestinationConnection connect];
-[_UIDruidDestinationConnection sessionIdentifier];
-[_UIDruidDestinationConnection setState:];
-[_UIDruidDestinationConnection state];
-[_UIDruidDestinationConnection itemsAddedBlock];
-[_UIDruidDestinationConnection sawDragEndEvent];
-[_UIDruidDestinationConnection connectionBlock];
-[_UIDruidDestinationConnection addedItemCollection:];
-[_UIDruidDestinationConnection dirtyItems:];
-[_UIDruidDestinationConnection dragEndBlock];
-[_UIDruidDestinationConnection dragEnded];
-[_UIDruidDestinationConnection dragPreviewProviderBlock];
-[_UIDruidDestinationConnection dropPerformBlock];
-[_UIDruidDestinationConnection enableKeyboardIfNeeded];
-[_UIDruidDestinationConnection handOffDroppedItems:withFence:completion:];
-[_UIDruidDestinationConnection handOffDroppedItemsBlock];
-[_UIDruidDestinationConnection initWithSessionIdentifier:systemPolicy:];
-[_UIDruidDestinationConnection invalidateLastPotentialDrop];
-[_UIDruidDestinationConnection isSystemPolicy];
-[_UIDruidDestinationConnection performDropWithItemCollection:dataProviderEndpoint:visibleDroppedItems:completion:];
-[_UIDruidDestinationConnection requestDragPreviewsForIndexSet:reply:];
-[_UIDruidDestinationConnection requestDropWithOperation:layerContext:];
-[_UIDruidDestinationConnection requestVisibleItems:];
-[_UIDruidDestinationConnection serverDestinationProxyWithErrorHandler:];
-[_UIDruidDestinationConnection setConnectionBlock:];
-[_UIDruidDestinationConnection setDragEndBlock:];
-[_UIDruidDestinationConnection setDragPreviewProviderBlock:];
-[_UIDruidDestinationConnection setDropPerformBlock:];
-[_UIDruidDestinationConnection setHandOffDroppedItemsBlock:];
-[_UIDruidDestinationConnection setItemsAddedBlock:];
-[_UIDruidDestinationConnection setSystemPolicy:];
-[_UIDruidDestinationConnection setUpdatedPresentationBlock:];
-[_UIDruidDestinationConnection takePotentialDrop:];
-[_UIDruidDestinationConnection updatedPresentation:];
-[_UIDruidDestinationConnection updatedPresentationBlock];
```
