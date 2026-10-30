# `AWDMETRICSKCellularPowerLogNRCdrxConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 11 instance variables, 20 properties, 43 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup" _endcScgDefaultDrx;
@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxSecondaryConfigPerCellGroup" _endcScgSecondaryDrx;
@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup" _mcgDefaultDrx;
@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxSecondaryConfigPerCellGroup" _mcgSecondaryDrx;
@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup" _scgDefaultDrx;
@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxSecondaryConfigPerCellGroup" _scgSecondaryDrx;
I _subsId;
B _isEndc;
B _vonrCallOngoing;
{?="timestamp"b1"subsId"b1"isEndc"b1"vonrCallOngoing"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,R,N) hasMcgDefaultDrx;
@property (T@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup",&,N,V_mcgDefaultDrx) mcgDefaultDrx;
@property (TB,R,N) hasMcgSecondaryDrx;
@property (T@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxSecondaryConfigPerCellGroup",&,N,V_mcgSecondaryDrx) mcgSecondaryDrx;
@property (TB,R,N) hasScgDefaultDrx;
@property (T@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup",&,N,V_scgDefaultDrx) scgDefaultDrx;
@property (TB,R,N) hasScgSecondaryDrx;
@property (T@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxSecondaryConfigPerCellGroup",&,N,V_scgSecondaryDrx) scgSecondaryDrx;
@property (TB,R,N) hasEndcScgDefaultDrx;
@property (T@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxConfigPerCellGroup",&,N,V_endcScgDefaultDrx) endcScgDefaultDrx;
@property (TB,R,N) hasEndcScgSecondaryDrx;
@property (T@"AWDMETRICSKCellularPowerLogNRCdrxConfigNrCdrxSecondaryConfigPerCellGroup",&,N,V_endcScgSecondaryDrx) endcScgSecondaryDrx;
@property (TB,N) hasVonrCallOngoing;
@property (TB,N,V_vonrCallOngoing) vonrCallOngoing;
@property (TB,N) hasIsEndc;
@property (TB,N,V_isEndc) isEndc;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasTimestamp];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setTimestamp:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig writeTo:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig mergeFrom:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig timestamp];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hash];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig copyTo:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig description];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig readFrom:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig copyWithZone:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig isEqual:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig mcgSecondaryDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig scgSecondaryDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig vonrCallOngoing];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig endcScgDefaultDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig endcScgSecondaryDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasEndcScgDefaultDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasEndcScgSecondaryDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasIsEndc];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasMcgDefaultDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasMcgSecondaryDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasScgDefaultDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasScgSecondaryDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasSubsId];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig hasVonrCallOngoing];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig isEndc];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig mcgDefaultDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig scgDefaultDrx];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setEndcScgDefaultDrx:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setEndcScgSecondaryDrx:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setHasIsEndc:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setHasSubsId:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setHasVonrCallOngoing:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setIsEndc:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setMcgDefaultDrx:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setMcgSecondaryDrx:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setScgDefaultDrx:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setScgSecondaryDrx:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setSubsId:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig setVonrCallOngoing:];
-[AWDMETRICSKCellularPowerLogNRCdrxConfig subsId];
```
