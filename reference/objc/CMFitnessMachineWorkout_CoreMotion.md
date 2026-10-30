# `CMFitnessMachineWorkout`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMWorkout`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSString" fManufacturerName;
@"NSString" fModel;
```

## Properties

```
@property (T@"NSString",R,N) manufacturerName;
@property (T@"NSString",R,N) model;
```

## Class methods

```
+[CMFitnessMachineWorkout supportsSecureCoding];
+[CMFitnessMachineWorkout isAvailable];
+[CMFitnessMachineWorkout fitnessMachineWorkoutInstance:];
```

## Instance methods

```
-[CMFitnessMachineWorkout model];
-[CMFitnessMachineWorkout dealloc];
-[CMFitnessMachineWorkout manufacturerName];
-[CMFitnessMachineWorkout encodeWithCoder:];
-[CMFitnessMachineWorkout description];
-[CMFitnessMachineWorkout initWithCoder:];
-[CMFitnessMachineWorkout copyWithZone:];
-[CMFitnessMachineWorkout initWithSessionId:workoutType:manufacturerName:model:];
```
