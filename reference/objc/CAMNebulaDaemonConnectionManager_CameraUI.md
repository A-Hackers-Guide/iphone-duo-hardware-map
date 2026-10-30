# `CAMNebulaDaemonConnectionManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCConnectionDelegate`, `CAMNebulaDaemonClientProtocol`, `CAMNebulaDaemonBundleIdentifierProtocol`
- 10 instance variables, 14 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"<CAMNebulaDaemonConnectionManagerDelegate>" _delegate;
@"NSString" _clientAccess;
@"Protocol" _allowedProtocol;
@"NSString" _bundleIdentifier;
@"NSXPCConnection" __connection;
@"NSString" __name;
@"NSObject<OS_dispatch_queue>" __queue;
@"NSMutableDictionary" __tasksPerIdentifier;
@"NSMutableArray" __registeredTargets;
@"NSMutableArray" __registeredProtocols;
```

## Properties

```
@property (T@"NSXPCConnection",R,N,V__connection) _connection;
@property (T@"NSString",R,C,N,V__name) _name;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__queue) _queue;
@property (T@"NSMutableDictionary",R,N,V__tasksPerIdentifier) _tasksPerIdentifier;
@property (T@"NSMutableArray",R,N,V__registeredTargets) _registeredTargets;
@property (T@"NSMutableArray",R,N,V__registeredProtocols) _registeredProtocols;
@property (T@"<CAMNebulaDaemonConnectionManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_clientAccess) clientAccess;
@property (T@"Protocol",R,C,N,V_allowedProtocol) allowedProtocol;
@property (T@"NSString",R,C,N,V_bundleIdentifier) bundleIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMNebulaDaemonConnectionManager _clientProtocolInterface];
+[CAMNebulaDaemonConnectionManager _daemonProtocolInterface];
```

## Instance methods

```
-[CAMNebulaDaemonConnectionManager _connection];
-[CAMNebulaDaemonConnectionManager _name];
-[CAMNebulaDaemonConnectionManager connection:handleInvocation:isReply:];
-[CAMNebulaDaemonConnectionManager forceStopTimelapseCaptureWithReasons:];
-[CAMNebulaDaemonConnectionManager bundleIdentifier];
-[CAMNebulaDaemonConnectionManager setDelegate:];
-[CAMNebulaDaemonConnectionManager _queue];
-[CAMNebulaDaemonConnectionManager delegate];
-[CAMNebulaDaemonConnectionManager description];
-[CAMNebulaDaemonConnectionManager allowedProtocol];
-[CAMNebulaDaemonConnectionManager _getProxyForExecutingBlock:];
-[CAMNebulaDaemonConnectionManager _registeredProtocols];
-[CAMNebulaDaemonConnectionManager _registeredTargets];
-[CAMNebulaDaemonConnectionManager _targetsForSelector:];
-[CAMNebulaDaemonConnectionManager _tasksPerIdentifier];
-[CAMNebulaDaemonConnectionManager addTarget:forProtocol:];
-[CAMNebulaDaemonConnectionManager clientAccess];
-[CAMNebulaDaemonConnectionManager initWithConnection:name:bundleIdentifier:queue:clientAccess:allowedProtocol:];
-[CAMNebulaDaemonConnectionManager pingAfterInterruption];
```
