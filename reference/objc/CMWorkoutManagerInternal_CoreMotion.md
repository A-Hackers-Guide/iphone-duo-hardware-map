# `CMWorkoutManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 27 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"<CMWorkoutManagerDelegate>" fDelegate;
@"CMWorkoutManager" fSender;
@"CMWorkout" fLastNonTransitionWorkout;
@"CMWorkout" fWorkout;
@"CMWorkoutOverview" fWorkoutOverview;
B fEnableWorkoutChangeDetection;
q fSessionState;
@"NSMutableDictionary" fMuteSettings;
@"NSMutableDictionary" fAutoPauseMuteSettings;
```

## Instance methods

```
-[CMWorkoutManagerInternal init];
-[CMWorkoutManagerInternal dealloc];
-[CMWorkoutManagerInternal _teardown];
-[CMWorkoutManagerInternal _resumeWorkout:];
-[CMWorkoutManagerInternal _beginWorkoutSession:withWorkout:enableWorkoutChangeDetection:];
-[CMWorkoutManagerInternal _checkWorkout:];
-[CMWorkoutManagerInternal _endWorkoutSession:];
-[CMWorkoutManagerInternal _getPromptsNeededForWorkoutType:handler:];
-[CMWorkoutManagerInternal _handleDaemonEvent:];
-[CMWorkoutManagerInternal _handleDaemonResponse:];
-[CMWorkoutManagerInternal _isAutoPauseAllowedForWorkoutType:];
-[CMWorkoutManagerInternal _isReminderAllowedForType:];
-[CMWorkoutManagerInternal _muteAutoPauseForWorkoutType:mute:];
-[CMWorkoutManagerInternal _muteReminderType:mute:];
-[CMWorkoutManagerInternal _pauseWorkout:];
-[CMWorkoutManagerInternal _registerForWorkoutEvents];
-[CMWorkoutManagerInternal _setCurrentWorkoutType:isManualTransition:];
-[CMWorkoutManagerInternal _setReminderMuteSettingsForType:mute:];
-[CMWorkoutManagerInternal _setSuggestedStopTimeout:];
-[CMWorkoutManagerInternal _setWorkout:];
-[CMWorkoutManagerInternal _shouldAllowMotionCalibrationPromptsForWorkoutType:];
-[CMWorkoutManagerInternal _snapshotWithCompletion:];
-[CMWorkoutManagerInternal _startWorkout:];
-[CMWorkoutManagerInternal _stopWorkout:];
-[CMWorkoutManagerInternal _triggerWorkoutLocationUpdateForTesting:];
-[CMWorkoutManagerInternal _unregisterForWorkoutEvents];
-[CMWorkoutManagerInternal _userDismissedWorkoutAlert];
```
