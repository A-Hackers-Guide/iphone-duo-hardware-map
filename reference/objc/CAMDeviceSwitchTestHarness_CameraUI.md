# `CAMDeviceSwitchTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMModeAndDeviceConfigurationTestHarness`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _testingAnimation;
@"CAMViewfinderViewController" _viewfinderViewController;
q _desiredDevicePosition;
q _startingCaptureMode;
d _postDelayInSeconds;
```

## Properties

```
@property (T@"CAMViewfinderViewController",R,N,V_viewfinderViewController) viewfinderViewController;
@property (Tq,R,N,V_desiredDevicePosition) desiredDevicePosition;
@property (Tq,R,N,V_startingCaptureMode) startingCaptureMode;
@property (TB,R,N,GisTestingAnimation,V_testingAnimation) testingAnimation;
@property (Td,R,N,V_postDelayInSeconds) postDelayInSeconds;
```

## Instance methods

```
-[CAMDeviceSwitchTestHarness viewfinderViewController];
-[CAMDeviceSwitchTestHarness _internalStopTesting];
-[CAMDeviceSwitchTestHarness desiredDevicePosition];
-[CAMDeviceSwitchTestHarness ensureCaptureDevicePosition:mode:thenPerform:];
-[CAMDeviceSwitchTestHarness handleDidOpenViewfinderForReason:];
-[CAMDeviceSwitchTestHarness initWithTestName:viewfinderViewController:devicePosition:testingAnimation:startingCaptureMode:postDelayInSeconds:];
-[CAMDeviceSwitchTestHarness isTestingAnimation];
-[CAMDeviceSwitchTestHarness postDelayInSeconds];
-[CAMDeviceSwitchTestHarness startTesting];
-[CAMDeviceSwitchTestHarness startingCaptureMode];
```
