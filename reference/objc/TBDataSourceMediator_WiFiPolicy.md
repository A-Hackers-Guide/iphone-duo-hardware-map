# `TBDataSourceMediator`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"TBCoreDataSource" _local;
@"TBDataSource" _remote;
@"NSOperationQueue" _fetchQueue;
```

## Properties

```
@property (T@"TBCoreDataSource",&,N,V_local) local;
@property (T@"TBDataSource",&,N,V_remote) remote;
@property (T@"NSOperationQueue",&,N,V_fetchQueue) fetchQueue;
```

## Instance methods

```
-[TBDataSourceMediator local];
-[TBDataSourceMediator setLocal:];
-[TBDataSourceMediator fetchQueue];
-[TBDataSourceMediator remote];
-[TBDataSourceMediator executeFetchRequest:];
-[TBDataSourceMediator setFetchQueue:];
-[TBDataSourceMediator removeAllWithCompletionHandler:];
-[TBDataSourceMediator setRemote:];
-[TBDataSourceMediator initWithLocalStoreDescriptor:];
-[TBDataSourceMediator initWithLocalStoreDescriptor:remoteStore:];
-[TBDataSourceMediator prune3BarsNetworks:completionHandler:];
-[TBDataSourceMediator removeWithFetchRequest:];
```
