# `BKUIFingerPrintEnrollmentPhaseViewController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTouchIDEnrollmentWelcomeController`
- 33 instance variables, 33 properties, 98 instance methods, 0 class methods

## Instance variables

```
B _inBuddy;
B _shouldShowFollowupFingerEnrollmentUpSell;
B _showFollowUpEnrollmentUpSellContent;
B _isSecondEnrollment;
B _hideUnlockMessage;
B _rotating;
B _disableContentViewSizing;
@"<BKUIEmbeddedEnrollmentSelectionType>" _delegate;
Q _enrollViewState;
@"NSString" _headerTitle;
q _initialInterfaceOrientation;
@"NSObject<OS_os_log>" _log;
@"BKUIAlertView" _alertView;
@"UIView" _mesaEnrollErrorButtonsContainer;
@"UIButton" _mesaEnrollErrorButtonRestartEnroll;
@"BKUICurvesView" _mesaFirstEnrollView;
@"BKUICurvesView" _mesaSecondEnrollView;
@"NSArray" _mesaEnrollContainerConstraints;
@"OBTrayButton" _continueButton;
@"OBTrayButton" _retryButton;
@"OBTrayButton" _skipButton;
@"OBTrayButton" _addAnotherFingerButton;
@"OBTrayButton" _setupLaterButton;
@"NSLayoutConstraint" _contentViewHeightConstraint;
@"NSLayoutConstraint" _enrollCurvesViewTopConstraint;
@"NSLayoutConstraint" _enrollCurvesViewCenterConstraint;
d _innerAndOuterCurvesViewHeightDiff;
d _enrollProgress;
@"BKUIIndicatorWindow" _touchindicatorWindow;
@"NSNumber" _lastCurvesWasCompact;
@"NSNumber" _lastCurvesWasLandscape;
{CGPoint="x"d"y"d} _anchorPoint;
{CGSize="width"d"height"d} _buttonTraySize;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (T@"BKUIAlertView",&,N,V_alertView) alertView;
@property (T@"UIView",&,N,V_mesaEnrollErrorButtonsContainer) mesaEnrollErrorButtonsContainer;
@property (T@"UIButton",&,N,V_mesaEnrollErrorButtonRestartEnroll) mesaEnrollErrorButtonRestartEnroll;
@property (TB,N,V_hideUnlockMessage) hideUnlockMessage;
@property (T@"BKUICurvesView",&,N,V_mesaFirstEnrollView) mesaFirstEnrollView;
@property (T@"BKUICurvesView",&,N,V_mesaSecondEnrollView) mesaSecondEnrollView;
@property (T@"NSArray",&,N,V_mesaEnrollContainerConstraints) mesaEnrollContainerConstraints;
@property (T@"OBTrayButton",&,N,V_continueButton) continueButton;
@property (T@"OBTrayButton",&,N,V_retryButton) retryButton;
@property (T@"OBTrayButton",&,N,V_skipButton) skipButton;
@property (T@"OBTrayButton",&,N,V_addAnotherFingerButton) addAnotherFingerButton;
@property (T@"OBTrayButton",&,N,V_setupLaterButton) setupLaterButton;
@property (T@"NSLayoutConstraint",&,N,V_contentViewHeightConstraint) contentViewHeightConstraint;
@property (TB,N,V_rotating) rotating;
@property (T{CGPoint=dd},N,V_anchorPoint) anchorPoint;
@property (T@"NSLayoutConstraint",&,N,V_enrollCurvesViewTopConstraint) enrollCurvesViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_enrollCurvesViewCenterConstraint) enrollCurvesViewCenterConstraint;
@property (TB,N,V_disableContentViewSizing) disableContentViewSizing;
@property (T@"NSString",&,N,V_headerTitle) headerTitle;
@property (Td,N,V_innerAndOuterCurvesViewHeightDiff) innerAndOuterCurvesViewHeightDiff;
@property (Td,N,V_enrollProgress) enrollProgress;
@property (T@"BKUIIndicatorWindow",&,N,V_touchindicatorWindow) touchindicatorWindow;
@property (T{CGSize=dd},N,V_buttonTraySize) buttonTraySize;
@property (T@"NSNumber",&,N,V_lastCurvesWasCompact) lastCurvesWasCompact;
@property (T@"NSNumber",&,N,V_lastCurvesWasLandscape) lastCurvesWasLandscape;
@property (T@"<BKUIEmbeddedEnrollmentSelectionType>",W,N,V_delegate) delegate;
@property (TQ,N,V_enrollViewState) enrollViewState;
@property (TB,N,V_inBuddy) inBuddy;
@property (TB,N,V_shouldShowFollowupFingerEnrollmentUpSell) shouldShowFollowupFingerEnrollmentUpSell;
@property (TB,N,V_showFollowUpEnrollmentUpSellContent) showFollowUpEnrollmentUpSellContent;
@property (TB,N,V_isSecondEnrollment) isSecondEnrollment;
@property (Tq,N,V_initialInterfaceOrientation) initialInterfaceOrientation;
```

