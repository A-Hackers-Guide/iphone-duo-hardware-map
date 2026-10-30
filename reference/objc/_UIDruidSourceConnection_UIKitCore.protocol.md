# `_UIDruidSourceConnection` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 19 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisCancelled) cancelled;
@property (T@?,C,N) dragPreviewProviderBlock;
@property (T@?,C,N) updatedPresentationBlock;
@property (T@?,C,N) canHandOffCancelledItemsBlock;
@property (T@?,C,N) handOffCancelledItemsBlock;
@property (T@?,C,N) dragCompletionBlock;
@property (T@?,C,N) dataTransferFinishedBlock;
```

## Instance methods

```
-[_UIDruidSourceConnection isCancelled];
-[_UIDruidSourceConnection addItems:withOldItemCollection:];
-[_UIDruidSourceConnection beginDragWithConfiguration:completion:];
-[_UIDruidSourceConnection canHandOffCancelledItemsBlock];
-[_UIDruidSourceConnection cancelDrag];
-[_UIDruidSourceConnection dataTransferFinishedBlock];
-[_UIDruidSourceConnection dirtyItems:];
-[_UIDruidSourceConnection dragCompletionBlock];
-[_UIDruidSourceConnection dragDidExitApp];
-[_UIDruidSourceConnection dragPreviewProviderBlock];
-[_UIDruidSourceConnection handOffCancelledItemsBlock];
-[_UIDruidSourceConnection setCanHandOffCancelledItemsBlock:];
-[_UIDruidSourceConnection setDataTransferFinishedBlock:];
-[_UIDruidSourceConnection setDragCompletionBlock:];
-[_UIDruidSourceConnection setDragPreviewProviderBlock:];
-[_UIDruidSourceConnection setHandOffCancelledItemsBlock:];
-[_UIDruidSourceConnection setUpdatedPresentationBlock:];
-[_UIDruidSourceConnection takeInsideAppSourceOperationMask:outsideAppSourceOperationMask:prefersFullSizePreview:];
-[_UIDruidSourceConnection updatedPresentationBlock];
```
