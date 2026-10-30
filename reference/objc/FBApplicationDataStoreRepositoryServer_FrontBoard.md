# `FBApplicationDataStoreRepositoryServer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacility`
- Protocols: `FBApplicationDataStoreRepositoryServerClientContextDelegate`
- 2 instance variables, 5 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<FBApplicationDataStoreRepository>" _dataStore;
@"FBServiceClientAuthenticator" _connectionAuthenticator;
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
+[FBApplicationDataStoreRepositoryServer sharedInstance];
```

## Instance methods

```
-[FBApplicationDataStoreRepositoryServer _init];
-[FBApplicationDataStoreRepositoryServer dataStore];
-[FBApplicationDataStoreRepositoryServer setDataStore:];
-[FBApplicationDataStoreRepositoryServer _prerequisiteMilestones];
-[FBApplicationDataStoreRepositoryServer noteClientDidConnect:withMessage:];
-[FBApplicationDataStoreRepositoryServer noteClientDidDisconnect:];
-[FBApplicationDataStoreRepositoryServer noteDidReceiveMessage:withType:fromClient:];
-[FBApplicationDataStoreRepositoryServer shouldAllowClientConnection:withMessage:];
-[FBApplicationDataStoreRepositoryServer _handleSetObjectForKey:context:];
-[FBApplicationDataStoreRepositoryServer _handleGetAvailableDataStores:];
-[FBApplicationDataStoreRepositoryServer _handleGetObjectForKey:];
-[FBApplicationDataStoreRepositoryServer _handleMigrateIdentifier:];
-[FBApplicationDataStoreRepositoryServer _handleRemoveAllObjects:];
-[FBApplicationDataStoreRepositoryServer _handleRemoveObjectForKey:context:];
-[FBApplicationDataStoreRepositoryServer _handleSetChangesInterest:context:];
-[FBApplicationDataStoreRepositoryServer _handleSetPrefetchedKeys:context:];
-[FBApplicationDataStoreRepositoryServer _handleSynchronize:];
-[FBApplicationDataStoreRepositoryServer applicationDataStoreRepositoryClientContext:repositoryInvalidatedForAppID:];
-[FBApplicationDataStoreRepositoryServer applicationDataStoreRepositoryClientContext:valueChangedForObject:key:appID:];
```
