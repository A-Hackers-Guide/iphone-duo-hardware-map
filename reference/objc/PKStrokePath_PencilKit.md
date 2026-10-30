# `PKStrokePath`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 12 properties, 60 instance methods, 3 class methods

## Instance variables

```
{PKStrokePathPointsPrivate="constants"{shared_ptr<PKStrokePathPointsShared>="__ptr_"^{PKStrokePathPointsShared}"__cntrl_"^{__shared_weak_count}}"pointsData"{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}}} _strokeDataPointsPrivate;
{shared_ptr<PKProtobufUnknownFields>="__ptr_"^{PKProtobufUnknownFields}"__cntrl_"^{__shared_weak_count}} _unknownFields;
B _didValidateTimestamps;
B _hasValidTimestampData;
d _cachedMaxWidth;
Q _immutablePointsCount;
Q _startIndex;
q _inputType;
@"NSUUID" _strokeDataUUID;
```

## Properties

```
@property (TQ,R,N) _pointsCount;
@property (TQ,R,N,V_startIndex) _startIndex;
@property (Tq,R,N,V_inputType) _inputType;
@property (TB,R,N) hasAzimuthAngles;
@property (TB,R,N) hasValidPointTimestampData;
@property (TQ,R,N,V_immutablePointsCount) _immutablePointsCount;
@property (T@"NSUUID",R,N,V_strokeDataUUID) _strokeDataUUID;
@property (Td,R,N) _timestamp;
@property (T@"NSUUID",R,N) strokePathID;
@property (TQ,R,N) count;
@property (T@"NSDate",R,N) creationDate;
@property (T^{CGPath=},R,N) bezierRepresentation;
```

## Class methods

```
+[PKStrokePath _calculateOffsets:sizes:];
+[PKStrokePath calculateOffsets];
+[PKStrokePath strokeDataFromDataArchive:];
```

## Instance methods

```
-[PKStrokePath init];
-[PKStrokePath objectAtIndexedSubscript:];
-[PKStrokePath rawValue];
-[PKStrokePath count];
-[PKStrokePath creationDate];
-[PKStrokePath deltaTo:];
-[PKStrokePath description];
-[PKStrokePath radiusAtIndex:];
-[PKStrokePath initWithRawValue:];
-[PKStrokePath copyWithZone:];
-[PKStrokePath _timestamp];
-[PKStrokePath _inputType];
-[PKStrokePath _setTimestamp:];
-[PKStrokePath locationAtIndex:];
-[PKStrokePath pointAtIndex:];
-[PKStrokePath timestampAtIndex:];
-[PKStrokePath _startIndex];
-[PKStrokePath enumerateInterpolatedPointsInRange:strideByDistance:usingBlock:];
-[PKStrokePath _strokeDataUUID];
-[PKStrokePath _compressedPointAt:];
-[PKStrokePath _enumerateInterpolatedPointsInRange:incrementBlock:usingBlock:];
-[PKStrokePath _immutablePointsCount];
-[PKStrokePath _legacyRandomSeed];
-[PKStrokePath _maxWidth];
-[PKStrokePath _newPathRepresentation];
-[PKStrokePath _pointsCount];
-[PKStrokePath _scaleRadius:isVector:];
-[PKStrokePath _transform:existingTransform:];
-[PKStrokePath bezierRepresentation];
-[PKStrokePath canApplyDelta:];
-[PKStrokePath copyTransformed:inCoordinateSpace:];
-[PKStrokePath copyWithScaledRadius:isVector:];
-[PKStrokePath copyWithStrokeDataUUID:];
-[PKStrokePath dataApplying:];
-[PKStrokePath decompressedPointAt:];
-[PKStrokePath deltaContainsNewInfo:];
-[PKStrokePath enumerateInterpolatedPointsInRange:strideByParametricStep:usingBlock:];
-[PKStrokePath enumerateInterpolatedPointsInRange:strideByTime:usingBlock:];
-[PKStrokePath hasAzimuthAngles];
-[PKStrokePath hasValidPointTimestampData];
-[PKStrokePath inflight];
-[PKStrokePath initWithBezierPath:creationDate:pointProvider:];
-[PKStrokePath initWithControlPoints:creationDate:];
-[PKStrokePath initWithControlPoints:creationDate:strokePathID:];
-[PKStrokePath initWithData:range:UUID:];
-[PKStrokePath initWithDataPoints:immutableCount:inputType:UUID:didValidateTimestamps:hasValidTimestampData:cachedMaxWidth:unknownFields:];
-[PKStrokePath initWithPoints:count:immutableCount:inputType:timestamp:UUID:];
-[PKStrokePath interpolatedLocationAt:];
-[PKStrokePath interpolatedPointAt:];
-[PKStrokePath interpolatedTimeoffsetAt:];
-[PKStrokePath locationOnSegment:t:];
-[PKStrokePath parametricValue:offsetByDistance:];
-[PKStrokePath parametricValue:offsetByTime:];
-[PKStrokePath readStrokeDataFromArchive:];
-[PKStrokePath saveToDataArchive:];
-[PKStrokePath setLocation:atIndex:];
-[PKStrokePath setPoints:pointsCount:timestamp:];
-[PKStrokePath setPointsFrom:range:];
-[PKStrokePath strokePathID];
-[PKStrokePath subpathWithRange:];
```
