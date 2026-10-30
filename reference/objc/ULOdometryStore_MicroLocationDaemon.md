# `ULOdometryStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 2 instance variables, 4 properties, 15 instance methods, 4 class methods

## Instance variables

```
{vector<ULOdometryDO, std::allocator<ULOdometryDO>>="__begin_"^{ULOdometryDO}"__end_"^{ULOdometryDO}""{?="__cap_"^{ULOdometryDO}}} _buffer;
{uuid="data"[16C]} _currentLocationId;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULOdometryStore bufferMaxSize];
+[ULOdometryStore MOClass];
+[ULOdometryStore defaultSortProperty];
+[ULOdometryStore maxEntriesInTable];
```

## Instance methods

```
-[ULOdometryStore count];
-[ULOdometryStore fetchAllRecordsWithLimit:];
-[ULOdometryStore deleteAllRecords];
-[ULOdometryStore deleteEntriesAfterTime:beforeTime:forLoiGroupUUID:odometrySource:];
-[ULOdometryStore deleteRecordsOlderThan:orNewerThan:];
-[ULOdometryStore efficientlyFetchOdometryEntriesWithLOIGroupUUIDs:odometrySource:startDate:endDate:fetchLimit:newest:ascending:];
-[ULOdometryStore fetchSessionTimesWithLOIGroupUUID:odometrySource:endDate:];
-[ULOdometryStore flushStoreBuffer];
-[ULOdometryStore getMostRecentOdometryTimeForLoiGroupId:odometrySource:];
-[ULOdometryStore initWithDbStore:];
-[ULOdometryStore insertDataObjects:atLoiUUID:];
-[ULOdometryStore insertDataObjectsBuffered:atLoiUUID:];
-[ULOdometryStore insertSessionBreakAtTime:odometrySource:atLoiUUID:];
-[ULOdometryStore isBufferingEnabled];
-[ULOdometryStore updateTrajectoryUUID:forOriginalUUID:fromTime:forLoiGroupUUID:odometrySource:];
```
