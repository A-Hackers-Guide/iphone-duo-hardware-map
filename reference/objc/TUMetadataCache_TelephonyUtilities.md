# `TUMetadataCache`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUMetadataCacheDataProviderDelegate`
- 2 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _providers;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSArray",R,C,N,V_providers) providers;
@property (TB,R,N,GisEmpty) empty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUMetadataCache classIdentifier];
```

## Instance methods

```
-[TUMetadataCache providers];
-[TUMetadataCache init];
-[TUMetadataCache queue];
-[TUMetadataCache isEmpty];
-[TUMetadataCache description];
-[TUMetadataCache _updateCacheWithDestinationIDs:onlyEmptyProviders:completion:];
-[TUMetadataCache dataProvider:requestedRefreshWithDestinationIDs:];
-[TUMetadataCache initWithDataProviders:];
-[TUMetadataCache initWithQueue:dataProviders:];
-[TUMetadataCache metadataForDestinationID:];
-[TUMetadataCache updateCacheForEmptyDataProvidersWithDestinationIDs:];
-[TUMetadataCache updateCacheForEmptyDataProvidersWithDestinationIDs:completion:];
-[TUMetadataCache updateCacheWithDestinationIDs:];
-[TUMetadataCache updateCacheWithDestinationIDs:completion:];
-[TUMetadataCache updateCacheWithDestinationIDs:didMakeChanges:];
```
