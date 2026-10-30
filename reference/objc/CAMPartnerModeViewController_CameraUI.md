# `CAMPartnerModeViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CAMElapsedTimeViewDelegate`, `CAMViewfinderTransitionable`
- 26 instance variables, 29 properties, 100 instance methods, 0 class methods

## Instance variables

```
B _previewNeedsHalfTurnCorrection;
B __videoCapturing;
B __isFlashActive;
B __nightModeShowing;
B __personalPhotographerCountdownShowing;
B __previewEnabled;
q _captureOrientation;
@"CAMCoverScreenStateWrapper" __state;
@"UIView" __captureIndicatorsView;
@"CAMInterfaceModulationView" __modulatingContentView;
@"AVCaptureVideoPreviewLayer" __videoPreviewLayer;
@"CAMCoverScreenPreviewView" __previewView;
@"CAMTimerIndicatorView" __timerIndicatorView;
@"CAMElapsedTimeView" __elapsedTimeView;
q __elapsedTimeBackgroundStyle;
@"CAMVideoPausedBadge" __videoPausedBadge;
@"UIImageView" __flashIconView;
Q __badgeCounter;
q __flashMode;
@"CAMNightModeInstructionLabel" __nightModeInstructionLabel;
@"UIColor" __nightModeInstructionLabelDefaultBackgroundColor;
@"UIView" __nightModeIconView;
@"UIViewController" __nightModeIconHost;
@"NSTimer" __nightModeCountdownTimer;
@"CAMPersonalPhotographerStatusInstructionLabel" __personalPhotographerInstructionLabel;
@"CAMViewfinderTransitionController" __transitionController;
```

## Properties

```
@property (T@"CAMCoverScreenStateWrapper",&,N,S_setState:,V__state) _state;
@property (T@"UIView",&,N,V__captureIndicatorsView) _captureIndicatorsView;
@property (T@"CAMInterfaceModulationView",&,N,V__modulatingContentView) _modulatingContentView;
@property (T@"AVCaptureVideoPreviewLayer",R,N,V__videoPreviewLayer) _videoPreviewLayer;
@property (T@"CAMCoverScreenPreviewView",&,N,V__previewView) _previewView;
@property (T@"CAMTimerIndicatorView",&,N,V__timerIndicatorView) _timerIndicatorView;
@property (T@"CAMElapsedTimeView",&,N,V__elapsedTimeView) _elapsedTimeView;
@property (Tq,N,S_setElapsedTimeBackgroundStyle:,V__elapsedTimeBackgroundStyle) _elapsedTimeBackgroundStyle;
@property (TB,N,V__videoCapturing) _videoCapturing;
@property (T@"CAMVideoPausedBadge",&,N,V__videoPausedBadge) _videoPausedBadge;
@property (T@"UIImageView",&,N,V__flashIconView) _flashIconView;
@property (TQ,N,V__badgeCounter) _badgeCounter;
@property (Tq,N,V__flashMode) _flashMode;
@property (TB,N,V__isFlashActive) _isFlashActive;
@property (TB,N,V__nightModeShowing) _nightModeShowing;
@property (T@"CAMNightModeInstructionLabel",&,N,V__nightModeInstructionLabel) _nightModeInstructionLabel;
@property (T@"UIColor",&,N,V__nightModeInstructionLabelDefaultBackgroundColor) _nightModeInstructionLabelDefaultBackgroundColor;
@property (T@"UIView",&,N,V__nightModeIconView) _nightModeIconView;
@property (T@"UIViewController",&,N,V__nightModeIconHost) _nightModeIconHost;
@property (T@"NSTimer",&,N,V__nightModeCountdownTimer) _nightModeCountdownTimer;
@property (TB,N,V__personalPhotographerCountdownShowing) _personalPhotographerCountdownShowing;
@property (T@"CAMPersonalPhotographerStatusInstructionLabel",&,N,V__personalPhotographerInstructionLabel) _personalPhotographerInstructionLabel;
@property (TB,N,V__previewEnabled) _previewEnabled;
@property (T@"CAMViewfinderTransitionController",&,N,V__transitionController) _transitionController;
@property (TQ,N) interfaceModulation;
@property (Tq,N,V_captureOrientation) captureOrientation;
@property (TB,N,V_previewNeedsHalfTurnCorrection) previewNeedsHalfTurnCorrection;
@property (T@"UIView",R,N) previewView;
@property (Tq,R,N) desiredAspectRatio;
```

## Instance methods

