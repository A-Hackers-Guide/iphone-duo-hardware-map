# `CLPAltimeterCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 10 instance variables, 15 properties, 50 instance methods, 3 class methods

## Instance variables

```
d _startTimestamp;
d _stopTimestamp;
i _collectionType;
@"CLPContext" _context;
@"CLPLocation" _location;
@"NSMutableArray" _locations;
@"CLPMeta" _meta;
@"NSMutableArray" _pressures;
@"NSMutableArray" _wifiScans;
{?="startTimestamp"b1"stopTimestamp"b1"collectionType"b1} _has;
```

## Properties

```
@property (TB,R,N) hasMeta;
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (TB,N) hasStartTimestamp;
@property (Td,N,V_startTimestamp) startTimestamp;
@property (TB,N) hasStopTimestamp;
@property (Td,N,V_stopTimestamp) stopTimestamp;
@property (TB,N) hasCollectionType;
@property (Ti,N,V_collectionType) collectionType;
@property (TB,R,N) hasContext;
@property (T@"CLPContext",&,N,V_context) context;
@property (TB,R,N) hasLocation;
@property (T@"CLPLocation",&,N,V_location) location;
@property (T@"NSMutableArray",&,N,V_pressures) pressures;
@property (T@"NSMutableArray",&,N,V_wifiScans) wifiScans;
@property (T@"NSMutableArray",&,N,V_locations) locations;
```

## Class methods

```
+[CLPAltimeterCollectionRequest locationsType];
+[CLPAltimeterCollectionRequest pressureType];
+[CLPAltimeterCollectionRequest wifiScanType];
```

## Instance methods

```
-[CLPAltimeterCollectionRequest collectionType];
-[CLPAltimeterCollectionRequest setLocations:];
-[CLPAltimeterCollectionRequest clearLocations];
-[CLPAltimeterCollectionRequest locations];
-[CLPAltimeterCollectionRequest writeTo:];
-[CLPAltimeterCollectionRequest setStartTimestamp:];
-[CLPAltimeterCollectionRequest hasLocation];
-[CLPAltimeterCollectionRequest location];
-[CLPAltimeterCollectionRequest mergeFrom:];
-[CLPAltimeterCollectionRequest hasContext];
-[CLPAltimeterCollectionRequest addLocations:];
-[CLPAltimeterCollectionRequest startTimestamp];
-[CLPAltimeterCollectionRequest setContext:];
-[CLPAltimeterCollectionRequest setLocation:];
-[CLPAltimeterCollectionRequest setCollectionType:];
-[CLPAltimeterCollectionRequest hash];
-[CLPAltimeterCollectionRequest copyTo:];
-[CLPAltimeterCollectionRequest description];
-[CLPAltimeterCollectionRequest readFrom:];
-[CLPAltimeterCollectionRequest copyWithZone:];
-[CLPAltimeterCollectionRequest locationsCount];
-[CLPAltimeterCollectionRequest context];
-[CLPAltimeterCollectionRequest isEqual:];
-[CLPAltimeterCollectionRequest dictionaryRepresentation];
-[CLPAltimeterCollectionRequest locationsAtIndex:];
-[CLPAltimeterCollectionRequest meta];
-[CLPAltimeterCollectionRequest setMeta:];
-[CLPAltimeterCollectionRequest hasStartTimestamp];
-[CLPAltimeterCollectionRequest setHasStartTimestamp:];
-[CLPAltimeterCollectionRequest hasCollectionType];
-[CLPAltimeterCollectionRequest setHasCollectionType:];
-[CLPAltimeterCollectionRequest StringAsCollectionType:];
-[CLPAltimeterCollectionRequest hasMeta];
-[CLPAltimeterCollectionRequest addPressure:];
-[CLPAltimeterCollectionRequest addWifiScan:];
-[CLPAltimeterCollectionRequest clearPressures];
-[CLPAltimeterCollectionRequest clearWifiScans];
-[CLPAltimeterCollectionRequest collectionTypeAsString:];
-[CLPAltimeterCollectionRequest hasStopTimestamp];
-[CLPAltimeterCollectionRequest pressureAtIndex:];
-[CLPAltimeterCollectionRequest pressures];
-[CLPAltimeterCollectionRequest pressuresCount];
-[CLPAltimeterCollectionRequest setHasStopTimestamp:];
-[CLPAltimeterCollectionRequest setPressures:];
-[CLPAltimeterCollectionRequest setStopTimestamp:];
-[CLPAltimeterCollectionRequest setWifiScans:];
-[CLPAltimeterCollectionRequest stopTimestamp];
-[CLPAltimeterCollectionRequest wifiScanAtIndex:];
-[CLPAltimeterCollectionRequest wifiScans];
-[CLPAltimeterCollectionRequest wifiScansCount];
```
