# `NIAlgorithmConvergenceState`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _insufficientSignalStrength;
B _insufficientHorizontalSweep;
B _insufficientVerticalSweep;
B _insufficientMovement;
B _insufficientLighting;
q _convergence;
```

## Properties

```
@property (Tq,N,V_convergence) convergence;
@property (TB,N,V_insufficientSignalStrength) insufficientSignalStrength;
@property (TB,N,V_insufficientHorizontalSweep) insufficientHorizontalSweep;
@property (TB,N,V_insufficientVerticalSweep) insufficientVerticalSweep;
@property (TB,N,V_insufficientMovement) insufficientMovement;
@property (TB,N,V_insufficientLighting) insufficientLighting;
```

## Class methods

```
+[NIAlgorithmConvergenceState supportsSecureCoding];
```

## Instance methods

```
-[NIAlgorithmConvergenceState encodeWithCoder:];
-[NIAlgorithmConvergenceState hash];
-[NIAlgorithmConvergenceState description];
-[NIAlgorithmConvergenceState initWithCoder:];
-[NIAlgorithmConvergenceState copyWithZone:];
-[NIAlgorithmConvergenceState isEqual:];
-[NIAlgorithmConvergenceState setConvergence:];
-[NIAlgorithmConvergenceState setInsufficientHorizontalSweep:];
-[NIAlgorithmConvergenceState convergence];
-[NIAlgorithmConvergenceState initWithAlgorithmConvergenceState:];
-[NIAlgorithmConvergenceState initWithConvergenceStatus:];
-[NIAlgorithmConvergenceState insufficientHorizontalSweep];
-[NIAlgorithmConvergenceState insufficientLighting];
-[NIAlgorithmConvergenceState insufficientMovement];
-[NIAlgorithmConvergenceState insufficientSignalStrength];
-[NIAlgorithmConvergenceState insufficientVerticalSweep];
-[NIAlgorithmConvergenceState setInsufficientLighting:];
-[NIAlgorithmConvergenceState setInsufficientMovement:];
-[NIAlgorithmConvergenceState setInsufficientSignalStrength:];
-[NIAlgorithmConvergenceState setInsufficientVerticalSweep:];
```
