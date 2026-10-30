# `BKUIPearlEnrollView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `BKUIVideoCaptureSesssionDelegate`
- 55 instance variables, 17 properties, 103 instance methods, 0 class methods

## Instance variables

```
@"BKUIPearlVideoCaptureSession" _videoCaptureSession;
B _didStartCapture;
B _activated;
@"UIView" _cameraShadeView;
B _progressiveBlur;
d _currentCorrectedPitch;
d _currentRawPitch;
d _lastLoggedCenterBinPitch;
B _blurInProgress;
@"UILabel" _repositionPhoneLabel;
@"NSDate" _startTime;
Q _frameCount;
@"NSString" _debugFrameInformation;
@"NSString" _debugTemplateInformation;
@"NSString" _debugStatusInformation;
d _pitchCorrectionSamples;
d _pitchCorrection;
Q _correctionSamplesCount;
d _pitchMin;
d _pitchMax;
Q _fillHoldoffFrameCount;
B _stateTransitionInProgress;
@"NSDate" _stateStart;
@"NSTimer" _nudgeTimer;
B _nudging;
Q _nudgesNudged;
B _nudgesPaused;
@"AVPlayer" _tutorialPlayer;
B _entryAnimationAlreadyRan;
@"BKUIPearlPositioningGuideView" _positioningGuide;
@"UIView" _circleMaskView;
@"CAShapeLayer" _circleMaskLayer;
@"UIView" _roundedRectMaskView;
@"CAShapeLayer" _roundedRectMaskLayer;
@"UILabel" _debugLabel;
Q _pendingRaiseLowerGuidanceState;
B _raiseLowerGuidanceStatePending;
@"NSTimer" _raiseLowerGuidanceDelayTimer;
B _transitioningToState;
B _debugOverlayVisible;
B _inSheet;
B _active;
B _squareNeedsPositionLayout;
i _state;
@"<BKUIPearlEnrollViewDelegate>" _delegate;
@"<BKUIPearlEnrollViewStateTransitionDelegate>" _transitionDelegate;
@"UILayoutGuide" _portalLayoutGuide;
@"BKUIPearlPillContainerView" _pillContainer;
@"BKUIPearlMovieLoopView" _tutorialMovieView;
@"NSArray" _portalLayoutGuideConstraints;
@"BKUIPearlCrossHairsView" _crossHairs;
@"OBAnimationView" _animationView;
@"OBAnimationController" _animationController;
@"NSLayoutConstraint" _successAnimationViewCenterYConstraint;
@"<UITraitChangeRegistration>" _traitChangeRegistration;
```

## Properties

```
@property (T@"BKUIPearlMovieLoopView",&,N,V_tutorialMovieView) tutorialMovieView;
@property (Ti,N,V_state) state;
@property (T@"BKUIPearlPillContainerView",&,N,V_pillContainer) pillContainer;
@property (T@"NSArray",&,N,V_portalLayoutGuideConstraints) portalLayoutGuideConstraints;
@property (TB,N,V_active) active;
@property (TB,N,V_squareNeedsPositionLayout) squareNeedsPositionLayout;
@property (T@"BKUIPearlCrossHairsView",&,N,V_crossHairs) crossHairs;
@property (T@"OBAnimationView",&,N,V_animationView) animationView;
@property (T@"OBAnimationController",&,N,V_animationController) animationController;
@property (T@"NSLayoutConstraint",&,N,V_successAnimationViewCenterYConstraint) successAnimationViewCenterYConstraint;
@property (T@"<UITraitChangeRegistration>",&,N,V_traitChangeRegistration) traitChangeRegistration;
@property (T@"<BKUIPearlEnrollViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisTransitioningToState,V_transitioningToState) transitioningToState;
@property (T@"<BKUIPearlEnrollViewStateTransitionDelegate>",W,N,V_transitionDelegate) transitionDelegate;
@property (TB,N,V_debugOverlayVisible) debugOverlayVisible;
@property (T@"UILayoutGuide",R,N,V_portalLayoutGuide) portalLayoutGuide;
@property (TB,N,V_inSheet) inSheet;
```

## Instance methods

