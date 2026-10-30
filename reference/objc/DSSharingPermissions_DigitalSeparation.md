# `DSSharingPermissions`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 21 properties, 64 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _permissionsLock;
@"NSMutableOrderedSet" _people;
@"NSOrderedSet" _filteredPeople;
@"NSMutableOrderedSet" _readOnlySharingPeople;
@"NSOrderedSet" _filteredReadOnlySharingPeople;
@"NSMutableOrderedSet" _sharingTypes;
@"NSOrderedSet" _filteredSharingTypes;
@"NSMutableOrderedSet" _readOnlySharingTypes;
@"NSOrderedSet" _filteredReadOnlySharingTypes;
@"NSMutableOrderedSet" _publicSharingTypes;
@"NSMutableDictionary" _fetchStartTimesBySource;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSObject<OS_dispatch_queue>" _dataUsageQueue;
@"DSSourceRepository" _repo;
@"DSMe" _me;
```

## Properties

```
@property (T@"NSMutableOrderedSet",&,N,V_people) people;
@property (T@"NSOrderedSet",&,N,V_filteredPeople) filteredPeople;
@property (T@"NSMutableOrderedSet",&,N,V_readOnlySharingPeople) readOnlySharingPeople;
@property (T@"NSOrderedSet",&,N,V_filteredReadOnlySharingPeople) filteredReadOnlySharingPeople;
@property (T@"NSMutableOrderedSet",&,N,V_sharingTypes) sharingTypes;
@property (T@"NSOrderedSet",&,N,V_filteredSharingTypes) filteredSharingTypes;
@property (T@"NSMutableOrderedSet",&,N,V_readOnlySharingTypes) readOnlySharingTypes;
@property (T@"NSOrderedSet",&,N,V_filteredReadOnlySharingTypes) filteredReadOnlySharingTypes;
@property (T@"NSMutableOrderedSet",&,N,V_publicSharingTypes) publicSharingTypes;
@property (T@"NSMutableDictionary",&,N,V_fetchStartTimesBySource) fetchStartTimesBySource;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dataUsageQueue) dataUsageQueue;
@property (T@"DSSourceRepository",&,N,V_repo) repo;
@property (T@"DSMe",&,V_me) me;
@property (Tq,R,N) publicSharingTypesCount;
@property (T@"NSArray",R,C,N) allPeople;
@property (T@"NSArray",R,C,N) allReadOnlySharingPeople;
@property (T@"NSArray",R,C,N) allSharingTypes;
@property (T@"NSArray",R,C,N) allReadOnlySharingTypes;
@property (T@"NSArray",R,C,N) allPublicSharingTypes;
@property (T@"NSDictionary",R,C,N) elapsedUnfinishedFetchesBySource;
```

## Class methods

```
+[DSSharingPermissions initialize];
```

## Instance methods

```
-[DSSharingPermissions setWorkQueue:];
-[DSSharingPermissions me];
-[DSSharingPermissions setPeople:];
-[DSSharingPermissions people];
-[DSSharingPermissions init];
-[DSSharingPermissions setMe:];
-[DSSharingPermissions workQueue];
-[DSSharingPermissions sort];
-[DSSharingPermissions allPeople];
-[DSSharingPermissions removePerson:];
-[DSSharingPermissions allSharingTypes];
-[DSSharingPermissions readOnlySharingType:withFilter:];
-[DSSharingPermissions _trackResourceForPublicAccess:source:];
-[DSSharingPermissions addParticipant:forSource:sharedResource:deviceOwnerRole:];
-[DSSharingPermissions allPublicSharingTypes];
-[DSSharingPermissions allReadOnlySharingPeople];
-[DSSharingPermissions allReadOnlySharingTypes];
-[DSSharingPermissions dataUsageQueue];
-[DSSharingPermissions elapsedUnfinishedFetchesBySource];
-[DSSharingPermissions fetchCompletedForSource:];
-[DSSharingPermissions fetchPermissionsFromSources:includingErrors:queue:completion:];
-[DSSharingPermissions fetchPermissionsOnQueue:completion:];
-[DSSharingPermissions fetchStartTimesBySource];
-[DSSharingPermissions fetchStartedForSource:];
-[DSSharingPermissions filterPeopleWithPredicate:];
-[DSSharingPermissions filterReadOnlySharingPeopleWithPredicate:];
-[DSSharingPermissions filterReadOnlySharingTypesWithPredicate:];
-[DSSharingPermissions filterSharingTypesWithPredicate:];
-[DSSharingPermissions filteredPeople];
-[DSSharingPermissions filteredReadOnlySharingPeople];
-[DSSharingPermissions filteredReadOnlySharingTypes];
-[DSSharingPermissions filteredSharingTypes];
-[DSSharingPermissions peopleCountWithFilter:];
-[DSSharingPermissions person:withFilter:];
-[DSSharingPermissions publicSharingType:];
-[DSSharingPermissions publicSharingTypes];
-[DSSharingPermissions publicSharingTypesCount];
-[DSSharingPermissions readOnlySharingPeople];
-[DSSharingPermissions readOnlySharingPeopleCountWithFilter:];
-[DSSharingPermissions readOnlySharingPerson:withFilter:];
-[DSSharingPermissions readOnlySharingTypes];
-[DSSharingPermissions readOnlySharingTypesCountWithFilter:];
-[DSSharingPermissions removePerson:sources:];
-[DSSharingPermissions removePublicSharingType:];
-[DSSharingPermissions removeSharingType:];
-[DSSharingPermissions removeSharingType:people:];
-[DSSharingPermissions repo];
-[DSSharingPermissions setDataUsageQueue:];
-[DSSharingPermissions setFetchStartTimesBySource:];
-[DSSharingPermissions setFilteredPeople:];
-[DSSharingPermissions setFilteredReadOnlySharingPeople:];
-[DSSharingPermissions setFilteredReadOnlySharingTypes:];
-[DSSharingPermissions setFilteredSharingTypes:];
-[DSSharingPermissions setPublicSharingTypes:];
-[DSSharingPermissions setReadOnlySharingPeople:];
-[DSSharingPermissions setReadOnlySharingTypes:];
-[DSSharingPermissions setRepo:];
-[DSSharingPermissions setSharingTypes:];
-[DSSharingPermissions sharingType:withFilter:];
-[DSSharingPermissions sharingTypes];
-[DSSharingPermissions sharingTypesCountWithFilter:];
-[DSSharingPermissions shouldAllowBundleIDWithNoPolicy:];
-[DSSharingPermissions stopAllSharingOnQueue:completion:];
-[DSSharingPermissions verifyDataUsagePoliciesForSources:queue:completion:];
```
