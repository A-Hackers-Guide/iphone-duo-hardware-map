# `_UIDruidSourceConnection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_DUIClientSource`, `_DUIClientSessionSource`, `_UIDruidSourceConnection`
- 10 instance variables, 11 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
@"NSObject<OS_dispatch_source>" _connectionWatchdogTimer;
@"<_DUIServerSessionSource>" _serverSession;
B _cancelled;
@? _dragPreviewProviderBlock;
@? _canHandOffCancelledItemsBlock;
@? _handOffCancelledItemsBlock;
@? _dragCompletionBlock;
@? _dataTransferFinishedBlock;
@? _updatedPresentationBlock;
```

## Properties

```
@property (TB,R,N,GisCancelled) cancelled;
@property (T@?,C,N,V_dragPreviewProviderBlock) dragPreviewProviderBlock;
@property (T@?,C,N,V_updatedPresentationBlock) updatedPresentationBlock;
@property (T@?,C,N,V_canHandOffCancelledItemsBlock) canHandOffCancelledItemsBlock;
@property (T@?,C,N,V_handOffCancelledItemsBlock) handOffCancelledItemsBlock;
@property (T@?,C,N,V_dragCompletionBlock) dragCompletionBlock;
@property (T@?,C,N,V_dataTransferFinishedBlock) dataTransferFinishedBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDruidSourceConnection init];
-[_UIDruidSourceConnection isCancelled];
-[_UIDruidSourceConnection addItems:withOldItemCollection:];
-[_UIDruidSourceConnection _internalDragFailed];
-[_UIDruidSourceConnection beginDragWithConfiguration:completion:];
-[_UIDruidSourceConnection canHandOffCancelledItems:withReply:];
-[_UIDruidSourceConnection canHandOffCancelledItemsBlock];
-[_UIDruidSourceConnection cancelAndClearWatchdogTimer];
-[_UIDruidSourceConnection cancelDrag];
-[_UIDruidSourceConnection dataTransferFinishedBlock];
-[_UIDruidSourceConnection dataTransferSessionFinished];
-[_UIDruidSourceConnection dirtyItems:];
-[_UIDruidSourceConnection dragCompletionBlock];
-[_UIDruidSourceConnection dragDidExitApp];
-[_UIDruidSourceConnection dragEndedWithOperation:];
-[_UIDruidSourceConnection dragFailed];
-[_UIDruidSourceConnection dragPreviewProviderBlock];
-[_UIDruidSourceConnection handOffCancelledItems:withFence:completion:];
-[_UIDruidSourceConnection handOffCancelledItemsBlock];
-[_UIDruidSourceConnection requestDragPreviewsForIndexSet:reply:];
-[_UIDruidSourceConnection setCanHandOffCancelledItemsBlock:];
-[_UIDruidSourceConnection setDataTransferFinishedBlock:];
-[_UIDruidSourceConnection setDragCompletionBlock:];
-[_UIDruidSourceConnection setDragPreviewProviderBlock:];
-[_UIDruidSourceConnection setHandOffCancelledItemsBlock:];
-[_UIDruidSourceConnection setUpdatedPresentationBlock:];
-[_UIDruidSourceConnection takeInsideAppSourceOperationMask:outsideAppSourceOperationMask:prefersFullSizePreview:];
-[_UIDruidSourceConnection updatedPresentation:];
-[_UIDruidSourceConnection updatedPresentationBlock];
```
