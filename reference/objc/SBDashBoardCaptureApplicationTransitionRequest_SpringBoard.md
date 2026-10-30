# `SBDashBoardCaptureApplicationTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<LCSCaptureApplicationDescribing>" _captureApplication;
@"SBApplicationController" _applicationController;
@"SBWindowScene" _windowScene;
@"NSSet" _launchActions;
@? _completion;
@"<SBDashBoardCaptureApplicationTransitionRequestDelegate>" _delegate;
```

## Properties

```
@property (T@"<LCSCaptureApplicationDescribing>",&,N,V_captureApplication) captureApplication;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (T@"SBWindowScene",&,N,V_windowScene) windowScene;
@property (T@?,C,N,V_completion) completion;
@property (T@"NSSet",&,N,V_launchActions) launchActions;
@property (T@"<SBDashBoardCaptureApplicationTransitionRequestDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBDashBoardCaptureApplicationTransitionRequest _unlock];
-[SBDashBoardCaptureApplicationTransitionRequest setCompletion:];
-[SBDashBoardCaptureApplicationTransitionRequest completion];
-[SBDashBoardCaptureApplicationTransitionRequest setWindowScene:];
-[SBDashBoardCaptureApplicationTransitionRequest applicationController];
-[SBDashBoardCaptureApplicationTransitionRequest setLaunchActions:];
-[SBDashBoardCaptureApplicationTransitionRequest setApplicationController:];
-[SBDashBoardCaptureApplicationTransitionRequest launchActions];
-[SBDashBoardCaptureApplicationTransitionRequest setDelegate:];
-[SBDashBoardCaptureApplicationTransitionRequest delegate];
-[SBDashBoardCaptureApplicationTransitionRequest windowScene];
-[SBDashBoardCaptureApplicationTransitionRequest _errorWithCode:underlyingError:];
-[SBDashBoardCaptureApplicationTransitionRequest captureApplication];
-[SBDashBoardCaptureApplicationTransitionRequest setCaptureApplication:];
-[SBDashBoardCaptureApplicationTransitionRequest initWithCaptureApplication:windowScene:applicationController:];
-[SBDashBoardCaptureApplicationTransitionRequest initiate];
```
