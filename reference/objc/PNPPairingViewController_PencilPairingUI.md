# `PNPPairingViewController`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PNPPairingViewDelegate`, `PNPChargingStatusViewDelegate`, `PNPPencilViewDelegate`, `PNPPlatterViewController`, `PNPDeviceStateConfigurable`, `PNPViewController`
- 23 instance variables, 12 properties, 102 instance methods, 0 class methods

## Instance variables

```
@"PNPPlatterContainerView" _wizardPlatterContainerView;
@"PNPPairingView" _pairingView;
@"PNPChargingStatusView" _pairingChargingStatusView;
@"PNPPlatterContainerView" _horizontalPencilPlatterContainerView;
@"PNPPencilHorizontalPresentationContainerView" _horizontalPresentationPencilContainerView;
@"PNPPencilView" _horizontalPencilView;
@"PNPChargingStatusView" _horizontalChargingStatusView;
B _showingChargingUI;
@"PNPPlatterTransitioningDelegate" _platterTransitioningDelegate;
B _inWizard;
@"UIAlertController" _alertVC;
@"NSTimer" _initialTimer;
d _spinnerElapsedTime;
@"NSTimer" _timeoutTimer;
@"PNPDeviceState" _deviceState;
B _viewDidAppearCalled;
B _viewRequestsDismissCalled;
@"UIPanGestureRecognizer" _panGestureRecognizer;
{CGPoint="x"d"y"d} _animationTranslation;
@"<PNPPlatterViewControllerPlatterDelegate>" platterDelegate;
@"<PNPViewControllerAppearanceDelegate>" appearanceDelegate;
@"<PNPPairingViewControllerDelegate>" _delegate;
q _pairingViewControllerState;
```

## Properties

```
@property (Tq,N,V_pairingViewControllerState) pairingViewControllerState;
@property (T@"<PNPPairingViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"PNPWizardViewController",R,N) wizardViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) preferredEdge;
@property (T@"<PNPPlatterViewControllerPlatterDelegate>",W,N,VplatterDelegate) platterDelegate;
@property (Td,?,R,N) preferredCornerRadius;
@property (T@"PNPDeviceState",C,N) deviceState;
@property (T@"<PNPViewControllerAppearanceDelegate>",W,N,VappearanceDelegate) appearanceDelegate;
```

## Instance methods

