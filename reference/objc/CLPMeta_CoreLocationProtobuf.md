# `CLPMeta`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 7 properties, 26 instance methods, 1 class methods

## Instance variables

```
q _submissionId;
@"NSString" _probeId;
@"NSString" _productId;
@"NSMutableArray" _regulatoryDomainEstimates;
@"NSString" _softwareVersion;
{?="submissionId"b1} _has;
```

## Properties

```
@property (T@"NSString",&,N,V_productId) productId;
@property (T@"NSString",&,N,V_softwareVersion) softwareVersion;
@property (TB,N) hasSubmissionId;
@property (Tq,N,V_submissionId) submissionId;
@property (TB,R,N) hasProbeId;
@property (T@"NSString",&,N,V_probeId) probeId;
@property (T@"NSMutableArray",&,N,V_regulatoryDomainEstimates) regulatoryDomainEstimates;
```

## Class methods

```
+[CLPMeta regulatoryDomainEstimatesType];
```

## Instance methods

```
-[CLPMeta softwareVersion];
-[CLPMeta productId];
-[CLPMeta writeTo:];
-[CLPMeta mergeFrom:];
-[CLPMeta hash];
-[CLPMeta copyTo:];
-[CLPMeta description];
-[CLPMeta readFrom:];
-[CLPMeta copyWithZone:];
-[CLPMeta isEqual:];
-[CLPMeta dictionaryRepresentation];
-[CLPMeta setSoftwareVersion:];
-[CLPMeta setProductId:];
-[CLPMeta hasSubmissionId];
-[CLPMeta probeId];
-[CLPMeta addRegulatoryDomainEstimates:];
-[CLPMeta clearRegulatoryDomainEstimates];
-[CLPMeta hasProbeId];
-[CLPMeta regulatoryDomainEstimates];
-[CLPMeta regulatoryDomainEstimatesAtIndex:];
-[CLPMeta regulatoryDomainEstimatesCount];
-[CLPMeta setHasSubmissionId:];
-[CLPMeta setProbeId:];
-[CLPMeta setRegulatoryDomainEstimates:];
-[CLPMeta setSubmissionId:];
-[CLPMeta submissionId];
```
