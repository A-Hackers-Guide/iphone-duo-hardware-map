# `ULServiceStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 18 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULServiceStore MOClass];
+[ULServiceStore defaultSortProperty];
+[ULServiceStore maxEntriesInTable];
```

## Instance methods

```
-[ULServiceStore fetchServiceManagedObjectWithUUID:withManagedObjectContext:];
-[ULServiceStore updateLastActiveTime:forService:];
-[ULServiceStore updateServiceLocationTypes:withLocationTypes:];
-[ULServiceStore updateAllServicesWithMatchingServiceUUID:withNewServiceUUID:];
-[ULServiceStore _fetchServicesByAndPredicates:sortDescriptors:andLimit:];
-[ULServiceStore updateService:withServiceType:toNewServiceType:];
-[ULServiceStore fetchAllRecordsWithLimit:];
-[ULServiceStore fetchAllServicesForClientId:andUserId:];
-[ULServiceStore fetchAllServicesForServiceType:onlyServicesWithLabels:];
-[ULServiceStore deleteAllServicesWithExceptions:];
-[ULServiceStore getAllServiceUUIDs:];
-[ULServiceStore insertDataObjects:];
-[ULServiceStore deleteServiceForUUID:];
-[ULServiceStore fetchServiceByUUID:];
-[ULServiceStore getServiceUUIDsWithServiceType:];
-[ULServiceStore updateAllServicesWithMatchingClientId:withNewClientId:];
-[ULServiceStore deleteOldestsServicesPerClientAboveMaxCount];
-[ULServiceStore deleteAllServicesWithUUIDs:];
```
