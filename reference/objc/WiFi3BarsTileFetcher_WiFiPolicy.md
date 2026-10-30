# `WiFi3BarsTileFetcher`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"TBDataSourceMediator" _dataSourceMediator;
Q _lastFetchedKey;
@"WiFi3BarsTileCacheObserver" _tileCacheObserver;
@"NSXPCConnection" _connectionToService;
```

## Properties

```
@property (T@"TBDataSourceMediator",&,N,V_dataSourceMediator) dataSourceMediator;
@property (TQ,N,V_lastFetchedKey) lastFetchedKey;
@property (T@"WiFi3BarsTileCacheObserver",&,N,V_tileCacheObserver) tileCacheObserver;
@property (T@"NSXPCConnection",R,N,V_connectionToService) connectionToService;
```

## Instance methods

```
-[WiFi3BarsTileFetcher dealloc];
-[WiFi3BarsTileFetcher _handleLocationManagerVisitCallbackWithVisit:];
-[WiFi3BarsTileFetcher connectionToService];
-[WiFi3BarsTileFetcher dataSourceMediator];
-[WiFi3BarsTileFetcher initWithDataSourceMediator:];
-[WiFi3BarsTileFetcher lastFetchedKey];
-[WiFi3BarsTileFetcher setDataSourceMediator:];
-[WiFi3BarsTileFetcher setLastFetchedKey:];
-[WiFi3BarsTileFetcher setTileCacheObserver:];
-[WiFi3BarsTileFetcher tileCacheObserver];
```
