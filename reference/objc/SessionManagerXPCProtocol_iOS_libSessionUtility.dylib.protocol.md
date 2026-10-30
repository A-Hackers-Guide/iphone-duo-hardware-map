# `SessionManagerXPCProtocol_iOS` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance methods

```
-[SessionManagerXPCProtocol_iOS getPropertiesIONode:properties:reply:];
-[SessionManagerXPCProtocol_iOS verifySessionExists:reply:];
-[SessionManagerXPCProtocol_iOS invalidateIONode:reply:];
-[SessionManagerXPCProtocol_iOS setSession:decoupledInput:hasIOEventListeners:reply:];
-[SessionManagerXPCProtocol_iOS setSessionPlayState:playState:playerType:playerRef:modes:reply:];
-[SessionManagerXPCProtocol_iOS setIONode:playState:modes:reply:];
-[SessionManagerXPCProtocol_iOS createProxySession:reply:];
-[SessionManagerXPCProtocol_iOS silenceOutput:options:reply:];
-[SessionManagerXPCProtocol_iOS setPropertiesIONode:values:reply:];
-[SessionManagerXPCProtocol_iOS getSpatialPreferencesForSession:contentType:reply:];
-[SessionManagerXPCProtocol_iOS getSpatialPreferencesForSession:reply:];
-[SessionManagerXPCProtocol_iOS createIONodeWithSourceSession:sessionOwnerPID:playerType:reply:];
-[SessionManagerXPCProtocol_iOS reconfigureIONode:withSourceSession:sessionOwnerPID:playerType:reply:];
-[SessionManagerXPCProtocol_iOS updateMicrophonePermission:clientToken:reply:];
-[SessionManagerXPCProtocol_iOS simulatePrimarySessionCreationInsideServerWithReply:];
-[SessionManagerXPCProtocol_iOS getIOControllerPeriod:decoupledInput:reply:];
-[SessionManagerXPCProtocol_iOS handleRemoteInterruption:interruptionStatus:postInterruptionNotification:reply:];
```
