# `RegulatorAverageCurrent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 25 instance methods, 0 class methods

## Instance variables

```
I _averageCurrentMa;
I _duration64ms;
I _regulatorId;
I _sampleCount;
{?="averageCurrentMa"b1"duration64ms"b1"regulatorId"b1"sampleCount"b1} _has;
```

## Properties

```
@property (TB,N) hasRegulatorId;
@property (TI,N,V_regulatorId) regulatorId;
@property (TB,N) hasSampleCount;
@property (TI,N,V_sampleCount) sampleCount;
@property (TB,N) hasDuration64ms;
@property (TI,N,V_duration64ms) duration64ms;
@property (TB,N) hasAverageCurrentMa;
@property (TI,N,V_averageCurrentMa) averageCurrentMa;
```

## Instance methods

```
-[RegulatorAverageCurrent writeTo:];
-[RegulatorAverageCurrent setSampleCount:];
-[RegulatorAverageCurrent mergeFrom:];
-[RegulatorAverageCurrent sampleCount];
-[RegulatorAverageCurrent hash];
-[RegulatorAverageCurrent copyTo:];
-[RegulatorAverageCurrent description];
-[RegulatorAverageCurrent readFrom:];
-[RegulatorAverageCurrent copyWithZone:];
-[RegulatorAverageCurrent isEqual:];
-[RegulatorAverageCurrent dictionaryRepresentation];
-[RegulatorAverageCurrent hasSampleCount];
-[RegulatorAverageCurrent setHasSampleCount:];
-[RegulatorAverageCurrent hasDuration64ms];
-[RegulatorAverageCurrent setRegulatorId:];
-[RegulatorAverageCurrent averageCurrentMa];
-[RegulatorAverageCurrent duration64ms];
-[RegulatorAverageCurrent hasAverageCurrentMa];
-[RegulatorAverageCurrent hasRegulatorId];
-[RegulatorAverageCurrent regulatorId];
-[RegulatorAverageCurrent setAverageCurrentMa:];
-[RegulatorAverageCurrent setDuration64ms:];
-[RegulatorAverageCurrent setHasAverageCurrentMa:];
-[RegulatorAverageCurrent setHasDuration64ms:];
-[RegulatorAverageCurrent setHasRegulatorId:];
```
