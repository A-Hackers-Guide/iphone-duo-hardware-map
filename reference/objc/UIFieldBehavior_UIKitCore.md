# `UIFieldBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 3 instance variables, 10 properties, 28 instance methods, 12 class methods

## Instance variables

```
@"PKPhysicsField" _field;
{?="fieldIsKindOfNoiseField"b1} _fieldFlags;
@"UIRegion" _region;
```

## Properties

```
@property (T@"PKPhysicsField",R,N) _field;
@property (T@"NSArray",R,C,N) items;
@property (T{CGPoint=dd},N) position;
@property (T@"UIRegion",&,N,V_region) region;
@property (Td,N) strength;
@property (Td,N) falloff;
@property (Td,N) minimumRadius;
@property (T{CGVector=dd},N) direction;
@property (Td,N) smoothness;
@property (Td,N) animationSpeed;
```

## Class methods

```
+[UIFieldBehavior radialGravityFieldWithPosition:];
+[UIFieldBehavior _isPrimitiveBehavior];
+[UIFieldBehavior dragField];
+[UIFieldBehavior electricField];
+[UIFieldBehavior fieldWithEvaluationBlock:];
+[UIFieldBehavior linearGravityFieldWithVector:];
+[UIFieldBehavior magneticField];
+[UIFieldBehavior noiseFieldWithSmoothness:animationSpeed:];
+[UIFieldBehavior springField];
+[UIFieldBehavior turbulenceFieldWithSmoothness:animationSpeed:];
+[UIFieldBehavior velocityFieldWithVector:];
+[UIFieldBehavior vortexField];
```

## Instance methods

```
-[UIFieldBehavior setRegion:];
-[UIFieldBehavior smoothness];
-[UIFieldBehavior setSmoothness:];
-[UIFieldBehavior setMinimumRadius:];
-[UIFieldBehavior minimumRadius];
-[UIFieldBehavior position];
-[UIFieldBehavior region];
-[UIFieldBehavior strength];
-[UIFieldBehavior init];
-[UIFieldBehavior setStrength:];
-[UIFieldBehavior setDirection:];
-[UIFieldBehavior items];
-[UIFieldBehavior removeItem:];
-[UIFieldBehavior isEnabled];
-[UIFieldBehavior direction];
-[UIFieldBehavior setEnabled:];
-[UIFieldBehavior addItem:];
-[UIFieldBehavior setPosition:];
-[UIFieldBehavior _initWithField:];
-[UIFieldBehavior falloff];
-[UIFieldBehavior _addFieldItem:];
-[UIFieldBehavior _associate];
-[UIFieldBehavior _changedParameter];
-[UIFieldBehavior _dissociate];
-[UIFieldBehavior _field];
-[UIFieldBehavior animationSpeed];
-[UIFieldBehavior setAnimationSpeed:];
-[UIFieldBehavior setFalloff:];
```
