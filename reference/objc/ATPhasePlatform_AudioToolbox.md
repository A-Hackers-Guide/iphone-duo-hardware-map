# `ATPhasePlatform`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PHASEPlatform`
- 4 instance variables, 11 properties, 31 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<Phase::ServerManager, std::default_delete<Phase::ServerManager>>=""{?="__ptr_"^{ServerManager}}} _serverManager;
@ _sessionInterface;
@ _tapInterface;
@ _roomCongruenceInterface;
```

## Properties

```
@property (T@"<PHASETapInterface>",R,N,V_tapInterface) tapInterface;
@property (Td,R,N) sampleRate;
@property (TB,R,N) running;
@property (TI,R,N) bufferFrameSize;
@property (T@"<PHASESessionInterface>",?,R,N) sessionInterface;
@property (T@"<PHASERoomCongruenceInterface>",?,R,N) roomCongruenceInterface;
@property (T@"OS_os_workgroup",?,R,N) workgroup;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ATPhasePlatform sampleRate];
-[ATPhasePlatform init];
-[ATPhasePlatform stop];
-[ATPhasePlatform dealloc];
-[ATPhasePlatform start];
-[ATPhasePlatform running];
-[ATPhasePlatform workgroup];
-[ATPhasePlatform lazyInitRoomCongruenceInterface];
-[ATPhasePlatform bufferFrameSize];
-[ATPhasePlatform muteSessionInput:mute:fadeTime:];
-[ATPhasePlatform activateSession:activate:];
-[ATPhasePlatform applyVolumeOnAllSessions];
-[ATPhasePlatform applyVolumeOnSession:];
-[ATPhasePlatform applyVolumeOnVolumeCategory:mode:value:];
-[ATPhasePlatform deviceLatencyInFramesForDirection:];
-[ATPhasePlatform enableIO:direction:];
-[ATPhasePlatform fadeClientsInSession:activating:fadeLevel:fadeTime:];
-[ATPhasePlatform lazyInitServerManager];
-[ATPhasePlatform lazyInitSessionInterface];
-[ATPhasePlatform muteAudioSessionBidirectional:mute:inputFadeTime:outputFadeTime:];
-[ATPhasePlatform numberOfStreamsForDirection:];
-[ATPhasePlatform refreshInputMuteOnAllSessions:];
-[ATPhasePlatform registerIOBlock:];
-[ATPhasePlatform registerOverloadNotification:];
-[ATPhasePlatform registerRouteChangeNotification:];
-[ATPhasePlatform registerTapInterface:];
-[ATPhasePlatform roomCongruenceInterface];
-[ATPhasePlatform sessionInterface];
-[ATPhasePlatform streamInfoForIndex:direction:];
-[ATPhasePlatform tapInterface];
-[ATPhasePlatform volumeScalarMappedToHWCurve:];
```