## Instance methods

```
-[BKUIFingerPrintEnrollmentPhaseViewController setLog:];
-[BKUIFingerPrintEnrollmentPhaseViewController setSkipButton:];
-[BKUIFingerPrintEnrollmentPhaseViewController anchorPoint];
-[BKUIFingerPrintEnrollmentPhaseViewController dealloc];
-[BKUIFingerPrintEnrollmentPhaseViewController _subtitleFont];
-[BKUIFingerPrintEnrollmentPhaseViewController viewDidLoad];
-[BKUIFingerPrintEnrollmentPhaseViewController viewDidLayoutSubviews];
-[BKUIFingerPrintEnrollmentPhaseViewController setHeaderTitle:];
-[BKUIFingerPrintEnrollmentPhaseViewController viewWillAppear:];
-[BKUIFingerPrintEnrollmentPhaseViewController setDelegate:];
-[BKUIFingerPrintEnrollmentPhaseViewController viewDidAppear:];
-[BKUIFingerPrintEnrollmentPhaseViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[BKUIFingerPrintEnrollmentPhaseViewController delegate];
-[BKUIFingerPrintEnrollmentPhaseViewController setRotating:];
-[BKUIFingerPrintEnrollmentPhaseViewController skipButton];
-[BKUIFingerPrintEnrollmentPhaseViewController log];
-[BKUIFingerPrintEnrollmentPhaseViewController prefersStatusBarHidden];
-[BKUIFingerPrintEnrollmentPhaseViewController setAnchorPoint:];
-[BKUIFingerPrintEnrollmentPhaseViewController headerTitle];
-[BKUIFingerPrintEnrollmentPhaseViewController setInitialInterfaceOrientation:];
-[BKUIFingerPrintEnrollmentPhaseViewController continueButton];
-[BKUIFingerPrintEnrollmentPhaseViewController initialInterfaceOrientation];
-[BKUIFingerPrintEnrollmentPhaseViewController rotating];
-[BKUIFingerPrintEnrollmentPhaseViewController setContinueButton:];
-[BKUIFingerPrintEnrollmentPhaseViewController _forceLayout];
-[BKUIFingerPrintEnrollmentPhaseViewController inBuddy];
-[BKUIFingerPrintEnrollmentPhaseViewController setInBuddy:];
-[BKUIFingerPrintEnrollmentPhaseViewController setSetupLaterButton:];
-[BKUIFingerPrintEnrollmentPhaseViewController setupLaterButton];
-[BKUIFingerPrintEnrollmentPhaseViewController alertView];
-[BKUIFingerPrintEnrollmentPhaseViewController setAlertView:];
-[BKUIFingerPrintEnrollmentPhaseViewController setContentViewHeightConstraint:];
-[BKUIFingerPrintEnrollmentPhaseViewController contentViewHeightConstraint];
-[BKUIFingerPrintEnrollmentPhaseViewController shouldAnimateEntireView];
-[BKUIFingerPrintEnrollmentPhaseViewController _isIPad];
-[BKUIFingerPrintEnrollmentPhaseViewController setEnrollViewState:];
-[BKUIFingerPrintEnrollmentPhaseViewController enrollViewState];
-[BKUIFingerPrintEnrollmentPhaseViewController mesaEnrollErrorButtonsContainer];
-[BKUIFingerPrintEnrollmentPhaseViewController setRetryButton:];
-[BKUIFingerPrintEnrollmentPhaseViewController _addAnotherFingerPressed];
-[BKUIFingerPrintEnrollmentPhaseViewController _continuePressed:];
-[BKUIFingerPrintEnrollmentPhaseViewController _detailPhasesText];
-[BKUIFingerPrintEnrollmentPhaseViewController _detailTextDonePhase];
-[BKUIFingerPrintEnrollmentPhaseViewController _enrollSkipped];
-[BKUIFingerPrintEnrollmentPhaseViewController _enrollViewTopPadding];
-[BKUIFingerPrintEnrollmentPhaseViewController _forceResetCurvesLayerToPercent:];
-[BKUIFingerPrintEnrollmentPhaseViewController _handleViewState:];
-[BKUIFingerPrintEnrollmentPhaseViewController _idealEnrollCurveViewSize];
-[BKUIFingerPrintEnrollmentPhaseViewController _unifiedMesaCurvesLandscape];
-[BKUIFingerPrintEnrollmentPhaseViewController _updateButtonTraySize];
-[BKUIFingerPrintEnrollmentPhaseViewController _updateContentViewSizeToMatchConstraints];
-[BKUIFingerPrintEnrollmentPhaseViewController _updateEnrollViewsForSize:];
-[BKUIFingerPrintEnrollmentPhaseViewController addAnotherFingerButton];
-[BKUIFingerPrintEnrollmentPhaseViewController buttonTraySize];
-[BKUIFingerPrintEnrollmentPhaseViewController disableContentViewSizing];
-[BKUIFingerPrintEnrollmentPhaseViewController enrollCurvesViewCenterConstraint];
-[BKUIFingerPrintEnrollmentPhaseViewController enrollCurvesViewTopConstraint];
-[BKUIFingerPrintEnrollmentPhaseViewController enrollProgress];
-[BKUIFingerPrintEnrollmentPhaseViewController handleEnrollmentDone];
-[BKUIFingerPrintEnrollmentPhaseViewController handleEnrollmentFailure];
-[BKUIFingerPrintEnrollmentPhaseViewController hideUnlockMessage];
-[BKUIFingerPrintEnrollmentPhaseViewController initInBuddy:hideUnlockMessage:headerTitle:firstEnrollView:secondEnrollView:];
-[BKUIFingerPrintEnrollmentPhaseViewController initInBuddy:hideUnlockMessage:showFollowUpSell:headerTitle:firstEnrollView:secondEnrollView:];
-[BKUIFingerPrintEnrollmentPhaseViewController innerAndOuterCurvesViewHeightDiff];
-[BKUIFingerPrintEnrollmentPhaseViewController isSecondEnrollment];
-[BKUIFingerPrintEnrollmentPhaseViewController lastCurvesWasCompact];
-[BKUIFingerPrintEnrollmentPhaseViewController lastCurvesWasLandscape];
-[BKUIFingerPrintEnrollmentPhaseViewController mesaEnrollContainerConstraints];
-[BKUIFingerPrintEnrollmentPhaseViewController mesaEnrollErrorButtonRestartEnroll];
-[BKUIFingerPrintEnrollmentPhaseViewController mesaFirstEnrollView];
-[BKUIFingerPrintEnrollmentPhaseViewController mesaSecondEnrollView];
-[BKUIFingerPrintEnrollmentPhaseViewController removeTouchIndicator];
-[BKUIFingerPrintEnrollmentPhaseViewController retryButton];
-[BKUIFingerPrintEnrollmentPhaseViewController setAddAnotherFingerButton:];
-[BKUIFingerPrintEnrollmentPhaseViewController setButtonTraySize:];
-[BKUIFingerPrintEnrollmentPhaseViewController setDisableContentViewSizing:];
-[BKUIFingerPrintEnrollmentPhaseViewController setEnrollCurvesViewCenterConstraint:];
-[BKUIFingerPrintEnrollmentPhaseViewController setEnrollCurvesViewTopConstraint:];
-[BKUIFingerPrintEnrollmentPhaseViewController setEnrollProgress:];
-[BKUIFingerPrintEnrollmentPhaseViewController setEnrollProgress:enrollView:];
-[BKUIFingerPrintEnrollmentPhaseViewController setHideUnlockMessage:];
-[BKUIFingerPrintEnrollmentPhaseViewController setInnerAndOuterCurvesViewHeightDiff:];
-[BKUIFingerPrintEnrollmentPhaseViewController setIsSecondEnrollment:];
-[BKUIFingerPrintEnrollmentPhaseViewController setLastCurvesWasCompact:];
-[BKUIFingerPrintEnrollmentPhaseViewController setLastCurvesWasLandscape:];
-[BKUIFingerPrintEnrollmentPhaseViewController setMesaEnrollContainerConstraints:];
-[BKUIFingerPrintEnrollmentPhaseViewController setMesaEnrollErrorButtonRestartEnroll:];
-[BKUIFingerPrintEnrollmentPhaseViewController setMesaEnrollErrorButtonsContainer:];
-[BKUIFingerPrintEnrollmentPhaseViewController setMesaFirstEnrollView:];
-[BKUIFingerPrintEnrollmentPhaseViewController setMesaSecondEnrollView:];
-[BKUIFingerPrintEnrollmentPhaseViewController setShouldShowFollowupFingerEnrollmentUpSell:];
-[BKUIFingerPrintEnrollmentPhaseViewController setShowFollowUpEnrollmentUpSellContent:];
-[BKUIFingerPrintEnrollmentPhaseViewController setTouchIndicatorVisible:];
-[BKUIFingerPrintEnrollmentPhaseViewController setTouchindicatorWindow:];
-[BKUIFingerPrintEnrollmentPhaseViewController shouldShowFollowupFingerEnrollmentUpSell];
-[BKUIFingerPrintEnrollmentPhaseViewController showFollowUpEnrollmentUpSellContent];
-[BKUIFingerPrintEnrollmentPhaseViewController touchindicatorWindow];
-[BKUIFingerPrintEnrollmentPhaseViewController updateHeaderWithTitle:animated:heightDifference:];
```
