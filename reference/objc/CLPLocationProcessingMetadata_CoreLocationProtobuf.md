# `CLPLocationProcessingMetadata`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
i _eventTimestampIndex;
i _tripSourceType;
{?="eventTimestampIndex"b1"tripSourceType"b1} _has;
```

## Properties

```
@property (TB,N) hasTripSourceType;
@property (Ti,N,V_tripSourceType) tripSourceType;
@property (TB,N) hasEventTimestampIndex;
@property (Ti,N,V_eventTimestampIndex) eventTimestampIndex;
```

## Instance methods

```
-[CLPLocationProcessingMetadata writeTo:];
-[CLPLocationProcessingMetadata mergeFrom:];
-[CLPLocationProcessingMetadata hash];
-[CLPLocationProcessingMetadata copyTo:];
-[CLPLocationProcessingMetadata description];
-[CLPLocationProcessingMetadata readFrom:];
-[CLPLocationProcessingMetadata copyWithZone:];
-[CLPLocationProcessingMetadata isEqual:];
-[CLPLocationProcessingMetadata dictionaryRepresentation];
-[CLPLocationProcessingMetadata StringAsTripSourceType:];
-[CLPLocationProcessingMetadata eventTimestampIndex];
-[CLPLocationProcessingMetadata hasEventTimestampIndex];
-[CLPLocationProcessingMetadata hasTripSourceType];
-[CLPLocationProcessingMetadata setEventTimestampIndex:];
-[CLPLocationProcessingMetadata setHasEventTimestampIndex:];
-[CLPLocationProcessingMetadata setHasTripSourceType:];
-[CLPLocationProcessingMetadata setTripSourceType:];
-[CLPLocationProcessingMetadata tripSourceType];
-[CLPLocationProcessingMetadata tripSourceTypeAsString:];
```
