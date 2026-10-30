# `_UICollectionViewDropCoordinatorItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragAnimating`
- 7 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _shouldRemainInHierarchy;
i _kind;
@"NSIndexPath" _destinationIndexPath;
@"UIDragItem" _dragItem;
@"UIDragPreviewTarget" _target;
@"_UIDropAnimationHandlers" _animationHandlers;
@? _previewParametersProvider;
```

## Properties

```
@property (T@"UIDragItem",W,N,V_dragItem) dragItem;
@property (T@"UIDragPreviewTarget",C,N,V_target) target;
@property (Ti,N,V_kind) kind;
@property (T@"_UIDropAnimationHandlers",&,N,V_animationHandlers) animationHandlers;
@property (T@?,C,N,V_previewParametersProvider) previewParametersProvider;
@property (T@"NSIndexPath",&,N,V_destinationIndexPath) destinationIndexPath;
@property (TB,N,V_shouldRemainInHierarchy) shouldRemainInHierarchy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewDropCoordinatorItem addAnimations:];
-[_UICollectionViewDropCoordinatorItem setKind:];
-[_UICollectionViewDropCoordinatorItem addCompletion:];
-[_UICollectionViewDropCoordinatorItem setTarget:];
-[_UICollectionViewDropCoordinatorItem description];
-[_UICollectionViewDropCoordinatorItem destinationIndexPath];
-[_UICollectionViewDropCoordinatorItem target];
-[_UICollectionViewDropCoordinatorItem kind];
-[_UICollectionViewDropCoordinatorItem initWithDestinationIndexPath:dragItem:placeholderConfiguration:];
-[_UICollectionViewDropCoordinatorItem animationHandlers];
-[_UICollectionViewDropCoordinatorItem dragItem];
-[_UICollectionViewDropCoordinatorItem initWithDestinationIndexPath:dragItem:];
-[_UICollectionViewDropCoordinatorItem initWithDragItem:target:];
-[_UICollectionViewDropCoordinatorItem previewParametersProvider];
-[_UICollectionViewDropCoordinatorItem setAnimationHandlers:];
-[_UICollectionViewDropCoordinatorItem setDestinationIndexPath:];
-[_UICollectionViewDropCoordinatorItem setDragItem:];
-[_UICollectionViewDropCoordinatorItem setPreviewParametersProvider:];
-[_UICollectionViewDropCoordinatorItem setShouldRemainInHierarchy:];
-[_UICollectionViewDropCoordinatorItem shouldRemainInHierarchy];
```
