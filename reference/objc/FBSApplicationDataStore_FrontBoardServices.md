# `FBSApplicationDataStore`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 25 instance methods, 13 class methods

## Instance variables

```
@"NSString" _identifier;
@"<FBSApplicationDataStoreRepositoryClient>" _client;
B _clientNeedsCheckin;
@"NSString" _bundleId;
@"LSApplicationIdentity" _identity;
```

## Properties

```
@property (T@"NSString",R,N,V_bundleId) bundleID;
@property (T@"LSApplicationIdentity",R,N,V_identity) identity;
@property (T@"<FBSApplicationIdentifying>",R,N,V_identifier) applicationIdentifier;
```

## Class methods

```
+[FBSApplicationDataStore synchronize];
+[FBSApplicationDataStore applicationsWithAvailableStores];
+[FBSApplicationDataStore isServerProcess];
+[FBSApplicationDataStore _doWithClassClient:];
+[FBSApplicationDataStore _setClassClient:];
+[FBSApplicationDataStore applicationIdentifiersWithAvailableStores];
+[FBSApplicationDataStore applicationIdentifiersWithAvailableStoresForBundleID:];
+[FBSApplicationDataStore applicationIdentitiesWithAvailableStores];
+[FBSApplicationDataStore setPrefetchedKeys:];
+[FBSApplicationDataStore storeForApplication:];
+[FBSApplicationDataStore storeForApplicationIdentifier:];
+[FBSApplicationDataStore storeForApplicationIdentity:];
+[FBSApplicationDataStore synchronizeWithCompletion:];
```

## Instance methods

```
-[FBSApplicationDataStore init];
-[FBSApplicationDataStore needsMigration];
-[FBSApplicationDataStore dealloc];
-[FBSApplicationDataStore objectForKey:];
-[FBSApplicationDataStore applicationIdentifier];
-[FBSApplicationDataStore identity];
-[FBSApplicationDataStore description];
-[FBSApplicationDataStore setObject:forKey:];
-[FBSApplicationDataStore bundleID];
-[FBSApplicationDataStore removeObjectForKey:];
-[FBSApplicationDataStore removeAllObjects];
-[FBSApplicationDataStore migrateWithError:];
-[FBSApplicationDataStore deserializeObjectForKey:ofType:];
-[FBSApplicationDataStore _initWithBundleId:identity:client:];
-[FBSApplicationDataStore archivedObjectForKey:];
-[FBSApplicationDataStore archivedObjectForKey:withResult:];
-[FBSApplicationDataStore deserializeObjectForKey:ofType:withResult:];
-[FBSApplicationDataStore migrateToIdentity:error:];
-[FBSApplicationDataStore objectForKey:withResult:];
-[FBSApplicationDataStore safeArchivedObjectForKey:ofType:];
-[FBSApplicationDataStore safeArchivedObjectForKey:ofType:withResult:];
-[FBSApplicationDataStore safeObjectForKey:ofType:];
-[FBSApplicationDataStore safeObjectForKey:ofType:withResult:];
-[FBSApplicationDataStore serializeObject:forKey:];
-[FBSApplicationDataStore setArchivedObject:forKey:];
```
