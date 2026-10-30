# `CFXCameraControlsViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 26 instance variables, 27 properties, 71 instance methods, 0 class methods

## Instance variables

```
B _dockIsMagnified;
@"CAMCreativeCameraButton" _effectButton;
@"CAMFlipButton" _flipButton;
@"<CFXCameraControlsViewControllerDelegate>" _delegate;
@"UIView" _appStripBackgroundView;
@"UIView" _backgroundView;
@"UIView" _effectButtonContainerPad;
@"UIView" _shutterButtonContainerPad;
@"UIView" _flipButtonContainerPad;
@"UIView" _bottomBlackView;
@"UIView" _appStripBackgroundContainerView;
@"NSLayoutConstraint" _backgroundViewHeightConstraint;
@"NSLayoutConstraint" _bottomBlackViewHeightConstraint;
@"NSLayoutConstraint" _bottomBlackViewTopConstraint;
@"NSLayoutConstraint" _bottomBlackViewWidthConstraint;
@"NSLayoutConstraint" _bottomBlackViewTrailingConstraint;
@"NSLayoutConstraint" _appStripBackgroundContainerViewTopConstraint;
@"NSLayoutConstraint" _appStripBackgroundContainerViewBottomConstraint;
@"NSLayoutConstraint" _appStripBackgroundContainerViewHeightConstraint;
@"NSLayoutConstraint" _appStripBackgroundContainerViewLeadingConstraint;
@"NSLayoutConstraint" _appStripBackgroundContainerViewTrailingConstraint;
@"CFXFeedbackController" _feedbackController;
q _captureMode;
@"CAMBottomBar" _bottomBar;
@"CUShutterButton" _shutterButton;
d _dockMagnifiedHeightDelta;
```

## Properties

```
@property (T@"UIView",W,N,V_effectButtonContainerPad) effectButtonContainerPad;
@property (T@"UIView",W,N,V_shutterButtonContainerPad) shutterButtonContainerPad;
@property (T@"UIView",W,N,V_flipButtonContainerPad) flipButtonContainerPad;
@property (T@"UIView",W,N,V_backgroundView) backgroundView;
@property (T@"UIView",W,N,V_bottomBlackView) bottomBlackView;
@property (T@"UIView",&,N,V_appStripBackgroundView) appStripBackgroundView;
@property (T@"UIView",W,N,V_appStripBackgroundContainerView) appStripBackgroundContainerView;
@property (T@"NSLayoutConstraint",W,N,V_backgroundViewHeightConstraint) backgroundViewHeightConstraint;
@property (T@"NSLayoutConstraint",W,N,V_bottomBlackViewHeightConstraint) bottomBlackViewHeightConstraint;
@property (T@"NSLayoutConstraint",W,N,V_bottomBlackViewTopConstraint) bottomBlackViewTopConstraint;
@property (T@"NSLayoutConstraint",W,N,V_bottomBlackViewWidthConstraint) bottomBlackViewWidthConstraint;
@property (T@"NSLayoutConstraint",W,N,V_bottomBlackViewTrailingConstraint) bottomBlackViewTrailingConstraint;
@property (T@"NSLayoutConstraint",W,N,V_appStripBackgroundContainerViewTopConstraint) appStripBackgroundContainerViewTopConstraint;
@property (T@"NSLayoutConstraint",W,N,V_appStripBackgroundContainerViewBottomConstraint) appStripBackgroundContainerViewBottomConstraint;
@property (T@"NSLayoutConstraint",W,N,V_appStripBackgroundContainerViewHeightConstraint) appStripBackgroundContainerViewHeightConstraint;
@property (T@"NSLayoutConstraint",W,N,V_appStripBackgroundContainerViewLeadingConstraint) appStripBackgroundContainerViewLeadingConstraint;
@property (T@"NSLayoutConstraint",W,N,V_appStripBackgroundContainerViewTrailingConstraint) appStripBackgroundContainerViewTrailingConstraint;
@property (T@"CFXFeedbackController",&,N,V_feedbackController) feedbackController;
@property (Tq,N,V_captureMode) captureMode;
@property (T@"CAMBottomBar",&,N,V_bottomBar) bottomBar;
@property (T@"CUShutterButton",&,N,V_shutterButton) shutterButton;
@property (TB,N,V_dockIsMagnified) dockIsMagnified;
@property (Td,N,V_dockMagnifiedHeightDelta) dockMagnifiedHeightDelta;
@property (T@"CAMCreativeCameraButton",&,N,V_effectButton) effectButton;
@property (T@"CAMFlipButton",&,N,V_flipButton) flipButton;
@property (T@"<CFXCameraControlsViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIColor",N) backgroundColor;
```

## Instance methods

