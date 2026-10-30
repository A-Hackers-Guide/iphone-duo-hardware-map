# `FBSqliteApplicationDataStoreRepository`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBApplicationDataStoreRepository`
- 7 instance variables, 5 properties, 41 instance methods, 3 class methods

## Instance variables

```
@"NSURL" _storeURL;
@"<FBApplicationDataStoreRepositoryDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _dbQueue;
@"BSSqliteDatabaseConnection" _dbQueue_dbConnection;
Q _dbQueue_batchDepth;
i _dbQueue_firstUnlockToken;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
```

## Properties

```
@property (T@"<FBApplicationDataStoreRepositoryDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSqliteApplicationDataStoreRepository _generateParameterizedQuery:forKeyList:outBindings:];
+[FBSqliteApplicationDataStoreRepository _objectForResultRow:index:];
+[FBSqliteApplicationDataStoreRepository _objectRequiresSerialization:];
```

## Instance methods

```
-[FBSqliteApplicationDataStoreRepository flushSynchronously];
-[FBSqliteApplicationDataStoreRepository _preserveFileAtURL:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_openDatabase];
-[FBSqliteApplicationDataStoreRepository removeObjectForKey:forApplication:];
-[FBSqliteApplicationDataStoreRepository close];
-[FBSqliteApplicationDataStoreRepository _dbQueue_notifyDelegateOfChangeForKeys:application:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_databaseVersion];
-[FBSqliteApplicationDataStoreRepository _dbQueue_notifyDelegateOfLateLoad];
-[FBSqliteApplicationDataStoreRepository setObject:forKey:forApplication:];
-[FBSqliteApplicationDataStoreRepository objectForKey:forApplication:];
-[FBSqliteApplicationDataStoreRepository _inAlternateSystemApp];
-[FBSqliteApplicationDataStoreRepository _isEligibleForSaving:];
-[FBSqliteApplicationDataStoreRepository endBatchedUpdate];
-[FBSqliteApplicationDataStoreRepository _dbQueue_executeStatement:bindings:resultRowHandler:error:];
-[FBSqliteApplicationDataStoreRepository dealloc];
-[FBSqliteApplicationDataStoreRepository containsKey:forApplication:];
-[FBSqliteApplicationDataStoreRepository keysForApplication:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_applicationIdentifiersWithState];
-[FBSqliteApplicationDataStoreRepository _dbQueue_tryPreserveDamagedDatabase];
-[FBSqliteApplicationDataStoreRepository migrateIdentifier:toIdentifier:];
-[FBSqliteApplicationDataStoreRepository setDelegate:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_load];
-[FBSqliteApplicationDataStoreRepository _dbQueue_keysForApplication:];
-[FBSqliteApplicationDataStoreRepository delegate];
-[FBSqliteApplicationDataStoreRepository removeAllObjectsForApplication:];
-[FBSqliteApplicationDataStoreRepository initWithStorePath:];
-[FBSqliteApplicationDataStoreRepository beginBatchedUpdate];
-[FBSqliteApplicationDataStoreRepository _dbQueue_loadDatabase];
-[FBSqliteApplicationDataStoreRepository _dbQueue_executeStatement:bindings:resultRowHandler:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_databaseIntegrityCheck];
-[FBSqliteApplicationDataStoreRepository _dbQueue_createTables];
-[FBSqliteApplicationDataStoreRepository _dbQueue_performWithSavepoint:handler:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_notifyDelegateOfStoreInvalidationForIdentifier:];
-[FBSqliteApplicationDataStoreRepository urlByAppendingString:toURL:];
-[FBSqliteApplicationDataStoreRepository removeObjectsForKeys:forApplication:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_truncateDamagedDatabase];
-[FBSqliteApplicationDataStoreRepository _dbQueue_objectForKey:forApplication:];
-[FBSqliteApplicationDataStoreRepository allObjectsForKeys:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_containsKey:forApplication:];
-[FBSqliteApplicationDataStoreRepository _dbQueue_objectsForKeys:];
-[FBSqliteApplicationDataStoreRepository applicationIdentifiersWithState];
```
