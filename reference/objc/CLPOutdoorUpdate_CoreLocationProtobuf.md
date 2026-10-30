# `CLPOutdoorUpdate`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
d _estimatedStateProbabilityOutdoor;
d _mctTimestamp;
d _timestamp;
i _confidence;
i _type;
{?="estimatedStateProbabilityOutdoor"b1"mctTimestamp"b1"timestamp"b1"confidence"b1"type"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (Td,N,V_timestamp) timestamp;
@property (TB,N) hasMctTimestamp;
@property (Td,N,V_mctTimestamp) mctTimestamp;
@property (TB,N) hasType;
@property (Ti,N,V_type) type;
@property (TB,N) hasConfidence;
@property (Ti,N,V_confidence) confidence;
@property (TB,N) hasEstimatedStateProbabilityOutdoor;
@property (Td,N,V_estimatedStateProbabilityOutdoor) estimatedStateProbabilityOutdoor;
```

## Instance methods

```
-[CLPOutdoorUpdate hasTimestamp];
-[CLPOutdoorUpdate setHasTimestamp:];
-[CLPOutdoorUpdate setTimestamp:];
-[CLPOutdoorUpdate writeTo:];
-[CLPOutdoorUpdate typeAsString:];
-[CLPOutdoorUpdate setHasType:];
-[CLPOutdoorUpdate mergeFrom:];
-[CLPOutdoorUpdate timestamp];
-[CLPOutdoorUpdate hasType];
-[CLPOutdoorUpdate StringAsType:];
-[CLPOutdoorUpdate setConfidence:];
-[CLPOutdoorUpdate hasConfidence];
-[CLPOutdoorUpdate setType:];
-[CLPOutdoorUpdate type];
-[CLPOutdoorUpdate hash];
-[CLPOutdoorUpdate copyTo:];
-[CLPOutdoorUpdate description];
-[CLPOutdoorUpdate readFrom:];
-[CLPOutdoorUpdate copyWithZone:];
-[CLPOutdoorUpdate isEqual:];
-[CLPOutdoorUpdate setHasConfidence:];
-[CLPOutdoorUpdate confidence];
-[CLPOutdoorUpdate dictionaryRepresentation];
-[CLPOutdoorUpdate StringAsConfidence:];
-[CLPOutdoorUpdate confidenceAsString:];
-[CLPOutdoorUpdate mctTimestamp];
-[CLPOutdoorUpdate setMctTimestamp:];
-[CLPOutdoorUpdate hasMctTimestamp];
-[CLPOutdoorUpdate estimatedStateProbabilityOutdoor];
-[CLPOutdoorUpdate hasEstimatedStateProbabilityOutdoor];
-[CLPOutdoorUpdate setEstimatedStateProbabilityOutdoor:];
-[CLPOutdoorUpdate setHasEstimatedStateProbabilityOutdoor:];
-[CLPOutdoorUpdate setHasMctTimestamp:];
```
