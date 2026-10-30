# `CLPLocationProcessingPipelineMetadata`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 3 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
{?="list"^q"count"Q"size"Q} _segmentEventTimestamps;
@"CLPConsolidation" _consolidation;
@"CLPPrivacySanitization" _privacySanitization;
```

## Properties

```
@property (TB,R,N) hasPrivacySanitization;
@property (T@"CLPPrivacySanitization",&,N,V_privacySanitization) privacySanitization;
@property (TB,R,N) hasConsolidation;
@property (T@"CLPConsolidation",&,N,V_consolidation) consolidation;
@property (TQ,R,N) segmentEventTimestampsCount;
@property (T^q,R,N) segmentEventTimestamps;
```

## Instance methods

```
-[CLPLocationProcessingPipelineMetadata writeTo:];
-[CLPLocationProcessingPipelineMetadata mergeFrom:];
-[CLPLocationProcessingPipelineMetadata dealloc];
-[CLPLocationProcessingPipelineMetadata hash];
-[CLPLocationProcessingPipelineMetadata copyTo:];
-[CLPLocationProcessingPipelineMetadata description];
-[CLPLocationProcessingPipelineMetadata readFrom:];
-[CLPLocationProcessingPipelineMetadata copyWithZone:];
-[CLPLocationProcessingPipelineMetadata isEqual:];
-[CLPLocationProcessingPipelineMetadata dictionaryRepresentation];
-[CLPLocationProcessingPipelineMetadata addSegmentEventTimestamps:];
-[CLPLocationProcessingPipelineMetadata clearSegmentEventTimestamps];
-[CLPLocationProcessingPipelineMetadata consolidation];
-[CLPLocationProcessingPipelineMetadata hasConsolidation];
-[CLPLocationProcessingPipelineMetadata hasPrivacySanitization];
-[CLPLocationProcessingPipelineMetadata privacySanitization];
-[CLPLocationProcessingPipelineMetadata segmentEventTimestamps];
-[CLPLocationProcessingPipelineMetadata segmentEventTimestampsAtIndex:];
-[CLPLocationProcessingPipelineMetadata segmentEventTimestampsCount];
-[CLPLocationProcessingPipelineMetadata setConsolidation:];
-[CLPLocationProcessingPipelineMetadata setPrivacySanitization:];
-[CLPLocationProcessingPipelineMetadata setSegmentEventTimestamps:count:];
```
