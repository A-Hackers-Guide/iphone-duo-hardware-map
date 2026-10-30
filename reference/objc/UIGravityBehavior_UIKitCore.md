# `UIGravityBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 1 instance variables, 4 properties, 25 instance methods, 1 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _gravity;
```

## Properties

```
@property (T@"NSArray",R,C,N) items;
@property (T{CGVector=dd},N) gravityDirection;
@property (Td,N) angle;
@property (Td,N) magnitude;
```

## Class methods

```
+[UIGravityBehavior _isPrimitiveBehavior];
```

## Instance methods

```
-[UIGravityBehavior setAngle:];
-[UIGravityBehavior angle];
-[UIGravityBehavior init];
-[UIGravityBehavior items];
-[UIGravityBehavior removeItem:];
-[UIGravityBehavior gravity];
-[UIGravityBehavior addItem:];
-[UIGravityBehavior description];
-[UIGravityBehavior setGravity:];
-[UIGravityBehavior initWithItems:];
-[UIGravityBehavior _addGravityItem:];
-[UIGravityBehavior _associate];
-[UIGravityBehavior _dissociate];
-[UIGravityBehavior _setAngle:magnitude:];
-[UIGravityBehavior denormalizedGravity];
-[UIGravityBehavior gravityDirection];
-[UIGravityBehavior magnitude];
-[UIGravityBehavior setAngle:magnitude:];
-[UIGravityBehavior setGravityDirection:];
-[UIGravityBehavior setMagnitude:];
-[UIGravityBehavior setXComponent:];
-[UIGravityBehavior setXComponent:yComponent:];
-[UIGravityBehavior setYComponent:];
-[UIGravityBehavior xComponent];
-[UIGravityBehavior yComponent];
```
