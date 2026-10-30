# `CMExerciseMinuteData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
q fRecordId;
d fStartDate;
@"NSUUID" fSourceId;
```

## Properties

```
@property (T@"NSDate",R,N) startDate;
@property (Tq,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
```

## Class methods

```
+[CMExerciseMinuteData supportsSecureCoding];
+[CMExerciseMinuteData maxExerciseMinuteDataEntries];
```

## Instance methods

```
-[CMExerciseMinuteData startDate];
-[CMExerciseMinuteData sourceId];
-[CMExerciseMinuteData recordId];
-[CMExerciseMinuteData dealloc];
-[CMExerciseMinuteData encodeWithCoder:];
-[CMExerciseMinuteData description];
-[CMExerciseMinuteData initWithCoder:];
-[CMExerciseMinuteData copyWithZone:];
-[CMExerciseMinuteData initWithStartDate:recordId:sourceId:];
```