```
-[CAMPartnerModeViewController _transitionController];
-[CAMPartnerModeViewController _state];
-[CAMPartnerModeViewController previewView];
-[CAMPartnerModeViewController _videoPreviewLayer];
-[CAMPartnerModeViewController setState:];
-[CAMPartnerModeViewController setCaptureOrientation:];
-[CAMPartnerModeViewController _setState:];
-[CAMPartnerModeViewController init];
-[CAMPartnerModeViewController supportedInterfaceOrientations];
-[CAMPartnerModeViewController _flashMode];
-[CAMPartnerModeViewController _previewView];
-[CAMPartnerModeViewController viewDidLoad];
-[CAMPartnerModeViewController _nightModeInstructionLabel];
-[CAMPartnerModeViewController viewDidLayoutSubviews];
-[CAMPartnerModeViewController prepareForResumingUsingCrossfade];
-[CAMPartnerModeViewController _modulatingContentView];
-[CAMPartnerModeViewController _isFlashActive];
-[CAMPartnerModeViewController _canShowWhileLocked];
-[CAMPartnerModeViewController loadView];
-[CAMPartnerModeViewController interfaceModulation];
-[CAMPartnerModeViewController removeInflightBlurAnimations];
-[CAMPartnerModeViewController setInterfaceModulation:animated:];
-[CAMPartnerModeViewController _shouldUpdateCaptureOrientation];
-[CAMPartnerModeViewController _elapsedTimeView];
-[CAMPartnerModeViewController elapasedTimeViewTextChanged:];
-[CAMPartnerModeViewController _timerIndicatorView];
-[CAMPartnerModeViewController setInterfaceModulation:];
-[CAMPartnerModeViewController desiredAspectRatio];
-[CAMPartnerModeViewController captureOrientation];
-[CAMPartnerModeViewController startVideoCapture];
-[CAMPartnerModeViewController stopVideoCapture];
-[CAMPartnerModeViewController _previewEnabled];
-[CAMPartnerModeViewController setCaptureOrientation:animated:];
-[CAMPartnerModeViewController _setElapsedTimeBackgroundStyle:];
-[CAMPartnerModeViewController _videoCapturing];
-[CAMPartnerModeViewController _applyCaptureOrientationTransformAnimated:];
-[CAMPartnerModeViewController _badgeCounter];
-[CAMPartnerModeViewController _captureIndicatorsView];
-[CAMPartnerModeViewController _elapsedTimeBackgroundStyle];
-[CAMPartnerModeViewController _flashIconView];
-[CAMPartnerModeViewController _nightModeCountdownTimer];
-[CAMPartnerModeViewController _nightModeIconHost];
-[CAMPartnerModeViewController _nightModeIconView];
-[CAMPartnerModeViewController _nightModeInstructionLabelBackgroundColor];
-[CAMPartnerModeViewController _nightModeInstructionLabelDefaultBackgroundColor];
-[CAMPartnerModeViewController _nightModeShowing];
-[CAMPartnerModeViewController _partnerPreviewTransform];
-[CAMPartnerModeViewController _personalPhotographerCountdownShowing];
-[CAMPartnerModeViewController _personalPhotographerInstructionLabel];
-[CAMPartnerModeViewController _renderCaptureIndicators];
-[CAMPartnerModeViewController _setChromeOrientationTransform:onView:animated:];
-[CAMPartnerModeViewController _stackedChromeTransformForView:relativeToAnchorView:anchorTransform:];
-[CAMPartnerModeViewController _topPreviewChromeTransformForView:];
-[CAMPartnerModeViewController _updateTimerLabelBoundsForFlashVisible:];
-[CAMPartnerModeViewController _videoPausedBadge];
-[CAMPartnerModeViewController _videoPreviewLayerDidStartRunning:];
-[CAMPartnerModeViewController createAndEmbedElapsedTimeViewIfNeeded];
-[CAMPartnerModeViewController createAndEmbedTimerIndicatorViewIfNeeded];
-[CAMPartnerModeViewController createAndEmbedVideoPausedBadgeIfNeeded];
-[CAMPartnerModeViewController endPreviewFlipTransition];
-[CAMPartnerModeViewController hideFlashIndicator];
-[CAMPartnerModeViewController hideNightModeInstruction];
-[CAMPartnerModeViewController hidePersonalPhotographerCountdown];
-[CAMPartnerModeViewController initWithVideoPreviewLayer:];
-[CAMPartnerModeViewController pauseVideoCapture];
-[CAMPartnerModeViewController performCaptureAnimation];
-[CAMPartnerModeViewController previewNeedsHalfTurnCorrection];
-[CAMPartnerModeViewController resumeVideoCapture];
-[CAMPartnerModeViewController setElapsedTimeBackgroundStyle:];
-[CAMPartnerModeViewController setElapsedTimeBackgroundStyle:animated:];
-[CAMPartnerModeViewController setPreviewNeedsHalfTurnCorrection:];
-[CAMPartnerModeViewController set_badgeCounter:];
-[CAMPartnerModeViewController set_captureIndicatorsView:];
-[CAMPartnerModeViewController set_elapsedTimeView:];
-[CAMPartnerModeViewController set_flashIconView:];
-[CAMPartnerModeViewController set_flashMode:];
-[CAMPartnerModeViewController set_isFlashActive:];
-[CAMPartnerModeViewController set_modulatingContentView:];
-[CAMPartnerModeViewController set_nightModeCountdownTimer:];
-[CAMPartnerModeViewController set_nightModeIconHost:];
-[CAMPartnerModeViewController set_nightModeIconView:];
-[CAMPartnerModeViewController set_nightModeInstructionLabel:];
-[CAMPartnerModeViewController set_nightModeInstructionLabelDefaultBackgroundColor:];
-[CAMPartnerModeViewController set_nightModeShowing:];
-[CAMPartnerModeViewController set_personalPhotographerCountdownShowing:];
-[CAMPartnerModeViewController set_personalPhotographerInstructionLabel:];
-[CAMPartnerModeViewController set_previewEnabled:];
-[CAMPartnerModeViewController set_previewView:];
-[CAMPartnerModeViewController set_timerIndicatorView:];
-[CAMPartnerModeViewController set_transitionController:];
-[CAMPartnerModeViewController set_videoCapturing:];
-[CAMPartnerModeViewController set_videoPausedBadge:];
-[CAMPartnerModeViewController setupAndStartTimerCaptureWith:];
-[CAMPartnerModeViewController showFlashIndicatorFor:isFlashActive:];
-[CAMPartnerModeViewController showNightModeCountdownFrom:];
-[CAMPartnerModeViewController showNightModeInstruction];
-[CAMPartnerModeViewController showPersonalPhotographerCountdownWithTicks:];
-[CAMPartnerModeViewController stopTimerCapture];
-[CAMPartnerModeViewController synchronizedCaptureTimerDelegateFired];
-[CAMPartnerModeViewController updateUIForStateChange];
```
