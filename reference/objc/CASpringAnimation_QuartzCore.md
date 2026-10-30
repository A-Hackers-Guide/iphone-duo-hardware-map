# `CASpringAnimation`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CABasicAnimation`
- 0 instance variables, 9 properties, 22 instance methods, 1 class methods

## Properties

```
@property (Td) velocity;
@property (Td) mass;
@property (Td) stiffness;
@property (Td) damping;
@property (Td) initialVelocity;
@property (TB) allowsOverdamping;
@property (Td,R) settlingDuration;
@property (Td,R) perceptualDuration;
@property (Td,R) bounce;
```

## Class methods

```
+[CASpringAnimation defaultValueForKey:];
```

## Instance methods

```
-[CASpringAnimation setDamping:];
-[CASpringAnimation setInitialVelocity:];
-[CASpringAnimation setMass:];
-[CASpringAnimation _setCARenderAnimation:layer:];
-[CASpringAnimation damping];
-[CASpringAnimation _solveForInput:];
-[CASpringAnimation setStiffness:];
-[CASpringAnimation velocity];
-[CASpringAnimation _propertyFlagsForLayer:];
-[CASpringAnimation initialVelocity];
-[CASpringAnimation stiffness];
-[CASpringAnimation settlingDuration];
-[CASpringAnimation _timeFunction:];
-[CASpringAnimation initWithPerceptualDuration:bounce:];
-[CASpringAnimation allowsOverdamping];
-[CASpringAnimation mass];
-[CASpringAnimation setVelocity:];
-[CASpringAnimation setAllowsOverdamping:];
-[CASpringAnimation durationForEpsilon:];
-[CASpringAnimation perceptualDuration];
-[CASpringAnimation bounce];
-[CASpringAnimation _copyRenderAnimationForLayer:];
```