```
-[PNPPairingViewController dismissViewControllerAnimated:completion:];
-[PNPPairingViewController _updatePreferredContentSize];
-[PNPPairingViewController viewWillDisappear:];
-[PNPPairingViewController supportedInterfaceOrientations];
-[PNPPairingViewController deviceState];
-[PNPPairingViewController viewDidLoad];
-[PNPPairingViewController initWithNibName:bundle:];
-[PNPPairingViewController setDeviceState:];
-[PNPPairingViewController _canShowWhileLocked];
-[PNPPairingViewController setDelegate:];
-[PNPPairingViewController viewDidAppear:];
-[PNPPairingViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[PNPPairingViewController preferredCornerRadius];
-[PNPPairingViewController loadView];
-[PNPPairingViewController delegate];
-[PNPPairingViewController setAppearanceDelegate:];
-[PNPPairingViewController viewWillLayoutSubviews];
-[PNPPairingViewController viewDidDisappear:];
-[PNPPairingViewController _handlePanGesture:];
-[PNPPairingViewController preferredContentSize];
-[PNPPairingViewController canBecomeFirstResponder];
-[PNPPairingViewController appearanceDelegate];
-[PNPPairingViewController _orientationChanged:];
-[PNPPairingViewController requestDismissal];
-[PNPPairingViewController _cancelTimeoutTimer];
-[PNPPairingViewController platterDelegate];
-[PNPPairingViewController setPlatterDelegate:];
-[PNPPairingViewController _updateForSize:];
-[PNPPairingViewController findMyNewPencilPairingSucceeded];
-[PNPPairingViewController pairingStartedWithDimmingState:];
-[PNPPairingViewController _actuallyTransitionToCharging];
-[PNPPairingViewController _actuallyTransitionToChargingByMovingPlatter];
-[PNPPairingViewController _actuallyTransitionToChargingBySlideOutAndPresent];
-[PNPPairingViewController _actuallyTransitionToSpinningPlatterWithDimmingState:];
-[PNPPairingViewController _actuallyTransitionToWizard];
-[PNPPairingViewController _centerContainerViews];
-[PNPPairingViewController _chargingStatusViewHostsLayoutIfNeeded];
-[PNPPairingViewController _chargingStatusViewHostsSetShowsChargingStatusView:];
-[PNPPairingViewController _chargingStatusViewHostsSetupChargingViews];
-[PNPPairingViewController _chargingStatusViewHostsTeardownChargingViews];
-[PNPPairingViewController _chargingStatusViewLayoutIfNeeded];
-[PNPPairingViewController _chargingStatusViewSetChargingState:];
-[PNPPairingViewController _chargingStatusViewSetDeviceState:];
-[PNPPairingViewController _chargingStatusViewSetIsTransitioningToBatteryUI:];
-[PNPPairingViewController _chargingStatusViewSetNeedsLayout];
-[PNPPairingViewController _chargingStatusViewSetShowCharging:];
-[PNPPairingViewController _chargingStatusViewUpdateConstraints];
-[PNPPairingViewController _chargingUIViewWillTransitionToSize:withTransitionCoordinator:];
-[PNPPairingViewController _currentPlatterContainerView];
-[PNPPairingViewController _dimmingState];
-[PNPPairingViewController _dismissChargingAndPresentSpinningPencilWithDimmingState:];
-[PNPPairingViewController _edgeToStickToPort];
-[PNPPairingViewController _effectivePencilView];
-[PNPPairingViewController _hideOrShowAllContainerViewsIfNeeded];
-[PNPPairingViewController _hideOrShowContainerViewIfNeeded:];
-[PNPPairingViewController _morphToSpinningPencilWithDimmingState:];
-[PNPPairingViewController _offsetContainerViewsIfNecessary];
-[PNPPairingViewController _performAnimations:completion:];
-[PNPPairingViewController _resetTimeoutTimer];
-[PNPPairingViewController _resetTimerForWizard];
-[PNPPairingViewController _showConnectingAnimationUI];
-[PNPPairingViewController _spinningPencilViewWillTransitionToSize:withTransitionCoordinator:];
-[PNPPairingViewController _startConnectingUITimer];
-[PNPPairingViewController _transitionPairingViewToWizardByMovingPlatter];
-[PNPPairingViewController _transitionToChargingFrom:];
-[PNPPairingViewController _transitionToChargingFromSpinner];
-[PNPPairingViewController _transitionToWizard];
-[PNPPairingViewController _transitionToWizardBySlideOutAndPresent];
-[PNPPairingViewController _translationAmountForDismiss];
-[PNPPairingViewController _updateAnimationTranslation];
-[PNPPairingViewController _updatePillUIAnimated:];
-[PNPPairingViewController _updatePlatterContainerView:toPreferredCornerRadius:edge:];
-[PNPPairingViewController _updateSubviewDeviceStateForContainerView:];
-[PNPPairingViewController _wizardViewWillTransitionToSize:withTransitionCoordinator:];
-[PNPPairingViewController didCompleteOneRevolution];
-[PNPPairingViewController didSelectPairNewPencil:pairingView:];
-[PNPPairingViewController didTapOnCancelButton];
-[PNPPairingViewController didTapOnConnectButton];
-[PNPPairingViewController intrinsicContentSizeDidChangeForView:];
-[PNPPairingViewController isShowingPairingEducationPane];
-[PNPPairingViewController pairingFailed];
-[PNPPairingViewController pairingStarted];
-[PNPPairingViewController pairingStartedWithDimming:];
-[PNPPairingViewController pairingStartedWithDimming:deviceType:];
-[PNPPairingViewController pairingSucceeded];
-[PNPPairingViewController pairingSucceededSubsequently];
-[PNPPairingViewController pairingSucceededWithControllerFlow:deviceType:];
-[PNPPairingViewController pairingSucceededWithShouldShowWhatsNew:];
-[PNPPairingViewController pairingSucceededWithShouldShowWhatsNew:deviceType:];
-[PNPPairingViewController pairingViewControllerState];
-[PNPPairingViewController pairingViewDidRequestSaveOnboardingStatus:];
-[PNPPairingViewController preferredEdge];
-[PNPPairingViewController setPairingViewControllerState:];
-[PNPPairingViewController showGenericBatteryUI];
-[PNPPairingViewController showInformationalPill];
-[PNPPairingViewController showNeedsInternetAlert];
-[PNPPairingViewController showPairingPrompt];
-[PNPPairingViewController showPairingPromptAlert];
-[PNPPairingViewController transitionToEducationFlowIfNecessary:];
-[PNPPairingViewController transitionToPairingMode:];
-[PNPPairingViewController viewRequestsDismiss:];
-[PNPPairingViewController wizardViewController];
```
