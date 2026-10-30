# `SHSSystemSoundsControl`

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
@"<SHSSystemSoundsControlDelegate>" _delegate;
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
@property (T@"<SHSSystemSoundsControlDelegate>",W,N,V_delegate) delegate;
@property (Tf,N,V_volume) volume;
@property (TB,N,V_appWantsVolumeChangeEvents) appWantsVolumeChangeEvents;
@property (TB,N) systemSoundsVolumeMatchesRingtone;
```

## Instance methods

```
-[SHSSystemSoundsControl _setup];
-[SHSSystemSoundsControl volume];
-[SHSSystemSoundsControl init];
-[SHSSystemSoundsControl dealloc];
-[SHSSystemSoundsControl setVolume:];
-[SHSSystemSoundsControl reload];
-[SHSSystemSoundsControl setDelegate:];
-[SHSSystemSoundsControl delegate];
-[SHSSystemSoundsControl _tearDown];
-[SHSSystemSoundsControl _updateVolume:];
-[SHSSystemSoundsControl _handleServerConnectionDiedNotification:];
-[SHSSystemSoundsControl _systemController];
-[SHSSystemSoundsControl _handleEffectiveVolumeDidChangeNotification:];
-[SHSSystemSoundsControl _logFaultCalledForBackground];
-[SHSSystemSoundsControl _logFaultCalledForInactive];
-[SHSSystemSoundsControl _volumeChangeCoalescingCount];
-[SHSSystemSoundsControl _volumeInitialized];
-[SHSSystemSoundsControl appWantsVolumeChangeEvents];
-[SHSSystemSoundsControl flushPendingVolumeChanges];
-[SHSSystemSoundsControl setAppWantsVolumeChangeEvents:];
-[SHSSystemSoundsControl setSystemSoundsVolumeMatchesRingtone:];
-[SHSSystemSoundsControl set_logFaultCalledForBackground:];
-[SHSSystemSoundsControl set_logFaultCalledForInactive:];
-[SHSSystemSoundsControl set_systemController:];
-[SHSSystemSoundsControl set_volumeChangeCoalescingCount:];
-[SHSSystemSoundsControl set_volumeInitialized:];
-[SHSSystemSoundsControl systemSoundsVolumeMatchesRingtone];
```
