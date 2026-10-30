# `_UIDragManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"CAContext" _dragImageContext;
q _pendingSessionRequests;
@"NSMutableArray" _pendingSessionRequestsCompletionBlocks;
@"NSArray" _dragSessionSources;
@"NSArray" _dragSessionDestinations;
@"UIScreen" _screen;
```

## Properties

```
@property (T@"NSArray",C,N,V_dragSessionSources) dragSessionSources;
@property (T@"NSArray",C,N,V_dragSessionDestinations) dragSessionDestinations;
@property (T@"CAContext",R,N) dragImageContext;
@property (T@"UIScreen",R,W,N,V_screen) screen;
```

## Class methods

```
+[_UIDragManager initializeDraggingSystem];
```

## Instance methods

```
-[_UIDragManager initWithScreen:];
-[_UIDragManager screen];
-[_UIDragManager beginDragWithSessionConfiguration:];
-[_UIDragManager deleteSlots:];
-[_UIDragManager dragDestinationWithEvent:];
-[_UIDragManager dragImageContext];
-[_UIDragManager dragSessionDestinations];
-[_UIDragManager dragSessionSources];
-[_UIDragManager hasPendingSessionRequests];
-[_UIDragManager performAfterCompletingPendingSessionRequests:];
-[_UIDragManager performPendingSessionCompletionBlocksIfPossible];
-[_UIDragManager sessionDestinationDidEnd:];
-[_UIDragManager sessionSourceDidEnd:];
-[_UIDragManager sessionSourceWithIdentifier:];
-[_UIDragManager setDragSessionDestinations:];
-[_UIDragManager setDragSessionSources:];
-[_UIDragManager uploadImage:];
```
