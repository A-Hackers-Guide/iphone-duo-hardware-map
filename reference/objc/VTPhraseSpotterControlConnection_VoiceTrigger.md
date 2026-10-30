# `VTPhraseSpotterControlConnection`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTPeerRemoteConnectionDelegate`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"VTPeerRemoteConnection" _peerConnection;
B _remotePhraseSpotterEnabled;
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
-[VTPhraseSpotterControlConnection init];
-[VTPhraseSpotterControlConnection notifyRemoteOfDismissal];
-[VTPhraseSpotterControlConnection notifyRemoteOfEarlyDetect];
-[VTPhraseSpotterControlConnection notifyRemoteOfTriggerEvent];
-[VTPhraseSpotterControlConnection remoteConnection:handleMessageType:completion:];
-[VTPhraseSpotterControlConnection updateRemotePhraseSpotterEnabled:];
```
