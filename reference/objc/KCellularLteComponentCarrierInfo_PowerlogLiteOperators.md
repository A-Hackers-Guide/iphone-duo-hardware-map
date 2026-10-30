# `KCellularLteComponentCarrierInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 13 instance variables, 23 properties, 65 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _carrierInfos;
i _pccBandwidth;
I _pccEarfcn;
I _pccRfBand;
i _scc0Bandwidth;
I _scc0Earfcn;
I _scc0RfBand;
i _scc1Bandwidth;
I _scc1Earfcn;
I _scc1RfBand;
I _subsId;
{?="timestamp"b1"pccBandwidth"b1"pccEarfcn"b1"pccRfBand"b1"scc0Bandwidth"b1"scc0Earfcn"b1"scc0RfBand"b1"scc1Bandwidth"b1"scc1Earfcn"b1"scc1RfBand"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasPccEarfcn;
@property (TI,N,V_pccEarfcn) pccEarfcn;
@property (TB,N) hasScc0Earfcn;
@property (TI,N,V_scc0Earfcn) scc0Earfcn;
@property (TB,N) hasScc1Earfcn;
@property (TI,N,V_scc1Earfcn) scc1Earfcn;
@property (TB,N) hasPccBandwidth;
@property (Ti,N,V_pccBandwidth) pccBandwidth;
@property (TB,N) hasScc0Bandwidth;
@property (Ti,N,V_scc0Bandwidth) scc0Bandwidth;
@property (TB,N) hasScc1Bandwidth;
@property (Ti,N,V_scc1Bandwidth) scc1Bandwidth;
@property (TB,N) hasPccRfBand;
@property (TI,N,V_pccRfBand) pccRfBand;
@property (TB,N) hasScc0RfBand;
@property (TI,N,V_scc0RfBand) scc0RfBand;
@property (TB,N) hasScc1RfBand;
@property (TI,N,V_scc1RfBand) scc1RfBand;
@property (T@"NSMutableArray",&,N,V_carrierInfos) carrierInfos;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Class methods

```
+[KCellularLteComponentCarrierInfo carrierInfoType];
```

## Instance methods

```
-[KCellularLteComponentCarrierInfo hasTimestamp];
-[KCellularLteComponentCarrierInfo setHasTimestamp:];
-[KCellularLteComponentCarrierInfo setTimestamp:];
-[KCellularLteComponentCarrierInfo writeTo:];
-[KCellularLteComponentCarrierInfo mergeFrom:];
-[KCellularLteComponentCarrierInfo timestamp];
-[KCellularLteComponentCarrierInfo hash];
-[KCellularLteComponentCarrierInfo copyTo:];
-[KCellularLteComponentCarrierInfo description];
-[KCellularLteComponentCarrierInfo readFrom:];
-[KCellularLteComponentCarrierInfo copyWithZone:];
-[KCellularLteComponentCarrierInfo isEqual:];
-[KCellularLteComponentCarrierInfo dictionaryRepresentation];
-[KCellularLteComponentCarrierInfo addCarrierInfo:];
-[KCellularLteComponentCarrierInfo carrierInfoAtIndex:];
-[KCellularLteComponentCarrierInfo carrierInfos];
-[KCellularLteComponentCarrierInfo carrierInfosCount];
-[KCellularLteComponentCarrierInfo clearCarrierInfos];
-[KCellularLteComponentCarrierInfo hasSubsId];
-[KCellularLteComponentCarrierInfo setCarrierInfos:];
-[KCellularLteComponentCarrierInfo setHasSubsId:];
-[KCellularLteComponentCarrierInfo setSubsId:];
-[KCellularLteComponentCarrierInfo subsId];
-[KCellularLteComponentCarrierInfo StringAsPccBandwidth:];
-[KCellularLteComponentCarrierInfo StringAsScc0Bandwidth:];
-[KCellularLteComponentCarrierInfo StringAsScc1Bandwidth:];
-[KCellularLteComponentCarrierInfo hasPccBandwidth];
-[KCellularLteComponentCarrierInfo hasPccEarfcn];
-[KCellularLteComponentCarrierInfo hasPccRfBand];
-[KCellularLteComponentCarrierInfo hasScc0Bandwidth];
-[KCellularLteComponentCarrierInfo hasScc0Earfcn];
-[KCellularLteComponentCarrierInfo hasScc0RfBand];
-[KCellularLteComponentCarrierInfo hasScc1Bandwidth];
-[KCellularLteComponentCarrierInfo hasScc1Earfcn];
-[KCellularLteComponentCarrierInfo hasScc1RfBand];
-[KCellularLteComponentCarrierInfo pccBandwidth];
-[KCellularLteComponentCarrierInfo pccBandwidthAsString:];
-[KCellularLteComponentCarrierInfo pccEarfcn];
-[KCellularLteComponentCarrierInfo pccRfBand];
-[KCellularLteComponentCarrierInfo scc0Bandwidth];
-[KCellularLteComponentCarrierInfo scc0BandwidthAsString:];
-[KCellularLteComponentCarrierInfo scc0Earfcn];
-[KCellularLteComponentCarrierInfo scc0RfBand];
-[KCellularLteComponentCarrierInfo scc1Bandwidth];
-[KCellularLteComponentCarrierInfo scc1BandwidthAsString:];
-[KCellularLteComponentCarrierInfo scc1Earfcn];
-[KCellularLteComponentCarrierInfo scc1RfBand];
-[KCellularLteComponentCarrierInfo setHasPccBandwidth:];
-[KCellularLteComponentCarrierInfo setHasPccEarfcn:];
-[KCellularLteComponentCarrierInfo setHasPccRfBand:];
-[KCellularLteComponentCarrierInfo setHasScc0Bandwidth:];
-[KCellularLteComponentCarrierInfo setHasScc0Earfcn:];
-[KCellularLteComponentCarrierInfo setHasScc0RfBand:];
-[KCellularLteComponentCarrierInfo setHasScc1Bandwidth:];
-[KCellularLteComponentCarrierInfo setHasScc1Earfcn:];
-[KCellularLteComponentCarrierInfo setHasScc1RfBand:];
-[KCellularLteComponentCarrierInfo setPccBandwidth:];
-[KCellularLteComponentCarrierInfo setPccEarfcn:];
-[KCellularLteComponentCarrierInfo setPccRfBand:];
-[KCellularLteComponentCarrierInfo setScc0Bandwidth:];
-[KCellularLteComponentCarrierInfo setScc0Earfcn:];
-[KCellularLteComponentCarrierInfo setScc0RfBand:];
-[KCellularLteComponentCarrierInfo setScc1Bandwidth:];
-[KCellularLteComponentCarrierInfo setScc1Earfcn:];
-[KCellularLteComponentCarrierInfo setScc1RfBand:];
```
