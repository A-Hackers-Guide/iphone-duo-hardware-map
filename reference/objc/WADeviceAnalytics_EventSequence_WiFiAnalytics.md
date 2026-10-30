# `WADeviceAnalytics_EventSequence`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _asc;
@"NSDictionary" _startEvent;
@"NSDictionary" _endEvent;
@"NSArray" _events;
@"NSManagedObject" _startEventMO;
@"NSManagedObject" _endEventMO;
@"NSArray" _eventMOs;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_startEvent) startEvent;
@property (T@"NSDictionary",&,N,V_endEvent) endEvent;
@property (T@"NSArray",&,N,V_events) events;
@property (T@"NSManagedObject",&,N,V_startEventMO) startEventMO;
@property (T@"NSManagedObject",&,N,V_endEventMO) endEventMO;
@property (T@"NSArray",&,N,V_eventMOs) eventMOs;
@property (TB,N,V_asc) asc;
```

## Instance methods

```
-[WADeviceAnalytics_EventSequence endEvent];
-[WADeviceAnalytics_EventSequence setEvents:];
-[WADeviceAnalytics_EventSequence events];
-[WADeviceAnalytics_EventSequence setEndEvent:];
-[WADeviceAnalytics_EventSequence description];
-[WADeviceAnalytics_EventSequence startEvent];
-[WADeviceAnalytics_EventSequence setStartEvent:];
-[WADeviceAnalytics_EventSequence setAsc:];
-[WADeviceAnalytics_EventSequence asc];
-[WADeviceAnalytics_EventSequence endEventMO];
-[WADeviceAnalytics_EventSequence eventMOs];
-[WADeviceAnalytics_EventSequence initFromDictionaryWithStartRecord:endRecord:sequenceRecords:asc:];
-[WADeviceAnalytics_EventSequence initFromMOWithStartRecord:endRecord:sequenceRecords:asc:];
-[WADeviceAnalytics_EventSequence setEndEventMO:];
-[WADeviceAnalytics_EventSequence setEventMOs:];
-[WADeviceAnalytics_EventSequence setStartEventMO:];
-[WADeviceAnalytics_EventSequence startEventMO];
```
