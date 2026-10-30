# `CAMModeAndDeviceConfigurationTestHarness`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMPerformanceTestHarness`
- 1 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" __modeChangeListeners;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__modeChangeListeners) _modeChangeListeners;
```

## Instance methods

```
-[CAMModeAndDeviceConfigurationTestHarness setupListeners];
-[CAMModeAndDeviceConfigurationTestHarness removeListeners];
-[CAMModeAndDeviceConfigurationTestHarness _handleChangeToMode:];
-[CAMModeAndDeviceConfigurationTestHarness _handleDidCloseViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness _handleDidOpenViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness _handleWillCloseViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness _handleWillOpenViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness _modeChangeListeners];
-[CAMModeAndDeviceConfigurationTestHarness handleChangeToMode:device:];
-[CAMModeAndDeviceConfigurationTestHarness handleDidCloseViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness handleDidOpenViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness handleWillCloseViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness handleWillOpenViewfinderForReason:];
-[CAMModeAndDeviceConfigurationTestHarness initWithTestName:];
-[CAMModeAndDeviceConfigurationTestHarness registerHandler:forChangeToMode:devicePosition:];
-[CAMModeAndDeviceConfigurationTestHarness startTesting];
-[CAMModeAndDeviceConfigurationTestHarness stopTesting];
```
