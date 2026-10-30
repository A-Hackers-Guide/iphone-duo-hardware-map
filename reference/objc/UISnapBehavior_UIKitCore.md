# `UISnapBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 7 instance variables, 2 properties, 13 instance methods, 1 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _anchorPoint;
d _damping;
d _distance;
d _frequency;
{?="attachedToView"b1"dampingSet"b1"frequencySet"b1"lengthSet"b1} _stateFlags;
@"NSMutableArray" _joints;
@"PKPhysicsBody" _anchorBody;
```

## Properties

```
@property (T{CGPoint=dd},N) snapPoint;
@property (Td,N,V_damping) damping;
```

## Class methods

```
+[UISnapBehavior _isPrimitiveBehavior];
```

## Instance methods

```
-[UISnapBehavior setDamping:];
-[UISnapBehavior init];
-[UISnapBehavior damping];
-[UISnapBehavior description];
-[UISnapBehavior _associate];
-[UISnapBehavior _dissociate];
-[UISnapBehavior _distance];
-[UISnapBehavior _frequency];
-[UISnapBehavior _setDistance:];
-[UISnapBehavior _setFrequency:];
-[UISnapBehavior initWithItem:snapToPoint:];
-[UISnapBehavior setSnapPoint:];
-[UISnapBehavior snapPoint];
```
