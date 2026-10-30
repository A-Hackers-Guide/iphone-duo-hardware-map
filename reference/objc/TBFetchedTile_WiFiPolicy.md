# `TBFetchedTile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBTile`, `NSCopying`
- 3 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
Q _key;
@"NSString" _etag;
@"NSDate" _created;
```

## Properties

```
@property (TQ,N,V_key) key;
@property (T@"NSDate",C,N,V_created) created;
@property (T@"NSString",?,&,N,V_etag) etag;
@property (TQ,?,R,N) networkCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBFetchedTile fetchedTileWithKey:etag:created:];
```

## Instance methods

```
-[TBFetchedTile created];
-[TBFetchedTile etag];
-[TBFetchedTile setEtag:];
-[TBFetchedTile setKey:];
-[TBFetchedTile setCreated:];
-[TBFetchedTile hash];
-[TBFetchedTile description];
-[TBFetchedTile copyWithZone:];
-[TBFetchedTile isEqual:];
-[TBFetchedTile key];
-[TBFetchedTile _isEqualToFetchedTile:];
-[TBFetchedTile initWithKey:etag:created:];
```
