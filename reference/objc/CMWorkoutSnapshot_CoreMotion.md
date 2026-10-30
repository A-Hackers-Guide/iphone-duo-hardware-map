# `CMWorkoutSnapshot`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _state;
@"CMWorkout" _workout;
@"NSDate" _entryDate;
```

## Properties

```
@property (Tq,R,N) state;
@property (T@"NSDate",R,N) entryDate;
@property (T@"CMWorkout",R,N) workout;
```

## Class methods

```
+[CMWorkoutSnapshot supportsSecureCoding];
```

## Instance methods

```
-[CMWorkoutSnapshot dealloc];
-[CMWorkoutSnapshot entryDate];
-[CMWorkoutSnapshot encodeWithCoder:];
-[CMWorkoutSnapshot description];
-[CMWorkoutSnapshot initWithCoder:];
-[CMWorkoutSnapshot copyWithZone:];
-[CMWorkoutSnapshot state];
-[CMWorkoutSnapshot workout];
-[CMWorkoutSnapshot initWithState:workout:entryDate:];
```
