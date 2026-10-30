# `CAFNowPlayingManager`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFNowPlayingClient`, `BSInvalidatable`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"CAFNowPlayingSnapshot" _lastSnapshot;
@? _snapshotObserver;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"BSServiceConnection" _connection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"BSServiceConnection",&,N,V_connection) connection;
@property (T@"CAFNowPlayingSnapshot",R,C,N,V_lastSnapshot) lastSnapshot;
@property (T@?,C,N,V_snapshotObserver) snapshotObserver;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFNowPlayingManager setWorkQueue:];
-[CAFNowPlayingManager workQueue];
-[CAFNowPlayingManager lastSnapshot];
-[CAFNowPlayingManager invalidate];
-[CAFNowPlayingManager connection];
-[CAFNowPlayingManager initWithObserver:];
-[CAFNowPlayingManager _setupConnection];
-[CAFNowPlayingManager setConnection:];
-[CAFNowPlayingManager _connectionInterrupted];
-[CAFNowPlayingManager setSnapshotObserver:];
-[CAFNowPlayingManager snapshotObserver];
-[CAFNowPlayingManager _connectionActivated];
-[CAFNowPlayingManager _fetchSnapshot];
-[CAFNowPlayingManager refreshNowPlayingSnapshot];
```
