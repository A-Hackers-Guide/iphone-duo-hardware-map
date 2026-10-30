# `TBRemoteFetchAndCacheOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOperation`
- 5 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _finished;
@"NSDate" _start;
@"<TBFetchResponse>" _response;
@"<TBFetchRequest>" _fetchRequest;
@"TBRemoteFetchAndCacheDataSource" _dataSource;
```

## Properties

```
@property (T@"<TBFetchRequest>",&,N,V_fetchRequest) fetchRequest;
@property (T@"<TBFetchResponse>",&,N,V_response) response;
@property (T@"TBRemoteFetchAndCacheDataSource",&,N,V_dataSource) dataSource;
```

## Instance methods

```
-[TBRemoteFetchAndCacheOperation isFinished];
-[TBRemoteFetchAndCacheOperation isReady];
-[TBRemoteFetchAndCacheOperation setResponse:];
-[TBRemoteFetchAndCacheOperation fetchRequest];
-[TBRemoteFetchAndCacheOperation setFetchRequest:];
-[TBRemoteFetchAndCacheOperation finish];
-[TBRemoteFetchAndCacheOperation start];
-[TBRemoteFetchAndCacheOperation setDataSource:];
-[TBRemoteFetchAndCacheOperation dataSource];
-[TBRemoteFetchAndCacheOperation name];
-[TBRemoteFetchAndCacheOperation response];
-[TBRemoteFetchAndCacheOperation initWithFetchRequest:dataSource:];
```
