# `ULEventLog`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{ULDatabaseStoreInterface=^^?} _dbStore;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Class methods

```
+[ULEventLog shared];
```

## Instance methods

```
-[ULEventLog init];
-[ULEventLog queue];
-[ULEventLog log:];
-[ULEventLog setQueue:];
-[ULEventLog disconnectFromDatabase];
-[ULEventLog dbStore];
-[ULEventLog connectToDatabase:];
-[ULEventLog printLogEventsSince:];
-[ULEventLog setDbStore:];
```
