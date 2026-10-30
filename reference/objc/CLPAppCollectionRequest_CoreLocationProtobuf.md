# `CLPAppCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _appLocations;
@"CLPMeta" _meta;
@"NSData" _signature;
```

## Properties

```
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_appLocations) appLocations;
@property (TB,R,N) hasSignature;
@property (T@"NSData",&,N,V_signature) signature;
```

## Class methods

```
+[CLPAppCollectionRequest appLocationType];
```

## Instance methods

```
-[CLPAppCollectionRequest writeTo:];
-[CLPAppCollectionRequest setSignature:];
-[CLPAppCollectionRequest responseClass];
-[CLPAppCollectionRequest appLocations];
-[CLPAppCollectionRequest setAppLocations:];
-[CLPAppCollectionRequest mergeFrom:];
-[CLPAppCollectionRequest signature];
-[CLPAppCollectionRequest requestTypeCode];
-[CLPAppCollectionRequest hash];
-[CLPAppCollectionRequest copyTo:];
-[CLPAppCollectionRequest description];
-[CLPAppCollectionRequest readFrom:];
-[CLPAppCollectionRequest copyWithZone:];
-[CLPAppCollectionRequest hasSignature];
-[CLPAppCollectionRequest isEqual:];
-[CLPAppCollectionRequest dictionaryRepresentation];
-[CLPAppCollectionRequest meta];
-[CLPAppCollectionRequest setMeta:];
-[CLPAppCollectionRequest addAppLocation:];
-[CLPAppCollectionRequest appLocationAtIndex:];
-[CLPAppCollectionRequest appLocationsCount];
-[CLPAppCollectionRequest clearAppLocations];
```
