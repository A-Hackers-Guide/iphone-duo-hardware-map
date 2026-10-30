# `_UIElasticValue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
d _currentValue;
d _targetValue;
d _speed;
d _friction;
d _momentum;
```

## Properties

```
@property (Td,N,V_currentValue) currentValue;
@property (Td,N,V_targetValue) targetValue;
@property (Td,N,V_speed) speed;
@property (TB,R,N,GisSteady) steady;
@property (Td,N,V_friction) friction;
@property (Td,N,V_momentum) momentum;
```

## Instance methods

```
-[_UIElasticValue setFriction:];
-[_UIElasticValue update:];
-[_UIElasticValue setSpeed:];
-[_UIElasticValue friction];
-[_UIElasticValue setTargetValue:];
-[_UIElasticValue speed];
-[_UIElasticValue init];
-[_UIElasticValue currentValue];
-[_UIElasticValue initWithValue:];
-[_UIElasticValue targetValue];
-[_UIElasticValue setCurrentValue:];
-[_UIElasticValue description];
-[_UIElasticValue isSteady];
-[_UIElasticValue momentum];
-[_UIElasticValue setMomentum:];
-[_UIElasticValue updateFromDisplayLink:];
```
