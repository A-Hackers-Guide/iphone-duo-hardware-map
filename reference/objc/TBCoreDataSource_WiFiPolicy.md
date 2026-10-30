# `TBCoreDataSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TBDataSource`
- Protocols: `TBCacheProvider`
- 5 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _hasStorageError;
Q _cacheExpirationInDays;
@"NSManagedObjectContext" _context;
@"TBPersistenceManager" _persistenceManager;
@"TBCoreDataStoreDescriptor" _descriptor;
```

## Properties

```
@property (T@"NSManagedObjectContext",&,N,V_context) context;
@property (T@"TBPersistenceManager",&,N,V_persistenceManager) persistenceManager;
@property (T@"TBCoreDataStoreDescriptor",&,N,V_descriptor) descriptor;
@property (TB,N,V_hasStorageError) hasStorageError;
@property (TQ,N,V_cacheExpirationInDays) cacheExpirationInDays;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TBCoreDataSource persistenceManager];
-[TBCoreDataSource setDescriptor:];
-[TBCoreDataSource setPersistenceManager:];
-[TBCoreDataSource descriptor];
-[TBCoreDataSource setContext:];
-[TBCoreDataSource type];
-[TBCoreDataSource executeFetchRequest:];
-[TBCoreDataSource context];
-[TBCoreDataSource removeAllWithCompletionHandler:];
-[TBCoreDataSource _createNewNetwork:tile:withMOC:];
-[TBCoreDataSource hasStorageError];
-[TBCoreDataSource _canSupportRequest:];
-[TBCoreDataSource _createNewNetworkFromDictionary:withMOC:];
-[TBCoreDataSource _executeFetchRequest:];
-[TBCoreDataSource _executePreferLocalFetchRequest:];
-[TBCoreDataSource cacheExpirationInDays];
-[TBCoreDataSource cacheFetchResponse:completionHandler:];
-[TBCoreDataSource importObjectsWithArray:completionHandler:];
-[TBCoreDataSource initWithStoreDescriptor:];
-[TBCoreDataSource prune3BarsNetworks:completionHandler:];
-[TBCoreDataSource removeWithFetchRequest:completionHandler:];
-[TBCoreDataSource setCacheExpirationInDays:];
-[TBCoreDataSource setHasStorageError:];
```
