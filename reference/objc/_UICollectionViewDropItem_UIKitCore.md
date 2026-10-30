# `_UICollectionViewDropItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionViewDropItem`
- 3 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIDragItem" _dragItem;
@"NSIndexPath" _sourceIndexPath;
{CGSize="width"d"height"d} _previewSize;
```

## Properties

```
@property (T@"UIDragItem",&,N,V_dragItem) dragItem;
@property (T{CGSize=dd},N,V_previewSize) previewSize;
@property (T@"NSIndexPath",&,N,V_sourceIndexPath) sourceIndexPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewDropItem description];
-[_UICollectionViewDropItem sourceIndexPath];
-[_UICollectionViewDropItem setPreviewSize:];
-[_UICollectionViewDropItem dragItem];
-[_UICollectionViewDropItem initWithDragItem:previewSize:sourceIndexPath:];
-[_UICollectionViewDropItem previewSize];
-[_UICollectionViewDropItem setDragItem:];
-[_UICollectionViewDropItem setSourceIndexPath:];
```
