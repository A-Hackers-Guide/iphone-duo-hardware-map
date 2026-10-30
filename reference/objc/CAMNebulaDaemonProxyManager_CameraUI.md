# `CAMNebulaDaemonProxyManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMNebulaDaemonClientProtocol`, `CAMNebulaDaemonProtocol`
- 4 instance variables, 8 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"<CAMNebulaDaemonTimelapseClientProtocol>" _timelapseClientDelegate;
@"NSObject<OS_dispatch_queue>" __queue;
@"NSXPCConnection" __connection;
q __connectionCount;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__queue) _queue;
@property (T@"NSXPCConnection",R,N,V__connection) _connection;
@property (Tq,R,N,V__connectionCount) _connectionCount;
@property (T@"<CAMNebulaDaemonTimelapseClientProtocol>",W,N,V_timelapseClientDelegate) timelapseClientDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMNebulaDaemonProxyManager _clientProtocolInterface];
+[CAMNebulaDaemonProxyManager _daemonProtocolInterface];
```

## Instance methods

```
-[CAMNebulaDaemonProxyManager _connection];
-[CAMNebulaDaemonProxyManager init];
-[CAMNebulaDaemonProxyManager forceStopTimelapseCaptureWithReasons:];
-[CAMNebulaDaemonProxyManager _queue];
-[CAMNebulaDaemonProxyManager _closeConnectionToDaemon];
-[CAMNebulaDaemonProxyManager _connectionCount];
-[CAMNebulaDaemonProxyManager _ensureConnectionToDaemon];
-[CAMNebulaDaemonProxyManager _getProxyForExecutingBlock:];
-[CAMNebulaDaemonProxyManager closeConnectionToDaemon];
-[CAMNebulaDaemonProxyManager ensureConnectionToDaemon];
-[CAMNebulaDaemonProxyManager finishCaptureForTimelapseWithUUID:];
-[CAMNebulaDaemonProxyManager performCrashRecoveryIfNeededForceEndLastTimelapseSession:];
-[CAMNebulaDaemonProxyManager pingAfterInterruption];
-[CAMNebulaDaemonProxyManager resumeTimelapseWithUUID:];
-[CAMNebulaDaemonProxyManager setTimelapseClientDelegate:];
-[CAMNebulaDaemonProxyManager startTimelapseWithUUID:];
-[CAMNebulaDaemonProxyManager stopTimelapseWithUUID:];
-[CAMNebulaDaemonProxyManager timelapseClientDelegate];
-[CAMNebulaDaemonProxyManager updatePendingWorkFromDiskForceEndLastSession:];
-[CAMNebulaDaemonProxyManager updateTimelapseWithUUID:];
```
