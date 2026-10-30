# `AWDMETRICSCellularPowerLogPLMNSearchEvent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 8 instance variables, 14 properties, 45 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _duration;
i _networkSelectionMode;
i _rat;
i _searchType;
i _state;
I _subsId;
{?="timestamp"b1"duration"b1"networkSelectionMode"b1"rat"b1"searchType"b1"state"b1"subsId"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasState;
@property (Ti,N,V_state) state;
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasSearchType;
@property (Ti,N,V_searchType) searchType;
@property (TB,N) hasNetworkSelectionMode;
@property (Ti,N,V_networkSelectionMode) networkSelectionMode;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasTimestamp];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasTimestamp:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setTimestamp:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent writeTo:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setState:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent mergeFrom:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasDuration];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent timestamp];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent stateAsString:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent StringAsState:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent searchType];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent rat];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent duration];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasDuration:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasState];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setSearchType:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hash];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent copyTo:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent description];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setDuration:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent readFrom:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent copyWithZone:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasState:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent isEqual:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent state];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent dictionaryRepresentation];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent StringAsSearchType:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasSearchType];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent searchTypeAsString:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasSearchType:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setRat:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasRat];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasRat:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent networkSelectionMode];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent StringAsNetworkSelectionMode:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent StringAsRat:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasNetworkSelectionMode];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent hasSubsId];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent networkSelectionModeAsString:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent ratAsString:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasNetworkSelectionMode:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setHasSubsId:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setNetworkSelectionMode:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent setSubsId:];
-[AWDMETRICSCellularPowerLogPLMNSearchEvent subsId];
```
