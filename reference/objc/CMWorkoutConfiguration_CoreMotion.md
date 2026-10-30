# `CMWorkoutConfiguration`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _workoutType;
q _locationType;
```

## Properties

```
@property (Tq,V_workoutType) workoutType;
@property (Tq,V_locationType) locationType;
```

## Class methods

```
+[CMWorkoutConfiguration supportsSecureCoding];
```

## Instance methods

```
-[CMWorkoutConfiguration setLocationType:];
-[CMWorkoutConfiguration init];
-[CMWorkoutConfiguration setWorkoutType:];
-[CMWorkoutConfiguration encodeWithCoder:];
-[CMWorkoutConfiguration workoutType];
-[CMWorkoutConfiguration description];
-[CMWorkoutConfiguration initWithCoder:];
-[CMWorkoutConfiguration copyWithZone:];
-[CMWorkoutConfiguration isEqual:];
-[CMWorkoutConfiguration locationType];
```
