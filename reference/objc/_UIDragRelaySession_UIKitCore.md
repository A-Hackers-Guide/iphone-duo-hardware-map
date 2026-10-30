# `_UIDragRelaySession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDraggingSessionDelegate`
- 4 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
I _sessionIdentifier;
@"<_UIDragRelaySessionDelegate>" _delegate;
@"_UIInternalDraggingSessionSource" _draggingSessionSource;
@"NSArray" _dragItems;
```

## Properties

```
@property (TI,V_sessionIdentifier) sessionIdentifier;
@property (T@"_UIInternalDraggingSessionSource",&,N,V_draggingSessionSource) draggingSessionSource;
@property (T@"NSArray",&,N,V_dragItems) dragItems;
@property (T@"<_UIDragRelaySessionDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDragRelaySession sessionIdentifier];
-[_UIDragRelaySession setSessionIdentifier:];
-[_UIDragRelaySession setDelegate:];
-[_UIDragRelaySession delegate];
-[_UIDragRelaySession _draggingSession:updatedPresentation:];
-[_UIDragRelaySession beginDragFromView:point:];
-[_UIDragRelaySession cancelDrag];
-[_UIDragRelaySession dragItems];
-[_UIDragRelaySession dragSessionCompletedInitialCheckIn];
-[_UIDragRelaySession draggingSession:sourceOperationMaskForDraggingWithinApp:];
-[_UIDragRelaySession draggingSessionDidEnd:withOperation:];
-[_UIDragRelaySession draggingSessionDidTransferItems:];
-[_UIDragRelaySession draggingSessionDynamicallyUpdatesPrefersFullSizePreviews:];
-[_UIDragRelaySession draggingSessionSource];
-[_UIDragRelaySession initWithDragItems:];
-[_UIDragRelaySession setDragItems:];
-[_UIDragRelaySession setDraggingSessionSource:];
-[_UIDragRelaySession updateDragPreviewForItemsAtIndexes:];
```
