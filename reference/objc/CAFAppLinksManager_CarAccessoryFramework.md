# `CAFAppLinksManager`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFAppLinksClient`, `BSInvalidatable`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"CAFAppLinksSnapshot" _lastSnapshot;
@? _snapshotChangeBlock;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"BSServiceConnection" _connection;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"BSServiceConnection",&,N,V_connection) connection;
@property (T@"CAFAppLinksSnapshot",R,C,N,V_lastSnapshot) lastSnapshot;
@property (T@?,C,N,V_snapshotChangeBlock) snapshotChangeBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAFAppLinksManager setWorkQueue:];
-[CAFAppLinksManager workQueue];
-[CAFAppLinksManager lastSnapshot];
-[CAFAppLinksManager invalidate];
-[CAFAppLinksManager connection];
-[CAFAppLinksManager _setupConnection];
-[CAFAppLinksManager setConnection:];
-[CAFAppLinksManager _connectionInterrupted];
-[CAFAppLinksManager _connectionActivated];
-[CAFAppLinksManager _fetchSnapshot];
-[CAFAppLinksManager initWithChangeBlock:];
-[CAFAppLinksManager refreshAppLinksSnapshot];
-[CAFAppLinksManager setSnapshotChangeBlock:];
-[CAFAppLinksManager snapshotChangeBlock];
```
