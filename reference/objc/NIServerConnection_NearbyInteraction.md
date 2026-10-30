# `NIServerConnection`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
Q _options;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_os_log>" _log;
@"NSUUID" _sessionID;
@ _exportedObject;
```

## Properties

```
@property (T@?,C) interruptionHandler;
@property (T@?,C) invalidationHandler;
@property (T@"NSUUID",R,V_sessionID) sessionID;
@property (T@,&,V_exportedObject) exportedObject;
```

## Class methods

```
+[NIServerConnection _internalBuildShouldDenyConnection];
+[NIServerConnection createOneShotConnectionAndResume:];
```

## Instance methods

```
-[NIServerConnection sessionID];
-[NIServerConnection setInvalidationHandler:];
-[NIServerConnection dealloc];
-[NIServerConnection synchronousRemoteObjectProxy];
-[NIServerConnection interruptionHandler];
-[NIServerConnection invalidate];
-[NIServerConnection exportedObject];
-[NIServerConnection setExportedObject:];
-[NIServerConnection setInterruptionHandler:];
-[NIServerConnection initWithSessionID:queue:exportedObject:options:];
-[NIServerConnection invalidationHandler];
-[NIServerConnection remoteObjectProxy];
-[NIServerConnection auditTokenForConnection];
-[NIServerConnection resume];
```
