# `ULConfigurationStore`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULStore`
- Protocols: `ULStoreProtocol`
- 0 instance variables, 4 properties, 11 instance methods, 3 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULConfigurationStore MOClass];
+[ULConfigurationStore defaultSortProperty];
+[ULConfigurationStore maxEntriesInTable];
```

## Instance methods

```
-[ULConfigurationStore fetchAllRecordsWithLimit:];
-[ULConfigurationStore insertDataObjects:];
-[ULConfigurationStore _fetchConfigurationsByAndPredicates:sortDescriptors:andLimit:];
-[ULConfigurationStore batchTransferRecordsUsingBatchSize:andLimit:intoTargetStore:];
-[ULConfigurationStore fetchAllConfigurationsOfType:loiGroupId:withLimit:];
-[ULConfigurationStore fetchAllConfigurationsforLoiGroup:withLimit:];
-[ULConfigurationStore fetchLatestConfigurationPerTypeAtLoi:withLimit:];
-[ULConfigurationStore fetchMostRecentAnchorAppearancesAtLoi:];
-[ULConfigurationStore fetchMostRecentConfiguration:atLoiGroupId:beforeTime:];
-[ULConfigurationStore fetchMostRecentConfiguration:atLoiType:loiGroupId:beforeTime:];
-[ULConfigurationStore fetchMostRecentWifiChannelHistogramAtLoi:];
```
