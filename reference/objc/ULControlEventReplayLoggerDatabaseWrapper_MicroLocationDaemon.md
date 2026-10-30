# `ULControlEventReplayLoggerDatabaseWrapper`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP19MicroLocationDaemon41ULControlEventReplayLoggerDatabaseService_`
- 1 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{ULDatabaseStoreInterface=^^?} _dbStore;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ULControlEventReplayLoggerDatabaseWrapper dbStore];
-[ULControlEventReplayLoggerDatabaseWrapper initWithDatabaseStoreInterface:];
-[ULControlEventReplayLoggerDatabaseWrapper insertEventType:timestamp:];
-[ULControlEventReplayLoggerDatabaseWrapper insertEventType:timestamp:atLoiUUID:];
-[ULControlEventReplayLoggerDatabaseWrapper isStoreReady];
-[ULControlEventReplayLoggerDatabaseWrapper setDbStore:];
```
