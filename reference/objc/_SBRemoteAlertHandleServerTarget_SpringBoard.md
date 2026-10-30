# `_SBRemoteAlertHandleServerTarget`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSRemoteAlertHandleServiceServerInterface`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnection" _connection;
@"<SBSRemoteAlertHandleServiceServerInterface>" _proxyInterface;
```

## Properties

```
@property (T@"BSServiceConnection",R,W,N,V_connection) connection;
@property (T@"<SBSRemoteAlertHandleServiceServerInterface>",W,N,V_proxyInterface) proxyInterface;
```

## Class methods

```
+[_SBRemoteAlertHandleServerTarget currentTarget];
```

## Instance methods

```
-[_SBRemoteAlertHandleServerTarget _performBlock:];
-[_SBRemoteAlertHandleServerTarget connection];
-[_SBRemoteAlertHandleServerTarget activateRemoteAlertHandleWithID:activationContext:];
-[_SBRemoteAlertHandleServerTarget createRemoteAlertHandleContextWithDefinition:configurationContext:];
-[_SBRemoteAlertHandleServerTarget invalidateRemoteAlertHandleWithID:];
-[_SBRemoteAlertHandleServerTarget remoteAlertHandleContextsForDefinition:allowsCreationValue:configurationContext:];
-[_SBRemoteAlertHandleServerTarget proxyInterface];
-[_SBRemoteAlertHandleServerTarget setProxyInterface:];
-[_SBRemoteAlertHandleServerTarget initWithConnection:proxyInterface:];
```
