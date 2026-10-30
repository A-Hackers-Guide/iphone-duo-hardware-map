# `AVAudioSessionServerPriv`

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioSessionServer`
- 2 instance variables, 4 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"AVAudioSessionXPCServer" _xpcServer;
@"<AVAudioSessionServerDelegate>" _serverDelegate;
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
-[AVAudioSessionServerPriv setPlayState:sessionID:playerType:playerRef:modes:subsessionRef:];
-[AVAudioSessionServerPriv deactivateWithFlags:auditToken:flags:];
-[AVAudioSessionServerPriv requestApplyInputMuteForSession:inputMuted:];
-[AVAudioSessionServerPriv createCoreMXSessionForPID:];
-[AVAudioSessionServerPriv init];
-[AVAudioSessionServerPriv createTimestampWriterForDevice:halID:isDecoupledInput:];
-[AVAudioSessionServerPriv setClientMuteState:sessionID:playerType:playerRef:];
-[AVAudioSessionServerPriv getSessionsWithMicrophoneInjectionPreference];
-[AVAudioSessionServerPriv activateWithFlags:auditToken:flags:];
-[AVAudioSessionServerPriv setMicrophoneInjectionCapability:];
-[AVAudioSessionServerPriv sampleRateChanged:forDevice:];
-[AVAudioSessionServerPriv isSessionMuted:];
-[AVAudioSessionServerPriv createCoreMXSessionForProcID:type:];
-[AVAudioSessionServerPriv destroyCMSessionForPID:sessionID:];
-[AVAudioSessionServerPriv setMXSessionProperty:forSessionID:value:];
-[AVAudioSessionServerPriv queuePIDOverridden:];
-[AVAudioSessionServerPriv destroySession:auditToken:];
-[AVAudioSessionServerPriv destroySession:procID:];
-[AVAudioSessionServerPriv destroyTimestampWriterForDevice:];
-[AVAudioSessionServerPriv getDefaultMXSession:];
-[AVAudioSessionServerPriv generateIOControllerEvent:forDevice:];
-[AVAudioSessionServerPriv checkBooleanEntitlementForSession:entitlementIdentifier:];
-[AVAudioSessionServerPriv getPrimarySessionForPID:createIfNecessary:];
-[AVAudioSessionServerPriv getSessionIDsForToken:];
-[AVAudioSessionServerPriv checkMicrophoneInjectionPermission];
-[AVAudioSessionServerPriv getMXSessionProperty:forSessionID:];
-[AVAudioSessionServerPriv getDescriptionForSession:];
-[AVAudioSessionServerPriv getSourceProcessAuditToken:];
-[AVAudioSessionServerPriv startXPCServer];
-[AVAudioSessionServerPriv dynamicLatencyForDevice:isInput:];
-[AVAudioSessionServerPriv getPrimarySessionForProcID:createIfNecessary:];
-[AVAudioSessionServerPriv getPrimarySession:createIfNecessary:];
-[AVAudioSessionServerPriv createCoreMXSession:type:];
-[AVAudioSessionServerPriv mapSession:isInput:toDevice:];
-[AVAudioSessionServerPriv handleInterruptionForPid:audioSessionID:mxSessionID:interruptionState:interruptionInfo:];
-[AVAudioSessionServerPriv allowEnhanceDialogue:];
-[AVAudioSessionServerPriv interruptDummyPlayersForSession:];
-[AVAudioSessionServerPriv handleInterruptionForPid:audioSessionID:interruptionState:interruptionInfo:];
-[AVAudioSessionServerPriv copyCMSession:];
-[AVAudioSessionServerPriv initWithAudioControlQueue:delegate:];
-[AVAudioSessionServerPriv getJSONDescriptionForSession:];
```
