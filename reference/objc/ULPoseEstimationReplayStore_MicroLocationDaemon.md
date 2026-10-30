# `ULPoseEstimationReplayStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 2 instance variables, 4 properties, 10 instance methods, 4 class methods

## Instance variables

```
{vector<ULPoseEstimationDO, std::allocator<ULPoseEstimationDO>>="__begin_"^{ULPoseEstimationDO}"__end_"^{ULPoseEstimationDO}""{?="__cap_"^{ULPoseEstimationDO}}} _buffer;
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
+[ULPoseEstimationReplayStore bufferMaxSize];
+[ULPoseEstimationReplayStore MOClass];
+[ULPoseEstimationReplayStore defaultSortProperty];
+[ULPoseEstimationReplayStore maxEntriesInTable];
```

## Instance methods

```
-[ULPoseEstimationReplayStore count];
-[ULPoseEstimationReplayStore deleteAllRecords];
-[ULPoseEstimationReplayStore deleteRecordsOlderThan:orNewerThan:];
-[ULPoseEstimationReplayStore efficientlyFetchPoseEstimationEntriesWithLOIGroupUUIDs:startDate:endDate:fetchLimit:newest:ascending:];
-[ULPoseEstimationReplayStore fetchAllPoseEstimationsWithLimit:];
-[ULPoseEstimationReplayStore flushStoreBuffer];
-[ULPoseEstimationReplayStore initWithDbStore:];
-[ULPoseEstimationReplayStore insertDataObjects:atLoiUUID:];
-[ULPoseEstimationReplayStore insertDataObjectsBuffered:atLoiUUID:];
-[ULPoseEstimationReplayStore isBufferingEnabled];
```
