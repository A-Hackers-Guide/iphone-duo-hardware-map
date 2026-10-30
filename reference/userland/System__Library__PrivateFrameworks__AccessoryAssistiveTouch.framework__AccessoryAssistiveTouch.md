# `/System/Library/PrivateFrameworks/AccessoryAssistiveTouch.framework/AccessoryAssistiveTouch`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 2 classes, 3 protocols, 53 methods, 12 properties

### Class pages

Every class and protocol, with its methods: [`ACCAssistiveTouchAccessory`](../objc/ACCAssistiveTouchAccessory_AccessoryAssistiveTouch.md), [`ACCAssistiveTouchProvider`](../objc/ACCAssistiveTouchProvider_AccessoryAssistiveTouch.md), [`ACCAssistiveTouchXPCClientProtocol`](../objc/ACCAssistiveTouchXPCClientProtocol_AccessoryAssistiveTouch.protocol.md), [`ACCAssistiveTouchXPCServerProtocol`](../objc/ACCAssistiveTouchXPCServerProtocol_AccessoryAssistiveTouch.protocol.md), [`NSObject`](../objc/NSObject_AccessoryAssistiveTouch.protocol.md)

### Classes

`ACCAssistiveTouchAccessory`, `ACCAssistiveTouchProvider`

### Protocols

`ACCAssistiveTouchXPCClientProtocol`, `ACCAssistiveTouchXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (TB,N,V_desiredAssistiveTouchState) desiredAssistiveTouchState;
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"<ACCAssistiveTouchProviderProtocol>",&,N,V_delegate) delegate;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCAssistiveTouchXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (TB,N,V_cachedState) cachedState;
```

## Strings (54)

```
com.apple.accessories.signposts
com.apple.accessories.assistivetouch.availability-changed
v12@?0B8
accessoryServer_isServerAvailableForServiceEntry
v16@?0@\"NSError\"8
null
_SetupAvailabilityChangedHandlerForServiceEntry
com.apple.accessories.frameworks
<Undefined>
General
Connection
Endpoint
com.apple.accessories.assistivetouch
v8@?0
Transport
v12@?0i8
%s did not register for notification (%d, %s), token (%d)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Created log object %s: %s
assistiveTouch Server availability changed! State: %d
assistiveTouch Trying to connect to server...
assistiveTouch Connecting to XPC server...
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
assistiveTouch XPC connection error!
accessoryAssistiveTouchAttached: accessory %@ (%@) already exists!
accessoryAssistiveTouchDetached: accessory %@ (%@) does not exist!
assistiveTouch setEnabled: accessory %@ (%@) does not exist! _accessories=%@
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
accessoryAssistiveTouchAttached: accessory %@ _accessories=%@
accessoryAssistiveTouchDetached: accessory %@, accessory=%@
assistiveTouch setEnabled: accessory %@, accessory=%@, flag=%d
assistiveTouch XPC connection interrupted!
%@
assistiveTouch setEnabled: accessory %@ (%@) does not exist!
assistiveTouch requestState: accessory %@, accessory=%@
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Register AvailabilityChangedHandler (%d, %s)
Failed to create os_log_t object %s: %s!
assistiveTouch Getting remote object...
%s (%d)
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Created %d log object(s)!
assistiveTouch XPC connection invalidated!
Unregister AvailabilityChangedHandler (%d, %s)
%s (%d, %s)
accessoryAssistiveTouchAttached: accessory %@, accessory=%@
assistiveTouch setEnabled: accessory %@ (%@) delegate does not respond to selector %@
assistiveTouch requestState: accessory %@ (%@) does not exist!
assistiveTouch shouldStayConnected: %d
accessoryAssistiveTouchDetached: accessory %@ _accessories=%@
accessoryAssistiveTouchDetachAll: detach %lu accessories!
assistiveTouch requestState: accessory %@ (%@) does not exist! _accessories=%@
%s cannot get server state (%d, %s)
```
