# `CAMCameraRollTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPerformanceTestHarness`
- Protocols: `CAMViewfinderViewControllerCameraRollTestingDelegate`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _awaitPreload;
B _testingWarmPresentation;
B _testingAnimation;
d _settlingDelay;
@"CAMViewfinderViewController" _viewfinderViewController;
```

## Properties

```
@property (TB,R,N,V_awaitPreload) awaitPreload;
@property (Td,R,N,V_settlingDelay) settlingDelay;
@property (TB,R,N,V_testingWarmPresentation) testingWarmPresentation;
@property (TB,R,N,GisTestingAnimation,V_testingAnimation) testingAnimation;
@property (T@"CAMViewfinderViewController",R,N,V_viewfinderViewController) viewfinderViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMCameraRollTestHarness viewfinderViewController];
-[CAMCameraRollTestHarness _dismissCameraRollImmediately];
-[CAMCameraRollTestHarness _handlePUDisplayLinkStarted:];
-[CAMCameraRollTestHarness _presentCameraRollAnimated];
-[CAMCameraRollTestHarness awaitPreload];
-[CAMCameraRollTestHarness initWithTestName:viewfinderViewController:testingAnimation:testingWarmPresentation:awaitPreload:settlingDelay:];
-[CAMCameraRollTestHarness isTestingAnimation];
-[CAMCameraRollTestHarness settlingDelay];
-[CAMCameraRollTestHarness startTesting];
-[CAMCameraRollTestHarness stopTesting];
-[CAMCameraRollTestHarness testingWarmPresentation];
-[CAMCameraRollTestHarness viewfinderViewController:didDismissPresentedCameraRoll:];
-[CAMCameraRollTestHarness viewfinderViewController:didPresentCameraRoll:];
-[CAMCameraRollTestHarness viewfinderViewController:willPresentCameraRoll:withOneUpController:];
```
