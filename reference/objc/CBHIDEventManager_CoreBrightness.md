# `CBHIDEventManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 1 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _internalALSFilterHistory;
Q _internalALSFilterHistorySize;
@"NSMutableArray" _hidServiceClients;
@"HIDEventSystemClient" _hidSystemClient;
@"NSMutableArray" _clients;
@"NSMutableSet" _unfilteredClients;
@"NSMutableDictionary" _lastReportedALSEvents;
f _luxAbsoluteSensitivity;
f _luxSensitivity;
f _colorSensitivity;
@"NSMutableArray" _filters;
B _displayOn;
@"AABCHistograms" _analyticsIlluminanceHist;
q _analyticsPeriodicSender;
B _filtersSuspended;
```

## Properties

```
@property (TB,N,V_filtersSuspended) filtersSuspended;
```

## Instance methods

```
-[CBHIDEventManager copyPropertyForKey:];
-[CBHIDEventManager setProperty:forKey:];
-[CBHIDEventManager initWithQueue:];
-[CBHIDEventManager removeClient:];
-[CBHIDEventManager displayBrightnessFactorPropertyHandler:];
-[CBHIDEventManager stop];
-[CBHIDEventManager removeHIDService:];
-[CBHIDEventManager dealloc];
-[CBHIDEventManager start];
-[CBHIDEventManager addClient:];
-[CBHIDEventManager addFilters:];
-[CBHIDEventManager initWithQueue:identifier:];
-[CBHIDEventManager hidEventCallbackWithEvent:from:];
-[CBHIDEventManager addHIDService:];
-[CBHIDEventManager addUnfilteredClient:];
-[CBHIDEventManager crossedAbsoluteLuxThreshold:compareWith:];
-[CBHIDEventManager crossedRelativeColorThreshold:compareWith:];
-[CBHIDEventManager crossedRelativeLuxThreshold:compareWith:];
-[CBHIDEventManager filtersSuspended];
-[CBHIDEventManager forceDispatchEvents];
-[CBHIDEventManager initialiseHidEventSystemClient];
-[CBHIDEventManager removeFilters];
-[CBHIDEventManager setALSReportInterval:];
-[CBHIDEventManager setALSReportIntervalForService:displayState:];
-[CBHIDEventManager setFiltersSuspended:];
-[CBHIDEventManager setMedianFilterSize:];
-[CBHIDEventManager updateInternalMedianFilter:];
```
