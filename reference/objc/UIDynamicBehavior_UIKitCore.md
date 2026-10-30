# `UIDynamicBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"UIDynamicAnimator" _context;
@"NSMutableArray" _items;
@"NSMutableArray" _behaviors;
@"NSMutableArray" _addedBehaviors;
@? _action;
```

## Properties

```
@property (T@"NSArray",R,C,N) childBehaviors;
@property (T@?,C,N,V_action) action;
@property (T@"UIDynamicAnimator",R,N) dynamicAnimator;
```

## Class methods

```
+[UIDynamicBehavior initialize];
+[UIDynamicBehavior _isPrimitiveBehavior];
```

## Instance methods

```
-[UIDynamicBehavior init];
-[UIDynamicBehavior setAction:];
-[UIDynamicBehavior action];
-[UIDynamicBehavior items];
-[UIDynamicBehavior _items];
-[UIDynamicBehavior description];
-[UIDynamicBehavior _setContext:];
-[UIDynamicBehavior dynamicAnimator];
-[UIDynamicBehavior _addItem:];
-[UIDynamicBehavior _associate];
-[UIDynamicBehavior _changedParameterForBody:];
-[UIDynamicBehavior _context];
-[UIDynamicBehavior _detachAutolayoutFromItemIfNecessary:];
-[UIDynamicBehavior _dissociate];
-[UIDynamicBehavior _itemsDescription];
-[UIDynamicBehavior _reattachAutolayoutToItemIfNecessary:];
-[UIDynamicBehavior _reevaluate:];
-[UIDynamicBehavior _removeItem:];
-[UIDynamicBehavior _setItems:];
-[UIDynamicBehavior _step];
-[UIDynamicBehavior _updateAutolayoutEngagementForItemIfNecessary:detach:];
-[UIDynamicBehavior addChildBehavior:];
-[UIDynamicBehavior allowsAnimatorToStop];
-[UIDynamicBehavior childBehaviors];
-[UIDynamicBehavior removeChildBehavior:];
-[UIDynamicBehavior willMoveToAnimator:];
```
