# `CBPacketLoggerClient`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBActivatable`, `CBErrorReporting`, `CBInterruptable`
- 9 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _activateCalled;
B _invalidateCalled;
B _invalidateDone;
@"NSObject<OS_xpc_object>" _xpcCnx;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _errorHandler;
@? _interruptionHandler;
@? _invalidationHandler;
@? _rawPacketHandler;
```

## Properties

```
@property (T@?,C,N,V_rawPacketHandler) rawPacketHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
```

## Instance methods

```
-[CBPacketLoggerClient dispatchQueue];
-[CBPacketLoggerClient _ensureXPCStarted];
-[CBPacketLoggerClient activateWithCompletion:];
-[CBPacketLoggerClient setInvalidationHandler:];
-[CBPacketLoggerClient init];
-[CBPacketLoggerClient _xpcReceivedEvent:];
-[CBPacketLoggerClient interruptionHandler];
-[CBPacketLoggerClient setDispatchQueue:];
-[CBPacketLoggerClient invalidate];
-[CBPacketLoggerClient _interrupted];
-[CBPacketLoggerClient setInterruptionHandler:];
-[CBPacketLoggerClient _activateWithCompletion:];
-[CBPacketLoggerClient invalidationHandler];
-[CBPacketLoggerClient setErrorHandler:];
-[CBPacketLoggerClient _invalidated];
-[CBPacketLoggerClient errorHandler];
-[CBPacketLoggerClient _activateXPC:completion:];
-[CBPacketLoggerClient _xpcReceivedPacket:];
-[CBPacketLoggerClient rawPacketHandler];
-[CBPacketLoggerClient setRawPacketHandler:];
```
