# `UIDragDropSession` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) items;
@property (TB,R,N) allowsMoveOperation;
@property (TB,R,N,GisRestrictedToDraggingApplication) restrictedToDraggingApplication;
```

## Instance methods

```
-[UIDragDropSession items];
-[UIDragDropSession locationInView:];
-[UIDragDropSession allowsMoveOperation];
-[UIDragDropSession canLoadObjectsOfClass:];
-[UIDragDropSession hasItemsConformingToTypeIdentifiers:];
-[UIDragDropSession isRestrictedToDraggingApplication];
```
