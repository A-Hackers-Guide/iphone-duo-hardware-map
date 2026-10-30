# `BKTouchDeliveryStatisticsLoggingObserver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKTouchLifecycleObserver`
- 22 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"BKEventStatisticsLoggingController" _loggingController;
@"BKIntegerEventStatistic" _touchUpCount;
@"BKIntegerEventStatistic" _touchDownCount;
@"BKIntegerEventStatistic" _rangeInCount;
@"BKIntegerEventStatistic" _rangeOutCount;
@"BKIntegerEventStatistic" _hardCancelCount;
@"BKIntegerEventStatistic" _softCancelCount;
@"BKIntegerEventStatistic" _tapToWakeCount;
@"BKIntegerEventStatistic" _stylusTouchCount;
@"BKIntegerEventStatistic" _detachedTouchCount;
@"BKIntegerEventStatistic" _transferredTouchCount;
@"BKIntegerEventStatistic" _fromEdgeCount;
@"BKHexadecimalIntegerEventStatistic" _pathsSeen;
@"BKHexadecimalIntegerEventStatistic" _pathsStillTouching;
@"BKHexadecimalIntegerEventStatistic" _pathsStillWithinRange;
@"BKAverageTimeIntervalEventStatistic" _touchProcessingTimeAverage;
@"BKTouchDestinationStatistic" _destinations;
@"<BSInvalidatable>" _logTransaction;
q _touchProcessingCumulativeTimeUS;
q _touchProcessingCollectionCount;
d _touchProcessingCollectionStartTime;
I _lastTouchID;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTouchDeliveryStatisticsLoggingObserver initWithLabel:];
-[BKTouchDeliveryStatisticsLoggingObserver touch:pathIndex:downAtPoint:eventMask:transducerType:];
-[BKTouchDeliveryStatisticsLoggingObserver touch:didAlwaysRouteToTargetID:clientTaskName:];
-[BKTouchDeliveryStatisticsLoggingObserver touchDidFinishProcessingTouchCollection];
-[BKTouchDeliveryStatisticsLoggingObserver touch:didMoveToPoint:eventMask:z:maxZ:];
-[BKTouchDeliveryStatisticsLoggingObserver touch:didHitTestToDestination:hostingChainIndex:];
-[BKTouchDeliveryStatisticsLoggingObserver hitTestRegionsDidChange:];
-[BKTouchDeliveryStatisticsLoggingObserver dealloc];
-[BKTouchDeliveryStatisticsLoggingObserver touchWillStartProcessingTouchCollection];
-[BKTouchDeliveryStatisticsLoggingObserver touchDidHIDCancel:];
-[BKTouchDeliveryStatisticsLoggingObserver touchDidSoftCancel:];
-[BKTouchDeliveryStatisticsLoggingObserver touch:pathIndex:rangeInAtPoint:eventMask:z:maxZ:transducerType:];
-[BKTouchDeliveryStatisticsLoggingObserver touch:pathIndex:upAtPoint:detached:];
-[BKTouchDeliveryStatisticsLoggingObserver touch:pathIndex:rangeOutAtPoint:];
-[BKTouchDeliveryStatisticsLoggingObserver touchDidDetach:destinations:];
-[BKTouchDeliveryStatisticsLoggingObserver touchDidTransfer:destination:];
```
