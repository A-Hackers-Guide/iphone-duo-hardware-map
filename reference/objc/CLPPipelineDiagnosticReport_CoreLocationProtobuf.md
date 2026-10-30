# `CLPPipelineDiagnosticReport`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 15 instance variables, 28 properties, 74 instance methods, 0 class methods

## Instance variables

```
{?="list"^d"count"Q"size"Q} _prbOnFloorEstimates;
d _prbCoarseIndoorSaysIndoor;
d _prbGpsSaysIndoor;
d _prbInjectionGainRetryLimitOk;
d _prbInjectionOccupancyRetryLimitOk;
d _prbInlierEstimate;
d _prbLocalizerIoWrapperSaysWifiOk;
d _prbOnFloorsEstimate;
d _prbParticleFilterSaysYield;
d _prbPipelinedSaysYield;
d _prbWifiSaysIndoor;
i _pfYieldStatusBeforeCalculatePose;
i _yieldStatusBeforeCalculatePose;
i _yieldType;
{?="prbCoarseIndoorSaysIndoor"b1"prbGpsSaysIndoor"b1"prbInjectionGainRetryLimitOk"b1"prbInjectionOccupancyRetryLimitOk"b1"prbInlierEstimate"b1"prbLocalizerIoWrapperSaysWifiOk"b1"prbOnFloorsEstimate"b1"prbParticleFilterSaysYield"b1"prbPipelinedSaysYield"b1"prbWifiSaysIndoor"b1"pfYieldStatusBeforeCalculatePose"b1"yieldStatusBeforeCalculatePose"b1"yieldType"b1} _has;
```

## Properties

```
@property (TB,N) hasYieldType;
@property (Ti,N,V_yieldType) yieldType;
@property (TB,N) hasPrbPipelinedSaysYield;
@property (Td,N,V_prbPipelinedSaysYield) prbPipelinedSaysYield;
@property (TB,N) hasPrbCoarseIndoorSaysIndoor;
@property (Td,N,V_prbCoarseIndoorSaysIndoor) prbCoarseIndoorSaysIndoor;
@property (TB,N) hasPrbWifiSaysIndoor;
@property (Td,N,V_prbWifiSaysIndoor) prbWifiSaysIndoor;
@property (TB,N) hasPrbGpsSaysIndoor;
@property (Td,N,V_prbGpsSaysIndoor) prbGpsSaysIndoor;
@property (TB,N) hasPrbParticleFilterSaysYield;
@property (Td,N,V_prbParticleFilterSaysYield) prbParticleFilterSaysYield;
@property (TB,N) hasPrbOnFloorsEstimate;
@property (Td,N,V_prbOnFloorsEstimate) prbOnFloorsEstimate;
@property (TQ,R,N) prbOnFloorEstimatesCount;
@property (T^d,R,N) prbOnFloorEstimates;
@property (TB,N) hasPrbInlierEstimate;
@property (Td,N,V_prbInlierEstimate) prbInlierEstimate;
@property (TB,N) hasPrbLocalizerIoWrapperSaysWifiOk;
@property (Td,N,V_prbLocalizerIoWrapperSaysWifiOk) prbLocalizerIoWrapperSaysWifiOk;
@property (TB,N) hasPrbInjectionOccupancyRetryLimitOk;
@property (Td,N,V_prbInjectionOccupancyRetryLimitOk) prbInjectionOccupancyRetryLimitOk;
@property (TB,N) hasPrbInjectionGainRetryLimitOk;
@property (Td,N,V_prbInjectionGainRetryLimitOk) prbInjectionGainRetryLimitOk;
@property (TB,N) hasPfYieldStatusBeforeCalculatePose;
@property (Ti,N,V_pfYieldStatusBeforeCalculatePose) pfYieldStatusBeforeCalculatePose;
@property (TB,N) hasYieldStatusBeforeCalculatePose;
@property (Ti,N,V_yieldStatusBeforeCalculatePose) yieldStatusBeforeCalculatePose;
```

## Instance methods

