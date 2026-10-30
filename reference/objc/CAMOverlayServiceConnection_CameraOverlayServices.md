# `CAMOverlayServiceConnection`

- Image: [`/System/Library/PrivateFrameworks/CameraOverlayServices.framework/CameraOverlayServices`](../userland/System__Library__PrivateFrameworks__CameraOverlayServices.framework__CameraOverlayServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMOverlayClientInterface`
- 10 instance variables, 14 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _focusLockGestureEnabled;
B __lastKnownOverlayVisibility;
B __lastKnownOverlayInterfaceReduced;
B __lastKnownFocusLocked;
@"<CAMOverlayServiceConnectionClient>" _client;
@"NSObject<OS_dispatch_queue>" _clientQueue;
Q _status;
@"BSServiceConnection" __serverConnection;
@"<CAMOverlayServerInterface>" __serverProxy;
@"NSObject<OS_dispatch_queue>" __connectionQueue;
```

## Properties

```
@property (TQ,N,S_setStatus:,V_status) status;
@property (T@"BSServiceConnection",&,N,S_setServerConnection:,V__serverConnection) _serverConnection;
@property (T@"<CAMOverlayServerInterface>",&,N,S_setServerProxy:,V__serverProxy) _serverProxy;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__connectionQueue) _connectionQueue;
@property (TB,N,S_setLastKnownOverlayVisibility:,V__lastKnownOverlayVisibility) _lastKnownOverlayVisibility;
@property (TB,N,S_setLastKnownOverlayInterfaceReduced:,V__lastKnownOverlayInterfaceReduced) _lastKnownOverlayInterfaceReduced;
@property (TB,N,S_setLastKnownFocusLocked:,V__lastKnownFocusLocked) _lastKnownFocusLocked;
@property (T@"<CAMOverlayServiceConnectionClient>",R,W,N,V_client) client;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_clientQueue) clientQueue;
@property (TB,N,V_focusLockGestureEnabled) focusLockGestureEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMOverlayServiceConnection clientQueue];
-[CAMOverlayServiceConnection serverDidChangeFocusLocked:];
-[CAMOverlayServiceConnection _handleInvalidatedConnection:];
-[CAMOverlayServiceConnection invalidateWithReason:];
-[CAMOverlayServiceConnection didChangeInterfaceReduced:];
-[CAMOverlayServiceConnection dealloc];
-[CAMOverlayServiceConnection status];
-[CAMOverlayServiceConnection focusLockGestureEnabled];
-[CAMOverlayServiceConnection _handleInterruptedConnection:];
-[CAMOverlayServiceConnection _lastKnownOverlayVisibility];
-[CAMOverlayServiceConnection _setServerProxy:];
-[CAMOverlayServiceConnection invalidate];
-[CAMOverlayServiceConnection _setLastKnownOverlayInterfaceReduced:];
-[CAMOverlayServiceConnection configureWithControls:initialUpdates:completion:];
-[CAMOverlayServiceConnection _serverConnection];
-[CAMOverlayServiceConnection _serverProxy];
-[CAMOverlayServiceConnection _connectionQueue];
-[CAMOverlayServiceConnection _setLastKnownFocusLocked:];
-[CAMOverlayServiceConnection _lastKnownOverlayInterfaceReduced];
-[CAMOverlayServiceConnection applyControlUpdate:completion:];
-[CAMOverlayServiceConnection serverDidChangeOverlayVisible:activeControlIdentifier:];
-[CAMOverlayServiceConnection serverDidChangeActiveControlIdentifier:];
-[CAMOverlayServiceConnection _lastKnownFocusLocked];
-[CAMOverlayServiceConnection _setServerConnection:];
-[CAMOverlayServiceConnection initWithClient:queue:];
-[CAMOverlayServiceConnection setFocusLockGestureEnabled:];
-[CAMOverlayServiceConnection serverDidUpdateControl:];
-[CAMOverlayServiceConnection _handleActivatedConnection:];
-[CAMOverlayServiceConnection _setStatus:];
-[CAMOverlayServiceConnection _updateStatusWithReason:];
-[CAMOverlayServiceConnection client];
-[CAMOverlayServiceConnection _setLastKnownOverlayVisibility:];
```
