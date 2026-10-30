# `CBBespokeModeManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _modes;
q _currentModeType;
q _previousModeType;
@"NSObject<OS_os_log>" _logHandle;
f _rampTimeGameModeEntry;
f _rampTimeGameModeExit;
f _activeTransitionRampTime;
```

## Instance methods

```
-[CBBespokeModeManager currentMode];
-[CBBespokeModeManager dealloc];
-[CBBespokeModeManager previousMode];
-[CBBespokeModeManager loadCurrentModeAABToWorkingAAB:];
-[CBBespokeModeManager currentModeType];
-[CBBespokeModeManager registeredModes];
-[CBBespokeModeManager setCustomRampTimeGameModeEntry:];
-[CBBespokeModeManager currentAAB];
-[CBBespokeModeManager executeTransitionToMode:];
-[CBBespokeModeManager getModeTransitionRampTime];
-[CBBespokeModeManager handleCurveReset];
-[CBBespokeModeManager handleCurveResetToGoodCurve];
-[CBBespokeModeManager handleGameModeTransitionNotification:withWorkingAAB:];
-[CBBespokeModeManager initWithAAB:andInitialMode:];
-[CBBespokeModeManager initializeRampTimesFromPreferences];
-[CBBespokeModeManager modeOfType:];
-[CBBespokeModeManager modeToString:];
-[CBBespokeModeManager previousModeType];
-[CBBespokeModeManager registerDefaultModesWithAAB:];
-[CBBespokeModeManager registerMode:];
-[CBBespokeModeManager registeredModeTypes];
-[CBBespokeModeManager saveWorkingAAB:toMode:];
-[CBBespokeModeManager saveWorkingAABToCurrentMode:];
-[CBBespokeModeManager setCustomRampTimeGameModeExit:];
-[CBBespokeModeManager transitionToMode:withWorkingAAB:];
```
