# `TBLocationFetchRequestDescriptor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchRequestDescriptor`, `NSCopying`
- 10 instance variables, 15 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSPredicate" _localFetchPredicate;
@"PBCodable" _remoteRequest;
Q _type;
@"NSDate" _maxCacheAge;
@"TBLocalFetchRequestDescriptor" _localFetchDescriptor;
@"TBLocalFetchRequestDescriptor" _preferLocalFetchDescriptor;
@"NSSet" _tileItems;
Q _primaryTileKey;
d _latitude;
d _longitude;
```

## Properties

```
@property (T@"NSPredicate",&,N,V_localFetchPredicate) localFetchPredicate;
@property (TQ,N,V_type) type;
@property (T@"NSSet",&,N,V_tileItems) tileItems;
@property (TQ,N,V_primaryTileKey) primaryTileKey;
@property (T@"NSDate",&,N,V_maxCacheAge) maxCacheAge;
@property (Td,N,V_latitude) latitude;
@property (Td,N,V_longitude) longitude;
@property (T@"TBLocalFetchRequestDescriptor",&,N,V_localFetchDescriptor) localFetchDescriptor;
@property (T@"TBLocalFetchRequestDescriptor",&,N,V_preferLocalFetchDescriptor) preferLocalFetchDescriptor;
@property (T@"PBCodable",R,N,V_remoteRequest) remoteRequest;
@property (T#,R,N) remoteRequestClass;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TBLocationFetchRequestDescriptor setLatitude:];
-[TBLocationFetchRequestDescriptor latitude];
-[TBLocationFetchRequestDescriptor longitude];
-[TBLocationFetchRequestDescriptor setLongitude:];
-[TBLocationFetchRequestDescriptor setType:];
-[TBLocationFetchRequestDescriptor type];
-[TBLocationFetchRequestDescriptor initWithLatitude:longitude:];
-[TBLocationFetchRequestDescriptor copyWithZone:];
-[TBLocationFetchRequestDescriptor remoteRequest];
-[TBLocationFetchRequestDescriptor setMaxCacheAge:];
-[TBLocationFetchRequestDescriptor _localFetchRequest];
-[TBLocationFetchRequestDescriptor _preferLocalCacheFetchRequest];
-[TBLocationFetchRequestDescriptor initWithLatitude:longitude:maxCacheAge:];
-[TBLocationFetchRequestDescriptor initWithLatitude:longitude:radius:maxCacheAge:];
-[TBLocationFetchRequestDescriptor localFetchDescriptor];
-[TBLocationFetchRequestDescriptor localFetchPredicate];
-[TBLocationFetchRequestDescriptor maxCacheAge];
-[TBLocationFetchRequestDescriptor preferLocalFetchDescriptor];
-[TBLocationFetchRequestDescriptor primaryTileKey];
-[TBLocationFetchRequestDescriptor remoteRequestClass];
-[TBLocationFetchRequestDescriptor setLocalFetchDescriptor:];
-[TBLocationFetchRequestDescriptor setLocalFetchPredicate:];
-[TBLocationFetchRequestDescriptor setPreferLocalFetchDescriptor:];
-[TBLocationFetchRequestDescriptor setPrimaryTileKey:];
-[TBLocationFetchRequestDescriptor setTileItems:];
-[TBLocationFetchRequestDescriptor tileItems];
```
