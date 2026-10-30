# `BLSHFlipbookWatchdog`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SWSystemSleepObserver`
- 6 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"<BLSHSystemSleepMonitoring>" _sleepMonitor;
^{__IOReportSubscriptionCF=} _ioReportSubscription;
^{__CFDictionary=} _ioReportSubscribedChannels;
q _lastKnown_aodStatsFlipbookMiss;
B _alertsEnabled;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHFlipbookWatchdog systemSleepMonitorDidWakeFromSleep:];
-[BLSHFlipbookWatchdog dealloc];
-[BLSHFlipbookWatchdog _globalQueue_initializeDCPStats];
-[BLSHFlipbookWatchdog _globalQueue_refreshDCPStats:];
-[BLSHFlipbookWatchdog _mainQueue_alertFor1hzFlipbookFrameMiss:];
-[BLSHFlipbookWatchdog enableAlertsUsingDefaults];
-[BLSHFlipbookWatchdog initWithOSInterfaceProvider:];
```
