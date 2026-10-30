# `WADeviceAnalyticsClient`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 20 properties, 126 instance methods, 28 class methods

## Instance variables

```
B _storeLoaded;
B _pendingPriorityBGTask;
I _bandForCachedNetworksAtLocation;
@"NSError" _storeLoadError;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"WAPersistentContainer" _persistentContainer;
@"AnalyticsReader" _analyticsReaderObj;
@"AnalyticsProcessor" _analyticsProcessorObj;
@"AnalyticsStoreFileWriter" _analyticsFileWriterObj;
@"WAAnalyticsAccess" _analyticsRawAccessObj;
@"NSString" _latestBssid;
@"NSString" _latestNetwork;
@"WADeviceAnalytics_EdgeBSSParameters" _cachedEdgeParams;
@"CLLocation" _locationForCachedGeoTags;
@"NSArray" _cachedGeoTagsForNetwork;
@"CLLocation" _locationForCachedNetworksAtLocation;
d _distanceForCachedNetworksAtLocation;
@"NSArray" _cachedNetworksAtLocation;
@"NSArray" _cachedNetworksInSameLanAsLatestSsid;
@"NSError" _cachedNetworksInSameLanAsLatestSsidError;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
@property (TB,N,V_storeLoaded) storeLoaded;
@property (T@"NSError",&,N,V_storeLoadError) storeLoadError;
@property (T@"AnalyticsReader",&,N,V_analyticsReaderObj) analyticsReaderObj;
@property (T@"AnalyticsProcessor",&,N,V_analyticsProcessorObj) analyticsProcessorObj;
@property (T@"AnalyticsStoreFileWriter",&,N,V_analyticsFileWriterObj) analyticsFileWriterObj;
@property (T@"WAAnalyticsAccess",&,N,V_analyticsRawAccessObj) analyticsRawAccessObj;
@property (TB,N,V_pendingPriorityBGTask) pendingPriorityBGTask;
@property (T@"NSString",&,N,V_latestBssid) latestBssid;
@property (T@"NSString",&,N,V_latestNetwork) latestNetwork;
@property (T@"WADeviceAnalytics_EdgeBSSParameters",&,N,V_cachedEdgeParams) cachedEdgeParams;
@property (T@"CLLocation",&,N,V_locationForCachedGeoTags) locationForCachedGeoTags;
@property (T@"NSArray",&,N,V_cachedGeoTagsForNetwork) cachedGeoTagsForNetwork;
@property (T@"CLLocation",&,N,V_locationForCachedNetworksAtLocation) locationForCachedNetworksAtLocation;
@property (Td,N,V_distanceForCachedNetworksAtLocation) distanceForCachedNetworksAtLocation;
@property (TI,N,V_bandForCachedNetworksAtLocation) bandForCachedNetworksAtLocation;
@property (T@"NSArray",&,N,V_cachedNetworksAtLocation) cachedNetworksAtLocation;
@property (T@"NSArray",&,N,V_cachedNetworksInSameLanAsLatestSsid) cachedNetworksInSameLanAsLatestSsid;
@property (T@"NSError",&,N,V_cachedNetworksInSameLanAsLatestSsidError) cachedNetworksInSameLanAsLatestSsidError;
```

## Class methods

```
+[WADeviceAnalyticsClient bandAsString:];
+[WADeviceAnalyticsClient motionStateAsString:];
+[WADeviceAnalyticsClient joinReasonAsString:];
+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient];
+[WADeviceAnalyticsClient eventsForEntityNames:withError:];
+[WADeviceAnalyticsClient addPersistentStoreRemoteChangeNotificationObserver:selector:coordinator:];
+[WADeviceAnalyticsClient aggregateNameFor:withError:];
+[WADeviceAnalyticsClient availableDimensionsFor:withError:];
+[WADeviceAnalyticsClient availableEventsWithError:];
+[WADeviceAnalyticsClient bandFromChannelFlags:];
+[WADeviceAnalyticsClient bandFromNSChannelFlags:];
+[WADeviceAnalyticsClient channelBitmapForChannel:band:];
+[WADeviceAnalyticsClient channelWidthAsString:];
+[WADeviceAnalyticsClient channelWidthFromChannelFlags:];
+[WADeviceAnalyticsClient channelsFromBitmap2And5:bitmap6:];
+[WADeviceAnalyticsClient convert32to16:];
+[WADeviceAnalyticsClient isMigrationError:];
+[WADeviceAnalyticsClient joinStatusAsString:];
+[WADeviceAnalyticsClient leaveReasonAsString:];
+[WADeviceAnalyticsClient ouiFromBssid:];
+[WADeviceAnalyticsClient removePersistentStoreRemoteChangeNotificationObserver:coordinator:];
+[WADeviceAnalyticsClient roamReasonAsString:];
+[WADeviceAnalyticsClient roamStatusAsString:];
+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithCustomStore:];
+[WADeviceAnalyticsClient subBandAsString:];
+[WADeviceAnalyticsClient subBandFromBand:channel:];
+[WADeviceAnalyticsClient timeSpanSelectorToString:];
+[WADeviceAnalyticsClient timeSpanToString:];
```

