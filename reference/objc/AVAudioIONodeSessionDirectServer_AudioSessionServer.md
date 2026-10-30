# `AVAudioIONodeSessionDirectServer`

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioIONodeSessionServer`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^v _sessionManager;
@"<AVAudioSessionServerDelegate>" _serverDelegate;
```

## Instance methods

```
-[AVAudioIONodeSessionDirectServer createIONodeWithSourceSession:sessionOwnerPID:playerType:error:];
-[AVAudioIONodeSessionDirectServer getPropertiesIONode:properties:status:error:];
-[AVAudioIONodeSessionDirectServer invalidateIONode:error:];
-[AVAudioIONodeSessionDirectServer reconfigureIONode:withSourceSession:sessionOwnerPID:playerType:error:];
-[AVAudioIONodeSessionDirectServer setIONode:playState:modes:error:];
-[AVAudioIONodeSessionDirectServer setPropertiesIONode:values:error:];
-[AVAudioIONodeSessionDirectServer initWithSessionManager:serverDelegate:];
```
