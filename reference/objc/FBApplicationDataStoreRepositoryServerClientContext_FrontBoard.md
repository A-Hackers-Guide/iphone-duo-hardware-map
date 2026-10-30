# `FBApplicationDataStoreRepositoryServerClientContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSServiceFacilityClientContext`
- 7 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<FBApplicationDataStoreRepository>" _dataStore;
@"NSSet" _prefetchedKeys;
@"NSObject<OS_dispatch_queue>" _queue;
B _interestedInAllChanges;
B _observingChanges;
@"<FBSServiceFacilityClientHandle>" _client;
@"<FBApplicationDataStoreRepositoryServerClientContextDelegate>" _delegate;
```

## Properties

```
@property (T@"<FBApplicationDataStoreRepositoryServerClientContextDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_interestedInAllChanges) interestedInAllChanges;
@property (T@"NSSet",C,N,V_prefetchedKeys) prefetchedKeys;
@property (T@"<FBSServiceFacilityClientHandle>",W,N,V_client) clientHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBApplicationDataStoreRepositoryServerClientContext dealloc];
-[FBApplicationDataStoreRepositoryServerClientContext setDelegate:];
-[FBApplicationDataStoreRepositoryServerClientContext delegate];
-[FBApplicationDataStoreRepositoryServerClientContext initWithDataStore:];
-[FBApplicationDataStoreRepositoryServerClientContext clientHandle];
-[FBApplicationDataStoreRepositoryServerClientContext prefetchedKeys];
-[FBApplicationDataStoreRepositoryServerClientContext setPrefetchedKeys:];
-[FBApplicationDataStoreRepositoryServerClientContext _valueChanged:];
-[FBApplicationDataStoreRepositoryServerClientContext _queue_updateObservers];
-[FBApplicationDataStoreRepositoryServerClientContext _repositoryInvalidated:];
-[FBApplicationDataStoreRepositoryServerClientContext interestedInAllChanges];
-[FBApplicationDataStoreRepositoryServerClientContext setClientHandle:];
-[FBApplicationDataStoreRepositoryServerClientContext setInterestedInAllChanges:];
```
