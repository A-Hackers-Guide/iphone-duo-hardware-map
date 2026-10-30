# `ASMCompanionServices`

- Image: [`/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`](../userland/System__Library__PrivateFrameworks__AccessorySensorManagerServices.framework__AccessorySensorManagerServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 4 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Class methods

```
+[ASMCompanionServices supportsSecureCoding];
```

## Instance methods

```
-[ASMCompanionServices clientID];
-[ASMCompanionServices dispatchQueue];
-[ASMCompanionServices _ensureXPCStarted];
-[ASMCompanionServices setClientID:];
-[ASMCompanionServices setInvalidationHandler:];
-[ASMCompanionServices init];
-[ASMCompanionServices interruptionHandler];
-[ASMCompanionServices setDispatchQueue:];
-[ASMCompanionServices invalidate];
-[ASMCompanionServices _interrupted];
-[ASMCompanionServices encodeWithCoder:];
-[ASMCompanionServices setInterruptionHandler:];
-[ASMCompanionServices description];
-[ASMCompanionServices initWithCoder:];
-[ASMCompanionServices invalidationHandler];
-[ASMCompanionServices _invalidated];
-[ASMCompanionServices forceStartWiFiAwareBrowser:];
-[ASMCompanionServices forceStartWiFiAwareListener:];
-[ASMCompanionServices setupDataPipeWithCompanionDevice:completion:];
-[ASMCompanionServices startWiFiAwarePublisherForHandoff:];
-[ASMCompanionServices startWiFiAwareSubscriberAndPairForHandoff:];
```
