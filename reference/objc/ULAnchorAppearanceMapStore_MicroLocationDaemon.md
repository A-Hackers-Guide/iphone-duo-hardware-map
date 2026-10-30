# `ULAnchorAppearanceMapStore`

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
+[ULAnchorAppearanceMapStore MOClass];
+[ULAnchorAppearanceMapStore defaultSortProperty];
+[ULAnchorAppearanceMapStore maxEntriesInTable];
```

## Instance methods

```
-[ULAnchorAppearanceMapStore fetchAllRecordsWithLimit:];
-[ULAnchorAppearanceMapStore _fetchAnchorAppearanceMapByAndPredicates:sortDescriptors:andLimit:];
-[ULAnchorAppearanceMapStore deleteOrphanRecords];
-[ULAnchorAppearanceMapStore fetchMostRecentAnchorAppearanceMapAtLoiGroupId:];
-[ULAnchorAppearanceMapStore insertDataObjects:atLoiUUID:];
```
