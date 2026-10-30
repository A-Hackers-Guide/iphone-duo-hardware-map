# `FBApplicationDataStoreInProcessRepositoryClient`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSApplicationDataStoreRepositoryClient`
- 7 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"<FBApplicationDataStoreRepository>" _dataStore;
@"NSCountedSet" _prefetchedKeys;
@"NSMutableDictionary" _prefetchedKeyValues;
@"NSObject<OS_dispatch_queue>" _prefetchQueue;
@"NSObject<OS_dispatch_queue>" _clientCalloutQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _observersLock;
@"NSHashTable" _observersLock_observers;
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
-[FBApplicationDataStoreInProcessRepositoryClient removeObserver:];
-[FBApplicationDataStoreInProcessRepositoryClient init];
-[FBApplicationDataStoreInProcessRepositoryClient objectForKey:forApplication:];
-[FBApplicationDataStoreInProcessRepositoryClient migrateIdentifier:toIdentifier:];
-[FBApplicationDataStoreInProcessRepositoryClient _observers];
-[FBApplicationDataStoreInProcessRepositoryClient addObserver:];
-[FBApplicationDataStoreInProcessRepositoryClient invalidate];
-[FBApplicationDataStoreInProcessRepositoryClient initWithDataStore:];
-[FBApplicationDataStoreInProcessRepositoryClient addPrefetchedKeys:];
-[FBApplicationDataStoreInProcessRepositoryClient availableDataStores];
-[FBApplicationDataStoreInProcessRepositoryClient prefetchedObjectIfAvailableForKey:application:outObject:];
-[FBApplicationDataStoreInProcessRepositoryClient removeAllObjectsForApplication:withCompletion:];
-[FBApplicationDataStoreInProcessRepositoryClient removeObjectForKey:forApplication:withCompletion:];
-[FBApplicationDataStoreInProcessRepositoryClient removePrefetchedKeys:withCompletion:];
-[FBApplicationDataStoreInProcessRepositoryClient setObject:forKey:forApplication:withCompletion:];
-[FBApplicationDataStoreInProcessRepositoryClient synchronizeWithCompletion:];
-[FBApplicationDataStoreInProcessRepositoryClient _valueChanged:];
-[FBApplicationDataStoreInProcessRepositoryClient _invalidateCacheForApplication:];
-[FBApplicationDataStoreInProcessRepositoryClient _invalidateCacheIfObjectIsNotEqual:forKey:forApplication:];
-[FBApplicationDataStoreInProcessRepositoryClient _prefetchQueue_prefetchedKeysForApplication:];
-[FBApplicationDataStoreInProcessRepositoryClient _prefetchQueue_updateNotificationListeners];
-[FBApplicationDataStoreInProcessRepositoryClient _repositoryInvalidated:];
-[FBApplicationDataStoreInProcessRepositoryClient _updateCacheIfNecessaryWithObject:forKey:forApplication:];
-[FBApplicationDataStoreInProcessRepositoryClient _updateNotificationListeners];
-[FBApplicationDataStoreInProcessRepositoryClient objectForKey:forApplication:withResult:];
```
