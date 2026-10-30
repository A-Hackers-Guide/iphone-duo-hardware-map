# `AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 28 instance methods, 0 class methods

## Instance variables

```
{?="list"^I"count"Q"size"Q} _counts;
i _chanType;
i _rat;
{?="chanType"b1"rat"b1} _has;
```

## Properties

```
@property (TB,N) hasRat;
@property (Ti,N,V_rat) rat;
@property (TB,N) hasChanType;
@property (Ti,N,V_chanType) chanType;
@property (TQ,R,N) countsCount;
@property (T^I,R,N) counts;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist writeTo:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist mergeFrom:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist dealloc];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist rat];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist hash];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist copyTo:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist description];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist counts];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist readFrom:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist copyWithZone:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist isEqual:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist setRat:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist hasRat];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist setHasRat:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist addCount:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist countsCount];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist StringAsChanType:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist StringAsRat:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist setHasChanType:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist chanType];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist chanTypeAsString:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist clearCounts];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist countAtIndex:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist hasChanType];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist ratAsString:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist setChanType:];
-[AWDMETRICSKCellularPowerLogLteNrTxPowerHistHist setCounts:count:];
```
