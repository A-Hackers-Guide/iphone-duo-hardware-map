# `_SBKeyboardServiceConnectionListener`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSKeyboardFocusServiceClientToServerInterface`, `BSServiceConnectionListenerDelegate`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _connectionContextToClientMap;
@"FBServiceClientAuthenticator" _serviceClientAuthenticator;
@"NSObject<OS_dispatch_queue>" _serviceQueue;
@"BSServiceConnectionListener" _connectionListener;
@"<_SBKeyboardServiceConnectionListenerDelegate>" _delegate;
```

## Properties

```
@property (T@"<_SBKeyboardServiceConnectionListenerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBKeyboardServiceConnectionListener listener:didReceiveConnection:withContext:];
-[_SBKeyboardServiceConnectionListener invalidate];
-[_SBKeyboardServiceConnectionListener setDelegate:];
-[_SBKeyboardServiceConnectionListener activate];
-[_SBKeyboardServiceConnectionListener delegate];
-[_SBKeyboardServiceConnectionListener setExternalSceneIdentities:];
-[_SBKeyboardServiceConnectionListener deferAdditionalEnvironments:whenSceneHasKeyboardFocus:pid:];
-[_SBKeyboardServiceConnectionListener removeKeyboardFocusFromSceneIdentity:pid:];
-[_SBKeyboardServiceConnectionListener requestKeyboardFocusForSceneIdentity:pid:completion:];
-[_SBKeyboardServiceConnectionListener stopApplyingAdditionalDeferringRulesWhenSceneHasKeyboardFocus:pid:];
-[_SBKeyboardServiceConnectionListener _clientForConnectionContext:];
-[_SBKeyboardServiceConnectionListener _handleDisconnectForServiceConnection:];
-[_SBKeyboardServiceConnectionListener _removeClientForConnectionContext:];
-[_SBKeyboardServiceConnectionListener initWithServiceQueue:];
```
