# `SHSAlarmControl`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
q _volumeFlushGeneration;
B _appWantsVolumeChangeEvents;
B __volumeInitialized;
B __logFaultCalledForInactive;
B __logFaultCalledForBackground;
f _volume;
@"<SHSAlarmControlDelegate>" _delegate;
@"AVSystemController" __systemController;
q __volumeChangeCoalescingCount;
```

## Properties

```
@property (T@"AVSystemController",&,N,V__systemController) _systemController;
@property (Tq,N,V__volumeChangeCoalescingCount) _volumeChangeCoalescingCount;
@property (TB,N,V__volumeInitialized) _volumeInitialized;
@property (TB,N,V__logFaultCalledForInactive) _logFaultCalledForInactive;
@property (TB,N,V__logFaultCalledForBackground) _logFaultCalledForBackground;
@property (T@"<SHSAlarmControlDelegate>",W,N,V_delegate) delegate;
@property (Tf,N,V_volume) volume;
@property (TB,N,V_appWantsVolumeChangeEvents) appWantsVolumeChangeEvents;
@property (TB,N) alarmVolumeMatchesRingtone;
```

## Instance methods

```
-[SHSAlarmControl _setup];
-[SHSAlarmControl volume];
-[SHSAlarmControl init];
-[SHSAlarmControl dealloc];
-[SHSAlarmControl setVolume:];
-[SHSAlarmControl reload];
-[SHSAlarmControl setDelegate:];
-[SHSAlarmControl delegate];
-[SHSAlarmControl _tearDown];
-[SHSAlarmControl _updateVolume:];
-[SHSAlarmControl _handleServerConnectionDiedNotification:];
-[SHSAlarmControl _systemController];
-[SHSAlarmControl _handleEffectiveVolumeDidChangeNotification:];
-[SHSAlarmControl _logFaultCalledForBackground];
-[SHSAlarmControl _logFaultCalledForInactive];
-[SHSAlarmControl _volumeChangeCoalescingCount];
-[SHSAlarmControl _volumeInitialized];
-[SHSAlarmControl alarmVolumeMatchesRingtone];
-[SHSAlarmControl appWantsVolumeChangeEvents];
-[SHSAlarmControl flushPendingVolumeChanges];
-[SHSAlarmControl setAlarmVolumeMatchesRingtone:];
-[SHSAlarmControl setAppWantsVolumeChangeEvents:];
-[SHSAlarmControl set_logFaultCalledForBackground:];
-[SHSAlarmControl set_logFaultCalledForInactive:];
-[SHSAlarmControl set_systemController:];
-[SHSAlarmControl set_volumeChangeCoalescingCount:];
-[SHSAlarmControl set_volumeInitialized:];
```
