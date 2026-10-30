# `_SBExternalDisplayServiceClient`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnection" _connection;
@"BSProcessHandle" _remoteProcess;
```

## Properties

```
@property (T@"BSServiceConnection",R,N,V_connection) connection;
@property (T@"BSProcessHandle",R,N,V_remoteProcess) remoteProcess;
@property (Ti,R,N) pid;
@property (T@"BSAuditToken",R,N) auditToken;
```

## Instance methods

```
-[_SBExternalDisplayServiceClient initWithConnection:remoteProcess:];
-[_SBExternalDisplayServiceClient pid];
-[_SBExternalDisplayServiceClient connection];
-[_SBExternalDisplayServiceClient description];
-[_SBExternalDisplayServiceClient auditToken];
-[_SBExternalDisplayServiceClient remoteProcess];
```
