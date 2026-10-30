# `TPDialerSoundController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 11 instance methods, 1 class methods

## Instance variables

```
^{__CFSet=} _inflightSounds;
b1 _soundsActivated;
Q _incompleteSoundCount;
```

## Properties

```
@property (TQ,V_incompleteSoundCount) incompleteSoundCount;
```

## Class methods

```
+[TPDialerSoundController _delayedDeactivate];
```

## Instance methods

```
-[TPDialerSoundController init];
-[TPDialerSoundController dealloc];
-[TPDialerSoundController _stopAllSoundsForcingCallbacks:];
-[TPDialerSoundController applicationResumedNotification:];
-[TPDialerSoundController applicationSuspendedNotification:];
-[TPDialerSoundController incompleteSoundCount];
-[TPDialerSoundController playSoundForDialerCharacter:];
-[TPDialerSoundController setIncompleteSoundCount:];
-[TPDialerSoundController setSoundsActivated:];
-[TPDialerSoundController soundCompletedPlaying:];
-[TPDialerSoundController stopSoundForDialerCharacter:];
```
