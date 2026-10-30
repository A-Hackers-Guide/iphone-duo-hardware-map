# `CMSwimData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 14 instance variables, 14 properties, 25 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSUUID" fSourceId;
@"NSUUID" fSessionId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
Q fStrokeCount;
d fDistance;
@"NSDate" fDistanceTimestamp;
d fAvgPace;
Q fLapCount;
q fStrokeType;
Q fSegment;
d fSWOLF;
d fSegmentSWOLF;
```

## Properties

```
@property (TQ,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
@property (T@"NSUUID",R,N) sessionId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (TQ,R,N) strokeCount;
@property (Td,R,N) distance;
@property (T@"NSDate",R,N) distanceTimestamp;
@property (Td,R,N) avgPace;
@property (TQ,R,N) lapCount;
@property (Tq,R,N) strokeType;
@property (TQ,R,N) segment;
@property (Td,R,N) SWOLF;
@property (Td,R,N) segmentSWOLF;
```

## Class methods

```
+[CMSwimData supportsSecureCoding];
+[CMSwimData strokeTypeName:];
+[CMSwimData maxSwimDataEntries];
```

## Instance methods

```
-[CMSwimData startDate];
-[CMSwimData distance];
-[CMSwimData sourceId];
-[CMSwimData sessionId];
-[CMSwimData recordId];
-[CMSwimData segment];
-[CMSwimData dealloc];
-[CMSwimData endDate];
-[CMSwimData encodeWithCoder:];
-[CMSwimData description];
-[CMSwimData initWithCoder:];
-[CMSwimData copyWithZone:];
-[CMSwimData strokeCount];
-[CMSwimData avgPace];
-[CMSwimData SWOLF];
-[CMSwimData convertToSwimEntry:];
-[CMSwimData distanceTimestamp];
-[CMSwimData initWithRecordId:sourceId:sessionId:startDate:endDate:strokeCount:distance:distanceTimestamp:avgPace:lapCount:strokeType:segment:SWOLF:segmentSWOLF:];
-[CMSwimData initWithSessionId:];
-[CMSwimData initWithSwimEntry:];
-[CMSwimData isSWOLFValid];
-[CMSwimData isSegmentSWOLFValid];
-[CMSwimData lapCount];
-[CMSwimData segmentSWOLF];
-[CMSwimData strokeType];
```
