# `CLPLocationCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 12 instance variables, 17 properties, 54 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _accessoryLocations;
@"CLPAccessoryMeta" _accessoryMeta;
@"NSString" _appBundleId;
@"NSMutableArray" _appBundleIds;
@"NSMutableArray" _locations;
i _mcc;
@"CLPMeta" _meta;
i _mnc;
@"CLPLocationProcessingPipelineMetadata" _pipelineMetadata;
i _rat;
@"NSString" _tripId;
{?="mcc"b1"mnc"b1"rat"b1} _has;
```

## Properties

```
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_locations) locations;
@property (TB,R,N) hasAppBundleId;
@property (T@"NSString",&,N,V_appBundleId) appBundleId;
@property (T@"NSString",&,N,V_tripId) tripId;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasMcc;
@property (Ti,N,V_mcc) mcc;
@property (TB,N) hasMnc;
@property (Ti,N,V_mnc) mnc;
@property (T@"NSMutableArray",&,N,V_appBundleIds) appBundleIds;
@property (TB,R,N) hasAccessoryMeta;
@property (T@"CLPAccessoryMeta",&,N,V_accessoryMeta) accessoryMeta;
@property (T@"NSMutableArray",&,N,V_accessoryLocations) accessoryLocations;
@property (TB,R,N) hasPipelineMetadata;
@property (T@"CLPLocationProcessingPipelineMetadata",&,N,V_pipelineMetadata) pipelineMetadata;
```

## Class methods

```
+[CLPLocationCollectionRequest locationType];
+[CLPLocationCollectionRequest accessoryLocationType];
+[CLPLocationCollectionRequest appBundleIdsType];
```

## Instance methods

```
-[CLPLocationCollectionRequest appBundleId];
-[CLPLocationCollectionRequest setLocations:];
-[CLPLocationCollectionRequest clearLocations];
-[CLPLocationCollectionRequest locations];
-[CLPLocationCollectionRequest writeTo:];
-[CLPLocationCollectionRequest responseClass];
-[CLPLocationCollectionRequest setAppBundleId:];
-[CLPLocationCollectionRequest mergeFrom:];
-[CLPLocationCollectionRequest hasAppBundleId];
-[CLPLocationCollectionRequest rat];
-[CLPLocationCollectionRequest mnc];
-[CLPLocationCollectionRequest requestTypeCode];
-[CLPLocationCollectionRequest addLocation:];
-[CLPLocationCollectionRequest hash];
-[CLPLocationCollectionRequest copyTo:];
-[CLPLocationCollectionRequest description];
-[CLPLocationCollectionRequest setMnc:];
-[CLPLocationCollectionRequest mcc];
-[CLPLocationCollectionRequest readFrom:];
-[CLPLocationCollectionRequest copyWithZone:];
-[CLPLocationCollectionRequest locationsCount];
-[CLPLocationCollectionRequest isEqual:];
-[CLPLocationCollectionRequest setMcc:];
-[CLPLocationCollectionRequest dictionaryRepresentation];
-[CLPLocationCollectionRequest locationAtIndex:];
-[CLPLocationCollectionRequest meta];
-[CLPLocationCollectionRequest setMeta:];
-[CLPLocationCollectionRequest setTripId:];
-[CLPLocationCollectionRequest tripId];
-[CLPLocationCollectionRequest setRat:];
-[CLPLocationCollectionRequest addAppBundleIds:];
-[CLPLocationCollectionRequest appBundleIds];
-[CLPLocationCollectionRequest appBundleIdsAtIndex:];
-[CLPLocationCollectionRequest appBundleIdsCount];
-[CLPLocationCollectionRequest clearAppBundleIds];
-[CLPLocationCollectionRequest hasRat];
-[CLPLocationCollectionRequest setAppBundleIds:];
-[CLPLocationCollectionRequest setHasRat:];
-[CLPLocationCollectionRequest accessoryLocationAtIndex:];
-[CLPLocationCollectionRequest accessoryLocations];
-[CLPLocationCollectionRequest accessoryLocationsCount];
-[CLPLocationCollectionRequest accessoryMeta];
-[CLPLocationCollectionRequest addAccessoryLocation:];
-[CLPLocationCollectionRequest clearAccessoryLocations];
-[CLPLocationCollectionRequest hasAccessoryMeta];
-[CLPLocationCollectionRequest hasMcc];
-[CLPLocationCollectionRequest hasMnc];
-[CLPLocationCollectionRequest hasPipelineMetadata];
-[CLPLocationCollectionRequest pipelineMetadata];
-[CLPLocationCollectionRequest setAccessoryLocations:];
-[CLPLocationCollectionRequest setAccessoryMeta:];
-[CLPLocationCollectionRequest setHasMcc:];
-[CLPLocationCollectionRequest setHasMnc:];
-[CLPLocationCollectionRequest setPipelineMetadata:];
```
