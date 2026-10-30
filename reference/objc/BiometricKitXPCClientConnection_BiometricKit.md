# `BiometricKitXPCClientConnection`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _deviceType;
@"NSXPCConnection" _xpcConnection;
B _invalidated;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _clients;
i _serverStartedNotificationToken;
```

## Properties

```
@property (T@"NSXPCConnection",R,N) xpcConnection;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
```

## Class methods

```
+[BiometricKitXPCClientConnection connectionWithDeviceType:];
```

## Instance methods

```
-[BiometricKitXPCClientConnection statusMessage:client:];
-[BiometricKitXPCClientConnection homeButtonPressed:];
-[BiometricKitXPCClientConnection statusMessage:details:client:];
-[BiometricKitXPCClientConnection removeClient:];
-[BiometricKitXPCClientConnection enrollUpdate:client:];
-[BiometricKitXPCClientConnection dealloc];
-[BiometricKitXPCClientConnection queue];
-[BiometricKitXPCClientConnection addClient:];
-[BiometricKitXPCClientConnection xpcConnection];
-[BiometricKitXPCClientConnection enrollResult:details:client:];
-[BiometricKitXPCClientConnection initWithDeviceType:];
-[BiometricKitXPCClientConnection templateUpdate:details:client:];
-[BiometricKitXPCClientConnection taskResumeStatus:client:];
-[BiometricKitXPCClientConnection client:];
-[BiometricKitXPCClientConnection touchIDButtonPressed:client:];
-[BiometricKitXPCClientConnection enrollFeedback:client:];
-[BiometricKitXPCClientConnection matchResult:details:client:];
```
