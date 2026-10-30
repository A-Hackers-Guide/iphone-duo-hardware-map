# `BacklightdExportedObj`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BacklightdXPCProtocol`
- 7 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _clientID;
B _clientIDSet;
@"NSArray" _clientProps;
@"NSMutableDictionary" _transactions;
@"BrightnessSystemInternal" _server;
@"NSXPCConnection" _connection;
Q _responseState;
```

## Properties

```
@property (T@"BrightnessSystemInternal",N,V_server) server;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (TQ,V_responseState) responseState;
@property (TB,R) hasActiveSubscriptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BacklightdExportedObj reconnect];
-[BacklightdExportedObj clientID];
-[BacklightdExportedObj copyClientID];
-[BacklightdExportedObj setServer:];
-[BacklightdExportedObj hasActiveSubscriptions];
-[BacklightdExportedObj server];
-[BacklightdExportedObj wasDisconnected];
-[BacklightdExportedObj init];
-[BacklightdExportedObj setResponseState:];
-[BacklightdExportedObj clientSetSYNCPropertyWithKey:property:reply:];
-[BacklightdExportedObj dealloc];
-[BacklightdExportedObj clientSetPropertyWithKey:property:];
-[BacklightdExportedObj clientCopyPropertyWithKey:reply:];
-[BacklightdExportedObj notifyClientForProperty:key:origin:];
-[BacklightdExportedObj processKey:];
-[BacklightdExportedObj connection];
-[BacklightdExportedObj clientSetProperty:forKey:andHandle:];
-[BacklightdExportedObj setConnection:];
-[BacklightdExportedObj responseState];
-[BacklightdExportedObj clientSetProperty:forKey:andHandle:reply:];
-[BacklightdExportedObj clientCopyPropertyWithKey:andHandle:reply:];
-[BacklightdExportedObj registerNotificationForProperties:];
```
