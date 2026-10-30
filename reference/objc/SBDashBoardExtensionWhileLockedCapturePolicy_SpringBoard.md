# `SBDashBoardExtensionWhileLockedCapturePolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LCSCaptureApplicationObserver`, `SBDashBoardCaptureLaunchPolicy`
- 4 instance variables, 4 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"<SBFAuthenticationStatusProvider>" _authenticationStatusProvider;
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

## Class methods

```
+[SBDashBoardExtensionWhileLockedCapturePolicy new];
+[SBDashBoardExtensionWhileLockedCapturePolicy policyWithAuthenticationStatusProvider:];
+[SBDashBoardExtensionWhileLockedCapturePolicy policyWithAuthenticationStatusProvider:applicationController:captureApplicationMonitor:];
```

## Instance methods

```
-[SBDashBoardExtensionWhileLockedCapturePolicy init];
-[SBDashBoardExtensionWhileLockedCapturePolicy initWithAuthenticationStatusProvider:captureApplicationMonitor:];
-[SBDashBoardExtensionWhileLockedCapturePolicy _authenticationStateDidChange:];
-[SBDashBoardExtensionWhileLockedCapturePolicy _notePolicyMayHaveChanged];
-[SBDashBoardExtensionWhileLockedCapturePolicy addLaunchPolicyObserver:];
-[SBDashBoardExtensionWhileLockedCapturePolicy captureApplicationProvider:didUpdateKnownApplications:];
-[SBDashBoardExtensionWhileLockedCapturePolicy initWithAuthenticationStatusProvider:applicationController:captureApplicationMonitor:];
-[SBDashBoardExtensionWhileLockedCapturePolicy prewarmingConfigurationForIdentifier:captureApplicationProvider:];
-[SBDashBoardExtensionWhileLockedCapturePolicy removeLaunchPolicyObserver:];
-[SBDashBoardExtensionWhileLockedCapturePolicy resolveCameraDestinationLaunchOf:fromSource:];
```
