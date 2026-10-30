# `TBRemoteFetchTileItem`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBFetchResponseTileItem`
- 4 instance variables, 8 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSError" _error;
@"NSArray" _networks;
Q _status;
@"<TBTile>" _tile;
```

## Properties

```
@property (TQ,R,N,V_status) status;
@property (T@"<TBTile>",R,N,V_tile) tile;
@property (T@"NSArray",R,N,V_networks) networks;
@property (T@"NSError",R,N,V_error) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TBRemoteFetchTileItem networks];
-[TBRemoteFetchTileItem status];
-[TBRemoteFetchTileItem error];
-[TBRemoteFetchTileItem tile];
-[TBRemoteFetchTileItem initWithTile:status:etag:error:];
-[TBRemoteFetchTileItem initWithEmptyTileKey:etag:error:];
```
