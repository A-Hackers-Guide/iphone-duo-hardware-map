# `SRResearchDataPerCategoryViewController`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- Protocols: `SRAuthorizationCellDelegate`, `SRSensorReaderDelegate`, `SRSensorPrunerDelegate`
- 18 instance variables, 22 properties, 65 instance methods, 1 class methods

## Instance variables

```
@"SRAuthorizationGroup" _authGroup;
@"SRAuthorizationStore" _authStore;
@"NSMutableSet" _authorizedBundleIds;
@"NSMutableSet" _authorizedWriterBundleIds;
@"NSArray" _appBundles;
@"NSArray" _writerAppBundles;
@"NSSet" _sensorIdentifiers;
@"NSMutableArray" _readers;
@"NSMutableArray" _pruners;
d _start;
d _end;
@"NSObject<OS_dispatch_group>" _fetchGroup;
@"NSMutableArray" _tombstones;
q _numberOfDays;
@? _cancelExportBlock;
q _datastoreBackend;
@"NSURL" _exportedDataURL;
q _sb_handle;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_authorizedBundleIds) authorizedBundleIds;
@property (T@"NSMutableSet",&,N,V_authorizedWriterBundleIds) authorizedWriterBundleIds;
@property (T@"NSArray",&,N,V_appBundles) appBundles;
@property (T@"NSArray",&,N,V_writerAppBundles) writerAppBundles;
@property (T@"NSSet",&,N,V_sensorIdentifiers) sensorIdentifiers;
@property (T@"NSMutableArray",&,N,V_readers) readers;
@property (T@"NSMutableArray",&,N,V_pruners) pruners;
@property (Td,N,V_start) start;
@property (Td,N,V_end) end;
@property (T@"NSObject<OS_dispatch_group>",&,N,V_fetchGroup) fetchGroup;
@property (T@"NSMutableArray",&,N,V_tombstones) tombstones;
@property (Tq,N,V_numberOfDays) numberOfDays;
@property (T@?,C,V_cancelExportBlock) cancelExportBlock;
@property (Tq,N,V_datastoreBackend) datastoreBackend;
@property (T@"NSURL",&,N,V_exportedDataURL) exportedDataURL;
@property (Tq,N,V_sb_handle) sb_handle;
@property (T@"SRAuthorizationGroup",&,N,V_authGroup) authGroup;
@property (T@"SRAuthorizationStore",&,V_authStore) authStore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRResearchDataPerCategoryViewController initialize];
```

## Instance methods

```
-[SRResearchDataPerCategoryViewController tableView:titleForFooterInSection:];
-[SRResearchDataPerCategoryViewController tableView:numberOfRowsInSection:];
-[SRResearchDataPerCategoryViewController numberOfSectionsInTableView:];
-[SRResearchDataPerCategoryViewController tableView:cellForRowAtIndexPath:];
-[SRResearchDataPerCategoryViewController viewWillDisappear:];
-[SRResearchDataPerCategoryViewController dealloc];
-[SRResearchDataPerCategoryViewController start];
-[SRResearchDataPerCategoryViewController tableView:titleForHeaderInSection:];
-[SRResearchDataPerCategoryViewController viewDidLoad];
-[SRResearchDataPerCategoryViewController setFetchGroup:];
-[SRResearchDataPerCategoryViewController end];
-[SRResearchDataPerCategoryViewController viewWillAppear:];
-[SRResearchDataPerCategoryViewController setEnd:];
-[SRResearchDataPerCategoryViewController setStart:];
-[SRResearchDataPerCategoryViewController tableView:didSelectRowAtIndexPath:];
-[SRResearchDataPerCategoryViewController tombstones];
-[SRResearchDataPerCategoryViewController fetchGroup];
-[SRResearchDataPerCategoryViewController cancelExport];
-[SRResearchDataPerCategoryViewController exportData];
-[SRResearchDataPerCategoryViewController daysFromDate:toDate:];
-[SRResearchDataPerCategoryViewController authStore];
-[SRResearchDataPerCategoryViewController datastoreBackend];
-[SRResearchDataPerCategoryViewController sensorReader:didCompleteFetch:];
-[SRResearchDataPerCategoryViewController sensorReader:fetchingRequest:didFetchResult:];
-[SRResearchDataPerCategoryViewController sensorReader:fetchingRequest:failedWithError:];
-[SRResearchDataPerCategoryViewController setAuthStore:];
-[SRResearchDataPerCategoryViewController setDatastoreBackend:];
-[SRResearchDataPerCategoryViewController setTombstones:];
-[SRResearchDataPerCategoryViewController numberOfDays];
-[SRResearchDataPerCategoryViewController readers];
-[SRResearchDataPerCategoryViewController setReaders:];
-[SRResearchDataPerCategoryViewController exportedDataURL];
-[SRResearchDataPerCategoryViewController pruners];
-[SRResearchDataPerCategoryViewController showActionSheet];
-[SRResearchDataPerCategoryViewController appBundles];
-[SRResearchDataPerCategoryViewController authGroup];
-[SRResearchDataPerCategoryViewController authorizationSwitchToggledWithValue:indexPath:];
-[SRResearchDataPerCategoryViewController authorizedBundleIds];
-[SRResearchDataPerCategoryViewController authorizedWriterBundleIds];
-[SRResearchDataPerCategoryViewController bundleForIndexPath:];
-[SRResearchDataPerCategoryViewController cancelExportBlock];
-[SRResearchDataPerCategoryViewController cleanupExportedFile];
-[SRResearchDataPerCategoryViewController confirmAuthChangeForBundle:value:authService:authorizedBundleIds:setOverride:];
-[SRResearchDataPerCategoryViewController deleteAllUnreleasedData];
-[SRResearchDataPerCategoryViewController navigateToAuthorization];
-[SRResearchDataPerCategoryViewController populateDays];
-[SRResearchDataPerCategoryViewController prepareDayCell];
-[SRResearchDataPerCategoryViewController prepareDeleteCell];
-[SRResearchDataPerCategoryViewController prepareExportCell];
-[SRResearchDataPerCategoryViewController presentDownloadPath:sandboxExtensionToken:];
-[SRResearchDataPerCategoryViewController sb_handle];
-[SRResearchDataPerCategoryViewController sensorIdentifiers];
-[SRResearchDataPerCategoryViewController setAppBundles:];
-[SRResearchDataPerCategoryViewController setAuthGroup:];
-[SRResearchDataPerCategoryViewController setAuthorizedBundleIds:];
-[SRResearchDataPerCategoryViewController setAuthorizedWriterBundleIds:];
-[SRResearchDataPerCategoryViewController setCancelExportBlock:];
-[SRResearchDataPerCategoryViewController setExportedDataURL:];
-[SRResearchDataPerCategoryViewController setNumberOfDays:];
-[SRResearchDataPerCategoryViewController setPruners:];
-[SRResearchDataPerCategoryViewController setSb_handle:];
-[SRResearchDataPerCategoryViewController setSensorIdentifiers:];
-[SRResearchDataPerCategoryViewController setWriterAppBundles:];
-[SRResearchDataPerCategoryViewController tableSectionFromIndexPathSection:];
-[SRResearchDataPerCategoryViewController writerAppBundles];
```
