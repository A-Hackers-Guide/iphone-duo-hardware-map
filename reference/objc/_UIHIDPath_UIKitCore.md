# `_UIHIDPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _touching;
I _identity;
@"NSNumber" _pathId;
d _force;
d _minorRadius;
d _majorRadius;
d _quality;
d _density;
d _irregularity;
d _twist;
q _generationCount;
@"NSNumber" _overridePathId;
q _deliveryPhase;
{CGPoint="x"d"y"d} _position;
```

## Properties

```
@property (T@"NSNumber",R,N,V_pathId) pathId;
@property (TI,R,N,V_identity) identity;
@property (Td,R,N,V_force) force;
@property (Td,R,N,V_minorRadius) minorRadius;
@property (Td,R,N,V_majorRadius) majorRadius;
@property (Td,R,N,V_quality) quality;
@property (Td,R,N,V_density) density;
@property (Td,R,N,V_irregularity) irregularity;
@property (Td,R,N,V_twist) twist;
@property (Tq,R,N,V_generationCount) generationCount;
@property (TB,R,N,GisTouching,V_touching) touching;
@property (T{CGPoint=dd},N,V_position) position;
@property (T@"NSNumber",&,N,V_overridePathId) overridePathId;
@property (Tq,N,V_deliveryPhase) deliveryPhase;
```

## Instance methods

```
-[_UIHIDPath generationCount];
-[_UIHIDPath position];
-[_UIHIDPath quality];
-[_UIHIDPath init];
-[_UIHIDPath density];
-[_UIHIDPath isTouching];
-[_UIHIDPath identity];
-[_UIHIDPath force];
-[_UIHIDPath setPosition:];
-[_UIHIDPath applyTransform:];
-[_UIHIDPath deliveryPhase];
-[_UIHIDPath irregularity];
-[_UIHIDPath majorRadius];
-[_UIHIDPath minorRadius];
-[_UIHIDPath overridePathId];
-[_UIHIDPath pathId];
-[_UIHIDPath setDeliveryPhase:];
-[_UIHIDPath setOverridePathId:];
-[_UIHIDPath twist];
-[_UIHIDPath updateWithHIDEvent:];
```
