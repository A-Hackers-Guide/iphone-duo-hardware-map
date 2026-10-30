# `CMFitnessPlusWorkout`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMWorkout`
- 2 instance variables, 2 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"NSString" fCatalogWorkoutId;
q fMediaType;
```

## Properties

```
@property (T@"NSString",R,N) catalogWorkoutId;
@property (Tq,R,N) mediaType;
```

## Class methods

```
+[CMFitnessPlusWorkout supportsSecureCoding];
+[CMFitnessPlusWorkout isAvailable];
+[CMFitnessPlusWorkout fitnessPlusWorkoutInstance:];
+[CMFitnessPlusWorkout mediaTypeName:];
```

## Instance methods

```
-[CMFitnessPlusWorkout dealloc];
-[CMFitnessPlusWorkout encodeWithCoder:];
-[CMFitnessPlusWorkout description];
-[CMFitnessPlusWorkout initWithCoder:];
-[CMFitnessPlusWorkout copyWithZone:];
-[CMFitnessPlusWorkout mediaType];
-[CMFitnessPlusWorkout catalogWorkoutId];
-[CMFitnessPlusWorkout initWithSessionId:type:catalogWorkoutId:mediaType:];
-[CMFitnessPlusWorkout initWithSessionId:type:catalogWorkoutId:mediaType:error:];
-[CMFitnessPlusWorkout initWithSessionId:type:catalogWorkoutId:mediaType:locationType:error:];
```
