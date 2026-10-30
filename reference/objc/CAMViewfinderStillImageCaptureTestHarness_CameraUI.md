# `CAMViewfinderStillImageCaptureTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPerformanceTestHarness`
- Protocols: `CAMViewfinderViewControllerStillImageCaptureRequestTestingDelegate`, `CAMViewfinderActionIntervalometerDelegate`
- 18 instance variables, 22 properties, 48 instance methods, 0 class methods

## Instance variables

```
B _stillDuringVideo;
B __performWarmupCapture;
B __waitingOnWarmupCapture;
B __capturesOnTouchDown;
@"CAMViewfinderActionIntervalometer" _testIntervalometer;
@? _didUpdateFinalThumbnailHandler;
@"NSString" __finalRequestPersistenceUUID;
q __mode;
@"NSCountedSet" __requestIDs;
Q __receivedCallbackCount;
Q __expectedNumberOfResponsesPerRequest;
d __delayBetweenCaptures;
d __lastCaptureCompletionTime;
@"CAMViewfinderViewController" __viewfinderViewController;
Q __maxStillImageCount;
Q __generatedRequestsCount;
d __initialDelayInSeconds;
d __postDelayInSeconds;
```

## Properties

```
@property (TB,N,V__performWarmupCapture) _performWarmupCapture;
@property (TB,N,V__waitingOnWarmupCapture) _waitingOnWarmupCapture;
@property (T@"NSString",&,N,V__finalRequestPersistenceUUID) _finalRequestPersistenceUUID;
@property (Tq,N,V__mode) _mode;
@property (T@"NSCountedSet",&,N,V__requestIDs) _requestIDs;
@property (TQ,N,V__receivedCallbackCount) _receivedCallbackCount;
@property (TQ,N,V__expectedNumberOfResponsesPerRequest) _expectedNumberOfResponsesPerRequest;
@property (Td,N,V__delayBetweenCaptures) _delayBetweenCaptures;
@property (Td,N,V__lastCaptureCompletionTime) _lastCaptureCompletionTime;
@property (T@"CAMViewfinderViewController",&,N,V__viewfinderViewController) _viewfinderViewController;
@property (TB,N,V__capturesOnTouchDown) _capturesOnTouchDown;
@property (TQ,N,V__maxStillImageCount) _maxStillImageCount;
@property (TQ,N,V__generatedRequestsCount) _generatedRequestsCount;
@property (Td,R,N,V__initialDelayInSeconds) _initialDelayInSeconds;
@property (Td,R,N,V__postDelayInSeconds) _postDelayInSeconds;
@property (T@"CAMViewfinderActionIntervalometer",&,N,V_testIntervalometer) testIntervalometer;
@property (T@?,C,N,V_didUpdateFinalThumbnailHandler) didUpdateFinalThumbnailHandler;
@property (TB,N,GisStillDuringVideo,V_stillDuringVideo) stillDuringVideo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMViewfinderStillImageCaptureTestHarness _mode];
-[CAMViewfinderStillImageCaptureTestHarness setStillDuringVideo:];
-[CAMViewfinderStillImageCaptureTestHarness executeAction];
-[CAMViewfinderStillImageCaptureTestHarness set_requestIDs:];
-[CAMViewfinderStillImageCaptureTestHarness _allowOverlappingCaptures];
-[CAMViewfinderStillImageCaptureTestHarness _capturesOnTouchDown];
-[CAMViewfinderStillImageCaptureTestHarness _delayBetweenCaptures];
-[CAMViewfinderStillImageCaptureTestHarness _expectedNumberOfResponsesPerRequest];
-[CAMViewfinderStillImageCaptureTestHarness _finalRequestPersistenceUUID];
-[CAMViewfinderStillImageCaptureTestHarness _generatedRequestsCount];
-[CAMViewfinderStillImageCaptureTestHarness _initialDelayInSeconds];
-[CAMViewfinderStillImageCaptureTestHarness _lastCaptureCompletionTime];
-[CAMViewfinderStillImageCaptureTestHarness _maxStillImageCount];
-[CAMViewfinderStillImageCaptureTestHarness _performWarmupCapture];
-[CAMViewfinderStillImageCaptureTestHarness _postDelayInSeconds];
-[CAMViewfinderStillImageCaptureTestHarness _receivedCallbackCount];
-[CAMViewfinderStillImageCaptureTestHarness _requestIDs];
-[CAMViewfinderStillImageCaptureTestHarness _viewfinderViewController];
-[CAMViewfinderStillImageCaptureTestHarness _waitingOnWarmupCapture];
-[CAMViewfinderStillImageCaptureTestHarness cancelTesting];
-[CAMViewfinderStillImageCaptureTestHarness didUpdateFinalThumbnailHandler];
-[CAMViewfinderStillImageCaptureTestHarness failedTestWithReason:];
-[CAMViewfinderStillImageCaptureTestHarness initWithTestName:maxStillImageCount:expectedNumberOfCapturesPerRequest:viewfinderViewController:performingWarmupCapture:forCaptureMode:delayBetweenCaptures:capturesOnTouchDown:];
-[CAMViewfinderStillImageCaptureTestHarness initWithTestName:maxStillImageCount:expectedNumberOfCapturesPerRequest:viewfinderViewController:performingWarmupCapture:forCaptureMode:delayBetweenCaptures:capturesOnTouchDown:initialDelayInSeconds:postDelayInSeconds:];
-[CAMViewfinderStillImageCaptureTestHarness isStillDuringVideo];
-[CAMViewfinderStillImageCaptureTestHarness setDidUpdateFinalThumbnailHandler:];
-[CAMViewfinderStillImageCaptureTestHarness setTestIntervalometer:];
-[CAMViewfinderStillImageCaptureTestHarness set_capturesOnTouchDown:];
-[CAMViewfinderStillImageCaptureTestHarness set_delayBetweenCaptures:];
-[CAMViewfinderStillImageCaptureTestHarness set_expectedNumberOfResponsesPerRequest:];
-[CAMViewfinderStillImageCaptureTestHarness set_finalRequestPersistenceUUID:];
-[CAMViewfinderStillImageCaptureTestHarness set_generatedRequestsCount:];
-[CAMViewfinderStillImageCaptureTestHarness set_lastCaptureCompletionTime:];
-[CAMViewfinderStillImageCaptureTestHarness set_maxStillImageCount:];
-[CAMViewfinderStillImageCaptureTestHarness set_mode:];
-[CAMViewfinderStillImageCaptureTestHarness set_performWarmupCapture:];
-[CAMViewfinderStillImageCaptureTestHarness set_receivedCallbackCount:];
-[CAMViewfinderStillImageCaptureTestHarness set_viewfinderViewController:];
-[CAMViewfinderStillImageCaptureTestHarness set_waitingOnWarmupCapture:];
-[CAMViewfinderStillImageCaptureTestHarness shouldAttemptAction];
-[CAMViewfinderStillImageCaptureTestHarness startTesting];
-[CAMViewfinderStillImageCaptureTestHarness stopTesting];
-[CAMViewfinderStillImageCaptureTestHarness testIntervalometer];
-[CAMViewfinderStillImageCaptureTestHarness viewfinderViewController:didReceiveStillImageRequestDidCompleteCapture:error:];
-[CAMViewfinderStillImageCaptureTestHarness viewfinderViewController:didReceiveStillImageRequestDidCompleteStillImageCapture:withResponse:error:];
-[CAMViewfinderStillImageCaptureTestHarness viewfinderViewController:didReceiveStillImageRequestDidStopCapturingStillImage:];
-[CAMViewfinderStillImageCaptureTestHarness viewfinderViewController:didUpdateImageWellWithRequest:response:error:];
-[CAMViewfinderStillImageCaptureTestHarness viewfinderViewController:willCaptureStillImageForRequest:];
```
