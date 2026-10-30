# `TBRemoteDataSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TBDataSource`
- 1 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
```

## Instance methods

```
-[TBRemoteDataSource init];
-[TBRemoteDataSource queue];
-[TBRemoteDataSource type];
-[TBRemoteDataSource executeFetchRequest:];
-[TBRemoteDataSource setQueue:];
-[TBRemoteDataSource _captureTileFetchError:tileKey:duration:trigger:];
-[TBRemoteDataSource _executeLocationFetchRequest:];
-[TBRemoteDataSource _executeNetworkFetchRequest:];
-[TBRemoteDataSource _executeTileFetchRequest:];
-[TBRemoteDataSource _fetchTilesForTileItems:completionHandler:trigger:];
-[TBRemoteDataSource _fetchTilesWithRequest:];
-[TBRemoteDataSource _submitNetworkSearch:completion:];
-[TBRemoteDataSource _writeSearchTileToFile:];
```
