# `CAMIntervalometerTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPerformanceTestHarness`
- Protocols: `CAMStillImageCaptureRequestDelegate`, `CAMCaptureRequestIntervalometerDelegate`
- 10 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"CUCaptureController" _captureController;
B _performWarmupCapture;
B _waitingOnWarmupCapture;
@"NSString" _finalRequestPersistenceUUID;
q _mode;
@"NSMutableDictionary" _numberOfResponsesForRequest;
Q _expectedNumberOfResponsesPerRequest;
d _delayBetweenCaptures;
d _lastCaptureCompletionTime;
@"CAMCaptureRequestIntervalometer" _testIntervalometer;
```

## Properties

```
@property (T@"CAMCaptureRequestIntervalometer",&,N,V_testIntervalometer) testIntervalometer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMIntervalometerTestHarness stillImageRequestDidCompleteStillImageCapture:withResponse:error:];
-[CAMIntervalometerTestHarness stillImageRequestDidCompleteCapture:error:];
-[CAMIntervalometerTestHarness intervalometer:didReachMaximumCountWithRequest:];
-[CAMIntervalometerTestHarness stillImageRequestDidStopCapturingStillImage:];
-[CAMIntervalometerTestHarness intervalometer:didGenerateCaptureRequest:];
-[CAMIntervalometerTestHarness _allowOverlappingCaptures];
-[CAMIntervalometerTestHarness _hasReceivedExpectedNumberOfResponsesForPersistenceUUID:failureReason:];
-[CAMIntervalometerTestHarness _hasReceivedExpectedNumberOfResponsesForRequestsWithFailureReason:];
-[CAMIntervalometerTestHarness _shouldDelayBeforeCapturing];
-[CAMIntervalometerTestHarness failedTestWithReason:];
-[CAMIntervalometerTestHarness initWithTestName:expectedNumberOfCapturesPerRequest:captureController:performingWarmupCapture:forCaptureMode:delayBetweenCaptures:];
-[CAMIntervalometerTestHarness setTestIntervalometer:];
-[CAMIntervalometerTestHarness startTesting];
-[CAMIntervalometerTestHarness stopTesting];
-[CAMIntervalometerTestHarness testIntervalometer];
```
