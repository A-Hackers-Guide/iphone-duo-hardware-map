# `CMSwimWorkout`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMWorkout`
- 2 instance variables, 2 properties, 11 instance methods, 4 class methods

## Instance variables

```
q fLocation;
d fPoolLength;
```

## Properties

```
@property (Tq,R,N) location;
@property (Td,R,N) poolLength;
```

## Class methods

```
+[CMSwimWorkout supportsSecureCoding];
+[CMSwimWorkout isAvailable];
+[CMSwimWorkout swimLocationName:];
+[CMSwimWorkout swimWorkoutInstance:];
```

## Instance methods

```
-[CMSwimWorkout location];
-[CMSwimWorkout dealloc];
-[CMSwimWorkout encodeWithCoder:];
-[CMSwimWorkout description];
-[CMSwimWorkout initWithCoder:];
-[CMSwimWorkout copyWithZone:];
-[CMSwimWorkout _initWithSessionId:locationType:poolLength:startDate:endDate:];
-[CMSwimWorkout initWithSessionId:location:poolLength:];
-[CMSwimWorkout initWithSessionId:locationType:poolLength:];
-[CMSwimWorkout initWithSessionId:locationType:poolLength:startDate:endDate:];
-[CMSwimWorkout poolLength];
```
