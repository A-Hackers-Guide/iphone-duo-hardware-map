# `CMWorkoutManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"CMWorkoutManagerInternal" _internal;
```

## Properties

```
@property (T@"CMWorkoutManagerInternal",R,N,V_internal) _internal;
@property (T@"<CMWorkoutManagerDelegate>",N) delegate;
```

## Class methods

```
+[CMWorkoutManager isAvailable];
+[CMWorkoutManager supportedMetricsForWorkoutType:];
```

## Instance methods

```
-[CMWorkoutManager _internal];
-[CMWorkoutManager endWorkoutSession:];
-[CMWorkoutManager init];
-[CMWorkoutManager dealloc];
-[CMWorkoutManager setDelegate:];
-[CMWorkoutManager delegate];
-[CMWorkoutManager beginWorkoutSession:withWorkout:enableWorkoutChangeDetection:];
-[CMWorkoutManager getPromptsNeededForWorkoutType:handler:];
-[CMWorkoutManager muteAutoPauseForWorkoutType:mute:];
-[CMWorkoutManager muteReminderType:mute:];
-[CMWorkoutManager pauseWorkout:];
-[CMWorkoutManager resumeWorkout:];
-[CMWorkoutManager setCurrentWorkoutType:isManualTransition:];
-[CMWorkoutManager setSuggestedStopTimeout:];
-[CMWorkoutManager snapshotWithCompletion:];
-[CMWorkoutManager startWorkout:];
-[CMWorkoutManager stopWorkout:];
-[CMWorkoutManager triggerWorkoutLocationUpdateForTesting:];
-[CMWorkoutManager userDismissedWorkoutAlert];
```
