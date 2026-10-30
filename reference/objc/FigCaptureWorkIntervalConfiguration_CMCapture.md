# `FigCaptureWorkIntervalConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _enabled;
B _startIntervalsProvisionally;
B _joinLeaveEnabled;
B _adaptiveDeadlineEnabled;
I _concurrentIntervalCount;
q _intervalDuration;
q _expectedThroughput;
```

## Properties

```
@property (TB,N,V_enabled) enabled;
@property (TI,N,V_concurrentIntervalCount) concurrentIntervalCount;
@property (Tq,N,V_intervalDuration) intervalDuration;
@property (Tq,N,V_expectedThroughput) expectedThroughput;
@property (TB,N,V_startIntervalsProvisionally) startIntervalsProvisionally;
@property (TB,N,V_joinLeaveEnabled) joinLeaveEnabled;
@property (TB,N,V_adaptiveDeadlineEnabled) adaptiveDeadlineEnabled;
```

## Class methods

```
+[FigCaptureWorkIntervalConfiguration configurationForType:];
```

## Instance methods

```
-[FigCaptureWorkIntervalConfiguration enabled];
-[FigCaptureWorkIntervalConfiguration setExpectedThroughput:];
-[FigCaptureWorkIntervalConfiguration setEnabled:];
-[FigCaptureWorkIntervalConfiguration expectedThroughput];
-[FigCaptureWorkIntervalConfiguration setStartIntervalsProvisionally:];
-[FigCaptureWorkIntervalConfiguration adaptiveDeadlineEnabled];
-[FigCaptureWorkIntervalConfiguration concurrentIntervalCount];
-[FigCaptureWorkIntervalConfiguration intervalDuration];
-[FigCaptureWorkIntervalConfiguration joinLeaveEnabled];
-[FigCaptureWorkIntervalConfiguration setAdaptiveDeadlineEnabled:];
-[FigCaptureWorkIntervalConfiguration setConcurrentIntervalCount:];
-[FigCaptureWorkIntervalConfiguration setIntervalDuration:];
-[FigCaptureWorkIntervalConfiguration setJoinLeaveEnabled:];
-[FigCaptureWorkIntervalConfiguration startIntervalsProvisionally];
```
