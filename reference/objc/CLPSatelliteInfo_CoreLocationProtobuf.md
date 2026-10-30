# `CLPSatelliteInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 10 properties, 40 instance methods, 0 class methods

## Instance variables

```
{?="list"^i"count"Q"size"Q} _azimuths;
{?="list"^i"count"Q"size"Q} _cnos;
{?="list"^i"count"Q"size"Q} _elevations;
{?="list"^B"count"Q"size"Q} _isUsedInFixes;
{?="list"^i"count"Q"size"Q} _satIds;
```

## Properties

```
@property (TQ,R,N) satIdsCount;
@property (T^i,R,N) satIds;
@property (TQ,R,N) cnosCount;
@property (T^i,R,N) cnos;
@property (TQ,R,N) azimuthsCount;
@property (T^i,R,N) azimuths;
@property (TQ,R,N) elevationsCount;
@property (T^i,R,N) elevations;
@property (TQ,R,N) isUsedInFixesCount;
@property (T^B,R,N) isUsedInFixes;
```

## Instance methods

```
-[CLPSatelliteInfo writeTo:];
-[CLPSatelliteInfo mergeFrom:];
-[CLPSatelliteInfo dealloc];
-[CLPSatelliteInfo hash];
-[CLPSatelliteInfo copyTo:];
-[CLPSatelliteInfo description];
-[CLPSatelliteInfo readFrom:];
-[CLPSatelliteInfo copyWithZone:];
-[CLPSatelliteInfo isEqual:];
-[CLPSatelliteInfo dictionaryRepresentation];
-[CLPSatelliteInfo elevations];
-[CLPSatelliteInfo clearElevations];
-[CLPSatelliteInfo elevationsCount];
-[CLPSatelliteInfo addAzimuths:];
-[CLPSatelliteInfo addCnos:];
-[CLPSatelliteInfo addElevations:];
-[CLPSatelliteInfo addIsUsedInFixes:];
-[CLPSatelliteInfo addSatIds:];
-[CLPSatelliteInfo azimuths];
-[CLPSatelliteInfo azimuthsAtIndex:];
-[CLPSatelliteInfo azimuthsCount];
-[CLPSatelliteInfo clearAzimuths];
-[CLPSatelliteInfo clearCnos];
-[CLPSatelliteInfo clearIsUsedInFixes];
-[CLPSatelliteInfo clearSatIds];
-[CLPSatelliteInfo cnos];
-[CLPSatelliteInfo cnosAtIndex:];
-[CLPSatelliteInfo cnosCount];
-[CLPSatelliteInfo elevationsAtIndex:];
-[CLPSatelliteInfo isUsedInFixes];
-[CLPSatelliteInfo isUsedInFixesAtIndex:];
-[CLPSatelliteInfo isUsedInFixesCount];
-[CLPSatelliteInfo satIds];
-[CLPSatelliteInfo satIdsAtIndex:];
-[CLPSatelliteInfo satIdsCount];
-[CLPSatelliteInfo setAzimuths:count:];
-[CLPSatelliteInfo setCnos:count:];
-[CLPSatelliteInfo setElevations:count:];
-[CLPSatelliteInfo setIsUsedInFixes:count:];
-[CLPSatelliteInfo setSatIds:count:];
```