```
-[CLPPipelineDiagnosticReport writeTo:];
-[CLPPipelineDiagnosticReport mergeFrom:];
-[CLPPipelineDiagnosticReport dealloc];
-[CLPPipelineDiagnosticReport hash];
-[CLPPipelineDiagnosticReport copyTo:];
-[CLPPipelineDiagnosticReport description];
-[CLPPipelineDiagnosticReport readFrom:];
-[CLPPipelineDiagnosticReport copyWithZone:];
-[CLPPipelineDiagnosticReport isEqual:];
-[CLPPipelineDiagnosticReport dictionaryRepresentation];
-[CLPPipelineDiagnosticReport StringAsPfYieldStatusBeforeCalculatePose:];
-[CLPPipelineDiagnosticReport StringAsYieldType:];
-[CLPPipelineDiagnosticReport prbLocalizerIoWrapperSaysWifiOk];
-[CLPPipelineDiagnosticReport StringAsYieldStatusBeforeCalculatePose:];
-[CLPPipelineDiagnosticReport hasPrbInjectionGainRetryLimitOk];
-[CLPPipelineDiagnosticReport addPrbOnFloorEstimate:];
-[CLPPipelineDiagnosticReport clearPrbOnFloorEstimates];
-[CLPPipelineDiagnosticReport hasPfYieldStatusBeforeCalculatePose];
-[CLPPipelineDiagnosticReport hasPrbCoarseIndoorSaysIndoor];
-[CLPPipelineDiagnosticReport hasPrbGpsSaysIndoor];
-[CLPPipelineDiagnosticReport hasPrbInjectionOccupancyRetryLimitOk];
-[CLPPipelineDiagnosticReport hasPrbInlierEstimate];
-[CLPPipelineDiagnosticReport hasPrbLocalizerIoWrapperSaysWifiOk];
-[CLPPipelineDiagnosticReport hasPrbOnFloorsEstimate];
-[CLPPipelineDiagnosticReport hasPrbParticleFilterSaysYield];
-[CLPPipelineDiagnosticReport hasPrbPipelinedSaysYield];
-[CLPPipelineDiagnosticReport hasPrbWifiSaysIndoor];
-[CLPPipelineDiagnosticReport hasYieldStatusBeforeCalculatePose];
-[CLPPipelineDiagnosticReport hasYieldType];
-[CLPPipelineDiagnosticReport pfYieldStatusBeforeCalculatePose];
-[CLPPipelineDiagnosticReport pfYieldStatusBeforeCalculatePoseAsString:];
-[CLPPipelineDiagnosticReport prbCoarseIndoorSaysIndoor];
-[CLPPipelineDiagnosticReport prbGpsSaysIndoor];
-[CLPPipelineDiagnosticReport prbInjectionGainRetryLimitOk];
-[CLPPipelineDiagnosticReport prbInjectionOccupancyRetryLimitOk];
-[CLPPipelineDiagnosticReport prbInlierEstimate];
-[CLPPipelineDiagnosticReport prbOnFloorEstimateAtIndex:];
-[CLPPipelineDiagnosticReport prbOnFloorEstimates];
-[CLPPipelineDiagnosticReport prbOnFloorEstimatesCount];
-[CLPPipelineDiagnosticReport prbOnFloorsEstimate];
-[CLPPipelineDiagnosticReport prbParticleFilterSaysYield];
-[CLPPipelineDiagnosticReport prbPipelinedSaysYield];
-[CLPPipelineDiagnosticReport prbWifiSaysIndoor];
-[CLPPipelineDiagnosticReport setHasPfYieldStatusBeforeCalculatePose:];
-[CLPPipelineDiagnosticReport setHasPrbCoarseIndoorSaysIndoor:];
-[CLPPipelineDiagnosticReport setHasPrbGpsSaysIndoor:];
-[CLPPipelineDiagnosticReport setHasPrbInjectionGainRetryLimitOk:];
-[CLPPipelineDiagnosticReport setHasPrbInjectionOccupancyRetryLimitOk:];
-[CLPPipelineDiagnosticReport setHasPrbInlierEstimate:];
-[CLPPipelineDiagnosticReport setHasPrbLocalizerIoWrapperSaysWifiOk:];
-[CLPPipelineDiagnosticReport setHasPrbOnFloorsEstimate:];
-[CLPPipelineDiagnosticReport setHasPrbParticleFilterSaysYield:];
-[CLPPipelineDiagnosticReport setHasPrbPipelinedSaysYield:];
-[CLPPipelineDiagnosticReport setHasPrbWifiSaysIndoor:];
-[CLPPipelineDiagnosticReport setHasYieldStatusBeforeCalculatePose:];
-[CLPPipelineDiagnosticReport setHasYieldType:];
-[CLPPipelineDiagnosticReport setPfYieldStatusBeforeCalculatePose:];
-[CLPPipelineDiagnosticReport setPrbCoarseIndoorSaysIndoor:];
-[CLPPipelineDiagnosticReport setPrbGpsSaysIndoor:];
-[CLPPipelineDiagnosticReport setPrbInjectionGainRetryLimitOk:];
-[CLPPipelineDiagnosticReport setPrbInjectionOccupancyRetryLimitOk:];
-[CLPPipelineDiagnosticReport setPrbInlierEstimate:];
-[CLPPipelineDiagnosticReport setPrbLocalizerIoWrapperSaysWifiOk:];
-[CLPPipelineDiagnosticReport setPrbOnFloorEstimates:count:];
-[CLPPipelineDiagnosticReport setPrbOnFloorsEstimate:];
-[CLPPipelineDiagnosticReport setPrbParticleFilterSaysYield:];
-[CLPPipelineDiagnosticReport setPrbPipelinedSaysYield:];
-[CLPPipelineDiagnosticReport setPrbWifiSaysIndoor:];
-[CLPPipelineDiagnosticReport setYieldStatusBeforeCalculatePose:];
-[CLPPipelineDiagnosticReport setYieldType:];
-[CLPPipelineDiagnosticReport yieldStatusBeforeCalculatePose];
-[CLPPipelineDiagnosticReport yieldStatusBeforeCalculatePoseAsString:];
-[CLPPipelineDiagnosticReport yieldType];
-[CLPPipelineDiagnosticReport yieldTypeAsString:];
```
