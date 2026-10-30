# `KCellularCellPlmnSearchCount`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 18 properties, 45 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _cdma1xSearchCount;
I _cdmaEvdoSearchCount;
I _durationMs;
I _gsmSearchCount;
I _lteSearchCount;
I _subsId;
I _tdscdmaSearchCount;
I _umtsSearchCount;
{?="timestamp"b1"cdma1xSearchCount"b1"cdmaEvdoSearchCount"b1"durationMs"b1"gsmSearchCount"b1"lteSearchCount"b1"subsId"b1"tdscdmaSearchCount"b1"umtsSearchCount"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (TB,N) hasGsmSearchCount;
@property (TI,N,V_gsmSearchCount) gsmSearchCount;
@property (TB,N) hasUmtsSearchCount;
@property (TI,N,V_umtsSearchCount) umtsSearchCount;
@property (TB,N) hasTdscdmaSearchCount;
@property (TI,N,V_tdscdmaSearchCount) tdscdmaSearchCount;
@property (TB,N) hasLteSearchCount;
@property (TI,N,V_lteSearchCount) lteSearchCount;
@property (TB,N) hasCdma1xSearchCount;
@property (TI,N,V_cdma1xSearchCount) cdma1xSearchCount;
@property (TB,N) hasCdmaEvdoSearchCount;
@property (TI,N,V_cdmaEvdoSearchCount) cdmaEvdoSearchCount;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[KCellularCellPlmnSearchCount hasTimestamp];
-[KCellularCellPlmnSearchCount setHasTimestamp:];
-[KCellularCellPlmnSearchCount setTimestamp:];
-[KCellularCellPlmnSearchCount writeTo:];
-[KCellularCellPlmnSearchCount mergeFrom:];
-[KCellularCellPlmnSearchCount timestamp];
-[KCellularCellPlmnSearchCount hash];
-[KCellularCellPlmnSearchCount copyTo:];
-[KCellularCellPlmnSearchCount description];
-[KCellularCellPlmnSearchCount readFrom:];
-[KCellularCellPlmnSearchCount copyWithZone:];
-[KCellularCellPlmnSearchCount isEqual:];
-[KCellularCellPlmnSearchCount dictionaryRepresentation];
-[KCellularCellPlmnSearchCount durationMs];
-[KCellularCellPlmnSearchCount hasDurationMs];
-[KCellularCellPlmnSearchCount setDurationMs:];
-[KCellularCellPlmnSearchCount setHasDurationMs:];
-[KCellularCellPlmnSearchCount hasSubsId];
-[KCellularCellPlmnSearchCount setHasSubsId:];
-[KCellularCellPlmnSearchCount setSubsId:];
-[KCellularCellPlmnSearchCount subsId];
-[KCellularCellPlmnSearchCount umtsSearchCount];
-[KCellularCellPlmnSearchCount cdma1xSearchCount];
-[KCellularCellPlmnSearchCount cdmaEvdoSearchCount];
-[KCellularCellPlmnSearchCount gsmSearchCount];
-[KCellularCellPlmnSearchCount hasCdma1xSearchCount];
-[KCellularCellPlmnSearchCount hasCdmaEvdoSearchCount];
-[KCellularCellPlmnSearchCount hasGsmSearchCount];
-[KCellularCellPlmnSearchCount hasLteSearchCount];
-[KCellularCellPlmnSearchCount hasTdscdmaSearchCount];
-[KCellularCellPlmnSearchCount hasUmtsSearchCount];
-[KCellularCellPlmnSearchCount lteSearchCount];
-[KCellularCellPlmnSearchCount setCdma1xSearchCount:];
-[KCellularCellPlmnSearchCount setCdmaEvdoSearchCount:];
-[KCellularCellPlmnSearchCount setGsmSearchCount:];
-[KCellularCellPlmnSearchCount setHasCdma1xSearchCount:];
-[KCellularCellPlmnSearchCount setHasCdmaEvdoSearchCount:];
-[KCellularCellPlmnSearchCount setHasGsmSearchCount:];
-[KCellularCellPlmnSearchCount setHasLteSearchCount:];
-[KCellularCellPlmnSearchCount setHasTdscdmaSearchCount:];
-[KCellularCellPlmnSearchCount setHasUmtsSearchCount:];
-[KCellularCellPlmnSearchCount setLteSearchCount:];
-[KCellularCellPlmnSearchCount setTdscdmaSearchCount:];
-[KCellularCellPlmnSearchCount setUmtsSearchCount:];
-[KCellularCellPlmnSearchCount tdscdmaSearchCount];
```
