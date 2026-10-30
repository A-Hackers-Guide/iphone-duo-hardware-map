# `SBRemoteAppResizingSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppResizingSessionDelegate`
- 4 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBAppResizingSession" _resizingSession;
@"BSServiceConnection" _connection;
B _clientInvalidated;
@"<SBRemoteAppResizingSessionDelegate>" _delegate;
```

## Properties

```
@property (T@"BSServiceConnection",R,N,V_connection) connection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRemoteAppResizingSession dealloc];
-[SBRemoteAppResizingSession isValid];
-[SBRemoteAppResizingSession activate];
-[SBRemoteAppResizingSession connection];
-[SBRemoteAppResizingSession isActive];
-[SBRemoteAppResizingSession updatePreferredSize:forAssertionWithIdentifier:];
-[SBRemoteAppResizingSession initWithResizingSession:connection:delegate:];
-[SBRemoteAppResizingSession invalidateForClient];
-[SBRemoteAppResizingSession invalidateForServer];
-[SBRemoteAppResizingSession managesResizingSession:];
-[SBRemoteAppResizingSession resizingSession:canReceiveSceneHandle:];
-[SBRemoteAppResizingSession resizingSession:changedMinimumSize:maximumSize:];
-[SBRemoteAppResizingSession resizingSession:committedResolvedSize:];
-[SBRemoteAppResizingSession resizingSessionDidInvalidate:];
```
