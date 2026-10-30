# `DSDaemonProxy`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"SCSharingReminderPeerService" _daemonConnection;
@"NSMutableSet" _unreportedSignals;
```

## Properties

```
@property (T@"SCSharingReminderPeerService",&,N,V_daemonConnection) daemonConnection;
@property (T@"NSMutableSet",&,N,V_unreportedSignals) unreportedSignals;
@property (T@"NSArray",R,N) signalsToReport;
```

## Class methods

```
+[DSDaemonProxy initialize];
```

## Instance methods

```
-[DSDaemonProxy init];
-[DSDaemonProxy setDaemonConnection:];
-[DSDaemonProxy daemonConnection];
-[DSDaemonProxy signalsToReport];
-[DSDaemonProxy addSignalWithIdentifier:sharingType:signalType:];
-[DSDaemonProxy removeSignalWithIdentifier:sharingType:signalType:];
-[DSDaemonProxy sendAggregatedSignals];
-[DSDaemonProxy setUnreportedSignals:];
-[DSDaemonProxy unreportedSignals];
```
