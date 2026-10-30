# `_UIDynamicValueAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDynamicAnimation`
- 11 instance variables, 4 properties, 26 instance methods, 1 class methods

## Instance variables

```
@? _applier;
@? _viewApplier;
d _value;
d _velocity;
d _unitSize;
d _friction;
d _decelerationFactor;
d _decelerationLnFactor;
d _multiplier;
@"NSMutableArray" _activeValues;
^v _stepFunction;
```

## Properties

```
@property (Td,N,V_value) value;
@property (Td,N,V_velocity) velocity;
@property (Td,N,V_friction) friction;
@property (T@"NSArray",C,N,V_activeValues) activeValues;
```

## Class methods

```
+[_UIDynamicValueAnimation _dynamicValueAnimationMatchingCASpringAnimationWithMass:stiffness:damping:velocity:fromValue:toValue:];
```

## Instance methods

```
-[_UIDynamicValueAnimation _setVelocity:];
-[_UIDynamicValueAnimation setFriction:];
-[_UIDynamicValueAnimation _stopAnimation];
-[_UIDynamicValueAnimation friction];
-[_UIDynamicValueAnimation observeValueForKeyPath:ofObject:change:context:];
-[_UIDynamicValueAnimation init];
-[_UIDynamicValueAnimation dealloc];
-[_UIDynamicValueAnimation value];
-[_UIDynamicValueAnimation velocity];
-[_UIDynamicValueAnimation runWithCompletion:];
-[_UIDynamicValueAnimation setValue:];
-[_UIDynamicValueAnimation settlingDuration];
-[_UIDynamicValueAnimation setVelocity:];
-[_UIDynamicValueAnimation _setMultiplier:];
-[_UIDynamicValueAnimation addActiveValue:];
-[_UIDynamicValueAnimation runWithValueApplier:completion:];
-[_UIDynamicValueAnimation _animateForInterval:];
-[_UIDynamicValueAnimation _appendSubclassDescription:atLevel:];
-[_UIDynamicValueAnimation _multiplier];
-[_UIDynamicValueAnimation _setDecelerationFactor:];
-[_UIDynamicValueAnimation _updateStepFunction];
-[_UIDynamicValueAnimation activeValues];
-[_UIDynamicValueAnimation initWithValue:velocity:unitSize:];
-[_UIDynamicValueAnimation removeActiveValue:];
-[_UIDynamicValueAnimation runWithValueApplier:completion:forScreen:runLoopMode:];
-[_UIDynamicValueAnimation setActiveValues:];
```
