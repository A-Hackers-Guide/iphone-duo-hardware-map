# `TBMutableTileFetchResponse`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchResponse`
- 4 instance variables, 9 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSError" error;
@"NSArray" results;
@"NSDictionary" resultsByBSSID;
@"NSMutableSet" _mutableTiles;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_mutableTiles) mutableTiles;
@property (T@"NSArray",R,N,Vresults) results;
@property (T@"NSError",R,C,N,Verror) error;
@property (T@"NSSet",R,N) tiles;
@property (T@"NSDictionary",?,R,N,VresultsByBSSID) resultsByBSSID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TBMutableTileFetchResponse init];
-[TBMutableTileFetchResponse tiles];
-[TBMutableTileFetchResponse error];
-[TBMutableTileFetchResponse results];
-[TBMutableTileFetchResponse addResponse:];
-[TBMutableTileFetchResponse mutableTiles];
-[TBMutableTileFetchResponse resultsByBSSID];
-[TBMutableTileFetchResponse setMutableTiles:];
```
