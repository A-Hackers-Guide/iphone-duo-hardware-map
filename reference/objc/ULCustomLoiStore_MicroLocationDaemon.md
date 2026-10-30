# `ULCustomLoiStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 9 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULCustomLoiStore MOClass];
+[ULCustomLoiStore defaultSortProperty];
+[ULCustomLoiStore maxEntriesInTable];
```

## Instance methods

```
-[ULCustomLoiStore fetchAllRecordsWithLimit:];
-[ULCustomLoiStore getAllCustomLoiIdsForServiceId:];
-[ULCustomLoiStore _fetchCustomLoisByAndPredicates:sortDescriptors:andLimit:];
-[ULCustomLoiStore addServiceToCustomLoiMapping:loiId:];
-[ULCustomLoiStore deleteOrphanRecords];
-[ULCustomLoiStore getAllDistinctCustomLoiIds];
-[ULCustomLoiStore getAllServicesEnabledAtCustomLoiId:];
-[ULCustomLoiStore insertDataObjects:forServiceUUID:atLoiUUID:];
-[ULCustomLoiStore removeServiceToCustomLoiMapping:loiId:];
```
