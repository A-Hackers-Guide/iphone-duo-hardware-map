# `SessionManagerXPCProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SessionManagerXPCProtocol_iOS`
- 0 instance variables, 0 properties, 29 instance methods, 0 class methods

## Instance methods

```
-[SessionManagerXPCProtocol pingWithReply:];
-[SessionManagerXPCProtocol testWorkloopDispatch:sessionID:reply:];
-[SessionManagerXPCProtocol muteInputForRecordingProcesses:];
-[SessionManagerXPCProtocol getApplicationProperty:clientID:propertyID:isMXProperty:reply:];
-[SessionManagerXPCProtocol createSession:reply:];
-[SessionManagerXPCProtocol sessionIDs:clientID:reply:];
-[SessionManagerXPCProtocol getProperties:properties:genericMXPipe:reply:];
-[SessionManagerXPCProtocol activateSession:options:requestID:reply:];
-[SessionManagerXPCProtocol getEnhanceDialogueLevelWithReply:];
-[SessionManagerXPCProtocol deactivateSession:options:priority:requestID:reply:];
-[SessionManagerXPCProtocol createAudioApplicationForSpecification:reply:];
-[SessionManagerXPCProtocol setEnhanceDialoguePreference:reply:];
-[SessionManagerXPCProtocol getDeferredMessages:reply:];
-[SessionManagerXPCProtocol getMXPropertyGenericPipe:propertyName:reply:];
-[SessionManagerXPCProtocol getPropertiesForCache:reply:];
-[SessionManagerXPCProtocol removeMXNotificationListener:notificationName:reply:];
-[SessionManagerXPCProtocol getProperty:propertyName:MXProperty:reply:];
-[SessionManagerXPCProtocol setMXPropertyOnAllSessions:clientID:MXProperty:values:reply:];
-[SessionManagerXPCProtocol setApplicationProperty:clientID:propertyID:propertyValue:reply:];
-[SessionManagerXPCProtocol setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:];
-[SessionManagerXPCProtocol setIOProperties:values:reply:];
-[SessionManagerXPCProtocol setEnhanceDialogueLevel:reply:];
-[SessionManagerXPCProtocol toggleInputMuteForRecordingProcess:];
-[SessionManagerXPCProtocol addMXNotificationListener:notificationName:reply:];
-[SessionManagerXPCProtocol getDeferredMessagesForSessions:reply:];
-[SessionManagerXPCProtocol destroySession:reply:];
-[SessionManagerXPCProtocol getApplicationMessages:clientID:reply:];
-[SessionManagerXPCProtocol updateApplicationProperty:clientID:propertyID:propertyValue:context:reply:];
-[SessionManagerXPCProtocol allowAppToInitiatePlaybackTemporarilyFromBackground:reply:];
```
