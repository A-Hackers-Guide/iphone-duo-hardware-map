# `TBTileFetchRequestDescriptor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchRequestDescriptor`, `NSCopying`
- 6 instance variables, 12 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"TBLocalFetchRequestDescriptor" _localFetchDescriptor;
Q _type;
@"NSSet" _tileItems;
@"TBLocalFetchRequestDescriptor" _preferLocalFetchDescriptor;
@"NSPredicate" _localFetchPredicate;
@"NSDate" _maxCacheAge;
```

## Properties

```
@property (T@"NSSet",&,N,V_tileItems) tileItems;
@property (T@"NSPredicate",&,N,V_localFetchPredicate) localFetchPredicate;
@property (TQ,N,V_type) type;
@property (T@"TBLocalFetchRequestDescriptor",&,N,V_localFetchDescriptor) localFetchDescriptor;
@property (T@"TBLocalFetchRequestDescriptor",&,N,V_preferLocalFetchDescriptor) preferLocalFetchDescriptor;
@property (T@"NSDate",&,N,V_maxCacheAge) maxCacheAge;
@property (T@"PBCodable",R,N) remoteRequest;
@property (T#,R,N) remoteRequestClass;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TBTileFetchRequestDescriptor setType:];
-[TBTileFetchRequestDescriptor type];
-[TBTileFetchRequestDescriptor copyWithZone:];
-[TBTileFetchRequestDescriptor remoteRequest];
-[TBTileFetchRequestDescriptor setMaxCacheAge:];
-[TBTileFetchRequestDescriptor _preferLocalCacheFetchRequest];
-[TBTileFetchRequestDescriptor initWithTileItems:];
-[TBTileFetchRequestDescriptor initWithTileItems:maxCacheAge:];
-[TBTileFetchRequestDescriptor localFetchDescriptor];
-[TBTileFetchRequestDescriptor localFetchPredicate];
-[TBTileFetchRequestDescriptor maxCacheAge];
-[TBTileFetchRequestDescriptor preferLocalFetchDescriptor];
-[TBTileFetchRequestDescriptor remoteRequestClass];
-[TBTileFetchRequestDescriptor setLocalFetchDescriptor:];
-[TBTileFetchRequestDescriptor setLocalFetchPredicate:];
-[TBTileFetchRequestDescriptor setPreferLocalFetchDescriptor:];
-[TBTileFetchRequestDescriptor setTileItems:];
-[TBTileFetchRequestDescriptor tileItems];
```