```
-[BKUIPearlEnrollView setSuspended:];
-[BKUIPearlEnrollView animationController];
-[BKUIPearlEnrollView active];
-[BKUIPearlEnrollView updateWithProgress:];
-[BKUIPearlEnrollView setState:];
-[BKUIPearlEnrollView setAnimationView:];
-[BKUIPearlEnrollView animationView];
-[BKUIPearlEnrollView dealloc];
-[BKUIPearlEnrollView layoutSubviews];
-[BKUIPearlEnrollView setActive:];
-[BKUIPearlEnrollView setBackgroundColor:];
-[BKUIPearlEnrollView setDelegate:];
-[BKUIPearlEnrollView delegate];
-[BKUIPearlEnrollView setAnimationController:];
-[BKUIPearlEnrollView startCapture];
-[BKUIPearlEnrollView _updateDebugOverlay];
-[BKUIPearlEnrollView state];
-[BKUIPearlEnrollView setTransitionDelegate:];
-[BKUIPearlEnrollView transitionDelegate];
-[BKUIPearlEnrollView setTraitChangeRegistration:];
-[BKUIPearlEnrollView traitChangeRegistration];
-[BKUIPearlEnrollView previewLayer];
-[BKUIPearlEnrollView didDisappear];
-[BKUIPearlEnrollView setState:completion:];
-[BKUIPearlEnrollView _updateRaiseLowerGuidanceLabelIfNeededForPitch:];
-[BKUIPearlEnrollView _nudgeIfNecessary];
-[BKUIPearlEnrollView crossHairs];
-[BKUIPearlEnrollView initWithVideoCaptureSession:inSheet:squareNeedsPositionLayout:];
-[BKUIPearlEnrollView percentOfPillsCompleted];
-[BKUIPearlEnrollView pillContainer];
-[BKUIPearlEnrollView preEnrollActivate];
-[BKUIPearlEnrollView setCameraBlurAmount:useShade:duration:completion:];
-[BKUIPearlEnrollView setCrosshairsHidden:];
-[BKUIPearlEnrollView setTutorialMovieView:];
-[BKUIPearlEnrollView tutorialMovieView];
-[BKUIPearlEnrollView _cleanupUIState];
-[BKUIPearlEnrollView _stopNudgeTimer];
-[BKUIPearlEnrollView inSheet];
-[BKUIPearlEnrollView setPillsHidden:];
-[BKUIPearlEnrollView _progressiveBlurAmountForPitch:];
-[BKUIPearlEnrollView _updateCorrectionEstimates:yaw:];
-[BKUIPearlEnrollView _animateCircleMaskWithPositioningGuide];
-[BKUIPearlEnrollView _animateToEntryAnimation];
-[BKUIPearlEnrollView _animateToFinishedWithCompletion:];
-[BKUIPearlEnrollView _animateToFirstScanCompleteWithCompletion:];
-[BKUIPearlEnrollView _animateToFirstScanWithCompletion:];
-[BKUIPearlEnrollView _animateToNeedsCenterBinWithCompletion:];
-[BKUIPearlEnrollView _animateToNeedsPositioningFromState:withCompletion:];
-[BKUIPearlEnrollView _animateToPartialCaptureWithCompletion:];
-[BKUIPearlEnrollView _animateToScanCompleteWithCompletion:];
-[BKUIPearlEnrollView _animateToScanningStateWithCompletion:];
-[BKUIPearlEnrollView _animateToState:fromState:completion:];
-[BKUIPearlEnrollView _animateToTutorialWithCompletion:];
-[BKUIPearlEnrollView _endAndCleanupEnrollSessionIfNeeded];
-[BKUIPearlEnrollView _enrollMaskPathWithRadius:];
-[BKUIPearlEnrollView _maskPathWithRadius:inFrame:];
-[BKUIPearlEnrollView _needsPositioningPreviewTransform];
-[BKUIPearlEnrollView _nonOccludingCircleMaskRadius];
-[BKUIPearlEnrollView _previewZoomLevel];
-[BKUIPearlEnrollView _recordDataFrameWithFaceState:];
-[BKUIPearlEnrollView _resetPreviewLayerBlur];
-[BKUIPearlEnrollView _runTutorialLoopWithDuration:delay:loopDelay:];
-[BKUIPearlEnrollView _scanningAndPartialCapturePreviewTransform];
-[BKUIPearlEnrollView _setRaiseLowerGuidanceLabelState:];
-[BKUIPearlEnrollView _setState:completion:];
-[BKUIPearlEnrollView _startNudgeTimer];
-[BKUIPearlEnrollView _updateToNeedsPositionWithoutAnimationWithCompletion:];
-[BKUIPearlEnrollView completedRingRadius];
-[BKUIPearlEnrollView debugOverlayVisible];
-[BKUIPearlEnrollView expectsRunningVideoCaptureSession:];
-[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:positioningGuideView:squareNeedsPositionLayout:];
-[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:positioningGuideView:squareNeedsPositionLayout:collectsFramesForAgeVerification:];
-[BKUIPearlEnrollView initWithFrame:videoCaptureSession:inSheet:squareNeedsPositionLayout:];
-[BKUIPearlEnrollView isTransitioningToState];
-[BKUIPearlEnrollView needsMaskedNeedsPositionStyleEnrollment];
-[BKUIPearlEnrollView pillRingRadius];
-[BKUIPearlEnrollView portalCenter];
-[BKUIPearlEnrollView portalLayoutGuide];
-[BKUIPearlEnrollView portalLayoutGuideConstraints];
-[BKUIPearlEnrollView portalOffset];
-[BKUIPearlEnrollView portalRadius];
-[BKUIPearlEnrollView postEnrollDeActivate];
-[BKUIPearlEnrollView resetPitchCorrection];
-[BKUIPearlEnrollView setCameraBlurred:];
-[BKUIPearlEnrollView setCrossHairs:];
-[BKUIPearlEnrollView setDebugOverlayVisible:];
-[BKUIPearlEnrollView setFailed];
-[BKUIPearlEnrollView setInSheet:];
-[BKUIPearlEnrollView setMovieViewHidden:];
-[BKUIPearlEnrollView setNudgesPaused:];
-[BKUIPearlEnrollView setPillContainer:];
-[BKUIPearlEnrollView setPitch:yaw:];
-[BKUIPearlEnrollView setPortalLayoutGuideConstraints:];
-[BKUIPearlEnrollView setSquareNeedsPositionLayout:];
-[BKUIPearlEnrollView setSuccessAnimationViewCenterYConstraint:];
-[BKUIPearlEnrollView setTransitioningToState:];
-[BKUIPearlEnrollView setupAnimationViewWithSuperView:];
-[BKUIPearlEnrollView squareNeedsPositionLayout];
-[BKUIPearlEnrollView successAnimationViewCenterYConstraint];
-[BKUIPearlEnrollView tutorialMovieSize];
-[BKUIPearlEnrollView tutorialRingRadius];
-[BKUIPearlEnrollView updatePortalLayoutGuide];
-[BKUIPearlEnrollView updateWithFaceState:];
```
