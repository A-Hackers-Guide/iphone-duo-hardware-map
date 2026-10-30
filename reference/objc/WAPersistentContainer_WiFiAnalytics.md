# `WAPersistentContainer`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSPersistentContainer`
- 1 instance variables, 1 properties, 105 instance methods, 21 class methods

## Instance variables

```
@"NSManagedObjectContext" _backgroundMOC;
```

## Properties

```
@property (T@"NSManagedObjectContext",&,N,V_backgroundMOC) backgroundMOC;
```

## Class methods

```
+[WAPersistentContainer predicateForRecordsOlderThan:];
+[WAPersistentContainer eventsForEntityNames:withError:];
+[WAPersistentContainer predicateForEntityWithDateField];
+[WAPersistentContainer sortByOlderDateFirstOnProperty:];
+[WAPersistentContainer availableEventsWithError:];
+[WAPersistentContainer constraintsForEntity:];
+[WAPersistentContainer defaultBinnedDateHigherEdgePropertyName];
+[WAPersistentContainer defaultBinnedDateLowerEdgePropertyName];
+[WAPersistentContainer defaultDatedPropertyName];
+[WAPersistentContainer dimensionsForUsageEntity:];
+[WAPersistentContainer getConstraintsValues:];
+[WAPersistentContainer performBlock:overConstraintsOfEntity:withConstraints:];
+[WAPersistentContainer predicateForEntityWithDateBinField];
+[WAPersistentContainer predicateForIsSubEntity];
+[WAPersistentContainer predicateForRecordsNewerThan:];
+[WAPersistentContainer sequenceForSuccessfulJoinAndLeaveWithPrefetchedProperties:withError:];
+[WAPersistentContainer sortByNewestDateFirst];
+[WAPersistentContainer sortByNewestDateFirstOnProperty:];
+[WAPersistentContainer sortByOlderDateFirst];
+[WAPersistentContainer validateEntityForGroupbyRequest:];
+[WAPersistentContainer waPersistentContainerWithName:managedObjectModel:storeDescriptor:];
```

## Instance methods

