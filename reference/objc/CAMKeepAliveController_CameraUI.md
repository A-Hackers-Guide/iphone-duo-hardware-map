# `CAMKeepAliveController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" __connection;
@"NSObject<OS_dispatch_queue>" __keepAliveQueue;
@"NSObject<OS_dispatch_source>" __heartbeatSource;
@"NSObject<OS_dispatch_queue>" __heartbeatQueue;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N,S_setConnection:,V__connection) _connection;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__keepAliveQueue) _keepAliveQueue;
@property (T@"NSObject<OS_dispatch_source>",&,N,S_setHeartbeatSource:,V__heartbeatSource) _heartbeatSource;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__heartbeatQueue) _heartbeatQueue;
```

## Instance methods

```
-[CAMKeepAliveController _keepAliveQueueTeardownConnection];
-[CAMKeepAliveController _teardownHeartbeat];
-[CAMKeepAliveController _handleApplicationWillEnterForeground:];
-[CAMKeepAliveController _keepAliveQueue];
-[CAMKeepAliveController _connection];
-[CAMKeepAliveController _setupConnectionIfNecessary];
-[CAMKeepAliveController _keepAliveQueueTeardownHeartbeat];
-[CAMKeepAliveController _handleHeartbeatConnectionReply:];
-[CAMKeepAliveController startKeepAliveSession];
-[CAMKeepAliveController init];
-[CAMKeepAliveController _setConnection:];
-[CAMKeepAliveController _handleApplicationDidEnterBackground:];
-[CAMKeepAliveController dealloc];
-[CAMKeepAliveController _heartbeatSource];
-[CAMKeepAliveController stopKeepAliveSession];
-[CAMKeepAliveController _handleHeartbeatSourceEvent];
-[CAMKeepAliveController _heartbeatQueue];
-[CAMKeepAliveController _teardownConnection];
-[CAMKeepAliveController _setHeartbeatSource:];
-[CAMKeepAliveController _keepAliveQueueCreateHeartbeatIfNecessary];
-[CAMKeepAliveController _keepAliveQueueCreateConnectionIfNecessary];
```
