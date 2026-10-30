# `BKSSystemShellServiceConfiguration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N) calloutQueue;
@property (T@?,C,N) collectiveWatchdogPingBlock;
@property (Td,N) idleSleepInterval;
@property (TB,N) waitForDataMigration;
```

## Instance methods

```
-[BKSSystemShellServiceConfiguration setCalloutQueue:];
-[BKSSystemShellServiceConfiguration calloutQueue];
-[BKSSystemShellServiceConfiguration setCollectiveWatchdogPingBlock:];
-[BKSSystemShellServiceConfiguration collectiveWatchdogPingBlock];
-[BKSSystemShellServiceConfiguration idleSleepInterval];
-[BKSSystemShellServiceConfiguration setIdleSleepInterval:];
-[BKSSystemShellServiceConfiguration setWaitForDataMigration:];
-[BKSSystemShellServiceConfiguration waitForDataMigration];
```
