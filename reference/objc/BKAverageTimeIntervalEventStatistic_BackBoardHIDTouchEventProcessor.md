# `BKAverageTimeIntervalEventStatistic`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKEventStatistic`
- 5 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _scale;
d _startInterval;
q _count;
d _cumulativeInterval;
d _value;
```

## Properties

```
@property (Td,N,V_value) value;
```

## Class methods

```
+[BKAverageTimeIntervalEventStatistic statisticWithLabel:scale:];
```

## Instance methods

```
-[BKAverageTimeIntervalEventStatistic begin];
-[BKAverageTimeIntervalEventStatistic appendDescriptionToFormatter:];
-[BKAverageTimeIntervalEventStatistic value];
-[BKAverageTimeIntervalEventStatistic reset];
-[BKAverageTimeIntervalEventStatistic end];
-[BKAverageTimeIntervalEventStatistic setValue:];
-[BKAverageTimeIntervalEventStatistic hash];
-[BKAverageTimeIntervalEventStatistic copyWithZone:];
-[BKAverageTimeIntervalEventStatistic isEqual:];
```
