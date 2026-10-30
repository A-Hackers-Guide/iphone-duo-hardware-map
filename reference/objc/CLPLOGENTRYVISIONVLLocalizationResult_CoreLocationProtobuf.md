# `CLPLOGENTRYVISIONVLLocalizationResult`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 28 instance methods, 0 class methods

## Instance variables

```
f _confidence;
@"CLPLOGENTRYVISIONVLMatrixfMxN" _covariance;
@"CLPLOGENTRYVISIONVLLocalizationDebugInfo" _debugInfo;
@"CLPLOGENTRYVISIONVLLocation" _location;
@"CLPLOGENTRYVISIONTimeStamp" _timestamp;
@"CLPLOGENTRYVISIONSimdDoubleMxN" _transform;
{?="confidence"b1} _has;
```

## Properties

```
@property (TB,R,N) hasTimestamp;
@property (T@"CLPLOGENTRYVISIONTimeStamp",&,N,V_timestamp) timestamp;
@property (TB,R,N) hasLocation;
@property (T@"CLPLOGENTRYVISIONVLLocation",&,N,V_location) location;
@property (TB,R,N) hasTransform;
@property (T@"CLPLOGENTRYVISIONSimdDoubleMxN",&,N,V_transform) transform;
@property (TB,R,N) hasCovariance;
@property (T@"CLPLOGENTRYVISIONVLMatrixfMxN",&,N,V_covariance) covariance;
@property (TB,N) hasConfidence;
@property (Tf,N,V_confidence) confidence;
@property (TB,R,N) hasDebugInfo;
@property (T@"CLPLOGENTRYVISIONVLLocalizationDebugInfo",&,N,V_debugInfo) debugInfo;
```

## Instance methods

```
-[CLPLOGENTRYVISIONVLLocalizationResult hasTimestamp];
-[CLPLOGENTRYVISIONVLLocalizationResult setTimestamp:];
-[CLPLOGENTRYVISIONVLLocalizationResult writeTo:];
-[CLPLOGENTRYVISIONVLLocalizationResult hasLocation];
-[CLPLOGENTRYVISIONVLLocalizationResult debugInfo];
-[CLPLOGENTRYVISIONVLLocalizationResult location];
-[CLPLOGENTRYVISIONVLLocalizationResult mergeFrom:];
-[CLPLOGENTRYVISIONVLLocalizationResult setDebugInfo:];
-[CLPLOGENTRYVISIONVLLocalizationResult timestamp];
-[CLPLOGENTRYVISIONVLLocalizationResult setTransform:];
-[CLPLOGENTRYVISIONVLLocalizationResult transform];
-[CLPLOGENTRYVISIONVLLocalizationResult setConfidence:];
-[CLPLOGENTRYVISIONVLLocalizationResult hasConfidence];
-[CLPLOGENTRYVISIONVLLocalizationResult setLocation:];
-[CLPLOGENTRYVISIONVLLocalizationResult hash];
-[CLPLOGENTRYVISIONVLLocalizationResult copyTo:];
-[CLPLOGENTRYVISIONVLLocalizationResult description];
-[CLPLOGENTRYVISIONVLLocalizationResult readFrom:];
-[CLPLOGENTRYVISIONVLLocalizationResult copyWithZone:];
-[CLPLOGENTRYVISIONVLLocalizationResult isEqual:];
-[CLPLOGENTRYVISIONVLLocalizationResult setHasConfidence:];
-[CLPLOGENTRYVISIONVLLocalizationResult confidence];
-[CLPLOGENTRYVISIONVLLocalizationResult dictionaryRepresentation];
-[CLPLOGENTRYVISIONVLLocalizationResult covariance];
-[CLPLOGENTRYVISIONVLLocalizationResult setCovariance:];
-[CLPLOGENTRYVISIONVLLocalizationResult hasTransform];
-[CLPLOGENTRYVISIONVLLocalizationResult hasCovariance];
-[CLPLOGENTRYVISIONVLLocalizationResult hasDebugInfo];
```
