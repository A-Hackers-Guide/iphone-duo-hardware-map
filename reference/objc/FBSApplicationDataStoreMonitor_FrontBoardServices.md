# `FBSApplicationDataStoreMonitor`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSApplicationDataStoreRepositoryClientObserver`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<FBSApplicationDataStoreRepositoryClient>" _client;
B _clientNeedsCheckin;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSHashTable" _lock_observers;
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
-[FBSApplicationDataStoreMonitor initWithClient:];
-[FBSApplicationDataStoreMonitor removeObserver:];
-[FBSApplicationDataStoreMonitor init];
-[FBSApplicationDataStoreMonitor add:];
-[FBSApplicationDataStoreMonitor remove:];
-[FBSApplicationDataStoreMonitor dealloc];
-[FBSApplicationDataStoreMonitor addObserver:];
-[FBSApplicationDataStoreMonitor _hasObserver:];
-[FBSApplicationDataStoreMonitor applicationDataStoreRepositoryClient:application:changedObject:forKey:];
-[FBSApplicationDataStoreMonitor applicationDataStoreRepositoryClient:storeInvalidatedForApplication:];
```
