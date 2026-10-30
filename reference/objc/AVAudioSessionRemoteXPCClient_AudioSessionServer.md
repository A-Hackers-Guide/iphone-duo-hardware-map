# `AVAudioSessionRemoteXPCClient`

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SessionManagerXPCProtocol`
- 6 instance variables, 0 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"AVAudioSessionXPCServer" _server;
{ProcessInfo="token"{ProcessToken="mValue"I}"xpcConnection"@"NSXPCConnection""mProcessName"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}} _clientProcess;
@"<AVAudioSessionServerDelegate>" _serverDelegate;
B _invalidated;
{reply_watchdog_factory="mDebugging"B"mDefaultTimeoutMS"i"mTimeoutHandler"{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}}} _defaultReplyWatchdogFactory;
{reply_watchdog_factory="mDebugging"B"mDefaultTimeoutMS"i"mTimeoutHandler"{function<void ()>="__f_"{__value_func<void ()>="__buf_"(type="__data"[24C])"__f_"^v}}} _longReplyWatchdogFactory;
```

## Instance methods

```
-[AVAudioSessionRemoteXPCClient getPropertiesIONode:properties:reply:];
-[AVAudioSessionRemoteXPCClient pingWithReply:];
-[AVAudioSessionRemoteXPCClient verifySessionExists:reply:];
-[AVAudioSessionRemoteXPCClient testWorkloopDispatch:sessionID:reply:];
-[AVAudioSessionRemoteXPCClient invalidateIONode:reply:];
-[AVAudioSessionRemoteXPCClient setSession:decoupledInput:hasIOEventListeners:reply:];
-[AVAudioSessionRemoteXPCClient muteInputForRecordingProcesses:];
-[AVAudioSessionRemoteXPCClient dealloc];
-[AVAudioSessionRemoteXPCClient getApplicationProperty:clientID:propertyID:isMXProperty:reply:];
-[AVAudioSessionRemoteXPCClient setSessionPlayState:playState:playerType:playerRef:modes:reply:];
-[AVAudioSessionRemoteXPCClient createSession:reply:];
-[AVAudioSessionRemoteXPCClient containsPrivilegedIONodeProperties:];
-[AVAudioSessionRemoteXPCClient sessionIDs:clientID:reply:];
-[AVAudioSessionRemoteXPCClient getProperties:properties:genericMXPipe:reply:];
-[AVAudioSessionRemoteXPCClient activateSession:options:requestID:reply:];
-[AVAudioSessionRemoteXPCClient getEnhanceDialogueLevelWithReply:];
-[AVAudioSessionRemoteXPCClient invalidate];
-[AVAudioSessionRemoteXPCClient deactivateSession:options:priority:requestID:reply:];
-[AVAudioSessionRemoteXPCClient setIONode:playState:modes:reply:];
-[AVAudioSessionRemoteXPCClient createAudioApplicationForSpecification:reply:];
-[AVAudioSessionRemoteXPCClient createProxySession:reply:];
-[AVAudioSessionRemoteXPCClient setEnhanceDialoguePreference:reply:];
-[AVAudioSessionRemoteXPCClient silenceOutput:options:reply:];
-[AVAudioSessionRemoteXPCClient getDeferredMessages:reply:];
-[AVAudioSessionRemoteXPCClient getMXPropertyGenericPipe:propertyName:reply:];
-[AVAudioSessionRemoteXPCClient getPropertiesForCache:reply:];
-[AVAudioSessionRemoteXPCClient removeMXNotificationListener:notificationName:reply:];
-[AVAudioSessionRemoteXPCClient getProperty:propertyName:MXProperty:reply:];
-[AVAudioSessionRemoteXPCClient initWithServer:process:delegate:];
-[AVAudioSessionRemoteXPCClient setMXPropertyOnAllSessions:clientID:MXProperty:values:reply:];
-[AVAudioSessionRemoteXPCClient setApplicationProperty:clientID:propertyID:propertyValue:reply:];
-[AVAudioSessionRemoteXPCClient setPropertiesIONode:values:reply:];
-[AVAudioSessionRemoteXPCClient getSpatialPreferencesForSession:contentType:reply:];
-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:];
-[AVAudioSessionRemoteXPCClient getSpatialPreferencesForSession:reply:];
-[AVAudioSessionRemoteXPCClient setIOProperties:values:reply:];
-[AVAudioSessionRemoteXPCClient setEnhanceDialogueLevel:reply:];
-[AVAudioSessionRemoteXPCClient toggleInputMuteForRecordingProcess:];
-[AVAudioSessionRemoteXPCClient createIONodeWithSourceSession:sessionOwnerPID:playerType:reply:];
-[AVAudioSessionRemoteXPCClient addMXNotificationListener:notificationName:reply:];
-[AVAudioSessionRemoteXPCClient getDeferredMessagesForSessions:reply:];
-[AVAudioSessionRemoteXPCClient reconfigureIONode:withSourceSession:sessionOwnerPID:playerType:reply:];
-[AVAudioSessionRemoteXPCClient updateMicrophonePermission:clientToken:reply:];
-[AVAudioSessionRemoteXPCClient simulatePrimarySessionCreationInsideServerWithReply:];
-[AVAudioSessionRemoteXPCClient destroySession:reply:];
-[AVAudioSessionRemoteXPCClient getApplicationMessages:clientID:reply:];
-[AVAudioSessionRemoteXPCClient updateApplicationProperty:clientID:propertyID:propertyValue:context:reply:];
-[AVAudioSessionRemoteXPCClient getIOControllerPeriod:decoupledInput:reply:];
-[AVAudioSessionRemoteXPCClient allowAppToInitiatePlaybackTemporarilyFromBackground:reply:];
-[AVAudioSessionRemoteXPCClient handleRemoteInterruption:interruptionStatus:postInterruptionNotification:reply:];
```
