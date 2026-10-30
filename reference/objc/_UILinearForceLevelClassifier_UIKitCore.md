# `_UILinearForceLevelClassifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIForceLevelClassifier`
- 11 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
d _smoothedForce;
B _anyForceObservations;
d _smoothedImpulse;
q _impulseObservationState;
d _lastForceForImpulse;
d _lastTimestampForImpulse;
d _revealThreshold;
d _standardThreshold;
d _strongThreshold;
d _smoothingFactor;
d _impulseSmoothingFactor;
```

## Properties

```
@property (Td,N,V_revealThreshold) revealThreshold;
@property (Td,N,V_standardThreshold) standardThreshold;
@property (Td,N,V_strongThreshold) strongThreshold;
@property (Td,N,V_smoothingFactor) smoothingFactor;
@property (Td,R,N) currentImpulse;
@property (Td,N,V_impulseSmoothingFactor) impulseSmoothingFactor;
```

## Instance methods

```
-[_UILinearForceLevelClassifier init];
-[_UILinearForceLevelClassifier dealloc];
-[_UILinearForceLevelClassifier reset];
-[_UILinearForceLevelClassifier revealThreshold];
-[_UILinearForceLevelClassifier setRevealThreshold:];
-[_UILinearForceLevelClassifier smoothingFactor];
-[_UILinearForceLevelClassifier strongThreshold];
-[_UILinearForceLevelClassifier _calculateProgressOfTouchForceValue:toForceLevel:minimumRequiredForceLevel:];
-[_UILinearForceLevelClassifier _forceLevelForTouchForceValue:];
-[_UILinearForceLevelClassifier _instantaneousImpulseForTouchForceValue:atTimestamp:];
-[_UILinearForceLevelClassifier _thresholdForForceLevel:];
-[_UILinearForceLevelClassifier _updateForceWithTouchForceValue:atTimestamp:];
-[_UILinearForceLevelClassifier _updateImpulseWithTouchForceValue:atTimestamp:];
-[_UILinearForceLevelClassifier currentImpulse];
-[_UILinearForceLevelClassifier debuggingPropertyForKey:changedToValue:];
-[_UILinearForceLevelClassifier impulseSmoothingFactor];
-[_UILinearForceLevelClassifier observeTouchWithForceValue:atTimestamp:withCentroidAtLocation:];
-[_UILinearForceLevelClassifier setImpulseSmoothingFactor:];
-[_UILinearForceLevelClassifier setSmoothingFactor:];
-[_UILinearForceLevelClassifier setStandardThreshold:];
-[_UILinearForceLevelClassifier setStrongThreshold:];
-[_UILinearForceLevelClassifier standardThreshold];
-[_UILinearForceLevelClassifier touchForceMultiplierDidChange];
-[_UILinearForceLevelClassifier transformerFromTouchForceMessageToProgressToForceLevel:minimumRequiredForceLevel:];
```
