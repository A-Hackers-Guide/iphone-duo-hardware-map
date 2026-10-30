# `/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 3 protocols, 50 methods, 13 properties

### Class pages

Every class and protocol, with its methods: [`AccessoryHIDClient`](../objc/AccessoryHIDClient_AccessoryHID.md), [`AccessoryHIDXPCClientProtocol`](../objc/AccessoryHIDXPCClientProtocol_AccessoryHID.protocol.md), [`AccessoryHIDXPCServerProtocol`](../objc/AccessoryHIDXPCServerProtocol_AccessoryHID.protocol.md), [`NSObject`](../objc/NSObject_AccessoryHID.protocol.md)

### Classes

`AccessoryHIDClient`

### Protocols

`AccessoryHIDXPCClientProtocol`, `AccessoryHIDXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<AccessoryHIDXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,V_registeredHIDDescriptors) registeredHIDDescriptors;
@property (T@"NSLock",&,N,V_registeredHIDDescriptorsLock) registeredHIDDescriptorsLock;
@property (T@"<AccessoryHIDClientProtocol>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (51)

```
Created %d log object(s)!
Server availability changed! State: %d
Getting remote object...
getReport result: %d
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Register AvailabilityChangedHandler (%d, %s)
Unregister AvailabilityChangedHandler (%d, %s)
%s cannot get server state (%d, %s)
Trying to connect to server...
shouldStayConnected: %d
%s (%d, %s)
%s did not register for notification (%d, %s), token (%d)
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Created log object %s: %s
Failed to create os_log_t object %s: %s!
Connecting to XPC server...
XPC connection error: %@
sendOutReport result: %d
componentUpdate result: %d
%s (%d)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
XPC connection invalidated!
XPC connection interrupted!
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
ReportType
com.apple.accessories.signposts
General
Transport
Enabled
accessoryServer_isServerAvailableForServiceEntry
v12@?0i8
<Undefined>
v12@?0B8
Report
ReportID
HIDComponentType
HIDServiceRegistryEntryID
_SetupAvailabilityChangedHandlerForServiceEntry
Connection
Endpoint
com.apple.accessories.hid.availability-changed
com.apple.accessories.hid
v16@?0@\"NSError\"8
HIDComponentID
v8@?0
ComponentID
HIDFunctionType
com.apple.accessories.frameworks
null
```
