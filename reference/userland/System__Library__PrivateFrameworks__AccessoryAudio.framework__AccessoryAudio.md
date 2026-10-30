# `/System/Library/PrivateFrameworks/AccessoryAudio.framework/AccessoryAudio`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 2 classes, 4 protocols, 51 methods, 16 properties

### Class pages

Every class and protocol, with its methods: [`ACCAudioClient`](../objc/ACCAudioClient_AccessoryAudio.md), [`ACCAudioClientProtocol`](../objc/ACCAudioClientProtocol_AccessoryAudio.protocol.md), [`ACCAudioManager`](../objc/ACCAudioManager_AccessoryAudio.md), [`ACCAudioXPCClientProtocol`](../objc/ACCAudioXPCClientProtocol_AccessoryAudio.protocol.md), [`ACCAudioXPCServerProtocol`](../objc/ACCAudioXPCServerProtocol_AccessoryAudio.protocol.md), [`NSObject`](../objc/NSObject_AccessoryAudio.protocol.md)

### Classes

`ACCAudioClient`, `ACCAudioManager`

### Protocols

`ACCAudioClientProtocol`, `ACCAudioXPCClientProtocol`, `ACCAudioXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCAudioXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"<ACCAudioClientProtocol>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"ACCAudioClient",&,N,V_audioClient) audioClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (55)

```
Connection
Endpoint
Transport
v12@?0B8
com.apple.accessories.audio.stateChanged
IAPAudioTransportUSBAudioStateKey
v12@?0i8
com.apple.accessories.audio.availability-changed
v16@?0@\"NSArray\"8
IAPAudioTransportLineoutStateKey
null
accessoryServer_isServerAvailableForServiceEntry
General
com.apple.accessories.signposts
IAPAudioTransportNameKey
v8@?0
com.apple.accessories.frameworks
com.apple.accessories.audio
v16@?0@\"NSError\"8
v12@?0I8
IAPAudioTransportLineinStateKey
<Undefined>
_SetupAvailabilityChangedHandlerForServiceEntry
Created log object %s: %s
Failed to create os_log_t object %s: %s!
no server connection when checking background audio state, won't allow background audio!
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
%s cannot get server state (%d, %s)
XPC connection error: %@
shouldStayConnected: %d
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
%s (%d)
XPC connection invalidated!
retValue: %d
inputRate: %d, supportedRate: %d
audioStates: %@
Created %d log object(s)!
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
%s (%d, %s)
%s did not register for notification (%d, %s), token (%d)
Connecting to XPC server...
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Server availability changed! State: %d
allowBackgroundAudioForClient reply: %d for client %@
Register AvailabilityChangedHandler (%d, %s)
Trying to connect to server...
XPC connection interrupted!
Unregister AvailabilityChangedHandler (%d, %s)
ACCAudioClient deallocated during server availability callback
ratesArray: %@
allowBackgroundAudio: %d for client %@
digitalAudioNotificationHandler FIRED!!
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Getting remote object...
```
