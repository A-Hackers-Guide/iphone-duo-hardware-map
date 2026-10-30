# `CLPPoiHarvest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 29 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _absoluteAltitudes;
@"NSMutableArray" _accessPoints;
@"NSMutableArray" _locations;
@"CLPPoiTriggerEvent" _triggerEvent;
```

## Properties

```
@property (T@"CLPPoiTriggerEvent",&,N,V_triggerEvent) triggerEvent;
@property (T@"NSMutableArray",&,N,V_locations) locations;
@property (T@"NSMutableArray",&,N,V_accessPoints) accessPoints;
@property (T@"NSMutableArray",&,N,V_absoluteAltitudes) absoluteAltitudes;
```

## Class methods

```
+[CLPPoiHarvest locationsType];
+[CLPPoiHarvest absoluteAltitudesType];
+[CLPPoiHarvest accessPointsType];
```

## Instance methods

```
-[CLPPoiHarvest triggerEvent];
-[CLPPoiHarvest setTriggerEvent:];
-[CLPPoiHarvest accessPoints];
-[CLPPoiHarvest setLocations:];
-[CLPPoiHarvest clearLocations];
-[CLPPoiHarvest locations];
-[CLPPoiHarvest writeTo:];
-[CLPPoiHarvest setAccessPoints:];
-[CLPPoiHarvest mergeFrom:];
-[CLPPoiHarvest addLocations:];
-[CLPPoiHarvest hash];
-[CLPPoiHarvest copyTo:];
-[CLPPoiHarvest description];
-[CLPPoiHarvest readFrom:];
-[CLPPoiHarvest copyWithZone:];
-[CLPPoiHarvest locationsCount];
-[CLPPoiHarvest isEqual:];
-[CLPPoiHarvest dictionaryRepresentation];
-[CLPPoiHarvest locationsAtIndex:];
-[CLPPoiHarvest accessPointsCount];
-[CLPPoiHarvest clearAccessPoints];
-[CLPPoiHarvest accessPointsAtIndex:];
-[CLPPoiHarvest addAccessPoints:];
-[CLPPoiHarvest absoluteAltitudes];
-[CLPPoiHarvest absoluteAltitudesAtIndex:];
-[CLPPoiHarvest absoluteAltitudesCount];
-[CLPPoiHarvest addAbsoluteAltitudes:];
-[CLPPoiHarvest clearAbsoluteAltitudes];
-[CLPPoiHarvest setAbsoluteAltitudes:];
```
