# `SHSAudioPlayback`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 32 instance methods, 0 class methods

## Instance variables

```
B __pendingRingtoneLoop;
B __pendingSystemSoundLoop;
B __retryingAfterReset;
f __pendingSystemSoundVolume;
@"TLAlert" _currentPreview;
@"TLAlert" _systemSoundsPreview;
@"NSString" __pendingRingtoneIdentifier;
q __pendingRingtoneAlertType;
@"NSString" __pendingSystemSoundIdentifier;
```

## Properties

```
@property (T@"TLAlert",&,N,V_currentPreview) currentPreview;
@property (T@"TLAlert",&,N,V_systemSoundsPreview) systemSoundsPreview;
@property (T@"NSString",C,N,V__pendingRingtoneIdentifier) _pendingRingtoneIdentifier;
@property (TB,N,V__pendingRingtoneLoop) _pendingRingtoneLoop;
@property (Tq,N,V__pendingRingtoneAlertType) _pendingRingtoneAlertType;
@property (T@"NSString",C,N,V__pendingSystemSoundIdentifier) _pendingSystemSoundIdentifier;
@property (TB,N,V__pendingSystemSoundLoop) _pendingSystemSoundLoop;
@property (Tf,N,V__pendingSystemSoundVolume) _pendingSystemSoundVolume;
@property (TB,N,V__retryingAfterReset) _retryingAfterReset;
```

## Instance methods

```
-[SHSAudioPlayback _setup];
-[SHSAudioPlayback init];
-[SHSAudioPlayback dealloc];
-[SHSAudioPlayback stopPlayback];
-[SHSAudioPlayback _tearDown];
-[SHSAudioPlayback isPlayingRingtoneOrAlarmPreview];
-[SHSAudioPlayback _handleMediaServicesWereResetNotification:];
-[SHSAudioPlayback _pendingRingtoneAlertType];
-[SHSAudioPlayback _pendingRingtoneIdentifier];
-[SHSAudioPlayback _pendingRingtoneLoop];
-[SHSAudioPlayback _pendingSystemSoundIdentifier];
-[SHSAudioPlayback _pendingSystemSoundLoop];
-[SHSAudioPlayback _pendingSystemSoundVolume];
-[SHSAudioPlayback _retryingAfterReset];
-[SHSAudioPlayback currentPreview];
-[SHSAudioPlayback deactivateAudioSession];
-[SHSAudioPlayback isPlayingRingtone];
-[SHSAudioPlayback isPlayingSystemSoundsPreview];
-[SHSAudioPlayback playRingtoneWithIdentifier:loop:];
-[SHSAudioPlayback playRingtoneWithIdentifier:loop:forAlertType:];
-[SHSAudioPlayback playSystemSoundPreviewWithIdentifier:loop:volume:];
-[SHSAudioPlayback setCurrentPreview:];
-[SHSAudioPlayback setSystemSoundsPreview:];
-[SHSAudioPlayback set_pendingRingtoneAlertType:];
-[SHSAudioPlayback set_pendingRingtoneIdentifier:];
-[SHSAudioPlayback set_pendingRingtoneLoop:];
-[SHSAudioPlayback set_pendingSystemSoundIdentifier:];
-[SHSAudioPlayback set_pendingSystemSoundLoop:];
-[SHSAudioPlayback set_pendingSystemSoundVolume:];
-[SHSAudioPlayback set_retryingAfterReset:];
-[SHSAudioPlayback stopRingtoneWithFadeOut:];
-[SHSAudioPlayback systemSoundsPreview];
```