```
-[WAPersistentContainer _eventSequencesInMOFormatFor:withSequenceStartEvents:withSequenceEndEvents:withSequenceEvents:since:until:sortingAsc:withError:];
-[WAPersistentContainer bssForBSSID:allowCreate:prefetchProperties:withError:];
-[WAPersistentContainer usageOf:inUsageTable:forDateSpan:withSorting:withError:];
-[WAPersistentContainer mostRecentPolicyFilteredBy:withError:];
-[WAPersistentContainer _usageEntities];
-[WAPersistentContainer leastRecent:withPredicate:withPrefetchedProperties:limit:];
-[WAPersistentContainer managedObjectContextSave:reset:release:withError:];
-[WAPersistentContainer networksInSameLANsAsBSS:withError:];
-[WAPersistentContainer networksWithPredicate:prefetchedProperties:withError:];
-[WAPersistentContainer successfulRoamCountFrom:to:];
-[WAPersistentContainer requestForDefaultAggregatedProperties:withPredicate:groupBy:having:withSorting:withLimit:];
-[WAPersistentContainer mostRecentPolicy:withError:];
-[WAPersistentContainer analyticsAgeOutTimeIntervalSecs];
-[WAPersistentContainer batchDeleteUsageRecordsHavingBSSInList:withError:];
-[WAPersistentContainer mostRecentRoamsFromBssid:withPrefetchedProperties:limit:];
-[WAPersistentContainer predicateForUniqueMO:withConstraints:atKeyPath:withError:];
-[WAPersistentContainer networksWithTrait:prefetchedProperties:withError:];
-[WAPersistentContainer _storeNeedsImmediatePruning:];
-[WAPersistentContainer batchDeleteDatedEntitiesOlderThan:withError:];
-[WAPersistentContainer setHasBandsForMO:forBand:];
-[WAPersistentContainer eventSequencesFor:since:until:sortingAsc:limit:withError:];
-[WAPersistentContainer newDatedEventObjectFor:withDate:withError:];
-[WAPersistentContainer datePropertyForEntity:];
-[WAPersistentContainer mostRecentDatedEvent:before:withPrefetchedProperties:withError:];
-[WAPersistentContainer networksInSameLANsAsNetwork:withError:];
-[WAPersistentContainer mostRecentRoamsFromBSS:withPrefetchedProperties:limit:];
-[WAPersistentContainer _prunableEntitiesWithDate];
-[WAPersistentContainer uniqueObjectPropertiesFor:withPredicate:prefetchProperties:withError:];
-[WAPersistentContainer viewContext];
-[WAPersistentContainer fetchDatedEvents:since:until:ascending:limit:withError:];
-[WAPersistentContainer setHasBandsForMO:forBand:to:];
-[WAPersistentContainer bssForBssid:prefetchProperties:withError:];
-[WAPersistentContainer countNetworksHavingBand:inLan:withError:];
-[WAPersistentContainer requestForDefaultAggregatedProperties:withPredicate:groupBy:having:withSorting:];
-[WAPersistentContainer predicatesForRecordsWithNoBssRelationshipByEntities:onlyDated:];
-[WAPersistentContainer releaseBackgroundMOC];
-[WAPersistentContainer bssesForBssids:allowCreate:prefetchProperties:withError:];
-[WAPersistentContainer predicateForLAN:withError:];
-[WAPersistentContainer lansInNetworksWithPredicate:withError:];
-[WAPersistentContainer requestForObjects:withPredicate:withSorting:withPrefetchedProperties:withLimit:];
-[WAPersistentContainer networkForBSSID:prefetchProperties:withError:];
-[WAPersistentContainer fetchDistinctPropertiesIn:withPredicate:withSorting:withPrefetchedProperties:withLimit:withError:];
-[WAPersistentContainer predicateForNetwork:atKeyPath:withError:];
-[WAPersistentContainer requestForObjectsInEntity:withBSSInList:];
-[WAPersistentContainer eventSequencesFor:since:until:sortingAsc:limit:forExport:withError:];
-[WAPersistentContainer requestForDistinctProperties:withPredicate:withSorting:withPrefetchedProperties:withLimit:];
-[WAPersistentContainer networksInLAN:withError:];
-[WAPersistentContainer createNewObjectForEntity:withError:];
-[WAPersistentContainer _datedRecordEntities];
-[WAPersistentContainer fetchCount:withError:];
-[WAPersistentContainer backgroundMOC];
-[WAPersistentContainer saveManagedObjectContextWithError:];
-[WAPersistentContainer lansCountInNetwork:withError:];
-[WAPersistentContainer validateUniqueObjectFor:withConstraints:withError:];
-[WAPersistentContainer createUniqueObjectFor:withConstraints:withError:];
-[WAPersistentContainer predicateForEntity:newerThanDate:withError:];
-[WAPersistentContainer updateUsage:with:on:at:withError:];
-[WAPersistentContainer batchDelete:olderThan:withError:];
-[WAPersistentContainer newDatedEventObjectFor:withDate:];
-[WAPersistentContainer batchDeleteBSSList:withError:];
-[WAPersistentContainer mostRecentDatedEvents:withError:];
-[WAPersistentContainer countObjects:withPredicate:withError:];
-[WAPersistentContainer _eventSequencesInDictionaryFormatFor:withSequenceStartEvents:withSequenceEndEvents:withSequenceEvents:since:until:sortingAsc:withError:];
-[WAPersistentContainer predicateForEntity:olderThan:withError:];
-[WAPersistentContainer predicateForEntity:before:withError:];
-[WAPersistentContainer ageOutAnalyticsWithReason:withExtraWeeks:withError:];
-[WAPersistentContainer setBackgroundMOC:];
-[WAPersistentContainer uniqueObjectFor:withConstraints:allowCreate:prefetchProperties:withError:];
-[WAPersistentContainer pruneFailedRoamEventsWithError:];
-[WAPersistentContainer uniqueObjectPropertiesFor:withConstraints:prefetchProperties:withError:];
-[WAPersistentContainer fetch:withError:];
-[WAPersistentContainer lanContainingBSS:prefetchProperties:withError:];
-[WAPersistentContainer ageOutAnalyticsWithReason:withError:];
-[WAPersistentContainer batchDeleteEntitiesWithNilBssWithError:];
-[WAPersistentContainer entitiesWithProperties:];
-[WAPersistentContainer predicateForEntity:newerThan:withError:];
-[WAPersistentContainer batchDelete:newerThanDate:andPredicate:withError:];
-[WAPersistentContainer uniqueObjectFor:withPredicate:prefetchProperties:withError:];
-[WAPersistentContainer _entitiesWithDate];
-[WAPersistentContainer defaultFetchMaxAgeForEntity:];
-[WAPersistentContainer predicateForLan:withError:];
-[WAPersistentContainer networksWithPredicate:inLANs:withError:];
-[WAPersistentContainer expressionWithAggregateFunction:overField:called:];
-[WAPersistentContainer updateBandsInUniqueMO:];
-[WAPersistentContainer batchDelete:where:withError:];
-[WAPersistentContainer uniqueObjectFor:withConstraints:allowCreate:prefetchProperties:];
-[WAPersistentContainer bssidCountBy:inUniqueMO:withError:];
-[WAPersistentContainer performPruneBasedOnStoreSize];
-[WAPersistentContainer fetchDatedEventsWithDictionaryResultType:since:until:ascending:limit:withError:];
-[WAPersistentContainer predicateForUniqueMO:withConstraints:withError:];
-[WAPersistentContainer requestFor:forEntity:withPredicate:withSorting:withPrefetchedProperties:withLimit:];
-[WAPersistentContainer lansWithPredicate:inNetworksWithPredicate:withError:];
-[WAPersistentContainer fetchObjects:withPredicate:withSorting:withPrefetchedProperties:withLimit:withError:];
-[WAPersistentContainer batchDelete:withError:];
-[WAPersistentContainer networkForSSID:prefetchProperties:withError:];
-[WAPersistentContainer networksWithPredicate:inLANsWithPredicate:withError:];
-[WAPersistentContainer fetchDefaultAggregatedPropertyIn:withPredicate:groupBy:having:withSorting:withError:];
-[WAPersistentContainer resetManagedObjectContext];
-[WAPersistentContainer lansWithPredicate:prefetchedProperties:withError:];
-[WAPersistentContainer _pruneManagedObjects];
-[WAPersistentContainer networkCountForLAN:withError:];
-[WAPersistentContainer lansInNetwork:withError:];
-[WAPersistentContainer defaultFetchLimitForEntity:];
-[WAPersistentContainer lanFor:prefetchProperties:withError:];
-[WAPersistentContainer requestFor:forEntity:orForEntityWithName:withPredicate:withSorting:withPrefetchedProperties:groupBy:having:withLimit:];
```
