# `SBCaptureApplicationCenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LCSCaptureApplicationObserver`, `SBFCaptureApplicationProviding`
- 4 instance variables, 7 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"LCSCaptureApplicationMonitor" _captureApplicationMonitor;
@"NSObject<OS_dispatch_queue>" _queue;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"LCSCaptureApplicationMonitor",R,N,V_captureApplicationMonitor) captureApplicationMonitor;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCaptureApplicationCenter sharedInstance];
+[SBCaptureApplicationCenter captureApplicationSettings];
```

## Instance methods

```
-[SBCaptureApplicationCenter applicationController];
-[SBCaptureApplicationCenter removeObserver:];
-[SBCaptureApplicationCenter initWithApplicationController:];
-[SBCaptureApplicationCenter setApplicationController:];
-[SBCaptureApplicationCenter queue];
-[SBCaptureApplicationCenter addObserver:];
-[SBCaptureApplicationCenter setQueue:];
-[SBCaptureApplicationCenter predictedPrewarmBundleIdentifierForApplicationBundleIdentifier:];
-[SBCaptureApplicationCenter _bundleHasCameraEntitlement:];
-[SBCaptureApplicationCenter _captureWindowScene];
-[SBCaptureApplicationCenter _isTCCGrantedForKey:applicationBundleIdentifier:];
-[SBCaptureApplicationCenter _sceneEntityForApplication:];
-[SBCaptureApplicationCenter _sceneEntityForApplication:windowScene:];
-[SBCaptureApplicationCenter _shouldPromptLaunchTerminationAlertForTerminationInfo:];
-[SBCaptureApplicationCenter _storeTerminationInfoWithProcessName:reason:];
-[SBCaptureApplicationCenter _terminationInfoList];
-[SBCaptureApplicationCenter captureApplicationForBundleIdentifier:];
-[SBCaptureApplicationCenter captureApplicationForExtensionIdentifier:];
-[SBCaptureApplicationCenter captureApplicationMonitor];
-[SBCaptureApplicationCenter captureApplicationProvider:didUpdateKnownApplications:];
-[SBCaptureApplicationCenter isApplicationLaunchNeededForApplicationBundleIdentifier:];
-[SBCaptureApplicationCenter knownCaptureApplications];
-[SBCaptureApplicationCenter launchActionsForCaptureApplication:launchTarget:launchType:];
-[SBCaptureApplicationCenter launchCaptureApplication:launchType:source:];
-[SBCaptureApplicationCenter launchForExtensionToApplicationTransition:windowScene:launchActions:completionHandler:];
-[SBCaptureApplicationCenter promptLaunchTerminationAlertIfNecessaryForProcess:afterDelay:reason:];
-[SBCaptureApplicationCenter shouldInstallLaunchMonitoringForCaptureApplicationBundleIdentfier:];
-[SBCaptureApplicationCenter suspendCaptureApplication:];
```
