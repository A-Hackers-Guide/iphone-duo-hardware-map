# `BKMRUEventStatistics`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKEventStatistic`
- 2 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableOrderedSet" _statistics;
q _capacity;
```

## Class methods

```
+[BKMRUEventStatistics statisticsWithLabel:capacity:];
```

## Instance methods

```
-[BKMRUEventStatistics appendDescriptionToFormatter:];
-[BKMRUEventStatistics reset];
-[BKMRUEventStatistics hash];
-[BKMRUEventStatistics copyWithZone:];
-[BKMRUEventStatistics isEqual:];
-[BKMRUEventStatistics pushStatistics:];
```
