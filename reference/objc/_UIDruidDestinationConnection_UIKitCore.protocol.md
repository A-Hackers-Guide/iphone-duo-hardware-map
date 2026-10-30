# `_UIDruidDestinationConnection` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 25 instance methods, 0 class methods

## Properties

```
@property (TI,R,N) sessionIdentifier;
@property (T@?,C,N) connectionBlock;
@property (T@?,C,N) dragPreviewProviderBlock;
@property (T@?,C,N) itemsAddedBlock;
@property (T@?,C,N) dropPerformBlock;
@property (T@?,C,N) handOffDroppedItemsBlock;
@property (T@?,C,N) dragEndBlock;
@property (T@?,C,N) updatedPresentationBlock;
```

## Instance methods

```
-[_UIDruidDestinationConnection connect];
-[_UIDruidDestinationConnection sessionIdentifier];
-[_UIDruidDestinationConnection init];
-[_UIDruidDestinationConnection itemsAddedBlock];
-[_UIDruidDestinationConnection sawDragEndEvent];
-[_UIDruidDestinationConnection connectionBlock];
-[_UIDruidDestinationConnection dirtyItems:];
-[_UIDruidDestinationConnection dragEndBlock];
-[_UIDruidDestinationConnection dragPreviewProviderBlock];
-[_UIDruidDestinationConnection dropPerformBlock];
-[_UIDruidDestinationConnection enableKeyboardIfNeeded];
-[_UIDruidDestinationConnection handOffDroppedItemsBlock];
-[_UIDruidDestinationConnection initWithSessionIdentifier:systemPolicy:];
-[_UIDruidDestinationConnection invalidateLastPotentialDrop];
-[_UIDruidDestinationConnection requestDropWithOperation:layerContext:];
-[_UIDruidDestinationConnection requestVisibleItems:];
-[_UIDruidDestinationConnection setConnectionBlock:];
-[_UIDruidDestinationConnection setDragEndBlock:];
-[_UIDruidDestinationConnection setDragPreviewProviderBlock:];
-[_UIDruidDestinationConnection setDropPerformBlock:];
-[_UIDruidDestinationConnection setHandOffDroppedItemsBlock:];
-[_UIDruidDestinationConnection setItemsAddedBlock:];
-[_UIDruidDestinationConnection setUpdatedPresentationBlock:];
-[_UIDruidDestinationConnection takePotentialDrop:];
-[_UIDruidDestinationConnection updatedPresentationBlock];
```
