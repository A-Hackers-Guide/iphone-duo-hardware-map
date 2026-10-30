# `_UIDynamicValueConvergenceAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDynamicAnimation`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@? _applier;
d _value;
d _targetValue;
d _convergenceRate;
d _minimumDifference;
```

## Properties

```
@property (Td,N,V_value) value;
@property (Td,N,V_targetValue) targetValue;
@property (Td,N,V_convergenceRate) convergenceRate;
@property (Td,N,V_minimumDifference) minimumDifference;
```

## Instance methods

```
-[_UIDynamicValueConvergenceAnimation setTargetValue:];
-[_UIDynamicValueConvergenceAnimation value];
-[_UIDynamicValueConvergenceAnimation targetValue];
-[_UIDynamicValueConvergenceAnimation setValue:];
-[_UIDynamicValueConvergenceAnimation convergenceRate];
-[_UIDynamicValueConvergenceAnimation runWithValueApplier:completion:];
-[_UIDynamicValueConvergenceAnimation _animateForInterval:];
-[_UIDynamicValueConvergenceAnimation initWithValue:targetValue:convergenceRate:minimumDifference:];
-[_UIDynamicValueConvergenceAnimation minimumDifference];
-[_UIDynamicValueConvergenceAnimation setConvergenceRate:];
-[_UIDynamicValueConvergenceAnimation setMinimumDifference:];
```
