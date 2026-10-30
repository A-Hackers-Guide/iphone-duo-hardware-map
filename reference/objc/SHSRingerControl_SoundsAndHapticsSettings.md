# `SHSRingerControl`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _appWantsVolumeChangeEvents;
B __volumeInitialized;
B __logFaultCalledForInactive;
B __logFaultCalledForBackground;
f _volume;
@"<SHSRingerControlDelegate>" _delegate;
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
@property (T@"<SHSRingerControlDelegate>",W,N,V_delegate) delegate;
@property (Tf,N,V_volume) volume;
@property (TB,N) canChangeRingtoneWithButtons;
@property (TB,N,V_appWantsVolumeChangeEvents) appWantsVolumeChangeEvents;
```

## Instance methods

```
-[SHSRingerControl _setup];
-[SHSRingerControl volume];
-[SHSRingerControl init];
-[SHSRingerControl dealloc];
-[SHSRingerControl setVolume:];
-[SHSRingerControl reload];
-[SHSRingerControl setDelegate:];
-[SHSRingerControl delegate];
-[SHSRingerControl _tearDown];
-[SHSRingerControl _updateVolume:];
-[SHSRingerControl _handleServerConnectionDiedNotification:];
-[SHSRingerControl _systemController];
-[SHSRingerControl _handleEffectiveVolumeDidChangeNotification:];
-[SHSRingerControl _logFaultCalledForBackground];
-[SHSRingerControl _logFaultCalledForInactive];
-[SHSRingerControl _volumeChangeCoalescingCount];
-[SHSRingerControl _volumeInitialized];
-[SHSRingerControl appWantsVolumeChangeEvents];
-[SHSRingerControl canChangeRingtoneWithButtons];
-[SHSRingerControl setAppWantsVolumeChangeEvents:];
-[SHSRingerControl setCanChangeRingtoneWithButtons:];
-[SHSRingerControl set_logFaultCalledForBackground:];
-[SHSRingerControl set_logFaultCalledForInactive:];
-[SHSRingerControl set_systemController:];
-[SHSRingerControl set_volumeChangeCoalescingCount:];
-[SHSRingerControl set_volumeInitialized:];
```
