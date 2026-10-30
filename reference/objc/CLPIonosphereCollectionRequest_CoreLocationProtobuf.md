# `CLPIonosphereCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 2 instance variables, 3 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _ionoDatas;
@"CLPMeta" _meta;
```

## Properties

```
@property (TB,R,N) hasMeta;
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_ionoDatas) ionoDatas;
```

## Class methods

```
+[CLPIonosphereCollectionRequest ionoDataType];
```

## Instance methods

```
-[CLPIonosphereCollectionRequest writeTo:];
-[CLPIonosphereCollectionRequest mergeFrom:];
-[CLPIonosphereCollectionRequest hash];
-[CLPIonosphereCollectionRequest copyTo:];
-[CLPIonosphereCollectionRequest description];
-[CLPIonosphereCollectionRequest readFrom:];
-[CLPIonosphereCollectionRequest copyWithZone:];
-[CLPIonosphereCollectionRequest isEqual:];
-[CLPIonosphereCollectionRequest dictionaryRepresentation];
-[CLPIonosphereCollectionRequest meta];
-[CLPIonosphereCollectionRequest setMeta:];
-[CLPIonosphereCollectionRequest hasMeta];
-[CLPIonosphereCollectionRequest addIonoData:];
-[CLPIonosphereCollectionRequest clearIonoDatas];
-[CLPIonosphereCollectionRequest ionoDataAtIndex:];
-[CLPIonosphereCollectionRequest ionoDatas];
-[CLPIonosphereCollectionRequest ionoDatasCount];
-[CLPIonosphereCollectionRequest setIonoDatas:];
```
