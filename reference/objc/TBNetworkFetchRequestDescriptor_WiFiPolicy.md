# `TBNetworkFetchRequestDescriptor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchRequestDescriptor`, `NSCopying`
- 7 instance variables, 13 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSPredicate" _localFetchPredicate;
@"GEOWiFiQualityNetworkSearch" _remoteRequest;
Q _type;
@"NSDate" _maxCacheAge;
@"TBLocalFetchRequestDescriptor" _localFetchDescriptor;
@"TBLocalFetchRequestDescriptor" _preferLocalFetchDescriptor;
@"NSSet" _bssids;
```

## Properties

```
@property (T@"GEOWiFiQualityNetworkSearch",&,N,V_remoteRequest) remoteRequest;
@property (T@"NSPredicate",&,N,V_localFetchPredicate) localFetchPredicate;
@property (T@"NSSet",&,N,V_bssids) bssids;
@property (TQ,N,V_type) type;
@property (T@"NSDate",&,N,V_maxCacheAge) maxCacheAge;
@property (T@"TBLocalFetchRequestDescriptor",&,N,V_localFetchDescriptor) localFetchDescriptor;
@property (T@"TBLocalFetchRequestDescriptor",&,N,V_preferLocalFetchDescriptor) preferLocalFetchDescriptor;
@property (T#,R,N) remoteRequestClass;
@property (T@"NSSet",?,R,N) tileItems;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TBNetworkFetchRequestDescriptor init];
-[TBNetworkFetchRequestDescriptor setType:];
-[TBNetworkFetchRequestDescriptor type];
-[TBNetworkFetchRequestDescriptor copyWithZone:];
-[TBNetworkFetchRequestDescriptor remoteRequest];
-[TBNetworkFetchRequestDescriptor initWithBSSIDs:];
-[TBNetworkFetchRequestDescriptor setMaxCacheAge:];
-[TBNetworkFetchRequestDescriptor bssids];
-[TBNetworkFetchRequestDescriptor initWithBSSIDs:maxCacheAge:];
-[TBNetworkFetchRequestDescriptor localFetchDescriptor];
-[TBNetworkFetchRequestDescriptor localFetchPredicate];
-[TBNetworkFetchRequestDescriptor maxCacheAge];
-[TBNetworkFetchRequestDescriptor preferLocalFetchDescriptor];
-[TBNetworkFetchRequestDescriptor remoteRequestClass];
-[TBNetworkFetchRequestDescriptor setBssids:];
-[TBNetworkFetchRequestDescriptor setLocalFetchDescriptor:];
-[TBNetworkFetchRequestDescriptor setLocalFetchPredicate:];
-[TBNetworkFetchRequestDescriptor setPreferLocalFetchDescriptor:];
-[TBNetworkFetchRequestDescriptor setRemoteRequest:];
```
