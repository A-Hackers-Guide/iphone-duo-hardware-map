# `ASMPeripheralControlServices`

- Image: [`/System/Library/PrivateFrameworks/AccessorySensorManagerServices.framework/AccessorySensorManagerServices`](../userland/System__Library__PrivateFrameworks__AccessorySensorManagerServices.framework__AccessorySensorManagerServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 4 properties, 18 instance methods, 1 class methods

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
+[ASMPeripheralControlServices supportsSecureCoding];
```

## Instance methods

```
-[ASMPeripheralControlServices clientID];
-[ASMPeripheralControlServices dispatchQueue];
-[ASMPeripheralControlServices _ensureXPCStarted];
-[ASMPeripheralControlServices setClientID:];
-[ASMPeripheralControlServices setInvalidationHandler:];
-[ASMPeripheralControlServices init];
-[ASMPeripheralControlServices interruptionHandler];
-[ASMPeripheralControlServices setDispatchQueue:];
-[ASMPeripheralControlServices invalidate];
-[ASMPeripheralControlServices _interrupted];
-[ASMPeripheralControlServices encodeWithCoder:];
-[ASMPeripheralControlServices setInterruptionHandler:];
-[ASMPeripheralControlServices description];
-[ASMPeripheralControlServices initWithCoder:];
-[ASMPeripheralControlServices invalidationHandler];
-[ASMPeripheralControlServices _invalidated];
-[ASMPeripheralControlServices modifyPeripheralConfiguration:identifier:completion:];
-[ASMPeripheralControlServices writeWithData:characteristic:identifier:completion:];
```
