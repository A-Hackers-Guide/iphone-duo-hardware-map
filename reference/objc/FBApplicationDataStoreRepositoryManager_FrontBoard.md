# `FBApplicationDataStoreRepositoryManager`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBApplicationDataStoreRepositoryDelegate`
- 4 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _dataStoreURL;
@"<FBApplicationDataStoreRepository>" _dataStore;
@"LSEnumerator" _lsEnumerator;
@"NSObject<OS_dispatch_queue>" _deferredWorkQueue;
```

## Properties

```
@property (T@"<FBApplicationDataStoreRepository>",&,N,V_dataStore) dataStore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBApplicationDataStoreRepositoryManager sharedInstance];
```

## Instance methods

```
-[FBApplicationDataStoreRepositoryManager init];
-[FBApplicationDataStoreRepositoryManager dealloc];
-[FBApplicationDataStoreRepositoryManager dataStore];
-[FBApplicationDataStoreRepositoryManager setDataStore:];
-[FBApplicationDataStoreRepositoryManager urlByAppendingString:toURL:];
-[FBApplicationDataStoreRepositoryManager _handleApplicationInstalled:];
-[FBApplicationDataStoreRepositoryManager _initWithDataStore:lsEnumerator:];
-[FBApplicationDataStoreRepositoryManager _performAfterDeferredWork:];
-[FBApplicationDataStoreRepositoryManager _safeObjectForKey:forApplication:ofType:];
-[FBApplicationDataStoreRepositoryManager clearExpiredUninstalledApplicationsFromStoreIfNecessary];
-[FBApplicationDataStoreRepositoryManager migrateApplicationStorePathIfNecessary];
-[FBApplicationDataStoreRepositoryManager migrateFromApplicationStore:toApplicationStore:error:];
-[FBApplicationDataStoreRepositoryManager migrateFromPlistStoreAtURL:toSqliteStoreAtURL:error:];
-[FBApplicationDataStoreRepositoryManager objectChangedForKeys:application:];
-[FBApplicationDataStoreRepositoryManager removeStoreAtURL:error:];
-[FBApplicationDataStoreRepositoryManager storeInvalidatedForIdentifier:];
```
