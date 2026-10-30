# `UICollisionBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 10 instance variables, 5 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _usesImplicitBounds;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _implicitBoundsInsets;
@"PKExtendedPhysicsBody" _implicitBoundsBody;
@"NSMutableDictionary" _boundaryBodies;
@"NSMutableDictionary" _boundaryPaths;
Q _collisionMode;
@"<UICollisionBehaviorDelegate>" _collisionDelegate;
I _groupVID;
I _groupBID;
{?="delegateBeganWithItem"b1"delegateEndedWithItem"b1"delegateBeganWithBoundary"b1"delegateEndedWithBoundary"b1} _collisionBehaviorFlags;
```

## Properties

```
@property (T@"NSArray",R,C,N) items;
@property (TQ,N) collisionMode;
@property (TB,N) translatesReferenceBoundsIntoBoundary;
@property (T@"NSArray",R,C,N) boundaryIdentifiers;
@property (T@"<UICollisionBehaviorDelegate>",W,N) collisionDelegate;
```

## Class methods

```
+[UICollisionBehavior _isPrimitiveBehavior];
```

## Instance methods

```
-[UICollisionBehavior init];
-[UICollisionBehavior items];
-[UICollisionBehavior removeItem:];
-[UICollisionBehavior addItem:];
-[UICollisionBehavior description];
-[UICollisionBehavior initWithItems:];
-[UICollisionBehavior _didEndContact:];
-[UICollisionBehavior _addCollisionItem:];
-[UICollisionBehavior _applySettings];
-[UICollisionBehavior _associate];
-[UICollisionBehavior _didBeginContact:];
-[UICollisionBehavior _dissociate];
-[UICollisionBehavior _reevaluate:];
-[UICollisionBehavior _registerBodyForIdentifier:path:];
-[UICollisionBehavior _registerBoundaryForIdentifier:path:];
-[UICollisionBehavior _removeExplicitBoundaryBodies];
-[UICollisionBehavior _removeExplicitBoundaryPaths];
-[UICollisionBehavior _removeImplicitBoundaries];
-[UICollisionBehavior _setCollisions:forBody:isEdge:];
-[UICollisionBehavior _setTranslatesReferenceItemBounds:intoBoundaryWithInsets:];
-[UICollisionBehavior _setupExplicitBoundaries];
-[UICollisionBehavior _setupImplicitBoundaries];
-[UICollisionBehavior addBoundaryWithIdentifier:forPath:];
-[UICollisionBehavior addBoundaryWithIdentifier:fromPoint:toPoint:];
-[UICollisionBehavior boundaryIdentifiers];
-[UICollisionBehavior boundaryWithIdentifier:];
-[UICollisionBehavior collisionDelegate];
-[UICollisionBehavior collisionMode];
-[UICollisionBehavior removeAllBoundaries];
-[UICollisionBehavior removeBoundaryWithIdentifier:];
-[UICollisionBehavior setCollisionDelegate:];
-[UICollisionBehavior setCollisionMode:];
-[UICollisionBehavior setTranslatesReferenceBoundsIntoBoundary:];
-[UICollisionBehavior setTranslatesReferenceBoundsIntoBoundaryWithInsets:];
-[UICollisionBehavior translatesReferenceBoundsIntoBoundary];
```
