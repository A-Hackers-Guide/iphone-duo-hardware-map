# `CMExerciseMinuteInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSObject<OS_dispatch_queue>" fAppQueue;
B fStartedUpdates;
@"CMExerciseMinuteData" fMostRecentRecord;
@? fHandler;
```

## Instance methods

```
-[CMExerciseMinuteInternal init];
-[CMExerciseMinuteInternal dealloc];
-[CMExerciseMinuteInternal _teardown];
-[CMExerciseMinuteInternal _queryExerciseMinutesFromRecord:handler:];
-[CMExerciseMinuteInternal _startUpdatesFromRecord:handler:];
-[CMExerciseMinuteInternal _startUpdatesWithHandler:];
-[CMExerciseMinuteInternal _stopUpdates];
```
