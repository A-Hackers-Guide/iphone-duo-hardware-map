# `_UIInternalDraggingSessionDestination`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDraggingImageSlotOwner`
- Protocols: `_UIDataTransferMonitorDelegate`, `NSProgressReporting`, `_UIDraggingInfo`
- 31 instance variables, 26 properties, 51 instance methods, 0 class methods

## Instance variables

```
I _sessionIdentifier;
I _touchRoutingPolicyContextID;
@"_UIInternalDraggingSessionSource" _sessionSource;
B _connectedToDruid;
B _isPolicyDriven;
B _dragInteractionDidEnd;
@"NSMutableSet" _enteredDestinations;
@"<_UIDropInteractionOwning>" _dropDestinationOwner;
@"UIWindow" _dropDestinationWindow;
@? _dropPerformBlock;
@? _dropCompletionBlock;
@? _postDropAnimationCompletionBlock;
@"_UIDragSetDownAnimation" _setDownAnimation;
@"PBItemCollection" _droppedItemCollection;
@"_UIDataTransferMonitor" _dataTransferMonitor;
@"_UIApplicationModalProgressController" _modalProgressAlertController;
B _dropWasPerformed;
@"NSPointerArray" _dragEvents;
B _isAccessibilitySession;
B _drivenByPointer;
@"_UIDropSessionImpl" _dropSession;
@"UIWindow" _centroidWindow;
@"UIWindow" _weakCentroidWindow;
@"NSArray" _dropItemProviders;
q _sourceDataOwner;
@"NSArray" _internalItems;
Q _outsideAppSourceOperationMask;
Q _progressIndicatorStyle;
@"<_UIDruidDestinationConnection>" _druidConnection;
@"NSProgress" _progress;
{CAPoint3D="x"d"y"d"z"d} _centroid;
```

## Properties

```
@property (T@"<_UIDruidDestinationConnection>",&,N,V_druidConnection) druidConnection;
@property (T@"NSProgress",&,N,V_progress) progress;
@property (T@"NSArray",R,N) dragEvents;
@property (TI,R,N,V_sessionIdentifier) sessionIdentifier;
@property (T@"UIDragEvent",R,N) activeDragEvent;
@property (T@"_UIInternalDraggingSessionSource",R,N) inAppSessionSource;
@property (T@"_UIDropSessionImpl",R,N,V_dropSession) dropSession;
@property (T{CAPoint3D=ddd},R,N,V_centroid) centroid;
@property (T@"UIWindow",R,N,V_centroidWindow) centroidWindow;
@property (T@"UIWindow",R,W,N,V_weakCentroidWindow) weakCentroidWindow;
@property (TB,R,N) shouldDragEventBeSentToGestureRecognizers;
@property (TB,R,N) didRequestDropToBePerformed;
@property (T@"NSArray",R,N) preDropItemProviders;
@property (T@"NSArray",R,N,V_dropItemProviders) dropItemProviders;
@property (Tq,R,N,V_sourceDataOwner) sourceDataOwner;
@property (T@"NSArray",C,N,V_internalItems) internalItems;
@property (TQ,R,N,V_outsideAppSourceOperationMask) outsideAppSourceOperationMask;
@property (TQ,R,N) sourceOperationMask;
@property (TB,R,N,V_isAccessibilitySession) isAccessibilitySession;
@property (TB,R,N,V_drivenByPointer) drivenByPointer;
@property (TQ,N,V_progressIndicatorStyle) progressIndicatorStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) draggingSourceOperationMask;
```

## Instance methods

```
-[_UIInternalDraggingSessionDestination dropSession];
-[_UIInternalDraggingSessionDestination connect];
-[_UIInternalDraggingSessionDestination centroid];
-[_UIInternalDraggingSessionDestination sessionIdentifier];
-[_UIInternalDraggingSessionDestination observeValueForKeyPath:ofObject:change:context:];
-[_UIInternalDraggingSessionDestination setProgress:];
-[_UIInternalDraggingSessionDestination progress];
-[_UIInternalDraggingSessionDestination progressIndicatorStyle];
-[_UIInternalDraggingSessionDestination setProgressIndicatorStyle:];
-[_UIInternalDraggingSessionDestination activeDragEvent];
-[_UIInternalDraggingSessionDestination drivenByPointer];
-[_UIInternalDraggingSessionDestination handOffDroppedItems:completion:];
-[_UIInternalDraggingSessionDestination sawDragEndEvent];
-[_UIInternalDraggingSessionDestination druidConnection];
-[_UIInternalDraggingSessionDestination sourceDataOwner];
-[_UIInternalDraggingSessionDestination _removeFromDragManager];
-[_UIInternalDraggingSessionDestination _sessionDidEndNormally:];
-[_UIInternalDraggingSessionDestination actualDragOperationForProposedDragOperation:destinationDataOwner:forbidden:];
-[_UIInternalDraggingSessionDestination addDragEvent:];
-[_UIInternalDraggingSessionDestination canBeDrivenByDragEvent:];
-[_UIInternalDraggingSessionDestination centroidWindow];
-[_UIInternalDraggingSessionDestination dataTransferMonitorBeganTransfers:];
-[_UIInternalDraggingSessionDestination dataTransferMonitorFinishedTransfers:];
-[_UIInternalDraggingSessionDestination didRequestDropToBePerformed];
-[_UIInternalDraggingSessionDestination dragDidExitApp];
-[_UIInternalDraggingSessionDestination dragEvents];
-[_UIInternalDraggingSessionDestination dragInteractionEnding];
-[_UIInternalDraggingSessionDestination draggingLocationInCoordinateSpace:];
-[_UIInternalDraggingSessionDestination draggingSourceOperationMask];
-[_UIInternalDraggingSessionDestination dropItemProviders];
-[_UIInternalDraggingSessionDestination enteredDestination:];
-[_UIInternalDraggingSessionDestination enumerateItemsUsingBlock:];
-[_UIInternalDraggingSessionDestination inAppSessionSource];
-[_UIInternalDraggingSessionDestination initWithDragManager:dragEvent:];
-[_UIInternalDraggingSessionDestination internalItems];
-[_UIInternalDraggingSessionDestination isAccessibilitySession];
-[_UIInternalDraggingSessionDestination itemsBecameDirty:];
-[_UIInternalDraggingSessionDestination outsideAppSourceOperationMask];
-[_UIInternalDraggingSessionDestination preDropItemProviders];
-[_UIInternalDraggingSessionDestination previewCenterForVisibleItem:inCoordinateSpace:];
-[_UIInternalDraggingSessionDestination requestDropOnOwner:withOperation:perform:completion:];
-[_UIInternalDraggingSessionDestination requestVisibleItems:];
-[_UIInternalDraggingSessionDestination setDruidConnection:];
-[_UIInternalDraggingSessionDestination setInternalItems:];
-[_UIInternalDraggingSessionDestination setUpDropAnimation:layerContext:];
-[_UIInternalDraggingSessionDestination shouldDragEventBeSentToGestureRecognizers];
-[_UIInternalDraggingSessionDestination sourceOperationMask];
-[_UIInternalDraggingSessionDestination takePotentialDrop:];
-[_UIInternalDraggingSessionDestination takeVisibleDroppedItems:];
-[_UIInternalDraggingSessionDestination updateCentroidFromDragEvent];
-[_UIInternalDraggingSessionDestination weakCentroidWindow];
```
