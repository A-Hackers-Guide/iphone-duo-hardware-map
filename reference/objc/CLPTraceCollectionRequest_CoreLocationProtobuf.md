# `CLPTraceCollectionRequest`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBRequest`
- Protocols: `NSCopying`
- 5 instance variables, 6 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _events;
@"CLPMeta" _meta;
i _triggerType;
i _type;
{?="triggerType"b1"type"b1} _has;
```

## Properties

```
@property (T@"CLPMeta",&,N,V_meta) meta;
@property (T@"NSMutableArray",&,N,V_events) events;
@property (TB,N) hasType;
@property (Ti,N,V_type) type;
@property (TB,N) hasTriggerType;
@property (Ti,N,V_triggerType) triggerType;
```

## Class methods

```
+[CLPTraceCollectionRequest eventsType];
```

## Instance methods

```
-[CLPTraceCollectionRequest writeTo:];
-[CLPTraceCollectionRequest responseClass];
-[CLPTraceCollectionRequest typeAsString:];
-[CLPTraceCollectionRequest setHasType:];
-[CLPTraceCollectionRequest setEvents:];
-[CLPTraceCollectionRequest mergeFrom:];
-[CLPTraceCollectionRequest setTriggerType:];
-[CLPTraceCollectionRequest hasType];
-[CLPTraceCollectionRequest addEvents:];
-[CLPTraceCollectionRequest events];
-[CLPTraceCollectionRequest requestTypeCode];
-[CLPTraceCollectionRequest StringAsType:];
-[CLPTraceCollectionRequest setType:];
-[CLPTraceCollectionRequest type];
-[CLPTraceCollectionRequest hash];
-[CLPTraceCollectionRequest triggerType];
-[CLPTraceCollectionRequest copyTo:];
-[CLPTraceCollectionRequest description];
-[CLPTraceCollectionRequest readFrom:];
-[CLPTraceCollectionRequest copyWithZone:];
-[CLPTraceCollectionRequest isEqual:];
-[CLPTraceCollectionRequest dictionaryRepresentation];
-[CLPTraceCollectionRequest clearEvents];
-[CLPTraceCollectionRequest eventsAtIndex:];
-[CLPTraceCollectionRequest eventsCount];
-[CLPTraceCollectionRequest meta];
-[CLPTraceCollectionRequest setMeta:];
-[CLPTraceCollectionRequest hasTriggerType];
-[CLPTraceCollectionRequest setHasTriggerType:];
-[CLPTraceCollectionRequest StringAsTriggerType:];
-[CLPTraceCollectionRequest triggerTypeAsString:];
```
