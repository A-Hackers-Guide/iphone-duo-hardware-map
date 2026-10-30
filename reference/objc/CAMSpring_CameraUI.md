# `CAMSpring`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 13 properties, 29 instance methods, 0 class methods

## Instance variables

```
B _converged;
d _tension;
d _friction;
d _target;
d _velocity;
d _epsilon;
d _maximumTimeDelta;
d __lastTimestamp;
d __current;
d __lowerBound;
d __upperBound;
```

## Properties

```
@property (Td,N,S_setLastTimestamp:,V__lastTimestamp) _lastTimestamp;
@property (TB,N,GisConverged,S_setConverged:,V_converged) converged;
@property (Td,N,S_setCurrent:,V__current) _current;
@property (Td,R,N,V__lowerBound) _lowerBound;
@property (Td,R,N,V__upperBound) _upperBound;
@property (Td,N,V_tension) tension;
@property (Td,N,V_friction) friction;
@property (Td,N,V_target) target;
@property (Td,N,V_velocity) velocity;
@property (Td,R,N) value;
@property (Td,R,N) unboundedValue;
@property (Td,R,N,V_epsilon) epsilon;
@property (Td,N,V_maximumTimeDelta) maximumTimeDelta;
```

## Instance methods

```
-[CAMSpring _upperBound];
-[CAMSpring updateForTimestamp:];
-[CAMSpring converge];
-[CAMSpring initWithTension:friction:epsilon:boundedBetween:and:];
-[CAMSpring _updateConverged];
-[CAMSpring _lowerBound];
-[CAMSpring _currentForce];
-[CAMSpring setMaximumTimeDelta:];
-[CAMSpring setFriction:];
-[CAMSpring unboundedValue];
-[CAMSpring _current];
-[CAMSpring _setCurrent:];
-[CAMSpring _setLastTimestamp:];
-[CAMSpring _lastTimestamp];
-[CAMSpring initWithTension:friction:epsilon:];
-[CAMSpring _updateWithForce:timestamp:];
-[CAMSpring _setConverged:];
-[CAMSpring tension];
-[CAMSpring resetToValue:];
-[CAMSpring maximumTimeDelta];
-[CAMSpring isConverged];
-[CAMSpring friction];
-[CAMSpring setTension:];
-[CAMSpring value];
-[CAMSpring velocity];
-[CAMSpring setTarget:];
-[CAMSpring setVelocity:];
-[CAMSpring epsilon];
-[CAMSpring target];
```
