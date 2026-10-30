# `ULUWBMeasurementStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 5 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULUWBMeasurementStore MOClass];
+[ULUWBMeasurementStore defaultSortProperty];
+[ULUWBMeasurementStore maxEntriesInTable];
```

## Instance methods

```
-[ULUWBMeasurementStore fetchAllRecordsWithLimit:];
-[ULUWBMeasurementStore insertDataObjects:];
-[ULUWBMeasurementStore _fetchUWBMeasurementByAndPredicates:sortDescriptors:andLimit:];
-[ULUWBMeasurementStore deleteOrphanRecords];
-[ULUWBMeasurementStore hasUWBMeasurementsBetween:and:];
```
