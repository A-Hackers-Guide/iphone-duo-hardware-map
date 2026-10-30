# `UIPushBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 8 instance variables, 6 properties, 29 instance methods, 1 class methods

## Instance variables

```
d _angle;
d _magnitude;
B _active;
q _mode;
{CGVector="dx"d"dy"d} _forceVector;
d _timeInterval;
@"NSMutableDictionary" _targetPoints;
i _i;
```

## Properties

```
@property (T@"NSArray",R,C,N) items;
@property (Tq,R,N) mode;
@property (TB,N) active;
@property (Td,N) angle;
@property (Td,N) magnitude;
@property (T{CGVector=dd},N) pushDirection;
```

## Class methods

```
+[UIPushBehavior _isPrimitiveBehavior];
```

## Instance methods

```
-[UIPushBehavior setAngle:];
-[UIPushBehavior angle];
-[UIPushBehavior active];
-[UIPushBehavior init];
-[UIPushBehavior setActive:];
-[UIPushBehavior items];
-[UIPushBehavior removeItem:];
-[UIPushBehavior addItem:];
-[UIPushBehavior mode];
-[UIPushBehavior description];
-[UIPushBehavior initWithItems:];
-[UIPushBehavior _associate];
-[UIPushBehavior _dissociate];
-[UIPushBehavior _step];
-[UIPushBehavior initWithItems:mode:];
-[UIPushBehavior magnitude];
-[UIPushBehavior pushDirection];
-[UIPushBehavior setAngle:magnitude:];
-[UIPushBehavior setMagnitude:];
-[UIPushBehavior setPushDirection:];
-[UIPushBehavior setTargetOffsetFromCenter:forItem:];
-[UIPushBehavior setTargetPoint:forItem:];
-[UIPushBehavior setXComponent:];
-[UIPushBehavior setXComponent:yComponent:];
-[UIPushBehavior setYComponent:];
-[UIPushBehavior targetOffsetFromCenterForItem:];
-[UIPushBehavior targetPointForItem:];
-[UIPushBehavior xComponent];
-[UIPushBehavior yComponent];
```
