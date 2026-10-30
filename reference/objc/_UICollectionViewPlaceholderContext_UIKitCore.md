# `_UICollectionViewPlaceholderContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UICollectionViewPlaceholderContext`, `_UICollectionViewDropPlaceholderContext`
- 7 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _shadowUpdateIdentifier;
@"NSString" _reuseIdentifier;
@"NSIndexPath" _originalInsertionIndexPath;
@? _cellUpdateHandler;
@"_UIDropAnimationHandlers" _animationHandlers;
@"<_UICollectionViewPlaceholderContextDelegate>" _delegate;
@"UIDragItem" _dragItem;
```

## Properties

```
@property (T@"<_UICollectionViewPlaceholderContextDelegate>",W,N,V_delegate) delegate;
@property (T@"UIDragItem",&,N,V_dragItem) dragItem;
@property (T@"_UIDropAnimationHandlers",&,N,V_animationHandlers) animationHandlers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewPlaceholderContext addAnimations:];
-[_UICollectionViewPlaceholderContext addCompletion:];
-[_UICollectionViewPlaceholderContext setDelegate:];
-[_UICollectionViewPlaceholderContext delegate];
-[_UICollectionViewPlaceholderContext description];
-[_UICollectionViewPlaceholderContext commitInsertionWithDataSourceUpdates:];
-[_UICollectionViewPlaceholderContext deletePlaceholder];
-[_UICollectionViewPlaceholderContext dragItem];
-[_UICollectionViewPlaceholderContext setAnimationHandlers:];
-[_UICollectionViewPlaceholderContext setDragItem:];
-[_UICollectionViewPlaceholderContext setNeedsCellUpdate];
```
