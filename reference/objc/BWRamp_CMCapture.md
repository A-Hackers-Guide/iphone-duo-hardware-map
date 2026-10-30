# `BWRamp`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
B _isRamping;
f _currentValue;
i _currentIteration;
f _startValue;
f _targetValue;
i _durationInIterations;
i _shape;
B _isRampingUp;
f _exponentialConvergenceFraction;
f _exponentialSnapFraction;
@"BWSpringSimulation" _spring;
{?="value"q"timescale"i"flags"I"epoch"q} _springPTS;
f _frameRate;
```

## Properties

```
@property (TB,R,N,V_isRamping) isRamping;
@property (Tf,R,N,V_currentValue) currentValue;
@property (TB,R,N,V_isRampingUp) isRampingUp;
```

## Class methods

```
+[BWRamp initialize];
```

## Instance methods

```
-[BWRamp init];
-[BWRamp dealloc];
-[BWRamp reset];
-[BWRamp currentValue];
-[BWRamp initWithName:];
-[BWRamp isRamping];
-[BWRamp isRampingUp];
-[BWRamp startRampFrom:to:iterations:shape:];
-[BWRamp startRampFrom:to:iterations:shape:exponentialConvergenceFraction:];
-[BWRamp startSpringRampFrom:to:withTension:friction:snapFraction:frameRate:];
-[BWRamp updateRampForNextIteration];
```
