# `_UITableViewDropPlaceholderContextImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITableViewPlaceholderContext`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reuseIdentifier;
d _rowHeight;
@? _cellUpdateHandler;
@"<UIDragAnimating>" _animator;
@"NSUUID" _shadowUpdateIdentifier;
@"<_UITableViewPlaceholderContextDelegate>" _delegate;
@"UIDragItem" _dragItem;
```

## Properties

```
@property (T@"<_UITableViewPlaceholderContextDelegate>",W,N,V_delegate) delegate;
@property (T@"UIDragItem",&,N,V_dragItem) dragItem;
@property (T@"NSString",&,N,V_reuseIdentifier) reuseIdentifier;
@property (Td,N,V_rowHeight) rowHeight;
@property (T@?,C,N,V_cellUpdateHandler) cellUpdateHandler;
@property (T@"<UIDragAnimating>",&,N,G_animator,S_setAnimator:,V_animator) animator;
@property (T@"NSUUID",&,N,G_shadowUpdateIdentifier,S_setShadowUpdateIdentifier:,V_shadowUpdateIdentifier) shadowUpdateIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITableViewDropPlaceholderContextImpl addAnimations:];
-[_UITableViewDropPlaceholderContextImpl addCompletion:];
-[_UITableViewDropPlaceholderContextImpl setRowHeight:];
-[_UITableViewDropPlaceholderContextImpl _animator];
-[_UITableViewDropPlaceholderContextImpl setDelegate:];
-[_UITableViewDropPlaceholderContextImpl _setAnimator:];
-[_UITableViewDropPlaceholderContextImpl delegate];
-[_UITableViewDropPlaceholderContextImpl reuseIdentifier];
-[_UITableViewDropPlaceholderContextImpl rowHeight];
-[_UITableViewDropPlaceholderContextImpl _setShadowUpdateIdentifier:];
-[_UITableViewDropPlaceholderContextImpl _shadowUpdateIdentifier];
-[_UITableViewDropPlaceholderContextImpl cellUpdateHandler];
-[_UITableViewDropPlaceholderContextImpl commitInsertionWithDataSourceUpdates:];
-[_UITableViewDropPlaceholderContextImpl deletePlaceholder];
-[_UITableViewDropPlaceholderContextImpl dragItem];
-[_UITableViewDropPlaceholderContextImpl initWithDelegate:dragItem:reuseIdentifier:rowHeight:cellUpdateHandler:];
-[_UITableViewDropPlaceholderContextImpl setCellUpdateHandler:];
-[_UITableViewDropPlaceholderContextImpl setDragItem:];
-[_UITableViewDropPlaceholderContextImpl setReuseIdentifier:];
```
