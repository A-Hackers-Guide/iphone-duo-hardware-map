# `ATServerDelegatePriv`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioSessionServerDelegate`
- 3 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _conclaveLaunchMutex;
{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}} _conclaveLaunchCondVar;
B _conclaveLaunched;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ATServerDelegatePriv init];
-[ATServerDelegatePriv conclaveLaunched];
-[ATServerDelegatePriv dolbyDigitalEncoderAvailable];
-[ATServerDelegatePriv handleCategoryOrModeChange:];
-[ATServerDelegatePriv handleInterruptionWithID:clientPID:interruptionState:interruptionInfo:];
-[ATServerDelegatePriv muteSessionInput:clientPID:muted:];
-[ATServerDelegatePriv refreshMicrophoneInjectionPermissions:];
-[ATServerDelegatePriv refreshRecordPermissions:];
-[ATServerDelegatePriv setIOPropertiesForSession:values:];
-[ATServerDelegatePriv setTelephonyClientSessionID:];
-[ATServerDelegatePriv spatialAudioEnabled:mode:];
-[ATServerDelegatePriv spatialPreferencesForSession:contentType:];
-[ATServerDelegatePriv updateContentMixingMode:forSession:];
-[ATServerDelegatePriv updateMicrophoneInjectionPreference:forSession:];
-[ATServerDelegatePriv waitForConclaveLaunch];
```
