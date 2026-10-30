# `WiFi3BarsSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAvailabilitySource`
- 9 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
@? changeHandler;
@? relevancyHandler;
@? removalHandler;
Q _cacheExpirationInDays;
@"NSMutableDictionary" _networks;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSURL" _storeURL;
@"TBDataSourceMediator" _sourceMediator;
@"WiFi3BarsTileFetcher" _tileFetcher;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_networks) networks;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSURL",C,N,V_storeURL) storeURL;
@property (T@"TBDataSourceMediator",&,N,V_sourceMediator) sourceMediator;
@property (T@"WiFi3BarsTileFetcher",&,N,V_tileFetcher) tileFetcher;
@property (TQ,N,V_cacheExpirationInDays) cacheExpirationInDays;
@property (T@?,C,N,VchangeHandler) changeHandler;
@property (T@?,C,N,VrelevancyHandler) relevancyHandler;
@property (T@?,C,N,VremovalHandler) removalHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFi3BarsSource setNetworks:];
-[WiFi3BarsSource networks];
-[WiFi3BarsSource storeURL];
-[WiFi3BarsSource queue];
-[WiFi3BarsSource setChangeHandler:];
-[WiFi3BarsSource changeHandler];
-[WiFi3BarsSource setStoreURL:];
-[WiFi3BarsSource setQueue:];
-[WiFi3BarsSource setTileFetcher:];
-[WiFi3BarsSource _descriptorForType:];
-[WiFi3BarsSource _handleRemoteFetchResponse:];
-[WiFi3BarsSource _matchSearchBSSIDs:toResponse:];
-[WiFi3BarsSource cacheExpirationInDays];
-[WiFi3BarsSource fetch3BarsNetworksFor:];
-[WiFi3BarsSource fetch3BarsNetworksForDestinationAirportWithCompletionHandler:];
-[WiFi3BarsSource fetch3BarsNetworksForLocation:forceRemote:trigger:completionHandler:];
-[WiFi3BarsSource fetch3BarsNetworksPredictedForLocation:duration:maxLocations:completionHandler:];
-[WiFi3BarsSource fetchCandidateNetworksMatchingBSSIDs:completionHandler:];
-[WiFi3BarsSource forceFetch3BarsNetworkMatchingBSSID:completionHandler:];
-[WiFi3BarsSource initWithChangeHandler:localStoreType:];
-[WiFi3BarsSource prune3BarsNetworks:completionHandler:];
-[WiFi3BarsSource relevancyHandler];
-[WiFi3BarsSource relevantNetworks];
-[WiFi3BarsSource removalHandler];
-[WiFi3BarsSource setCacheExpirationInDays:];
-[WiFi3BarsSource setRelevancyHandler:];
-[WiFi3BarsSource setRemovalHandler:];
-[WiFi3BarsSource setSourceMediator:];
-[WiFi3BarsSource sourceMediator];
-[WiFi3BarsSource submitCacheAnalyticsEvent];
-[WiFi3BarsSource tileFetcher];
```
