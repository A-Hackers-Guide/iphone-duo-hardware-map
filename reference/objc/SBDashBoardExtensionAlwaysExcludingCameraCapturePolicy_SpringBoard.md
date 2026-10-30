# `SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LCSCaptureApplicationObserver`, `SBDashBoardCaptureLaunchPolicy`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"LCSCaptureApplicationMonitor" _applicationMonitor;
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy init];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy initWithApplicationController:];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy addLaunchPolicyObserver:];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy captureApplicationProvider:didUpdateKnownApplications:];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy initWithApplicationController:captureApplicationMonitor:];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy prewarmingConfigurationForIdentifier:captureApplicationProvider:];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy removeLaunchPolicyObserver:];
-[SBDashBoardExtensionAlwaysExcludingCameraCapturePolicy resolveCameraDestinationLaunchOf:fromSource:];
```
