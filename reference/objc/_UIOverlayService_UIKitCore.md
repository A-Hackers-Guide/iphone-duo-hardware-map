# `_UIOverlayService`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIOverlayServiceServerToClientInterface`
- 3 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<_UIOverlayServiceDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnection<BSServiceConnectionClient>" _serviceConnection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_connectionQueue) connectionQueue;
@property (T@"BSServiceConnection<BSServiceConnectionClient>",&,N,V_serviceConnection) serviceConnection;
@property (T@"<_UIOverlayServiceDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIOverlayService setServiceConnection:];
-[_UIOverlayService connectionQueue];
-[_UIOverlayService serviceConnection];
-[_UIOverlayService setConnectionQueue:];
-[_UIOverlayService init];
-[_UIOverlayService dealloc];
-[_UIOverlayService setDelegate:];
-[_UIOverlayService delegate];
-[_UIOverlayService _asyncTargetWithHandler:];
-[_UIOverlayService _makeConnectionIfNecessaryWithConnectionHandler:];
-[_UIOverlayService performOverlayClientAction:];
-[_UIOverlayService prewarmConnection];
-[_UIOverlayService sendOverlayAction:];
```
