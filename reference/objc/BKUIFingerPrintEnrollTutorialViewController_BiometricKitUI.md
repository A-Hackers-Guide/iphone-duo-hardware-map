# `BKUIFingerPrintEnrollTutorialViewController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBWelcomeController`
- 17 instance variables, 17 properties, 57 instance methods, 1 class methods

## Instance variables

```
B _inBuddy;
B _showFollowUpEnrollmentUpSellContent;
B _isSecondEnrollment;
@"<BKUIEmbeddedEnrollmentSelectionType>" _delegate;
Q _enrollViewState;
q _initialInterfaceOrientation;
@"NSObject<OS_os_log>" _log;
@"OBTrayButton" _skipButton;
@"OBTrayButton" _continueButton;
@"UIImageView" _enrollTutorialImageView;
@"OBAnimationController" _animationController;
@"BKUIAnimationView" _animationView;
@"NSLayoutConstraint" _contentViewTopConstraint;
@"BKUIFingerPrintPosedVideoPlayerView" _posedVideoPlayerView;
@"NSTimer" _animationTimer;
@"<UITraitChangeRegistration>" _traitChangeRegistration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _displayRect;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (T@"OBTrayButton",&,N,V_skipButton) skipButton;
@property (T@"OBTrayButton",&,N,V_continueButton) continueButton;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_displayRect) displayRect;
@property (T@"UIImageView",&,N,V_enrollTutorialImageView) enrollTutorialImageView;
@property (T@"OBAnimationController",&,N,V_animationController) animationController;
@property (T@"BKUIAnimationView",&,N,V_animationView) animationView;
@property (T@"NSLayoutConstraint",&,N,V_contentViewTopConstraint) contentViewTopConstraint;
@property (T@"BKUIFingerPrintPosedVideoPlayerView",&,N,V_posedVideoPlayerView) posedVideoPlayerView;
@property (T@"NSTimer",&,N,V_animationTimer) animationTimer;
@property (T@"<UITraitChangeRegistration>",&,N,V_traitChangeRegistration) traitChangeRegistration;
@property (T@"<BKUIEmbeddedEnrollmentSelectionType>",W,N,V_delegate) delegate;
@property (TQ,N,V_enrollViewState) enrollViewState;
@property (TB,N,V_inBuddy) inBuddy;
@property (TB,N,V_showFollowUpEnrollmentUpSellContent) showFollowUpEnrollmentUpSellContent;
@property (TB,N,V_isSecondEnrollment) isSecondEnrollment;
@property (Tq,N,V_initialInterfaceOrientation) initialInterfaceOrientation;
```

## Class methods

```
+[BKUIFingerPrintEnrollTutorialViewController _introText];
```

## Instance methods

```
-[BKUIFingerPrintEnrollTutorialViewController setLog:];
-[BKUIFingerPrintEnrollTutorialViewController animationController];
-[BKUIFingerPrintEnrollTutorialViewController setAnimationView:];
-[BKUIFingerPrintEnrollTutorialViewController animationView];
-[BKUIFingerPrintEnrollTutorialViewController setSkipButton:];
-[BKUIFingerPrintEnrollTutorialViewController viewIsAppearing:];
-[BKUIFingerPrintEnrollTutorialViewController viewDidLoad];
-[BKUIFingerPrintEnrollTutorialViewController viewDidLayoutSubviews];
-[BKUIFingerPrintEnrollTutorialViewController setAnimationTimer:];
-[BKUIFingerPrintEnrollTutorialViewController setDelegate:];
-[BKUIFingerPrintEnrollTutorialViewController viewDidAppear:];
-[BKUIFingerPrintEnrollTutorialViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[BKUIFingerPrintEnrollTutorialViewController delegate];
-[BKUIFingerPrintEnrollTutorialViewController viewDidDisappear:];
-[BKUIFingerPrintEnrollTutorialViewController animationTimer];
-[BKUIFingerPrintEnrollTutorialViewController skipButton];
-[BKUIFingerPrintEnrollTutorialViewController log];
-[BKUIFingerPrintEnrollTutorialViewController setAnimationController:];
-[BKUIFingerPrintEnrollTutorialViewController setInitialInterfaceOrientation:];
-[BKUIFingerPrintEnrollTutorialViewController contentViewTopConstraint];
-[BKUIFingerPrintEnrollTutorialViewController continueButton];
-[BKUIFingerPrintEnrollTutorialViewController initialInterfaceOrientation];
-[BKUIFingerPrintEnrollTutorialViewController setContentViewTopConstraint:];
-[BKUIFingerPrintEnrollTutorialViewController setContinueButton:];
-[BKUIFingerPrintEnrollTutorialViewController _contentViewHeight];
-[BKUIFingerPrintEnrollTutorialViewController inBuddy];
-[BKUIFingerPrintEnrollTutorialViewController setInBuddy:];
-[BKUIFingerPrintEnrollTutorialViewController setTraitChangeRegistration:];
-[BKUIFingerPrintEnrollTutorialViewController traitChangeRegistration];
-[BKUIFingerPrintEnrollTutorialViewController setDisplayRect:];
-[BKUIFingerPrintEnrollTutorialViewController displayRect];
-[BKUIFingerPrintEnrollTutorialViewController setEnrollViewState:];
-[BKUIFingerPrintEnrollTutorialViewController _enrollSkipped:];
-[BKUIFingerPrintEnrollTutorialViewController _videoAssetName];
-[BKUIFingerPrintEnrollTutorialViewController enrollViewState];
-[BKUIFingerPrintEnrollTutorialViewController _contentViewTopOffset];
-[BKUIFingerPrintEnrollTutorialViewController _continuePressed:];
-[BKUIFingerPrintEnrollTutorialViewController _detailTextPhase1];
-[BKUIFingerPrintEnrollTutorialViewController _devicePrefix];
-[BKUIFingerPrintEnrollTutorialViewController _headerTitlePhase1];
-[BKUIFingerPrintEnrollTutorialViewController _headerTitlePhase2];
-[BKUIFingerPrintEnrollTutorialViewController _performInitialAnimationSetup];
-[BKUIFingerPrintEnrollTutorialViewController _restartAnimation];
-[BKUIFingerPrintEnrollTutorialViewController _setupTouchIDAnimation];
-[BKUIFingerPrintEnrollTutorialViewController combinedTutorialText];
-[BKUIFingerPrintEnrollTutorialViewController enrollTutorialImageView];
-[BKUIFingerPrintEnrollTutorialViewController initInBuddy:displayRect:];
-[BKUIFingerPrintEnrollTutorialViewController isSecondEnrollment];
-[BKUIFingerPrintEnrollTutorialViewController loadAVPlayer];
-[BKUIFingerPrintEnrollTutorialViewController posedVideoPlayerView];
-[BKUIFingerPrintEnrollTutorialViewController setEnrollTutorialImageView:];
-[BKUIFingerPrintEnrollTutorialViewController setIsSecondEnrollment:];
-[BKUIFingerPrintEnrollTutorialViewController setPosedVideoPlayerView:];
-[BKUIFingerPrintEnrollTutorialViewController setShowFollowUpEnrollmentUpSellContent:];
-[BKUIFingerPrintEnrollTutorialViewController showFollowUpEnrollmentUpSellContent];
-[BKUIFingerPrintEnrollTutorialViewController tutorialImage];
-[BKUIFingerPrintEnrollTutorialViewController tutorialText];
```
