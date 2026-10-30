# `_UITableViewDropItemImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITableViewDropItem`
- 3 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIDragItem" _dragItem;
@"NSIndexPath" _sourceIndexPath;
@"NSIndexPath" _translatedSourceIndexPath;
```

## Properties

```
@property (T@"UIDragItem",&,N,V_dragItem) dragItem;
@property (T@"NSIndexPath",&,N,V_sourceIndexPath) sourceIndexPath;
@property (T@"NSIndexPath",&,N,G_translatedSourceIndexPath,S_setTranslatedSourceIndexPath:,V_translatedSourceIndexPath) translatedSourceIndexPath;
@property (T{CGSize=dd},R,N) previewSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITableViewDropItemImpl sourceIndexPath];
-[_UITableViewDropItemImpl _setTranslatedSourceIndexPath:];
-[_UITableViewDropItemImpl _translateSourceIndexPath:];
-[_UITableViewDropItemImpl _translatedSourceIndexPath];
-[_UITableViewDropItemImpl dragItem];
-[_UITableViewDropItemImpl initWithDragItem:sourceIndexPath:];
-[_UITableViewDropItemImpl previewSize];
-[_UITableViewDropItemImpl setDragItem:];
-[_UITableViewDropItemImpl setSourceIndexPath:];
```