```
-[CFXCameraControlsViewController init];
-[CFXCameraControlsViewController viewDidLoad];
-[CFXCameraControlsViewController setBackgroundColor:];
-[CFXCameraControlsViewController viewWillAppear:];
-[CFXCameraControlsViewController setCaptureMode:];
-[CFXCameraControlsViewController setDelegate:];
-[CFXCameraControlsViewController viewDidAppear:];
-[CFXCameraControlsViewController captureMode];
-[CFXCameraControlsViewController delegate];
-[CFXCameraControlsViewController backgroundColor];
-[CFXCameraControlsViewController backgroundView];
-[CFXCameraControlsViewController viewWillLayoutSubviews];
-[CFXCameraControlsViewController viewDidDisappear:];
-[CFXCameraControlsViewController setBackgroundView:];
-[CFXCameraControlsViewController shutterButton];
-[CFXCameraControlsViewController feedbackController];
-[CFXCameraControlsViewController flipButton];
-[CFXCameraControlsViewController setFlipButton:];
-[CFXCameraControlsViewController setFeedbackController:];
-[CFXCameraControlsViewController bottomBar];
-[CFXCameraControlsViewController setShutterButton:];
-[CFXCameraControlsViewController backgroundViewHeightConstraint];
-[CFXCameraControlsViewController setBackgroundViewHeightConstraint:];
-[CFXCameraControlsViewController setBottomBar:];
-[CFXCameraControlsViewController CFX_smallPhoneDockHeightAdjustment];
-[CFXCameraControlsViewController bottomBlackView];
-[CFXCameraControlsViewController appStripBackgroundContainerView];
-[CFXCameraControlsViewController bottomBlackViewHeightConstraint];
-[CFXCameraControlsViewController dockIsMagnified];
-[CFXCameraControlsViewController JFX_orientationMonitorInterfaceOrientationNotification:];
-[CFXCameraControlsViewController appStripBackgroundContainerViewBottomConstraint];
-[CFXCameraControlsViewController appStripBackgroundContainerViewHeightConstraint];
-[CFXCameraControlsViewController appStripBackgroundContainerViewLeadingConstraint];
-[CFXCameraControlsViewController appStripBackgroundContainerViewTopConstraint];
-[CFXCameraControlsViewController appStripBackgroundContainerViewTrailingConstraint];
-[CFXCameraControlsViewController appStripBackgroundView];
-[CFXCameraControlsViewController bottomBlackViewTopConstraint];
-[CFXCameraControlsViewController bottomBlackViewTrailingConstraint];
-[CFXCameraControlsViewController bottomBlackViewWidthConstraint];
-[CFXCameraControlsViewController configureUIForOrientation];
-[CFXCameraControlsViewController dockMagnifiedHeightDelta];
-[CFXCameraControlsViewController effectButton];
-[CFXCameraControlsViewController effectButtonContainerPad];
-[CFXCameraControlsViewController effectsButtonTapped:];
-[CFXCameraControlsViewController flipButtonContainerPad];
-[CFXCameraControlsViewController initWithDelegate:captureMode:];
-[CFXCameraControlsViewController setAppStripBackgroundContainerView:];
-[CFXCameraControlsViewController setAppStripBackgroundContainerViewBottomConstraint:];
-[CFXCameraControlsViewController setAppStripBackgroundContainerViewHeightConstraint:];
-[CFXCameraControlsViewController setAppStripBackgroundContainerViewLeadingConstraint:];
-[CFXCameraControlsViewController setAppStripBackgroundContainerViewTopConstraint:];
-[CFXCameraControlsViewController setAppStripBackgroundContainerViewTrailingConstraint:];
-[CFXCameraControlsViewController setAppStripBackgroundView:];
-[CFXCameraControlsViewController setBottomBlackView:];
-[CFXCameraControlsViewController setBottomBlackViewHeightConstraint:];
-[CFXCameraControlsViewController setBottomBlackViewTopConstraint:];
-[CFXCameraControlsViewController setBottomBlackViewTrailingConstraint:];
-[CFXCameraControlsViewController setBottomBlackViewWidthConstraint:];
-[CFXCameraControlsViewController setDockIsMagnified:];
-[CFXCameraControlsViewController setDockMagnifiedHeightDelta:];
-[CFXCameraControlsViewController setEffectButton:];
-[CFXCameraControlsViewController setEffectButtonContainerPad:];
-[CFXCameraControlsViewController setFlipButtonContainerPad:];
-[CFXCameraControlsViewController setShutterButtonAlpha:];
-[CFXCameraControlsViewController setShutterButtonContainerPad:];
-[CFXCameraControlsViewController setShutterButtonEnabled:];
-[CFXCameraControlsViewController shutterButtonContainerPad];
-[CFXCameraControlsViewController shutterButtonTapped:];
-[CFXCameraControlsViewController switchCameraButtonTapped:];
-[CFXCameraControlsViewController updateUIForDockMagnify:dockHeightDelta:];
-[CFXCameraControlsViewController updateUIForVideoRecording:];
```
