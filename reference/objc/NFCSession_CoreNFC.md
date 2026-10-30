# `NFCSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSLock" _connectionLock;
@"NSXPCConnection" _connection;
q _connectionID;
@"NSObject<OS_dispatch_queue>" _xpcQueue;
@"NSXPCInterface" _remoteObjectInterface;
@"NSXPCInterface" _exportedObjectInterface;
@"NSString" _machServiceName;
@ _exportedObject;
@"<NFCSessionCallbacks>" _delegate;
```

## Instance methods

```
-[NFCSession _connection];
-[NFCSession _invalidate];
-[NFCSession dealloc];
-[NFCSession synchronousRemoteObjectProxyWithErrorHandler:];
-[NFCSession remoteObjectProxyWithErrorHandler:];
-[NFCSession _connectIfNeeded];
-[NFCSession _connectionLock];
-[NFCSession _exportedObjectClassName];
-[NFCSession initWithMachServiceName:remoteObjectInterface:exportedObjectInterface:exportedObject:delegate:];
```
