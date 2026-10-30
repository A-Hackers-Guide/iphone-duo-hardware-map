# `SBSleepWakeHardwareButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHardwareButtonInteraction`, `SBHardwareButtonGestureParametersObserver`
- 8 instance variables, 12 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _inhibitNextSinglePressUp;
B _SOSGestureActive;
B _fadeOutInProgressFromLockButtonWhileUnlocked;
B _undidFadeOutFromLockButton;
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SpringBoard" _SBApp;
d _multiplePressTimeInterval;
```

## Properties

```
@property (T@"SBBacklightCoordinator",&,N,V_backlightCoordinator) backlightCoordinator;
@property (T@"SBLockScreenCoordinator",&,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (T@"SpringBoard",&,N,V_SBApp) SBApp;
@property (Td,N,V_multiplePressTimeInterval) multiplePressTimeInterval;
@property (TB,N,V_fadeOutInProgressFromLockButtonWhileUnlocked) fadeOutInProgressFromLockButtonWhileUnlocked;
@property (TB,N,V_undidFadeOutFromLockButton) undidFadeOutFromLockButton;
@property (TB,N,V_inhibitNextSinglePressUp) inhibitNextSinglePressUp;
@property (TB,N,GisSOSGestureActive,V_SOSGestureActive) SOSGestureActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSleepWakeHardwareButtonInteraction consumeInitialPressDown];
-[SBSleepWakeHardwareButtonInteraction setMultiplePressTimeInterval:];
-[SBSleepWakeHardwareButtonInteraction init];
-[SBSleepWakeHardwareButtonInteraction _performSleep];
-[SBSleepWakeHardwareButtonInteraction _performWake];
-[SBSleepWakeHardwareButtonInteraction provider:didUpdateButtonGestureParameters:];
-[SBSleepWakeHardwareButtonInteraction setBacklightCoordinator:];
-[SBSleepWakeHardwareButtonInteraction multiplePressTimeInterval];
-[SBSleepWakeHardwareButtonInteraction backlightCoordinator];
-[SBSleepWakeHardwareButtonInteraction lockScreenCoordinator];
-[SBSleepWakeHardwareButtonInteraction setLockScreenCoordinator:];
-[SBSleepWakeHardwareButtonInteraction SBApp];
-[SBSleepWakeHardwareButtonInteraction reverseSleepIfNeededAndPossible];
-[SBSleepWakeHardwareButtonInteraction _isAnySleepAnimationInProgress];
-[SBSleepWakeHardwareButtonInteraction _isAnyWakeAnimationInProgressForSource:];
-[SBSleepWakeHardwareButtonInteraction _playLockSound];
-[SBSleepWakeHardwareButtonInteraction consumeSinglePressUp];
-[SBSleepWakeHardwareButtonInteraction fadeOutInProgressFromLockButtonWhileUnlocked];
-[SBSleepWakeHardwareButtonInteraction inhibitNextSinglePressUp];
-[SBSleepWakeHardwareButtonInteraction isSOSGestureActive];
-[SBSleepWakeHardwareButtonInteraction performSleepForReason:];
-[SBSleepWakeHardwareButtonInteraction setFadeOutInProgressFromLockButtonWhileUnlocked:];
-[SBSleepWakeHardwareButtonInteraction setInhibitNextSinglePressUp:];
-[SBSleepWakeHardwareButtonInteraction setSBApp:];
-[SBSleepWakeHardwareButtonInteraction setSOSGestureActive:];
-[SBSleepWakeHardwareButtonInteraction setUndidFadeOutFromLockButton:];
-[SBSleepWakeHardwareButtonInteraction undidFadeOutFromLockButton];
```
