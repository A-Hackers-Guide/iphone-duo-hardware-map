# `CLPPassCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"CLPMeta" _meta;
@"NSMutableArray" _passLocations;
@"NSData" _signature;
```

## Properties

```
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_passLocations) passLocations;
@property (TB,R,N) hasSignature;
@property (T@"NSData",&,N,V_signature) signature;
```

## Class methods

```
+[CLPPassCollectionRequest passLocationType];
```

## Instance methods

```
-[CLPPassCollectionRequest writeTo:];
-[CLPPassCollectionRequest setSignature:];
-[CLPPassCollectionRequest responseClass];
-[CLPPassCollectionRequest mergeFrom:];
-[CLPPassCollectionRequest signature];
-[CLPPassCollectionRequest requestTypeCode];
-[CLPPassCollectionRequest hash];
-[CLPPassCollectionRequest copyTo:];
-[CLPPassCollectionRequest description];
-[CLPPassCollectionRequest readFrom:];
-[CLPPassCollectionRequest copyWithZone:];
-[CLPPassCollectionRequest hasSignature];
-[CLPPassCollectionRequest isEqual:];
-[CLPPassCollectionRequest dictionaryRepresentation];
-[CLPPassCollectionRequest meta];
-[CLPPassCollectionRequest setMeta:];
-[CLPPassCollectionRequest addPassLocation:];
-[CLPPassCollectionRequest clearPassLocations];
-[CLPPassCollectionRequest passLocationAtIndex:];
-[CLPPassCollectionRequest passLocations];
-[CLPPassCollectionRequest passLocationsCount];
-[CLPPassCollectionRequest setPassLocations:];
```
