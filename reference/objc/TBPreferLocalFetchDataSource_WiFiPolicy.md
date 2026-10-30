# `TBPreferLocalFetchDataSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"TBDataSource" _localDataSource;
@"TBDataSource" _remoteDataSource;
@"<TBCacheProvider>" _cacheProvider;
```

## Properties

```
@property (T@"TBDataSource",&,N,V_localDataSource) localDataSource;
@property (T@"TBDataSource",&,N,V_remoteDataSource) remoteDataSource;
@property (T@"<TBCacheProvider>",&,N,V_cacheProvider) cacheProvider;
```

## Instance methods

```
-[TBPreferLocalFetchDataSource localDataSource];
-[TBPreferLocalFetchDataSource setLocalDataSource:];
-[TBPreferLocalFetchDataSource cacheProvider];
-[TBPreferLocalFetchDataSource initWithLocalDataSource:remoteDataSource:cacheProvider:];
-[TBPreferLocalFetchDataSource remoteDataSource];
-[TBPreferLocalFetchDataSource setCacheProvider:];
-[TBPreferLocalFetchDataSource setRemoteDataSource:];
```
