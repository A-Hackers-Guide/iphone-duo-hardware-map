# `_UIContextMenuCommitAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 30 instance methods, 0 class methods

## Instance variables

```
d _sourceRadius;
d _destinationRadius;
@"UIView" _source;
@"UIView" _destination;
@"UIView" _container;
@"UIView" _morphContainer;
@"UIView" _sourceSnapshotView;
@"UIView" _sourceTransformView;
@"UIView" _destinationTransformView;
@"UIView" _originalContentSnapshotView;
@"_UIPortalView" _destinationContentPortalView;
@"_UIContextMenuCommitContainerView" _animationContainer;
Q _animationCount;
```

## Properties

```
@property (T@"UIView",&,N,V_source) source;
@property (T@"UIView",&,N,V_destination) destination;
@property (T@"UIView",&,N,V_container) container;
@property (T@"UIView",&,N,V_morphContainer) morphContainer;
@property (T@"UIView",&,N,V_sourceSnapshotView) sourceSnapshotView;
@property (T@"UIView",&,N,V_sourceTransformView) sourceTransformView;
@property (T@"UIView",&,N,V_destinationTransformView) destinationTransformView;
@property (T@"UIView",&,N,V_originalContentSnapshotView) originalContentSnapshotView;
@property (T@"_UIPortalView",&,N,V_destinationContentPortalView) destinationContentPortalView;
@property (T@"_UIContextMenuCommitContainerView",&,N,V_animationContainer) animationContainer;
@property (TQ,N,V_animationCount) animationCount;
@property (Td,N,V_sourceRadius) sourceRadius;
@property (Td,N,V_destinationRadius) destinationRadius;
```

## Instance methods

```
-[_UIContextMenuCommitAnimation animationCount];
-[_UIContextMenuCommitAnimation destination];
-[_UIContextMenuCommitAnimation setContainer:];
-[_UIContextMenuCommitAnimation setSource:];
-[_UIContextMenuCommitAnimation setDestination:];
-[_UIContextMenuCommitAnimation setAnimationCount:];
-[_UIContextMenuCommitAnimation source];
-[_UIContextMenuCommitAnimation container];
-[_UIContextMenuCommitAnimation setOriginalContentSnapshotView:];
-[_UIContextMenuCommitAnimation _prepareAnimationViews];
-[_UIContextMenuCommitAnimation _prepareSnapshots];
-[_UIContextMenuCommitAnimation animateWithAlongsideActions:completion:];
-[_UIContextMenuCommitAnimation animationContainer];
-[_UIContextMenuCommitAnimation destinationContentPortalView];
-[_UIContextMenuCommitAnimation destinationRadius];
-[_UIContextMenuCommitAnimation destinationTransformView];
-[_UIContextMenuCommitAnimation initWithSource:container:];
-[_UIContextMenuCommitAnimation morphContainer];
-[_UIContextMenuCommitAnimation originalContentSnapshotView];
-[_UIContextMenuCommitAnimation setAnimationContainer:];
-[_UIContextMenuCommitAnimation setDestinationContentPortalView:];
-[_UIContextMenuCommitAnimation setDestinationRadius:];
-[_UIContextMenuCommitAnimation setDestinationTransformView:];
-[_UIContextMenuCommitAnimation setMorphContainer:];
-[_UIContextMenuCommitAnimation setSourceRadius:];
-[_UIContextMenuCommitAnimation setSourceSnapshotView:];
-[_UIContextMenuCommitAnimation setSourceTransformView:];
-[_UIContextMenuCommitAnimation sourceRadius];
-[_UIContextMenuCommitAnimation sourceSnapshotView];
-[_UIContextMenuCommitAnimation sourceTransformView];
```
