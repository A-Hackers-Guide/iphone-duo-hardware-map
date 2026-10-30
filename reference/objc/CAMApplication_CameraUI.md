# `CAMApplication`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIApplication`
- 1 instance variables, 1 properties, 25 instance methods, 4 class methods

## Instance variables

```
@"CAMPerformanceTestPlan" _currentTestPlan;
```

## Properties

```
@property (T@"CAMPerformanceTestPlan",&,N,V_currentTestPlan) currentTestPlan;
```

## Class methods

```
+[CAMApplication appOrPlugInState];
+[CAMApplication appOrPlugInInterfaceOrientation];
+[CAMApplication mainEntryTime];
+[CAMApplication isAppOrPlugInSuspended];
```

## Instance methods

```
-[CAMApplication prepareForDefaultImageSnapshotForScreen:];
-[CAMApplication runNewPPTUICaptureTestWithTestPlan:options:];
-[CAMApplication runSwitchModesWithTestPlan:options:userPreferencesOverrides:];
-[CAMApplication supportedInterfaceOrientationsForWindow:];
-[CAMApplication runLibrarySelectionWithTestPlan:options:];
-[CAMApplication willCloseViewfinderForReason:];
-[CAMApplication didChangeToMode:device:];
-[CAMApplication didOpenViewfinderForReason:];
-[CAMApplication runTakePictureFrontPortraitWithTestPlan:options:prototype:];
-[CAMApplication runPresentCameraRollWithTestPlan:options:];
-[CAMApplication didCloseViewfinderForReason:];
-[CAMApplication runTest:options:];
-[CAMApplication _registerPreviewStartBlock:];
-[CAMApplication _configureExtendedLaunchTestIfNeeded];
-[CAMApplication runSwitchToPortraitFrontWithTestPlan:options:];
-[CAMApplication runTakePictureTestWithTestPlan:options:prototype:forCaptureMode:];
-[CAMApplication runTakeVideoTestWithTestPlan:options:userPreferencesOverrides:];
-[CAMApplication _extendLaunchTest];
-[CAMApplication runSwitchCamerasTestWithTestPlan:options:];
-[CAMApplication setCurrentTestPlan:];
-[CAMApplication runPersonalPhotographerTestWithTestPlan:options:];
-[CAMApplication willOpenViewfinderForReason:];
-[CAMApplication runTakePicturePortraitWithTestPlan:options:prototype:];
-[CAMApplication runTakePictureFrontCameraWithTestPlan:options:prototype:forCaptureMode:];
-[CAMApplication currentTestPlan];
```
