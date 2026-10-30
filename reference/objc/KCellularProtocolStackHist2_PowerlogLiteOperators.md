# `KCellularProtocolStackHist2`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _bins;
I _duration;
I _subsId;
I _version;
{?="timestamp"b1"duration"b1"subsId"b1"version"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,N) hasVersion;
@property (TI,N,V_version) version;
@property (TB,N) hasDuration;
@property (TI,N,V_duration) duration;
@property (T@"NSMutableArray",&,N,V_bins) bins;
```

## Class methods

```
+[KCellularProtocolStackHist2 binType];
```

## Instance methods

```
-[KCellularProtocolStackHist2 hasVersion];
-[KCellularProtocolStackHist2 hasTimestamp];
-[KCellularProtocolStackHist2 setHasTimestamp:];
-[KCellularProtocolStackHist2 setTimestamp:];
-[KCellularProtocolStackHist2 writeTo:];
-[KCellularProtocolStackHist2 mergeFrom:];
-[KCellularProtocolStackHist2 hasDuration];
-[KCellularProtocolStackHist2 timestamp];
-[KCellularProtocolStackHist2 setHasVersion:];
-[KCellularProtocolStackHist2 version];
-[KCellularProtocolStackHist2 duration];
-[KCellularProtocolStackHist2 setHasDuration:];
-[KCellularProtocolStackHist2 hash];
-[KCellularProtocolStackHist2 copyTo:];
-[KCellularProtocolStackHist2 description];
-[KCellularProtocolStackHist2 setVersion:];
-[KCellularProtocolStackHist2 setDuration:];
-[KCellularProtocolStackHist2 readFrom:];
-[KCellularProtocolStackHist2 copyWithZone:];
-[KCellularProtocolStackHist2 isEqual:];
-[KCellularProtocolStackHist2 dictionaryRepresentation];
-[KCellularProtocolStackHist2 bins];
-[KCellularProtocolStackHist2 setBins:];
-[KCellularProtocolStackHist2 addBin:];
-[KCellularProtocolStackHist2 binAtIndex:];
-[KCellularProtocolStackHist2 binsCount];
-[KCellularProtocolStackHist2 clearBins];
-[KCellularProtocolStackHist2 hasSubsId];
-[KCellularProtocolStackHist2 setHasSubsId:];
-[KCellularProtocolStackHist2 setSubsId:];
-[KCellularProtocolStackHist2 subsId];
```
