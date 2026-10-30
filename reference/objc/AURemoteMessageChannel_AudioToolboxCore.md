# `AURemoteMessageChannel`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `AUAudioUnitMessageChannelProtocol`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<AUMessageChannel>" _messageChannel;
@"NSXPCListener" _listener;
@"NSXPCConnection" _xpcConnection;
@"AURemoteMessageChannel" _selfRetained;
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
-[AURemoteMessageChannel listener:shouldAcceptNewConnection:];
-[AURemoteMessageChannel endpoint];
-[AURemoteMessageChannel initWithMessageChannel:];
-[AURemoteMessageChannel onCallRemoteAU:reply:];
-[AURemoteMessageChannel releaseChannel];
-[AURemoteMessageChannel retainSelfIfRequired];
```
