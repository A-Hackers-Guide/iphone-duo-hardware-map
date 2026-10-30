# `TUCallSoundPlayerDescriptor`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _audioPlayingWarmupNeeded;
q _soundType;
@"NSNumber" _sound;
Q _iterations;
d _pauseDuration;
```

## Properties

```
@property (Tq,N,V_soundType) soundType;
@property (TB,N,V_audioPlayingWarmupNeeded) audioPlayingWarmupNeeded;
@property (T@"NSNumber",&,N,V_sound) sound;
@property (TQ,N,V_iterations) iterations;
@property (Td,N,V_pauseDuration) pauseDuration;
```

## Instance methods

```
-[TUCallSoundPlayerDescriptor setSound:];
-[TUCallSoundPlayerDescriptor setSoundType:];
-[TUCallSoundPlayerDescriptor iterations];
-[TUCallSoundPlayerDescriptor setIterations:];
-[TUCallSoundPlayerDescriptor sound];
-[TUCallSoundPlayerDescriptor description];
-[TUCallSoundPlayerDescriptor soundType];
-[TUCallSoundPlayerDescriptor pauseDuration];
-[TUCallSoundPlayerDescriptor audioPlayingWarmupNeeded];
-[TUCallSoundPlayerDescriptor initWithSoundType:call:];
-[TUCallSoundPlayerDescriptor initWithSoundType:provider:video:region:];
-[TUCallSoundPlayerDescriptor initWithSoundType:provider:video:region:audioPlayingWarmupNeeded:];
-[TUCallSoundPlayerDescriptor initWithSoundType:sound:iterations:pauseDuration:audioPlayingWarmupNeeded:];
-[TUCallSoundPlayerDescriptor setAudioPlayingWarmupNeeded:];
-[TUCallSoundPlayerDescriptor setPauseDuration:];
```
