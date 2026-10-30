# `_UIInternalDraggingSessionSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDraggingImageSlotOwner`
- Protocols: `_UIDraggingInfo`
- 26 instance variables, 24 properties, 61 instance methods, 0 class methods

## Instance variables

```
{CAPoint3D="x"d"y"d"z"d} _lastNotifiedCentroid;
B _didHandOffDragImage;
@"PBItemCollection" _pbItemCollection;
@"UIDraggingSystemTouchRoutingPolicy" _touchRoutingPolicy;
@"_UIDragSetDownAnimation" _setDownAnimation;
q _stateAfterSetDown;
B _sentWillEnd;
B _hostIsActive;
B _originatedInHostedWindow;
@"NSTimer" _waitingToSendDidExitAppTimer;
@"UIDraggingBeginningSessionConfiguration" _configuration;
B _restrictedToSourceApp;
I _sessionIdentifier;
@"<_UIDraggingSessionDelegate>" _delegate;
@"UIDragEvent" _dragEvent;
@"UIView" _sourceView;
q _state;
Q _resultOperation;
@"NSArray" _internalItems;
q _dataOwner;
@"UIWindow" _centroidWindow;
@"UIWindow" _weakCentroidWindow;
Q _withinAppSourceOperationMask;
Q _outsideAppSourceOperationMask;
@"_UIDruidSourceConnection" _druidConnection;
{CAPoint3D="x"d"y"d"z"d} _centroid;
```

## Properties

```
@property (T@"_UIDruidSourceConnection",&,N,V_druidConnection) druidConnection;
@property (T@"<_UIDraggingSessionDelegate>",W,N,V_delegate) delegate;
@property (T@"UIDragEvent",W,N,V_dragEvent) dragEvent;
@property (T@"UIView",W,N,V_sourceView) sourceView;
@property (Tq,N,V_state) state;
@property (TQ,N,V_resultOperation) resultOperation;
@property (T@"NSArray",C,N,V_internalItems) internalItems;
@property (Tq,N,V_dataOwner) dataOwner;
@property (T{CAPoint3D=ddd},R,N,V_centroid) centroid;
@property (T@"UIWindow",R,N,V_centroidWindow) centroidWindow;
@property (T@"UIWindow",R,W,N,V_weakCentroidWindow) weakCentroidWindow;
@property (TI,R,N,V_sessionIdentifier) sessionIdentifier;
@property (TB,R,N,V_restrictedToSourceApp) restrictedToSourceApp;
@property (TQ,R,N,V_withinAppSourceOperationMask) withinAppSourceOperationMask;
@property (TQ,R,N,V_outsideAppSourceOperationMask) outsideAppSourceOperationMask;
@property (TB,R,N) prefersFullSizePreview;
@property (TB,R,N) canAddItems;
@property (TB,R,N) isActive;
@property (TB,R,N) didHandOffDragImage;
@property (TQ,R,N) draggingSourceOperationMask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIInternalDraggingSessionSource centroid];
-[_UIInternalDraggingSessionSource sessionIdentifier];
-[_UIInternalDraggingSessionSource setState:];
-[_UIInternalDraggingSessionSource setDelegate:];
-[_UIInternalDraggingSessionSource setSourceView:];
-[_UIInternalDraggingSessionSource delegate];
-[_UIInternalDraggingSessionSource isActive];
-[_UIInternalDraggingSessionSource state];
-[_UIInternalDraggingSessionSource sourceView];
-[_UIInternalDraggingSessionSource addPublicItems:];
-[_UIInternalDraggingSessionSource resultOperation];
-[_UIInternalDraggingSessionSource _sendHandedOffDragImageForItem:];
-[_UIInternalDraggingSessionSource dragIsInsideApp];
-[_UIInternalDraggingSessionSource druidConnection];
-[_UIInternalDraggingSessionSource _canHandOffCancelledItems:];
-[_UIInternalDraggingSessionSource _didBeginDrag];
-[_UIInternalDraggingSessionSource _endWithOperation:];
-[_UIInternalDraggingSessionSource _getOperationMaskFromDelegate];
-[_UIInternalDraggingSessionSource _handOffCancelledItems:completion:];
-[_UIInternalDraggingSessionSource _hostDidDeactivate];
-[_UIInternalDraggingSessionSource _hostWillBecomeActive];
-[_UIInternalDraggingSessionSource _routingPolicyHasSpecificTouchContextIDs];
-[_UIInternalDraggingSessionSource _sendDataTransferFinished];
-[_UIInternalDraggingSessionSource _sendDidEndWithOperation:];
-[_UIInternalDraggingSessionSource _sendDidMove];
-[_UIInternalDraggingSessionSource _sendDragPreviewReplyWithIndexSet:dragPreviews:completion:];
-[_UIInternalDraggingSessionSource _sendHandedOffDragImage];
-[_UIInternalDraggingSessionSource _sendWillAddItems:];
-[_UIInternalDraggingSessionSource _sendWillBegin];
-[_UIInternalDraggingSessionSource _sendWillEndWithOperation:];
-[_UIInternalDraggingSessionSource _setupAnimationForCancelledItems:returningLayerContext:];
-[_UIInternalDraggingSessionSource _updatedPresentation:];
-[_UIInternalDraggingSessionSource beginDrag:];
-[_UIInternalDraggingSessionSource canAddItems];
-[_UIInternalDraggingSessionSource cancelDrag];
-[_UIInternalDraggingSessionSource centroidWindow];
-[_UIInternalDraggingSessionSource dataOwner];
-[_UIInternalDraggingSessionSource didHandOffDragImage];
-[_UIInternalDraggingSessionSource dragDidExitApp];
-[_UIInternalDraggingSessionSource dragEvent];
-[_UIInternalDraggingSessionSource draggingLocationInCoordinateSpace:];
-[_UIInternalDraggingSessionSource draggingSourceOperationMask];
-[_UIInternalDraggingSessionSource dynamicallyUpdatesPrefersFullSizePreviews];
-[_UIInternalDraggingSessionSource enumerateItemsUsingBlock:];
-[_UIInternalDraggingSessionSource initWithDragManager:configuration:];
-[_UIInternalDraggingSessionSource internalItems];
-[_UIInternalDraggingSessionSource itemsBecameDirty:];
-[_UIInternalDraggingSessionSource outsideAppSourceOperationMask];
-[_UIInternalDraggingSessionSource prefersFullSizePreview];
-[_UIInternalDraggingSessionSource preventsSimultaneousDragFromView:];
-[_UIInternalDraggingSessionSource restrictedToSourceApp];
-[_UIInternalDraggingSessionSource setDataOwner:];
-[_UIInternalDraggingSessionSource setDragEvent:];
-[_UIInternalDraggingSessionSource setDruidConnection:];
-[_UIInternalDraggingSessionSource setInternalItems:];
-[_UIInternalDraggingSessionSource setResultOperation:];
-[_UIInternalDraggingSessionSource touchRoutingPolicy];
-[_UIInternalDraggingSessionSource touchRoutingPolicyContainsContextIDToAlwaysSend:];
-[_UIInternalDraggingSessionSource updateCentroidFromDragEvent];
-[_UIInternalDraggingSessionSource weakCentroidWindow];
-[_UIInternalDraggingSessionSource withinAppSourceOperationMask];
```
