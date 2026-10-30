# `KCellularProtocolStackPerStateHist`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
I _duration;
@"NSMutableArray" _hists;
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
@property (T@"NSMutableArray",&,N,V_hists) hists;
```

## Class methods

```
+[KCellularProtocolStackPerStateHist histType];
```

## Instance methods

```
-[KCellularProtocolStackPerStateHist hasVersion];
-[KCellularProtocolStackPerStateHist hasTimestamp];
-[KCellularProtocolStackPerStateHist setHasTimestamp:];
-[KCellularProtocolStackPerStateHist setTimestamp:];
-[KCellularProtocolStackPerStateHist writeTo:];
-[KCellularProtocolStackPerStateHist mergeFrom:];
-[KCellularProtocolStackPerStateHist hasDuration];
-[KCellularProtocolStackPerStateHist timestamp];
-[KCellularProtocolStackPerStateHist setHasVersion:];
-[KCellularProtocolStackPerStateHist version];
-[KCellularProtocolStackPerStateHist duration];
-[KCellularProtocolStackPerStateHist setHasDuration:];
-[KCellularProtocolStackPerStateHist hash];
-[KCellularProtocolStackPerStateHist copyTo:];
-[KCellularProtocolStackPerStateHist description];
-[KCellularProtocolStackPerStateHist setVersion:];
-[KCellularProtocolStackPerStateHist setDuration:];
-[KCellularProtocolStackPerStateHist readFrom:];
-[KCellularProtocolStackPerStateHist copyWithZone:];
-[KCellularProtocolStackPerStateHist isEqual:];
-[KCellularProtocolStackPerStateHist dictionaryRepresentation];
-[KCellularProtocolStackPerStateHist addHist:];
-[KCellularProtocolStackPerStateHist clearHists];
-[KCellularProtocolStackPerStateHist hasSubsId];
-[KCellularProtocolStackPerStateHist histAtIndex:];
-[KCellularProtocolStackPerStateHist hists];
-[KCellularProtocolStackPerStateHist histsCount];
-[KCellularProtocolStackPerStateHist setHasSubsId:];
-[KCellularProtocolStackPerStateHist setHists:];
-[KCellularProtocolStackPerStateHist setSubsId:];
-[KCellularProtocolStackPerStateHist subsId];
```
