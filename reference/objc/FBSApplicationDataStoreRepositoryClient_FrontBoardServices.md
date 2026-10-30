# `FBSApplicationDataStoreRepositoryClient`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacilityClient`
- Protocols: `FBSApplicationDataStoreRepositoryClient`
- 6 instance variables, 4 properties, 27 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _prefetchedDataLock;
@"NSCountedSet" _prefetchedKeys;
@"NSMutableDictionary" _prefetchedKeyValues;
@"NSMutableDictionary" _pendingChangesToPrefetchedKeys;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _observersLock;
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSApplicationDataStoreRepositoryClient removeObserver:];
-[FBSApplicationDataStoreRepositoryClient init];
-[FBSApplicationDataStoreRepositoryClient handleMessage:withType:];
-[FBSApplicationDataStoreRepositoryClient objectForKey:forApplication:];
-[FBSApplicationDataStoreRepositoryClient migrateIdentifier:toIdentifier:];
-[FBSApplicationDataStoreRepositoryClient _observers];
-[FBSApplicationDataStoreRepositoryClient addObserver:];
-[FBSApplicationDataStoreRepositoryClient invalidate];
-[FBSApplicationDataStoreRepositoryClient fireCompletion:error:];
-[FBSApplicationDataStoreRepositoryClient _sendMessageType:withMessage:withReplyHandler:waitForReply:];
-[FBSApplicationDataStoreRepositoryClient _allPrefetchedChangesInFlightForApplication:];
-[FBSApplicationDataStoreRepositoryClient _calloutQueue_handleStoreInvalidated:];
-[FBSApplicationDataStoreRepositoryClient _calloutQueue_handleValueChanged:];
-[FBSApplicationDataStoreRepositoryClient _clearAllPrefetchedObjectsForApplication:];
-[FBSApplicationDataStoreRepositoryClient _isChangeInFlightForPrefetchedKey:application:];
-[FBSApplicationDataStoreRepositoryClient _sendPrefetchedKeys:withCompletion:];
-[FBSApplicationDataStoreRepositoryClient _setChangeInFlight:forAllPrefetchedKeysInApplication:];
-[FBSApplicationDataStoreRepositoryClient _setChangeInFlight:forPrefetchedKey:application:];
-[FBSApplicationDataStoreRepositoryClient _setPrefetchedObjectIfNecessary:forKey:application:];
-[FBSApplicationDataStoreRepositoryClient addPrefetchedKeys:];
-[FBSApplicationDataStoreRepositoryClient availableDataStores];
-[FBSApplicationDataStoreRepositoryClient prefetchedObjectIfAvailableForKey:application:outObject:];
-[FBSApplicationDataStoreRepositoryClient removeAllObjectsForApplication:withCompletion:];
-[FBSApplicationDataStoreRepositoryClient removeObjectForKey:forApplication:withCompletion:];
-[FBSApplicationDataStoreRepositoryClient removePrefetchedKeys:withCompletion:];
-[FBSApplicationDataStoreRepositoryClient setObject:forKey:forApplication:withCompletion:];
-[FBSApplicationDataStoreRepositoryClient synchronizeWithCompletion:];
```
