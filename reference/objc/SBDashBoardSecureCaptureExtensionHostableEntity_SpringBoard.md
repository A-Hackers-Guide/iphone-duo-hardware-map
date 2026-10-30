# `SBDashBoardSecureCaptureExtensionHostableEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSCameraExtensionViewControllerDelegate`, `FBSceneObserver`, `SBFCaptureApplicationLaunchMonitorDelegate`, `SBCameraViewfinderMonitorObserver`, `SBDashBoardCaptureApplicationTransitionRequestDelegate`, `CSHostableEntity`
- 11 instance variables, 10 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"CSCameraExtensionViewController" _cameraExtensionViewController;
@"SBCaptureApplicationLaunchMonitor" _launchMonitor;
@"SBCaptureExtensionIdleTimerManager" _idleTimerManager;
@"SBDashBoardCaptureApplicationTransitionRequest" _transitionToApplicationRequest;
B _isCameraPrewarmed;
@"FBScene" _extensionScene;
@"SBWindowScene" _extensionSceneHostingWindowScene;
@"<BSInvalidatable>" _keyboardFocusDeferringRule;
@"<LCSCaptureApplicationDescribing>" _captureApplication;
Q _launchType;
```

## Properties

```
@property (T@"<LCSCaptureApplicationDescribing>",R,N,V_captureApplication) captureApplication;
@property (TQ,R,N,V_launchType) launchType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CSCoverSheetViewControllerBase<CSCoverSheetViewPresenting><CSHostableEntityPresenting><BSInvalidatable>",R,N) hostingViewController;
@property (Tq,R,N) presentationPriority;
@property (T@"SBDisplayItem",R,N) displayItemRepresentation;
@property (T@"NSString",R,C,N) applicationBundleIdentifier;
```

## Instance methods

```
-[SBDashBoardSecureCaptureExtensionHostableEntity scene:clientDidConnect:];
-[SBDashBoardSecureCaptureExtensionHostableEntity launchType];
-[SBDashBoardSecureCaptureExtensionHostableEntity dealloc];
-[SBDashBoardSecureCaptureExtensionHostableEntity presentationPriority];
-[SBDashBoardSecureCaptureExtensionHostableEntity sceneDidInvalidate:];
-[SBDashBoardSecureCaptureExtensionHostableEntity hostingContainerViewController];
-[SBDashBoardSecureCaptureExtensionHostableEntity displayItemRepresentation];
-[SBDashBoardSecureCaptureExtensionHostableEntity applicationBundleIdentifier];
-[SBDashBoardSecureCaptureExtensionHostableEntity hostingViewController];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:requestsLaunchMonitoringForScene:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:didCreateScene:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:didDestroyScene:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:didMoveToWindow:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:requestsLaunchAfterTransitionCompletionWithAction:completion:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:requestsLaunchWithAction:completion:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewControllerWillPresent:];
-[SBDashBoardSecureCaptureExtensionHostableEntity captureApplication];
-[SBDashBoardSecureCaptureExtensionHostableEntity captureApplicationMonitor:hasMetLaunchRequirements:unmetReason:];
-[SBDashBoardSecureCaptureExtensionHostableEntity _cameraPrewarmer];
-[SBDashBoardSecureCaptureExtensionHostableEntity _requestTransitionToCaptureApplication:actions:completion:];
-[SBDashBoardSecureCaptureExtensionHostableEntity _resetTransitionRequest];
-[SBDashBoardSecureCaptureExtensionHostableEntity _updateKeyboardFocusDeferringRuleForReason:];
-[SBDashBoardSecureCaptureExtensionHostableEntity cameraExtensionViewController:cancelLaunchMonitoringForScene:];
-[SBDashBoardSecureCaptureExtensionHostableEntity captureApplicationTransitionRequest:didCompleteWithError:];
-[SBDashBoardSecureCaptureExtensionHostableEntity captureApplicationTransitionRequestWillLaunchApplication:];
-[SBDashBoardSecureCaptureExtensionHostableEntity iconZoomingViewIdentifier];
-[SBDashBoardSecureCaptureExtensionHostableEntity initWithCaptureApplication:launchType:applicationController:];
```
