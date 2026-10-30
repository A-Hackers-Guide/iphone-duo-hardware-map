# `AWDMETRICSKCellularPowerLogPlmnSearchEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 45 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _duration;
i _rat;
i _result;
i _searchReason;
i _searchType;
I _subsId;
{?="timestamp"b1"duration"b1"rat"b1"result"b1"searchReason"b1"searchType"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasResult;
@property (Ti,N,V_result) result;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasSearchType;
@property (Ti,N,V_searchType) searchType;
@property (TB,N) hasSearchReason;
@property (Ti,N,V_searchReason) searchReason;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasResult];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasTimestamp];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setResult:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setTimestamp:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent writeTo:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent mergeFrom:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasDuration];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent timestamp];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent searchType];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent rat];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent duration];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasDuration:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent result];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setSearchType:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hash];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent copyTo:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent description];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setDuration:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent readFrom:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent copyWithZone:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent isEqual:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasResult:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent StringAsSearchType:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasSearchType];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent searchTypeAsString:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasSearchType:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent resultAsString:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent StringAsResult:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setRat:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasRat];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasRat:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent StringAsRat:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent StringAsSearchReason:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasSearchReason];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent hasSubsId];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent ratAsString:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent searchReason];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent searchReasonAsString:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasSearchReason:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setHasSubsId:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setSearchReason:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent setSubsId:];
-[AWDMETRICSKCellularPowerLogPlmnSearchEvent subsId];
```
