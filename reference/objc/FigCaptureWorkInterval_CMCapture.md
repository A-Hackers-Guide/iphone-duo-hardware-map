# `FigCaptureWorkInterval`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 4 properties, 14 instance methods, 6 class methods

## Instance variables

```
@"NSString" _name;
i _workIntervalType;
@"NSArray" _workIntervalPool;
^^{work_interval_instance} _provisionallyStartedInstances;
@"NSMutableArray" _workGroupPool;
^I _machPortPool;
^@ _workGroupArray;
q _intervalDurationNanoseconds;
q _expectedThroughputNanoseconds;
Q _frameId;
@"NSMutableDictionary" _frameIdToWorkIntervalInstance;
@"NSMutableArray" _recentIntervalDurations;
i _recentIntervalNextIndex;
i _recentIntervalCount;
i _recentIntervalWindowCapacity;
d _recentIntervalSum;
B _intervalTrackingEnabled;
B _joinLeaveEnabled;
i _concurrentIntervalCount;
i _nextIntervalIndex;
B _startIntervalsProvisionally;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _intervalPoolLock;
i _staleInstanceCounter;
B _adaptiveDeadlineEnabled;
q _intervalDuration;
```

## Properties

```
@property (Tq,N,V_intervalDuration) intervalDuration;
@property (TI,R,N) intervalCount;
@property (T@"NSArray",R,N) machPorts;
@property (T@"NSArray",R,N) osWorkgroups;
```

## Class methods

```
+[FigCaptureWorkInterval intervalFromSampleBuffer:];
+[FigCaptureWorkInterval intervalIndexForSampleBuffer:];
+[FigCaptureWorkInterval leaveInterval:];
+[FigCaptureWorkInterval workIntervalInfoFromSampleBuffer:];
+[FigCaptureWorkInterval workIntervalInfoFromSampleBufferAttachments:];
+[FigCaptureWorkInterval workIntervalInfoFromWorkIntervalDictionary:];
```

## Instance methods

```
-[FigCaptureWorkInterval dealloc];
-[FigCaptureWorkInterval intervalCount];
-[FigCaptureWorkInterval finishInterval:displayTime:];
-[FigCaptureWorkInterval finishIntervalWithWorkIntervalDictionary:];
-[FigCaptureWorkInterval initWithName:workIntervalType:];
-[FigCaptureWorkInterval intervalDuration];
-[FigCaptureWorkInterval joinInterval:fromInterval:withOptionalLog:];
-[FigCaptureWorkInterval machPorts];
-[FigCaptureWorkInterval osWorkgroups];
-[FigCaptureWorkInterval setIntervalDuration:];
-[FigCaptureWorkInterval startInterval:];
-[FigCaptureWorkInterval startInterval:withStartPts:workIntervalMetadata:];
-[FigCaptureWorkInterval startTrackingRecurringWorkWithIntervals];
-[FigCaptureWorkInterval stopTrackingRecurringWorkWithIntervals];
```
