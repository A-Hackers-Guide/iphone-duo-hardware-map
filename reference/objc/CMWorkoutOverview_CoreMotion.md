# `CMWorkoutOverview`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _overviewId;
@"NSArray" _workouts;
```

## Properties

```
@property (T@"NSUUID",R,N) overviewId;
@property (T@"NSArray",R,N) workouts;
```

## Class methods

```
+[CMWorkoutOverview supportsSecureCoding];
```

## Instance methods

```
-[CMWorkoutOverview dealloc];
-[CMWorkoutOverview workouts];
-[CMWorkoutOverview encodeWithCoder:];
-[CMWorkoutOverview description];
-[CMWorkoutOverview initWithCoder:];
-[CMWorkoutOverview copyWithZone:];
-[CMWorkoutOverview initWithOverviewId:workouts:];
-[CMWorkoutOverview overviewId];
```
