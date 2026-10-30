# `CLPSatelliteReport`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"CLPSatelliteInfo" _galileo;
@"CLPSatelliteInfo" _glonass;
@"CLPSatelliteInfo" _gps;
@"CLPSatelliteInfo" _qzss;
```

## Properties

```
@property (TB,R,N) hasGps;
@property (T@"CLPSatelliteInfo",&,N,V_gps) gps;
@property (TB,R,N) hasGlonass;
@property (T@"CLPSatelliteInfo",&,N,V_glonass) glonass;
@property (TB,R,N) hasQzss;
@property (T@"CLPSatelliteInfo",&,N,V_qzss) qzss;
@property (TB,R,N) hasGalileo;
@property (T@"CLPSatelliteInfo",&,N,V_galileo) galileo;
```

## Instance methods

```
-[CLPSatelliteReport writeTo:];
-[CLPSatelliteReport mergeFrom:];
-[CLPSatelliteReport hash];
-[CLPSatelliteReport copyTo:];
-[CLPSatelliteReport description];
-[CLPSatelliteReport readFrom:];
-[CLPSatelliteReport copyWithZone:];
-[CLPSatelliteReport isEqual:];
-[CLPSatelliteReport dictionaryRepresentation];
-[CLPSatelliteReport gps];
-[CLPSatelliteReport galileo];
-[CLPSatelliteReport glonass];
-[CLPSatelliteReport hasQzss];
-[CLPSatelliteReport setGps:];
-[CLPSatelliteReport hasGalileo];
-[CLPSatelliteReport hasGlonass];
-[CLPSatelliteReport hasGps];
-[CLPSatelliteReport qzss];
-[CLPSatelliteReport setGalileo:];
-[CLPSatelliteReport setGlonass:];
-[CLPSatelliteReport setQzss:];
```
