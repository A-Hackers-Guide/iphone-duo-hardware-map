# `ULPeripheralOdometryReplayStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 2 instance variables, 4 properties, 10 instance methods, 4 class methods

## Instance variables

```
{vector<ULPeripheralOdometryDO, std::allocator<ULPeripheralOdometryDO>>="__begin_"^{ULPeripheralOdometryDO}"__end_"^{ULPeripheralOdometryDO}""{?="__cap_"^{ULPeripheralOdometryDO}}} _buffer;
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
+[ULPeripheralOdometryReplayStore bufferMaxSize];
+[ULPeripheralOdometryReplayStore MOClass];
+[ULPeripheralOdometryReplayStore defaultSortProperty];
+[ULPeripheralOdometryReplayStore maxEntriesInTable];
```

## Instance methods

```
-[ULPeripheralOdometryReplayStore count];
-[ULPeripheralOdometryReplayStore fetchAllRecordsWithLimit:];
-[ULPeripheralOdometryReplayStore deleteAllRecords];
-[ULPeripheralOdometryReplayStore deleteRecordsOlderThan:orNewerThan:];
-[ULPeripheralOdometryReplayStore efficientlyFetchAudioOdometryEntriesWithLOIGroupUUIDs:startDate:endDate:fetchLimit:newest:ascending:];
-[ULPeripheralOdometryReplayStore flushStoreBuffer];
-[ULPeripheralOdometryReplayStore initWithDbStore:];
-[ULPeripheralOdometryReplayStore insertDataObjects:atLoiUUID:];
-[ULPeripheralOdometryReplayStore insertDataObjectsBuffered:atLoiUUID:];
-[ULPeripheralOdometryReplayStore isBufferingEnabled];
```
