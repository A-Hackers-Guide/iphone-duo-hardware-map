# `CLPProximityTriggerInfoEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 4 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
d _timestamp;
i _triggerType;
i _useCase;
{?="timestamp"b1"triggerType"b1"useCase"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasUseCase;
@property (Ti,N,V_useCase) useCase;
@property (TB,N) hasTriggerType;
@property (Ti,N,V_triggerType) triggerType;
```

## Instance methods

```
-[CLPProximityTriggerInfoEvent useCase];
-[CLPProximityTriggerInfoEvent hasTimestamp];
-[CLPProximityTriggerInfoEvent setHasTimestamp:];
-[CLPProximityTriggerInfoEvent setTimestamp:];
-[CLPProximityTriggerInfoEvent writeTo:];
-[CLPProximityTriggerInfoEvent mergeFrom:];
-[CLPProximityTriggerInfoEvent setTriggerType:];
-[CLPProximityTriggerInfoEvent timestamp];
-[CLPProximityTriggerInfoEvent setUseCase:];
-[CLPProximityTriggerInfoEvent hash];
-[CLPProximityTriggerInfoEvent triggerType];
-[CLPProximityTriggerInfoEvent copyTo:];
-[CLPProximityTriggerInfoEvent description];
-[CLPProximityTriggerInfoEvent readFrom:];
-[CLPProximityTriggerInfoEvent copyWithZone:];
-[CLPProximityTriggerInfoEvent isEqual:];
-[CLPProximityTriggerInfoEvent dictionaryRepresentation];
-[CLPProximityTriggerInfoEvent hasUseCase];
-[CLPProximityTriggerInfoEvent setHasUseCase:];
-[CLPProximityTriggerInfoEvent hasTriggerType];
-[CLPProximityTriggerInfoEvent setHasTriggerType:];
```