## Instance methods

```
-[WADeviceAnalyticsClient initWithStore:];
-[WADeviceAnalyticsClient isNetworkWithinRangeOfLocation:range:location:];
-[WADeviceAnalyticsClient entities];
-[WADeviceAnalyticsClient dispatchQueue];
-[WADeviceAnalyticsClient insideOutsideClassifierForSSID:];
-[WADeviceAnalyticsClient event:andDeferReclaimMem:andRunPostProcessing:withError:];
-[WADeviceAnalyticsClient updateNetwork:withIs2GHzRelevant:is5GHzRelevant:is6GHzRelevant:];
-[WADeviceAnalyticsClient eventSequencesFor:since:until:sortingAsc:withError:];
-[WADeviceAnalyticsClient copyAllStoredNetworkSsids];
-[WADeviceAnalyticsClient setCachedGeoTagsForNetwork:];
-[WADeviceAnalyticsClient analyticsFileWriterObj];
-[WADeviceAnalyticsClient setAnalyticsReaderObj:];
-[WADeviceAnalyticsClient setAnalyticsFileWriterObj:];
-[WADeviceAnalyticsClient edgeParamsForBSS:];
-[WADeviceAnalyticsClient locationForCachedNetworksAtLocation];
-[WADeviceAnalyticsClient performPruneTestEntity:since:withPredicate:withError:];
-[WADeviceAnalyticsClient processDeferredPoliciesWithReason:];
-[WADeviceAnalyticsClient updateNetwork:withInsideOutsideClassifierBestBand:rssiThreshold:];
-[WADeviceAnalyticsClient copyAllBSSEssentialInfoForNetwork:];
-[WADeviceAnalyticsClient analyticsFileWriter];
-[WADeviceAnalyticsClient analyticsReader];
-[WADeviceAnalyticsClient asyncAddEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:];
-[WADeviceAnalyticsClient lanForBssid:withError:];
-[WADeviceAnalyticsClient cachedGeoTagsForNetwork];
-[WADeviceAnalyticsClient setCachedParamsWithBssid:ssid:];
-[WADeviceAnalyticsClient copyLocationsForNetwork:];
-[WADeviceAnalyticsClient eventSequencesFor:since:until:sortingAsc:limit:withError:];
-[WADeviceAnalyticsClient setPersistentContainer:];
-[WADeviceAnalyticsClient dealloc];
-[WADeviceAnalyticsClient deploymentCongestionForSSID:withError:];
-[WADeviceAnalyticsClient setAnalyticsRawAccessObj:];
-[WADeviceAnalyticsClient storeLoadError];
-[WADeviceAnalyticsClient deleteStoreAndStartFreshWithError:];
-[WADeviceAnalyticsClient performPrunePoliciesWithReasons:withError:];
-[WADeviceAnalyticsClient cachedNetworksAtLocation];
-[WADeviceAnalyticsClient setCachedNetworksInSameLanAsLatestSsidError:];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsUsingBatchSizeToFileWithCompletion:batchSize:maxAge:];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:];
-[WADeviceAnalyticsClient addPersistentStoreRemoteChangeNotificationObserver:selector:];
-[WADeviceAnalyticsClient locationForCachedGeoTags];
-[WADeviceAnalyticsClient networksInSameLanAs:withError:];
-[WADeviceAnalyticsClient deploymentCoverageForSSID:withError:];
-[WADeviceAnalyticsClient performPruneTestBSSes:networks:lans:withError:];
-[WADeviceAnalyticsClient updateCachedParamsIfNeeded:];
-[WADeviceAnalyticsClient rawAccessCanWrite];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithCompletion:batchSize:maxAge:];
-[WADeviceAnalyticsClient countNetworksHavingBand:inLan:withError:];
-[WADeviceAnalyticsClient _event:andDeferReclaimMem:andRunPostProcessing:withError:];
-[WADeviceAnalyticsClient analyticsProcessor];
-[WADeviceAnalyticsClient setDispatchQueue:];
-[WADeviceAnalyticsClient setBandForCachedNetworksAtLocation:];
-[WADeviceAnalyticsClient event:withError:];
-[WADeviceAnalyticsClient getPolicyHandlersConfig];
-[WADeviceAnalyticsClient adaptiveRoamingParamsForBSS:];
-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile];
-[WADeviceAnalyticsClient managedObjectContextResetAndRelease:];
-[WADeviceAnalyticsClient analyticsProcessorObj];
-[WADeviceAnalyticsClient copyGeoTagsForNetwork:location:];
-[WADeviceAnalyticsClient isBandRelevantForSSID:onBand:];
-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFileWithCompletion:];
-[WADeviceAnalyticsClient distanceForCachedNetworksAtLocation];
-[WADeviceAnalyticsClient setDistanceForCachedNetworksAtLocation:];
-[WADeviceAnalyticsClient setCachedNetworksInSameLanAsLatestSsid:];
-[WADeviceAnalyticsClient prunableEntitiesWithDate];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:];
-[WADeviceAnalyticsClient updateRoamPoliciesForSourceBssid:andUpdateRoamCache:];
-[WADeviceAnalyticsClient processWiFiStats:];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:];
-[WADeviceAnalyticsClient processDatapathMetricStream:withDate:];
-[WADeviceAnalyticsClient bssidCountByBandInLAN:withError:];
-[WADeviceAnalyticsClient usageForNetwork:withError:];
-[WADeviceAnalyticsClient persistentContainer];
-[WADeviceAnalyticsClient setCachedEdgeParams:];
-[WADeviceAnalyticsClient usageOf:timeSpan:around:withError:];
-[WADeviceAnalyticsClient resetPolicyHandlersConfig];
-[WADeviceAnalyticsClient bandForCachedNetworksAtLocation];
-[WADeviceAnalyticsClient bandsInNetwork:withError:];
-[WADeviceAnalyticsClient latestNetwork];
-[WADeviceAnalyticsClient cachedNetworksInSameLanAsLatestSsid];
-[WADeviceAnalyticsClient setCachedNetworksAtLocation:];
-[WADeviceAnalyticsClient setPendingPriorityBGTask:];
-[WADeviceAnalyticsClient lansForSsid:withError:];
-[WADeviceAnalyticsClient apProfileForBssid:];
-[WADeviceAnalyticsClient setPolicyHandlersConfig:];
-[WADeviceAnalyticsClient setStoreLoadError:];
-[WADeviceAnalyticsClient performPruneTestEntityInAnyType:withPredicate:withError:];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithCompletion:fetchLimit:maxAge:];
-[WADeviceAnalyticsClient setLatestBssid:];
-[WADeviceAnalyticsClient usageForLAN:withError:];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithCompletion:];
-[WADeviceAnalyticsClient setStoreLoaded:];
-[WADeviceAnalyticsClient analyticsRawAccessObj];
-[WADeviceAnalyticsClient setLocationForCachedNetworksAtLocation:];
-[WADeviceAnalyticsClient latestBssid];
-[WADeviceAnalyticsClient setAnalyticsProcessorObj:];
-[WADeviceAnalyticsClient networksInSameLanAsBssid:withError:];
-[WADeviceAnalyticsClient lanForSsid:withError:];
-[WADeviceAnalyticsClient asyncAddEvent:uponCompletionDo:];
-[WADeviceAnalyticsClient countNetworksAvailableAtLocation:withinDistance:inBand:];
-[WADeviceAnalyticsClient parsedBeaconInfoIsStored:ssid:];
-[WADeviceAnalyticsClient setLatestNetwork:];
-[WADeviceAnalyticsClient performPruneBasedOnStoreSizeAndSaveWithReason:];
-[WADeviceAnalyticsClient updateBSS:withIsEdgeForLeave:autoLeaveRssi:];
-[WADeviceAnalyticsClient performFetch:error:];
-[WADeviceAnalyticsClient networkSsidsByTraits:withError:];
-[WADeviceAnalyticsClient loadStoreIfNeeded];
-[WADeviceAnalyticsClient setLocationForCachedGeoTags:];
-[WADeviceAnalyticsClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:];
-[WADeviceAnalyticsClient removePersistentStoreRemoteChangeNotificationObserver:];
-[WADeviceAnalyticsClient analyticsRawAccess];
-[WADeviceAnalyticsClient networksInLan:withError:];
-[WADeviceAnalyticsClient usageOf:during:timeSpan:withError:];
-[WADeviceAnalyticsClient pendingPriorityBGTask];
-[WADeviceAnalyticsClient analyticsReaderObj];
-[WADeviceAnalyticsClient knownChannelsBitmapForSSID:withError:];
-[WADeviceAnalyticsClient countNetworksInSameLanAsBssid:withError:];
-[WADeviceAnalyticsClient processDeferredPriorityPoliciesWithReason:];
-[WADeviceAnalyticsClient knownChannelsBitmapForBSSID:withError:];
-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile];
-[WADeviceAnalyticsClient countForFetchRequest:error:];
-[WADeviceAnalyticsClient networksAvailableAtLocation:withinDistance:inBand:];
-[WADeviceAnalyticsClient cachedNetworksInSameLanAsLatestSsidError];
-[WADeviceAnalyticsClient cachedEdgeParams];
-[WADeviceAnalyticsClient networkCountForLAN:withError:];
-[WADeviceAnalyticsClient storeLoaded];
-[WADeviceAnalyticsClient countNetworksInSameLanAs:withError:];
```
