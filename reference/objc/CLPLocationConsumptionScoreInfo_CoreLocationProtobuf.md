# `CLPLocationConsumptionScoreInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
d _startTime;
d _stopTime;
@"NSString" _clientKey;
i _score;
{?="startTime"b1"stopTime"b1"score"b1} _has;
```

## Properties

```
@property (TB,N) hasStartTime;
@property (Td,N,V_startTime) startTime;
@property (TB,N) hasStopTime;
@property (Td,N,V_stopTime) stopTime;
@property (TB,R,N) hasClientKey;
@property (T@"NSString",&,N,V_clientKey) clientKey;
@property (TB,N) hasScore;
@property (Ti,N,V_score) score;
```

## Instance methods

```
-[CLPLocationConsumptionScoreInfo setHasStartTime:];
-[CLPLocationConsumptionScoreInfo writeTo:];
-[CLPLocationConsumptionScoreInfo hasStartTime];
-[CLPLocationConsumptionScoreInfo startTime];
-[CLPLocationConsumptionScoreInfo setScore:];
-[CLPLocationConsumptionScoreInfo mergeFrom:];
-[CLPLocationConsumptionScoreInfo stopTime];
-[CLPLocationConsumptionScoreInfo setHasScore:];
-[CLPLocationConsumptionScoreInfo score];
-[CLPLocationConsumptionScoreInfo clientKey];
-[CLPLocationConsumptionScoreInfo hasScore];
-[CLPLocationConsumptionScoreInfo setStartTime:];
-[CLPLocationConsumptionScoreInfo setHasStopTime:];
-[CLPLocationConsumptionScoreInfo hasClientKey];
-[CLPLocationConsumptionScoreInfo hash];
-[CLPLocationConsumptionScoreInfo copyTo:];
-[CLPLocationConsumptionScoreInfo setClientKey:];
-[CLPLocationConsumptionScoreInfo description];
-[CLPLocationConsumptionScoreInfo hasStopTime];
-[CLPLocationConsumptionScoreInfo readFrom:];
-[CLPLocationConsumptionScoreInfo setStopTime:];
-[CLPLocationConsumptionScoreInfo copyWithZone:];
-[CLPLocationConsumptionScoreInfo isEqual:];
-[CLPLocationConsumptionScoreInfo dictionaryRepresentation];
```
