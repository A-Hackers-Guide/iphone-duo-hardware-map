# `TUMetadataCacheDataProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"<TUMetadataCacheDataProviderDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _providerCache;
@"NSMutableDictionary" _providerDictCache;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSMutableDictionary",R,N,V_providerCache) providerCache;
@property (T@"NSMutableDictionary",R,N,V_providerDictCache) providerDictCache;
@property (T@"<TUMetadataCacheDataProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisEmpty) empty;
```

## Class methods

```
+[TUMetadataCacheDataProvider classIdentifier];
```

## Instance methods

```
-[TUMetadataCacheDataProvider invalidateCache];
-[TUMetadataCacheDataProvider initWithQueue:];
-[TUMetadataCacheDataProvider init];
-[TUMetadataCacheDataProvider refresh];
-[TUMetadataCacheDataProvider queue];
-[TUMetadataCacheDataProvider setDelegate:];
-[TUMetadataCacheDataProvider isEmpty];
-[TUMetadataCacheDataProvider delegate];
-[TUMetadataCacheDataProvider description];
-[TUMetadataCacheDataProvider _invalidateCache];
-[TUMetadataCacheDataProvider metadataDictForDestinationID:];
-[TUMetadataCacheDataProvider metadataForDestinationID:];
-[TUMetadataCacheDataProvider providerCache];
-[TUMetadataCacheDataProvider providerDictCache];
-[TUMetadataCacheDataProvider setMetadataDict:forDestinationID:];
-[TUMetadataCacheDataProvider setObject:forDestinationID:];
-[TUMetadataCacheDataProvider updateCacheWithDestinationIDs:withGroup:];
```
