# `CAMPerformanceTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isSetupHarness;
B _runningTest;
@"NSString" _testName;
@? _completionHandler;
@? _startHandler;
@"<CAMPerformanceTestHarnessDelegate>" _delegate;
```

## Properties

```
@property (TB,N,GisRunningTest,V_runningTest) runningTest;
@property (T@"NSString",R,C,N,V_testName) testName;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@?,C,N,V_startHandler) startHandler;
@property (T@"<CAMPerformanceTestHarnessDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_isSetupHarness) isSetupHarness;
```

## Instance methods

```
-[CAMPerformanceTestHarness setCompletionHandler:];
-[CAMPerformanceTestHarness completionHandler];
-[CAMPerformanceTestHarness setDelegate:];
-[CAMPerformanceTestHarness startHandler];
-[CAMPerformanceTestHarness delegate];
-[CAMPerformanceTestHarness isRunningTest];
-[CAMPerformanceTestHarness testName];
-[CAMPerformanceTestHarness setStartHandler:];
-[CAMPerformanceTestHarness setRunningTest:];
-[CAMPerformanceTestHarness failedTestWithReason:];
-[CAMPerformanceTestHarness initWithTestName:];
-[CAMPerformanceTestHarness isSetupHarness];
-[CAMPerformanceTestHarness setIsSetupHarness:];
-[CAMPerformanceTestHarness startSubtestWithName:];
-[CAMPerformanceTestHarness startSubtestWithName:withMetrics:];
-[CAMPerformanceTestHarness startTesting];
-[CAMPerformanceTestHarness stopSubtestWithName:];
-[CAMPerformanceTestHarness stopTesting];
```
