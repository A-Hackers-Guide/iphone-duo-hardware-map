# `VTCoreSpeechKeepAliveHandler`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTSiriEnabledMonitorDelegate`
- 5 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
i _activeNotificationToken;
i _inactiveNotificationToken;
@"NSObject<OS_dispatch_queue>" _queue;
B _voiceTriggerEnabled;
B _speakerStateActivated;
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
-[VTCoreSpeechKeepAliveHandler init];
-[VTCoreSpeechKeepAliveHandler dealloc];
-[VTCoreSpeechKeepAliveHandler start];
-[VTCoreSpeechKeepAliveHandler VTSiriEnabledMonitor:didReceiveEnabled:];
-[VTCoreSpeechKeepAliveHandler _coreSpeechDaemonKeepAlived];
-[VTCoreSpeechKeepAliveHandler _disableCoreSpeechDaemonKeepAlive];
-[VTCoreSpeechKeepAliveHandler _enableCoreSpeechDaemonKeepAlive];
-[VTCoreSpeechKeepAliveHandler _handleSpeakerActivated];
-[VTCoreSpeechKeepAliveHandler _handleSpeakerInactivated];
-[VTCoreSpeechKeepAliveHandler _voiceTriggerPolicyDisabled];
-[VTCoreSpeechKeepAliveHandler _voiceTriggerPolicyEnabled];
-[VTCoreSpeechKeepAliveHandler voiceTriggerPolicyDidChange:];
```
