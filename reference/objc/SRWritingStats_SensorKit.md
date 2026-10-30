# `SRWritingStats`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _totalSegmentsCreated;
d _totalFillDuration;
d _sessionStart;
@"NSString" _sensor;
Q _totalBytesWritten;
Q _totalSamplesWritten;
d _segmentCreationTime;
Q _rateAdjustedSegmentSize;
```

## Properties

```
@property (TQ,R,N,V_totalSegmentsCreated) totalSegmentsCreated;
@property (Td,R,N,V_totalFillDuration) totalFillDuration;
@property (Td,N,V_segmentCreationTime) segmentCreationTime;
```

## Instance methods

```
-[SRWritingStats dealloc];
-[SRWritingStats description];
-[SRWritingStats setSegmentCreationTime:];
-[SRWritingStats totalFillDuration];
-[SRWritingStats totalSegmentsCreated];
```
