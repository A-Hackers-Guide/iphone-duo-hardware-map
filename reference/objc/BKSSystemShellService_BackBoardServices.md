# `BKSSystemShellService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSSystemShellClientInterface`, `BKSSystemShellServiceConfiguration`
- 7 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"BSServiceConnection" _connection;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
d _idleSleepInterval;
B _waitForDataMigration;
B _configurationFinished;
@? _watchdogPingBlock;
Aq _checkInStatus;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",&,N) calloutQueue;
@property (T@?,C,N) collectiveWatchdogPingBlock;
@property (Td,N) idleSleepInterval;
@property (TB,N) waitForDataMigration;
```

## Instance methods

```
-[BKSSystemShellService setCalloutQueue:];
-[BKSSystemShellService calloutQueue];
-[BKSSystemShellService start];
-[BKSSystemShellService didFinishLaunching];
-[BKSSystemShellService setCollectiveWatchdogPingBlock:];
-[BKSSystemShellService collectiveWatchdogPing];
-[BKSSystemShellService collectiveWatchdogPingBlock];
-[BKSSystemShellService idleSleepInterval];
-[BKSSystemShellService initWithConfigurator:];
-[BKSSystemShellService restartWithOptions:];
-[BKSSystemShellService setIdleSleepInterval:];
-[BKSSystemShellService setIndependentWatchdogEnabled:];
-[BKSSystemShellService setWaitForDataMigration:];
-[BKSSystemShellService waitForDataMigration];
```
