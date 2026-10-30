# `TBGloriaTile`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBTile`
- 10 instance variables, 17 properties, 25 instance methods, 2 class methods

## Instance variables

```
C _zoom;
Q _key;
d _lat;
d _lng;
@"NSString" _WKTString;
d _tileSize;
d _north;
d _south;
d _east;
d _west;
```

## Properties

```
@property (Td,N,V_lat) lat;
@property (Td,N,V_lng) lng;
@property (TC,N,V_zoom) zoom;
@property (TQ,N,V_key) key;
@property (Td,N,V_north) north;
@property (Td,N,V_south) south;
@property (Td,N,V_east) east;
@property (Td,N,V_west) west;
@property (T@"NSString",C,N,V_WKTString) WKTString;
@property (Td,N,V_tileSize) tileSize;
@property (T@"NSDate",?,R,C,N) created;
@property (T@"NSString",?,&,N) etag;
@property (TQ,?,R,N) networkCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBGloriaTile defaultZoomLevel];
+[TBGloriaTile gloriaTileWithLat:lng:zoom:];
```

## Instance methods

```
-[TBGloriaTile setZoom:];
-[TBGloriaTile tileSize];
-[TBGloriaTile setLat:];
-[TBGloriaTile setKey:];
-[TBGloriaTile zoom];
-[TBGloriaTile lat];
-[TBGloriaTile setLng:];
-[TBGloriaTile lng];
-[TBGloriaTile key];
-[TBGloriaTile setTileSize:];
-[TBGloriaTile WKTString];
-[TBGloriaTile adjacentTileKeysWithLevel:];
-[TBGloriaTile east];
-[TBGloriaTile initWithEncodedKey:zoom:];
-[TBGloriaTile initWithLat:lng:];
-[TBGloriaTile initWithLat:lng:zoom:];
-[TBGloriaTile neighborTileKeysWithRadius:];
-[TBGloriaTile north];
-[TBGloriaTile setEast:];
-[TBGloriaTile setNorth:];
-[TBGloriaTile setSouth:];
-[TBGloriaTile setWKTString:];
-[TBGloriaTile setWest:];
-[TBGloriaTile south];
-[TBGloriaTile west];
```
