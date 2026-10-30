# `_UIDragDestinationControllerReorderingState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _supportsLocalSessionReordering;
B _hasStartedInteractiveReorder;
@"_UIVelocityIntegrator" _velocityIntegrator;
q _reorderCount;
@"_UIDragMovementCadenceSettings" _reorderCadenceSettings;
@"_UIDragDestinationControllerSessionState" _sessionState;
@"UICollectionView" _collectionView;
d _reorderBecamePossibleTime;
q _dragMovementPhase;
```

## Properties

```
@property (T@"_UIDragDestinationControllerSessionState",&,N,V_sessionState) sessionState;
@property (T@"UICollectionView",W,N,V_collectionView) collectionView;
@property (T@"_UIVelocityIntegrator",&,N,V_velocityIntegrator) velocityIntegrator;
@property (Tq,N,V_reorderCount) reorderCount;
@property (Td,N,V_reorderBecamePossibleTime) reorderBecamePossibleTime;
@property (Tq,N,V_dragMovementPhase) dragMovementPhase;
@property (T@"_UIDragMovementCadenceSettings",&,N,V_reorderCadenceSettings) reorderCadenceSettings;
@property (TB,N,V_hasStartedInteractiveReorder) hasStartedInteractiveReorder;
```

## Instance methods

```
-[_UIDragDestinationControllerReorderingState sessionState];
-[_UIDragDestinationControllerReorderingState collectionView];
-[_UIDragDestinationControllerReorderingState setCollectionView:];
-[_UIDragDestinationControllerReorderingState setSessionState:];
-[_UIDragDestinationControllerReorderingState setVelocityIntegrator:];
-[_UIDragDestinationControllerReorderingState _reorderCadenceSettings];
-[_UIDragDestinationControllerReorderingState dragMovementPhase];
-[_UIDragDestinationControllerReorderingState reorderBecamePossibleTime];
-[_UIDragDestinationControllerReorderingState reorderResetToStartingLocation];
-[_UIDragDestinationControllerReorderingState setDragMovementPhase:];
-[_UIDragDestinationControllerReorderingState setHasStartedInteractiveReorder:];
-[_UIDragDestinationControllerReorderingState setReorderBecamePossibleTime:];
-[_UIDragDestinationControllerReorderingState setReorderCadenceSettings:];
-[_UIDragDestinationControllerReorderingState setReorderCount:];
```
