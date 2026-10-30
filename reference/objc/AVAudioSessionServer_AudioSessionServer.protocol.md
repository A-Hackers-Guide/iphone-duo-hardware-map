# `AVAudioSessionServer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 36 instance methods, 0 class methods

## Instance methods

```
-[AVAudioSessionServer setPlayState:sessionID:playerType:playerRef:modes:subsessionRef:];
-[AVAudioSessionServer deactivateWithFlags:auditToken:flags:];
-[AVAudioSessionServer requestApplyInputMuteForSession:inputMuted:];
-[AVAudioSessionServer createCoreMXSessionForPID:];
-[AVAudioSessionServer createTimestampWriterForDevice:halID:isDecoupledInput:];
-[AVAudioSessionServer setClientMuteState:sessionID:playerType:playerRef:];
-[AVAudioSessionServer getSessionsWithMicrophoneInjectionPreference];
-[AVAudioSessionServer activateWithFlags:auditToken:flags:];
-[AVAudioSessionServer setMicrophoneInjectionCapability:];
-[AVAudioSessionServer sampleRateChanged:forDevice:];
-[AVAudioSessionServer isSessionMuted:];
-[AVAudioSessionServer destroyCMSessionForPID:sessionID:];
-[AVAudioSessionServer setMXSessionProperty:forSessionID:value:];
-[AVAudioSessionServer queuePIDOverridden:];
-[AVAudioSessionServer destroySession:auditToken:];
-[AVAudioSessionServer destroyTimestampWriterForDevice:];
-[AVAudioSessionServer getDefaultMXSession:];
-[AVAudioSessionServer generateIOControllerEvent:forDevice:];
-[AVAudioSessionServer checkBooleanEntitlementForSession:entitlementIdentifier:];
-[AVAudioSessionServer getPrimarySessionForPID:createIfNecessary:];
-[AVAudioSessionServer getSessionIDsForToken:];
-[AVAudioSessionServer checkMicrophoneInjectionPermission];
-[AVAudioSessionServer getMXSessionProperty:forSessionID:];
-[AVAudioSessionServer getDescriptionForSession:];
-[AVAudioSessionServer getSourceProcessAuditToken:];
-[AVAudioSessionServer startXPCServer];
-[AVAudioSessionServer dynamicLatencyForDevice:isInput:];
-[AVAudioSessionServer getPrimarySession:createIfNecessary:];
-[AVAudioSessionServer createCoreMXSession:type:];
-[AVAudioSessionServer mapSession:isInput:toDevice:];
-[AVAudioSessionServer handleInterruptionForPid:audioSessionID:mxSessionID:interruptionState:interruptionInfo:];
-[AVAudioSessionServer allowEnhanceDialogue:];
-[AVAudioSessionServer interruptDummyPlayersForSession:];
-[AVAudioSessionServer handleInterruptionForPid:audioSessionID:interruptionState:interruptionInfo:];
-[AVAudioSessionServer copyCMSession:];
-[AVAudioSessionServer getJSONDescriptionForSession:];
```
