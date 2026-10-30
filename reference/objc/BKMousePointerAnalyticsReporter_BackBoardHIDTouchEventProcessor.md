# `BKMousePointerAnalyticsReporter`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKMousePointerGlobalDevicePreferencesObserver`
- 4 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _analyticsReportingQueue;
@"NSCalendar" _gregorianCalendar;
@"BKMousePointerController" _mousePointerController;
d _lastReportedPeriodicTriggerTime;
```

## Properties

```
@property (T@"BKMousePointerController",&,N,V_mousePointerController) mousePointerController;
```

## Instance methods

```
-[BKMousePointerAnalyticsReporter init];
-[BKMousePointerAnalyticsReporter mousePointerGlobalDevicePreferencesDidChange:];
-[BKMousePointerAnalyticsReporter availableDevicesDidChange];
-[BKMousePointerAnalyticsReporter evaluatePeriodicReportingTrigger];
-[BKMousePointerAnalyticsReporter mousePointerController];
-[BKMousePointerAnalyticsReporter setMousePointerController:];
```
