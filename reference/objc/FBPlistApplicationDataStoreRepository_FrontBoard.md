# `FBPlistApplicationDataStoreRepository`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBApplicationDataStoreRepository`
- 9 instance variables, 5 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _storeURL;
@"NSMutableDictionary" _state;
B _dirty;
Q _batchCount;
i _autoFlushDuration;
@"<FBApplicationDataStoreRepositoryDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _stateQueue;
@"NSObject<OS_dispatch_queue>" _writeQueue;
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

## Instance methods

```
-[FBPlistApplicationDataStoreRepository flushSynchronously];
-[FBPlistApplicationDataStoreRepository removeObjectForKey:forApplication:];
-[FBPlistApplicationDataStoreRepository close];
-[FBPlistApplicationDataStoreRepository setObject:forKey:forApplication:];
-[FBPlistApplicationDataStoreRepository objectForKey:forApplication:];
-[FBPlistApplicationDataStoreRepository location];
-[FBPlistApplicationDataStoreRepository _isEligibleForSaving:];
-[FBPlistApplicationDataStoreRepository endBatchedUpdate];
-[FBPlistApplicationDataStoreRepository dealloc];
-[FBPlistApplicationDataStoreRepository containsKey:forApplication:];
-[FBPlistApplicationDataStoreRepository keysForApplication:];
-[FBPlistApplicationDataStoreRepository migrateIdentifier:toIdentifier:];
-[FBPlistApplicationDataStoreRepository setDelegate:];
-[FBPlistApplicationDataStoreRepository delegate];
-[FBPlistApplicationDataStoreRepository removeAllObjectsForApplication:];
-[FBPlistApplicationDataStoreRepository initWithStorePath:];
-[FBPlistApplicationDataStoreRepository beginBatchedUpdate];
-[FBPlistApplicationDataStoreRepository _load];
-[FBPlistApplicationDataStoreRepository isDirty];
-[FBPlistApplicationDataStoreRepository removeObjectsForKeys:forApplication:];
-[FBPlistApplicationDataStoreRepository allObjectsForKeys:];
-[FBPlistApplicationDataStoreRepository applicationIdentifiersWithState];
-[FBPlistApplicationDataStoreRepository _stateQueue_storeForIdentifier:];
-[FBPlistApplicationDataStoreRepository _notifyDelegateOfChangeForKeys:application:];
-[FBPlistApplicationDataStoreRepository _notifyDelegateOfStoreInvalidationForIdentifier:];
-[FBPlistApplicationDataStoreRepository _stateQueue_addStoreForIdentifierIfNecessary:];
-[FBPlistApplicationDataStoreRepository _stateQueue_markDirty];
-[FBPlistApplicationDataStoreRepository _stateQueue_objectForKey:forIdentifier:];
-[FBPlistApplicationDataStoreRepository _stateQueue_objectsForKeys:];
-[FBPlistApplicationDataStoreRepository _stateQueue_removeStoreForIdentifier:];
-[FBPlistApplicationDataStoreRepository _writeQueue_flushSynchronously];
```
