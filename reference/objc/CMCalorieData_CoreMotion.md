# `CMCalorieData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
q fWorkoutType;
d fDuration;
d fMets;
d fBasalMets;
d fTotalCalories;
d fBasalCalories;
```

## Properties

```
@property (Tq,R,N) workoutType;
@property (Td,R,N) duration;
@property (T@"NSNumber",R,N) mets;
@property (T@"NSNumber",R,N) basalMets;
@property (T@"NSNumber",R,N) totalCalories;
@property (T@"NSNumber",R,N) basalCalories;
```

## Class methods

```
+[CMCalorieData supportsSecureCoding];
```

## Instance methods

```
-[CMCalorieData dealloc];
-[CMCalorieData duration];
-[CMCalorieData encodeWithCoder:];
-[CMCalorieData workoutType];
-[CMCalorieData description];
-[CMCalorieData initWithCoder:];
-[CMCalorieData copyWithZone:];
-[CMCalorieData basalCalories];
-[CMCalorieData basalMets];
-[CMCalorieData initWithWorkoutType:duration:mets:basalMets:totalCalories:basalCalories:];
-[CMCalorieData mets];
-[CMCalorieData totalCalories];
```
