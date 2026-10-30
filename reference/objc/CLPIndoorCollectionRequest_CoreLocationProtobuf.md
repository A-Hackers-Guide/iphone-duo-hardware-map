# `CLPIndoorCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 55 instance methods, 7 class methods

## Instance variables

```
@"NSMutableArray" _bundleIds;
@"NSMutableArray" _indoorCMAttitudes;
@"NSMutableArray" _indoorCMPedometers;
@"NSMutableArray" _indoorLocations;
@"NSMutableArray" _indoorMotionActivitys;
@"NSMutableArray" _indoorPressures;
@"NSMutableArray" _indoorWifis;
@"CLPMeta" _meta;
```

## Properties

```
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_indoorWifis) indoorWifis;
@property (T@"NSMutableArray",&,N,V_indoorLocations) indoorLocations;
@property (T@"NSMutableArray",&,N,V_indoorCMAttitudes) indoorCMAttitudes;
@property (T@"NSMutableArray",&,N,V_indoorCMPedometers) indoorCMPedometers;
@property (T@"NSMutableArray",&,N,V_indoorMotionActivitys) indoorMotionActivitys;
@property (T@"NSMutableArray",&,N,V_indoorPressures) indoorPressures;
@property (T@"NSMutableArray",&,N,V_bundleIds) bundleIds;
```

## Class methods

```
+[CLPIndoorCollectionRequest indoorWifisType];
+[CLPIndoorCollectionRequest bundleIdType];
+[CLPIndoorCollectionRequest indoorCMAttitudeType];
+[CLPIndoorCollectionRequest indoorCMPedometerType];
+[CLPIndoorCollectionRequest indoorLocationsType];
+[CLPIndoorCollectionRequest indoorMotionActivityType];
+[CLPIndoorCollectionRequest indoorPressureType];
```

## Instance methods

```
-[CLPIndoorCollectionRequest bundleIds];
-[CLPIndoorCollectionRequest writeTo:];
-[CLPIndoorCollectionRequest responseClass];
-[CLPIndoorCollectionRequest mergeFrom:];
-[CLPIndoorCollectionRequest requestTypeCode];
-[CLPIndoorCollectionRequest setBundleIds:];
-[CLPIndoorCollectionRequest hash];
-[CLPIndoorCollectionRequest copyTo:];
-[CLPIndoorCollectionRequest description];
-[CLPIndoorCollectionRequest readFrom:];
-[CLPIndoorCollectionRequest copyWithZone:];
-[CLPIndoorCollectionRequest isEqual:];
-[CLPIndoorCollectionRequest dictionaryRepresentation];
-[CLPIndoorCollectionRequest meta];
-[CLPIndoorCollectionRequest setMeta:];
-[CLPIndoorCollectionRequest addBundleId:];
-[CLPIndoorCollectionRequest bundleIdAtIndex:];
-[CLPIndoorCollectionRequest bundleIdsCount];
-[CLPIndoorCollectionRequest clearBundleIds];
-[CLPIndoorCollectionRequest addIndoorWifis:];
-[CLPIndoorCollectionRequest indoorLocations];
-[CLPIndoorCollectionRequest indoorPressures];
-[CLPIndoorCollectionRequest setIndoorWifis:];
-[CLPIndoorCollectionRequest addIndoorCMAttitude:];
-[CLPIndoorCollectionRequest addIndoorCMPedometer:];
-[CLPIndoorCollectionRequest addIndoorLocations:];
-[CLPIndoorCollectionRequest addIndoorMotionActivity:];
-[CLPIndoorCollectionRequest addIndoorPressure:];
-[CLPIndoorCollectionRequest clearIndoorCMAttitudes];
-[CLPIndoorCollectionRequest clearIndoorCMPedometers];
-[CLPIndoorCollectionRequest clearIndoorLocations];
-[CLPIndoorCollectionRequest clearIndoorMotionActivitys];
-[CLPIndoorCollectionRequest clearIndoorPressures];
-[CLPIndoorCollectionRequest clearIndoorWifis];
-[CLPIndoorCollectionRequest indoorCMAttitudeAtIndex:];
-[CLPIndoorCollectionRequest indoorCMAttitudes];
-[CLPIndoorCollectionRequest indoorCMAttitudesCount];
-[CLPIndoorCollectionRequest indoorCMPedometerAtIndex:];
-[CLPIndoorCollectionRequest indoorCMPedometers];
-[CLPIndoorCollectionRequest indoorCMPedometersCount];
-[CLPIndoorCollectionRequest indoorLocationsAtIndex:];
-[CLPIndoorCollectionRequest indoorLocationsCount];
-[CLPIndoorCollectionRequest indoorMotionActivityAtIndex:];
-[CLPIndoorCollectionRequest indoorMotionActivitys];
-[CLPIndoorCollectionRequest indoorMotionActivitysCount];
-[CLPIndoorCollectionRequest indoorPressureAtIndex:];
-[CLPIndoorCollectionRequest indoorPressuresCount];
-[CLPIndoorCollectionRequest indoorWifis];
-[CLPIndoorCollectionRequest indoorWifisAtIndex:];
-[CLPIndoorCollectionRequest indoorWifisCount];
-[CLPIndoorCollectionRequest setIndoorCMAttitudes:];
-[CLPIndoorCollectionRequest setIndoorCMPedometers:];
-[CLPIndoorCollectionRequest setIndoorLocations:];
-[CLPIndoorCollectionRequest setIndoorMotionActivitys:];
-[CLPIndoorCollectionRequest setIndoorPressures:];
```
