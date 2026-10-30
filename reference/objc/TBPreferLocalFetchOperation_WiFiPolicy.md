# `TBPreferLocalFetchOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOperation`
- 9 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _finished;
@"NSDate" _start;
@"<TBFetchRequest>" _fetchRequest;
@"<TBFetchRequest>" _fetchRequestCopy;
@"<TBFetchResponse>" _response;
@"TBPreferLocalFetchDataSource" _dataSource;
@"NSOperationQueue" _fetchQueue;
@"NSArray" _remoteKeysToFetch;
@"NSArray" _satisfiedLocalKeys;
```

## Properties

```
@property (T@"<TBFetchRequest>",&,N,V_fetchRequest) fetchRequest;
@property (T@"<TBFetchRequest>",&,N,V_fetchRequestCopy) fetchRequestCopy;
@property (T@"<TBFetchResponse>",&,N,V_response) response;
@property (T@"TBPreferLocalFetchDataSource",&,N,V_dataSource) dataSource;
@property (T@"NSOperationQueue",&,N,V_fetchQueue) fetchQueue;
@property (T@"NSArray",&,N,V_remoteKeysToFetch) remoteKeysToFetch;
@property (T@"NSArray",&,N,V_satisfiedLocalKeys) satisfiedLocalKeys;
```

## Instance methods

```
-[TBPreferLocalFetchOperation isFinished];
-[TBPreferLocalFetchOperation isReady];
-[TBPreferLocalFetchOperation setResponse:];
-[TBPreferLocalFetchOperation fetchRequest];
-[TBPreferLocalFetchOperation setFetchRequest:];
-[TBPreferLocalFetchOperation finish];
-[TBPreferLocalFetchOperation start];
-[TBPreferLocalFetchOperation setDataSource:];
-[TBPreferLocalFetchOperation fetchQueue];
-[TBPreferLocalFetchOperation dataSource];
-[TBPreferLocalFetchOperation name];
-[TBPreferLocalFetchOperation setFetchQueue:];
-[TBPreferLocalFetchOperation response];
-[TBPreferLocalFetchOperation _captureCacheEventWithStatus:userInfo:error:type:];
-[TBPreferLocalFetchOperation _doResults:satisfyFetchRequest:keysToFetchRemotely:satisfiedKeys:];
-[TBPreferLocalFetchOperation _fetchLocal];
-[TBPreferLocalFetchOperation _fetchRemote];
-[TBPreferLocalFetchOperation _mergeLocalAndRemoteResults:];
-[TBPreferLocalFetchOperation _tileItemsFromTileKeys:];
-[TBPreferLocalFetchOperation fetchRequestCopy];
-[TBPreferLocalFetchOperation finishAndCallCompletionWithResponse:];
-[TBPreferLocalFetchOperation initWithFetchRequest:dataSource:fetchQueue:];
-[TBPreferLocalFetchOperation remoteKeysToFetch];
-[TBPreferLocalFetchOperation satisfiedLocalKeys];
-[TBPreferLocalFetchOperation setFetchRequestCopy:];
-[TBPreferLocalFetchOperation setRemoteKeysToFetch:];
-[TBPreferLocalFetchOperation setSatisfiedLocalKeys:];
```
