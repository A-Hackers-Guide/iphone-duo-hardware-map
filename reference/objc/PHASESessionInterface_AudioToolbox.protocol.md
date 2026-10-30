# `PHASESessionInterface` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"<PHASESessionVolumeInterface>",?,R,N) sessionVolumeInterface;
```

## Instance methods

```
-[PHASESessionInterface setClientStateOnSession:clientToken:modes:state:outDuckingInfo:];
-[PHASESessionInterface setClientStateFromCallbackOnSession:clientToken:modes:state:outDuckingInfo:];
-[PHASESessionInterface getInputMuteStateForSession:fromCallback:];
-[PHASESessionInterface registerActivateAudioSessionBlock:];
-[PHASESessionInterface registerFadeClientsInAudioSessionBlock:];
-[PHASESessionInterface registerMuteInputClientsInAudioSessionBlock:];
-[PHASESessionInterface sessionVolumeInterface];
-[PHASESessionInterface setInputMuteStateFromCallbackOnSession:clientToken:isMuted:];
-[PHASESessionInterface setInputMuteStateOnSession:clientToken:isMuted:];
```
