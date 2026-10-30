# `_SBInCallPresentationRequestServerTarget`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSInCallPresentationClientToServerInterface`
- 3 instance variables, 7 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnection" _connection;
@"<SBSInCallPresentationClientToServerInterface>" _proxyInterface;
@"NSUUID" _clientIdentifier;
```

## Properties

```
@property (T@"BSServiceConnection",R,W,N,V_connection) connection;
@property (T@"<SBSInCallPresentationClientToServerInterface>",W,N,V_proxyInterface) proxyInterface;
@property (T@"NSUUID",R,C,N,V_clientIdentifier) clientIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBInCallPresentationRequestServerTarget currentTarget];
```

## Instance methods

```
-[_SBInCallPresentationRequestServerTarget clientIdentifier];
-[_SBInCallPresentationRequestServerTarget _performBlock:];
-[_SBInCallPresentationRequestServerTarget connection];
-[_SBInCallPresentationRequestServerTarget presentWithConfiguration:completion:];
-[_SBInCallPresentationRequestServerTarget proxyInterface];
-[_SBInCallPresentationRequestServerTarget setProxyInterface:];
-[_SBInCallPresentationRequestServerTarget initWithConnection:proxyInterface:];
```
