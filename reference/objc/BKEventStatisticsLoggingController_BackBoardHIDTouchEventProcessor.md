# `BKEventStatisticsLoggingController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 10 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _label;
@"NSObject<OS_os_log>" _logCategory;
@"NSArray" _statistics;
@"BSCompoundAssertion" _transactionAssertion;
d _startCoalescingTime;
@"BSAbsoluteMachTimer" _timer;
@"NSObject<OS_dispatch_queue>" _workQueue;
B _resetStartTime;
B _needsFlush;
B _invalid;
```

## Properties

```
@property (T@"NSArray",C,N,V_statistics) statistics;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKEventStatisticsLoggingController workQueue];
```

## Instance methods

```
-[BKEventStatisticsLoggingController updateStatistics:];
-[BKEventStatisticsLoggingController statistics];
-[BKEventStatisticsLoggingController setStatistics:];
-[BKEventStatisticsLoggingController dealloc];
-[BKEventStatisticsLoggingController invalidate];
-[BKEventStatisticsLoggingController beginTransactionForReason:];
-[BKEventStatisticsLoggingController initWithLabel:logCategory:];
```
