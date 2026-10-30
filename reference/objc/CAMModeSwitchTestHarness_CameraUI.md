# `CAMModeSwitchTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMModeAndDeviceConfigurationTestHarness`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _testingAnimation;
@"CAMViewfinderViewController" _viewfinderViewController;
q _desiredMode;
q _startingMode;
d _postDelayInSeconds;
```

## Properties

```
@property (T@"CAMViewfinderViewController",R,N,V_viewfinderViewController) viewfinderViewController;
@property (Tq,R,N,V_desiredMode) desiredMode;
@property (Tq,R,N,V_startingMode) startingMode;
@property (TB,R,N,GisTestingAnimation,V_testingAnimation) testingAnimation;
@property (Td,R,N,V_postDelayInSeconds) postDelayInSeconds;
```

## Instance methods

```
-[CAMModeSwitchTestHarness viewfinderViewController];
-[CAMModeSwitchTestHarness desiredMode];
-[CAMModeSwitchTestHarness _ensureCaptureMode:thenPerform:];
-[CAMModeSwitchTestHarness _internalStopTesting];
-[CAMModeSwitchTestHarness _startTestingAfterModeSwitchIsTestingAnimation:];
-[CAMModeSwitchTestHarness handleDidOpenViewfinderForReason:];
-[CAMModeSwitchTestHarness initWithTestName:viewfinderViewController:startingMode:destinationMode:testingAnimation:postDelayInSeconds:];
-[CAMModeSwitchTestHarness isTestingAnimation];
-[CAMModeSwitchTestHarness postDelayInSeconds];
-[CAMModeSwitchTestHarness startTesting];
-[CAMModeSwitchTestHarness startingMode];
```
