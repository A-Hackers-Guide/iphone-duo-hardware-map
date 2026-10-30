# `_SBExternalDisplayServiceConnectionListener`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSExternalDisplayServiceClientToServerInterface`, `BSServiceConnectionListenerDelegate`
- 6 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMapTable" _lock_connectionToClientMap;
@"FBServiceClientAuthenticator" _serviceClientAuthenticator;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
@"BSServiceConnectionListener" _connectionListener;
@"<_SBExternalDisplayServiceConnectionListenerDelegate>" _delegate;
```

## Properties

```
@property (T@"<_SBExternalDisplayServiceConnectionListenerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBExternalDisplayServiceConnectionListener listener:didReceiveConnection:withContext:];
-[_SBExternalDisplayServiceConnectionListener invalidate];
-[_SBExternalDisplayServiceConnectionListener setDelegate:];
-[_SBExternalDisplayServiceConnectionListener activate];
-[_SBExternalDisplayServiceConnectionListener delegate];
-[_SBExternalDisplayServiceConnectionListener getConnectedDisplayInfoWithCompletion:];
-[_SBExternalDisplayServiceConnectionListener setDisplayArrangement:forDisplay:];
-[_SBExternalDisplayServiceConnectionListener setDisplayMirroringEnabled:forDisplay:];
-[_SBExternalDisplayServiceConnectionListener setDisplayModeSettings:forDisplay:options:completionHandler:];
-[_SBExternalDisplayServiceConnectionListener _clientForConnection:];
-[_SBExternalDisplayServiceConnectionListener _createClientForConnection:];
-[_SBExternalDisplayServiceConnectionListener _handleDisconnectForServiceConnection:];
-[_SBExternalDisplayServiceConnectionListener _removeClientForConnection:];
-[_SBExternalDisplayServiceConnectionListener initWithServiceQueue:];
-[_SBExternalDisplayServiceConnectionListener notifyObserversExternalDisplayDidConnect:];
-[_SBExternalDisplayServiceConnectionListener notifyObserversExternalDisplayDidUpdateProperties:requestingClient:];
-[_SBExternalDisplayServiceConnectionListener notifyObserversExternalDisplayWillDisconnect:];
```
