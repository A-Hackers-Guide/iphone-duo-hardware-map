# `_UIDragMovementCadenceSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
d _velocityMagnitudeThreshold;
d _dwellTimeThreshold;
```

## Properties

```
@property (Td,N,V_velocityMagnitudeThreshold) velocityMagnitudeThreshold;
@property (Td,N,V_dwellTimeThreshold) dwellTimeThreshold;
```

## Class methods

```
+[_UIDragMovementCadenceSettings defaultSettingsForMovementPhase:cadence:];
```

## Instance methods

```
-[_UIDragMovementCadenceSettings _applyDragPlaceholderInitialPhaseDefaultsForCadence:];
-[_UIDragMovementCadenceSettings _applyDragPlaceholderSubsequentPhaseDefaultsForCadence:];
-[_UIDragMovementCadenceSettings _applyImmediateSettings];
-[_UIDragMovementCadenceSettings _applyInteractiveReorderInitialPhaseDefaultsForCadence:];
-[_UIDragMovementCadenceSettings _applyInteractiveReorderSubsequentPhaseDefaultsForCadence:];
-[_UIDragMovementCadenceSettings dwellTimeThreshold];
-[_UIDragMovementCadenceSettings initWithMovementPhase:cadence:];
-[_UIDragMovementCadenceSettings initWithVelocityMagnitudeThreshold:dwellTimeThreshold:];
-[_UIDragMovementCadenceSettings setDwellTimeThreshold:];
-[_UIDragMovementCadenceSettings setVelocityMagnitudeThreshold:];
-[_UIDragMovementCadenceSettings velocityMagnitudeThreshold];
```
