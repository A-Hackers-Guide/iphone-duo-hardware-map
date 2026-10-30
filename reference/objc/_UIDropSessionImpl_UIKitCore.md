# `_UIDropSessionImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDropSession`, `_UIDragDropSessionInternal`, `_UIDropSessionPrivate`
- 4 instance variables, 16 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _items;
@"<UIDragSession>" _localDragSession;
Q _progressIndicatorStyle;
@"_UIInternalDraggingSessionDestination" _sessionDestination;
```

## Properties

```
@property (T@"_UIInternalDraggingSessionDestination",R,N,V_sessionDestination) sessionDestination;
@property (TQ,R,N,G_operationMask) operationMask;
@property (T@"<UIDragSession>",R,N,V_localDragSession) localDragSession;
@property (TQ,N,V_progressIndicatorStyle) progressIndicatorStyle;
@property (T@"NSArray",R,N) items;
@property (TB,R,N) allowsMoveOperation;
@property (TB,R,N,GisRestrictedToDraggingApplication) restrictedToDraggingApplication;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSProgress",R) progress;
@property (TB,R,N,G_allowsItemsToUpdate) _allowsItemsToUpdate;
@property (Tq,R,N) _dataOwner;
@property (TI,R,N) _sessionIdentifier;
@property (TB,R,N,G_drivenByPointer) drivenByPointer;
```

## Instance methods

```
-[_UIDropSessionImpl items];
-[_UIDropSessionImpl locationInView:];
-[_UIDropSessionImpl progress];
-[_UIDropSessionImpl progressIndicatorStyle];
-[_UIDropSessionImpl sessionDestination];
-[_UIDropSessionImpl setProgressIndicatorStyle:];
-[_UIDropSessionImpl _sessionIdentifier];
-[_UIDropSessionImpl _allowsItemsToUpdate];
-[_UIDropSessionImpl _createItemsOfClass:synchronouslyIfPossible:completion:];
-[_UIDropSessionImpl _dataOwner];
-[_UIDropSessionImpl _drivenByPointer];
-[_UIDropSessionImpl _internalSession];
-[_UIDropSessionImpl _itemsNeedUpdate:];
-[_UIDropSessionImpl _operationMask];
-[_UIDropSessionImpl _previewCenterForVisibleItem:inView:];
-[_UIDropSessionImpl _previewSizeForVisibleItem:];
-[_UIDropSessionImpl allowsMoveOperation];
-[_UIDropSessionImpl canLoadObjectsOfClass:];
-[_UIDropSessionImpl hasItemsConformingToTypeIdentifiers:];
-[_UIDropSessionImpl initWithSessionDestination:];
-[_UIDropSessionImpl isRestrictedToDraggingApplication];
-[_UIDropSessionImpl loadObjectsOfClass:completion:];
-[_UIDropSessionImpl localDragSession];
-[_UIDropSessionImpl requestVisibleItems:];
```
