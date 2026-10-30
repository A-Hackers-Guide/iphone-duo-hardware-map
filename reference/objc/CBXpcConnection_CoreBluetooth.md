# `CBXpcConnection`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 1 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _eventQueue;
@"NSMutableDictionary" _options;
i _sessionType;
@"NSObject<OS_dispatch_queue>" _xpcQueue;
@"NSObject<OS_xpc_object>" _xpcConnection;
B _uiAppIsBackgrounded;
B _xpcConnectionConnected;
@? _whbReplyHandler;
@"NSMutableDictionary" _whbRemoteToLocalUuidMap;
@"<CBXpcConnectionDelegate>" _delegate;
```

## Properties

```
@property (T@"<CBXpcConnectionDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CBXpcConnection connect];
-[CBXpcConnection setTargetQueue:];
-[CBXpcConnection _handleFinalized];
-[CBXpcConnection _checkOut];
-[CBXpcConnection removeWhbRemoteId:];
-[CBXpcConnection sendSyncMsg:args:];
-[CBXpcConnection getWhbLocalIdForRemoteId:];
-[CBXpcConnection initWithDelegate:queue:options:sessionType:];
-[CBXpcConnection setWhbLocalId:forRemoteId:];
-[CBXpcConnection didReceiveForwardedDelegateCallbackMessage:];
-[CBXpcConnection sendMsg:args:];
-[CBXpcConnection forwardWhbMsg:args:cnx:];
-[CBXpcConnection _handleReset];
-[CBXpcConnection didReceiveForwardedMessage:];
-[CBXpcConnection _handleInvalid];
-[CBXpcConnection disconnect];
-[CBXpcConnection setDelegate:];
-[CBXpcConnection _nameForMessage:];
-[CBXpcConnection sendMsgWithReply:args:replyBlock:];
-[CBXpcConnection _sendBarrier];
-[CBXpcConnection getEventQueue];
-[CBXpcConnection delegate];
-[CBXpcConnection _applicationDidEnterBackgroundNotification];
-[CBXpcConnection _checkIn];
-[CBXpcConnection _applicationWillEnterForegroundNotification];
-[CBXpcConnection _allocXpcMsg:args:];
-[CBXpcConnection setWhbReplyHandler:];
-[CBXpcConnection _handleConnectionEvent:];
-[CBXpcConnection _handleMsg:];
```
