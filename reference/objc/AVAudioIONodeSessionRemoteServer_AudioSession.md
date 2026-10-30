# `AVAudioIONodeSessionRemoteServer`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioIONodeSessionServer`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<std::recursive_mutex>="__ptr_"^{recursive_mutex}"__cntrl_"^{__shared_weak_count}} _mutex;
{shared_ptr<avas::client::XPCConnection>="__ptr_"^{XPCConnection}"__cntrl_"^{__shared_weak_count}} _xpcConnection;
```

## Instance methods

```
-[AVAudioIONodeSessionRemoteServer init];
-[AVAudioIONodeSessionRemoteServer createIONodeWithSourceSession:sessionOwnerPID:playerType:error:];
-[AVAudioIONodeSessionRemoteServer getPropertiesIONode:properties:status:error:];
-[AVAudioIONodeSessionRemoteServer invalidateIONode:error:];
-[AVAudioIONodeSessionRemoteServer reconfigureIONode:withSourceSession:sessionOwnerPID:playerType:error:];
-[AVAudioIONodeSessionRemoteServer setIONode:playState:modes:error:];
-[AVAudioIONodeSessionRemoteServer setPropertiesIONode:values:error:];
```
