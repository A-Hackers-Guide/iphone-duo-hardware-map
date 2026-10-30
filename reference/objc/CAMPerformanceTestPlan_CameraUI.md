# `CAMPerformanceTestPlan`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMPerformanceTestHarnessDelegate`
- 9 instance variables, 13 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _runningTest;
B __hasTriggeredTestStart;
I _settlingDelaySeconds;
@? _startHandler;
@? _completionHandler;
@"NSString" _testName;
@"NSMutableArray" __harnesses;
Q __completedHarnesses;
Q __startedHarnesses;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V__harnesses) _harnesses;
@property (TQ,N,V__completedHarnesses) _completedHarnesses;
@property (TQ,N,V__startedHarnesses) _startedHarnesses;
@property (TB,N,V__hasTriggeredTestStart) _hasTriggeredTestStart;
@property (TB,R,N,GisRunningTest,V_runningTest) runningTest;
@property (T@?,C,N,V_startHandler) startHandler;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"NSString",R,C,N,V_testName) testName;
@property (TI,N,V_settlingDelaySeconds) settlingDelaySeconds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMPerformanceTestPlan setCompletionHandler:];
-[CAMPerformanceTestPlan completionHandler];
-[CAMPerformanceTestPlan startHandler];
-[CAMPerformanceTestPlan isRunningTest];
-[CAMPerformanceTestPlan run];
-[CAMPerformanceTestPlan testName];
-[CAMPerformanceTestPlan setStartHandler:];
-[CAMPerformanceTestPlan _completedHarnesses];
-[CAMPerformanceTestPlan _failedTestWithReason:];
-[CAMPerformanceTestPlan _findHarnessAfter:];
-[CAMPerformanceTestPlan _harnesses];
-[CAMPerformanceTestPlan _hasTriggeredTestStart];
-[CAMPerformanceTestPlan _runHarnessAfter:];
-[CAMPerformanceTestPlan _startTesting];
-[CAMPerformanceTestPlan _startedHarnesses];
-[CAMPerformanceTestPlan _stopTesting];
-[CAMPerformanceTestPlan didFailTestHarness:withReason:];
-[CAMPerformanceTestPlan didStartSubtest:withName:withMetrics:];
-[CAMPerformanceTestPlan didStopSubtest:withName:];
-[CAMPerformanceTestPlan initWithTestName:];
-[CAMPerformanceTestPlan queueHarness:];
-[CAMPerformanceTestPlan runHarness:];
-[CAMPerformanceTestPlan runWithSecondsDelay:];
-[CAMPerformanceTestPlan setSettlingDelaySeconds:];
-[CAMPerformanceTestPlan set_completedHarnesses:];
-[CAMPerformanceTestPlan set_harnesses:];
-[CAMPerformanceTestPlan set_hasTriggeredTestStart:];
-[CAMPerformanceTestPlan set_startedHarnesses:];
-[CAMPerformanceTestPlan settlingDelaySeconds];
-[CAMPerformanceTestPlan startSubtestWithName:withMetrics:];
-[CAMPerformanceTestPlan stopSubtestWithName:];
-[CAMPerformanceTestPlan willEndTestHarness:];
-[CAMPerformanceTestPlan willStartTestHarness:];
```
