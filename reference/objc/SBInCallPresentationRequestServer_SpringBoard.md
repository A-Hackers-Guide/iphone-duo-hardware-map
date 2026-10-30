# `SBInCallPresentationRequestServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSInCallPresentationClientToServerInterface`, `BSInvalidatable`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _targets;
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"BSServiceConnectionListener" _connectionListener;
@"NSObject<OS_dispatch_queue>" _queue;
@"<SBInCallPresentationRequestServerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBInCallPresentationRequestServerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInCallPresentationRequestServer listener:didReceiveConnection:withContext:];
-[SBInCallPresentationRequestServer init];
-[SBInCallPresentationRequestServer invalidate];
-[SBInCallPresentationRequestServer setDelegate:];
-[SBInCallPresentationRequestServer activate];
-[SBInCallPresentationRequestServer delegate];
-[SBInCallPresentationRequestServer presentWithConfiguration:completion:];
```
