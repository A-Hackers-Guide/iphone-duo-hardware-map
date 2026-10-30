# `SAReplay`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogPersistenceDelegate`, `OSActivityStreamDelegate`, `OSDeviceDelegate`
- 10 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SAService" _service;
@"OSLogPersistence" _persistence;
@"OSActivityStream" _stream;
@"NSObject<OS_dispatch_semaphore>" _persistenceWait;
@"NSObject<OS_dispatch_semaphore>" _streamWait;
@"NSURL" _outputPath;
@"NSURL" _inputPersistencePath;
@"SAAnalytics" _analytics;
@"NSMutableDictionary" _eventMessages;
@"NSMutableArray" _eventOrder;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_eventMessages) eventMessages;
@property (T@"NSMutableArray",&,N,V_eventOrder) eventOrder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SAReplay streamDidStart:];
-[SAReplay streamDidStop:];
-[SAReplay activityStream:deviceUDID:deviceID:status:error:];
-[SAReplay activityStream:results:];
-[SAReplay persistence:results:error:];
-[SAReplay persistenceDidFinishReadingForStartDate:endDate:];
-[SAReplay streamDidFail:error:];
-[SAReplay eventMessages];
-[SAReplay eventOrder];
-[SAReplay initWithLogArchive:outputPath:inputPersistencePath:];
-[SAReplay replaySingleEventLogString:];
-[SAReplay replayWithStartDate:endDate:];
-[SAReplay setEventMessages:];
-[SAReplay setEventOrder:];
```
