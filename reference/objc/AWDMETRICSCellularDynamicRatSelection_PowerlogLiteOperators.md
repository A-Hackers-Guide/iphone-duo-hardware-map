# `AWDMETRICSCellularDynamicRatSelection`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 11 instance variables, 20 properties, 53 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _bwObservedAfterSwitch;
I _bwObservedBeforeSwitch;
i _destRat;
I _dlTputObservedAfterSwitch;
I _dlTputObservedBeforeSwitch;
i _sourceRat;
I _subsId;
I _ulTputObservedAfterSwitch;
I _ulTputObservedBeforeSwitch;
{?="timestamp"b1"bwObservedAfterSwitch"b1"bwObservedBeforeSwitch"b1"destRat"b1"dlTputObservedAfterSwitch"b1"dlTputObservedBeforeSwitch"b1"sourceRat"b1"subsId"b1"ulTputObservedAfterSwitch"b1"ulTputObservedBeforeSwitch"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSourceRat;
@property (Ti,N,V_sourceRat) sourceRat;
@property (TB,N) hasDestRat;
@property (Ti,N,V_destRat) destRat;
@property (TB,N) hasDlTputObservedBeforeSwitch;
@property (TI,N,V_dlTputObservedBeforeSwitch) dlTputObservedBeforeSwitch;
@property (TB,N) hasDlTputObservedAfterSwitch;
@property (TI,N,V_dlTputObservedAfterSwitch) dlTputObservedAfterSwitch;
@property (TB,N) hasBwObservedBeforeSwitch;
@property (TI,N,V_bwObservedBeforeSwitch) bwObservedBeforeSwitch;
@property (TB,N) hasBwObservedAfterSwitch;
@property (TI,N,V_bwObservedAfterSwitch) bwObservedAfterSwitch;
@property (TB,N) hasUlTputObservedBeforeSwitch;
@property (TI,N,V_ulTputObservedBeforeSwitch) ulTputObservedBeforeSwitch;
@property (TB,N) hasUlTputObservedAfterSwitch;
@property (TI,N,V_ulTputObservedAfterSwitch) ulTputObservedAfterSwitch;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
```

## Instance methods

```
-[AWDMETRICSCellularDynamicRatSelection hasTimestamp];
-[AWDMETRICSCellularDynamicRatSelection setHasTimestamp:];
-[AWDMETRICSCellularDynamicRatSelection setTimestamp:];
-[AWDMETRICSCellularDynamicRatSelection writeTo:];
-[AWDMETRICSCellularDynamicRatSelection mergeFrom:];
-[AWDMETRICSCellularDynamicRatSelection timestamp];
-[AWDMETRICSCellularDynamicRatSelection hash];
-[AWDMETRICSCellularDynamicRatSelection copyTo:];
-[AWDMETRICSCellularDynamicRatSelection description];
-[AWDMETRICSCellularDynamicRatSelection readFrom:];
-[AWDMETRICSCellularDynamicRatSelection copyWithZone:];
-[AWDMETRICSCellularDynamicRatSelection isEqual:];
-[AWDMETRICSCellularDynamicRatSelection dictionaryRepresentation];
-[AWDMETRICSCellularDynamicRatSelection StringAsSourceRat:];
-[AWDMETRICSCellularDynamicRatSelection StringAsDestRat:];
-[AWDMETRICSCellularDynamicRatSelection destRat];
-[AWDMETRICSCellularDynamicRatSelection bwObservedAfterSwitch];
-[AWDMETRICSCellularDynamicRatSelection bwObservedBeforeSwitch];
-[AWDMETRICSCellularDynamicRatSelection destRatAsString:];
-[AWDMETRICSCellularDynamicRatSelection dlTputObservedAfterSwitch];
-[AWDMETRICSCellularDynamicRatSelection dlTputObservedBeforeSwitch];
-[AWDMETRICSCellularDynamicRatSelection hasBwObservedAfterSwitch];
-[AWDMETRICSCellularDynamicRatSelection hasBwObservedBeforeSwitch];
-[AWDMETRICSCellularDynamicRatSelection hasDestRat];
-[AWDMETRICSCellularDynamicRatSelection hasDlTputObservedAfterSwitch];
-[AWDMETRICSCellularDynamicRatSelection hasDlTputObservedBeforeSwitch];
-[AWDMETRICSCellularDynamicRatSelection hasSourceRat];
-[AWDMETRICSCellularDynamicRatSelection hasSubsId];
-[AWDMETRICSCellularDynamicRatSelection hasUlTputObservedAfterSwitch];
-[AWDMETRICSCellularDynamicRatSelection hasUlTputObservedBeforeSwitch];
-[AWDMETRICSCellularDynamicRatSelection setBwObservedAfterSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setBwObservedBeforeSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setDestRat:];
-[AWDMETRICSCellularDynamicRatSelection setDlTputObservedAfterSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setDlTputObservedBeforeSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setHasBwObservedAfterSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setHasBwObservedBeforeSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setHasDestRat:];
-[AWDMETRICSCellularDynamicRatSelection setHasDlTputObservedAfterSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setHasDlTputObservedBeforeSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setHasSourceRat:];
-[AWDMETRICSCellularDynamicRatSelection setHasSubsId:];
-[AWDMETRICSCellularDynamicRatSelection setHasUlTputObservedAfterSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setHasUlTputObservedBeforeSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setSourceRat:];
-[AWDMETRICSCellularDynamicRatSelection setSubsId:];
-[AWDMETRICSCellularDynamicRatSelection setUlTputObservedAfterSwitch:];
-[AWDMETRICSCellularDynamicRatSelection setUlTputObservedBeforeSwitch:];
-[AWDMETRICSCellularDynamicRatSelection sourceRat];
-[AWDMETRICSCellularDynamicRatSelection sourceRatAsString:];
-[AWDMETRICSCellularDynamicRatSelection subsId];
-[AWDMETRICSCellularDynamicRatSelection ulTputObservedAfterSwitch];
-[AWDMETRICSCellularDynamicRatSelection ulTputObservedBeforeSwitch];
```
