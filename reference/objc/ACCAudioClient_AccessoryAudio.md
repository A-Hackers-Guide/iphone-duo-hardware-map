# `ACCAudioClient`

- Image: [`/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio`](../userland/System__Library__PrivateFrameworks__AccessoryAudio.framework__AccessoryAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCAudioXPCClientProtocol`
- 3 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<ACCAudioClientProtocol>" _delegate;
@"NSXPCConnection" _serverConnection;
@"<ACCAudioXPCServerProtocol>" _remoteObject;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCAudioXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"<ACCAudioClientProtocol>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ACCAudioClient initWithDelegate:];
-[ACCAudioClient connectToServer];
-[ACCAudioClient setRemoteObject:];
-[ACCAudioClient serverConnection];
-[ACCAudioClient dealloc];
-[ACCAudioClient remoteObject];
-[ACCAudioClient setDelegate:];
-[ACCAudioClient delegate];
-[ACCAudioClient setServerConnection:];
-[ACCAudioClient allowBackgroundAudioForClient:];
-[ACCAudioClient deviceAudioStates];
-[ACCAudioClient registerForAccessoryDigitalAudioNotifications];
-[ACCAudioClient setDigitalAudioSampleRate:];
-[ACCAudioClient supportedDigitalAudioSampleRate:];
-[ACCAudioClient supportedDigitalAudioSampleRates];
-[ACCAudioClient unregisterForAccessoryDigitalAudioNotifications];
```
