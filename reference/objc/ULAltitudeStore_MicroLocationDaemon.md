# `ULAltitudeStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 2 instance variables, 4 properties, 12 instance methods, 4 class methods

## Instance variables

```
{vector<ULAltitudeDO, std::allocator<ULAltitudeDO>>="__begin_"^{ULAltitudeDO}"__end_"^{ULAltitudeDO}""{?="__cap_"^{ULAltitudeDO}}} _buffer;
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
+[ULAltitudeStore bufferMaxSize];
+[ULAltitudeStore MOClass];
+[ULAltitudeStore defaultSortProperty];
+[ULAltitudeStore maxEntriesInTable];
```

## Instance methods

```
-[ULAltitudeStore count];
-[ULAltitudeStore fetchAllRecordsWithLimit:];
-[ULAltitudeStore fetchAltitudeEntriesWithStartDate:endDate:fetchLimit:ascending:];
-[ULAltitudeStore deleteAllRecords];
-[ULAltitudeStore deleteRecordsOlderThan:orNewerThan:];
-[ULAltitudeStore fetchAltitudeEntriesWithLOIGroupUUIDs:startDate:endDate:fetchLimit:ascending:];
-[ULAltitudeStore fetchAltitudeEntriesWithLoiUUID:startDate:endDate:fetchLimit:ascending:];
-[ULAltitudeStore flushStoreBuffer];
-[ULAltitudeStore initWithDbStore:];
-[ULAltitudeStore insertDataObjects:atLoiUUID:];
-[ULAltitudeStore insertDataObjectsBuffered:atLoiUUID:];
-[ULAltitudeStore isBufferingEnabled];
```
