# `PNPPairingView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PNPWizardViewDelegate`, `PNPDeviceStateConfigurable`, `PNPChargingStatusViewHosting`
- 12 instance variables, 16 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"PNPDeviceState" _deviceState;
@"PNPPencilView" _pencilView;
B _finishedWizardTransition;
@"PNPChargingStatusView" _chargingStatusView;
B _showsChargingStatusView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _pencilSpinningRect;
B _showWizardContents;
Q _state;
@"<PNPPairingViewDelegate>" _delegate;
q _controllerFlow;
q _deviceType;
@"PNPWizardViewController" _wizardViewController;
```

## Properties

```
@property (T@"PNPWizardViewController",&,N,V_wizardViewController) wizardViewController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) mainScreenBounds;
@property (T{CGSize=dd},R,N) insetMainScreenSize;
@property (TQ,N,V_state) state;
@property (T@"<PNPPairingViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_showWizardContents) showWizardContents;
@property (T@"PNPPencilView",R,N) pencilView;
@property (Tq,N,V_controllerFlow) controllerFlow;
@property (Tq,N,V_deviceType) deviceType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"PNPDeviceState",C,N) deviceState;
@property (T@"PNPChargingStatusView",&,N,V_chargingStatusView) chargingStatusView;
@property (TB,N,V_showsChargingStatusView) showsChargingStatusView;
```

## Instance methods

```
-[PNPPairingView setDeviceType:];
-[PNPPairingView setState:];
-[PNPPairingView intrinsicContentSize];
-[PNPPairingView deviceType];
-[PNPPairingView deviceState];
-[PNPPairingView layoutSubviews];
-[PNPPairingView setDeviceState:];
-[PNPPairingView setDelegate:];
-[PNPPairingView delegate];
-[PNPPairingView initWithFrame:];
-[PNPPairingView state];
-[PNPPairingView mainScreenBounds];
-[PNPPairingView findMyNewPencilPairingSucceeded];
-[PNPPairingView _intrinsicContentSizeForState:deviceState:];
-[PNPPairingView _pencilSizeForState:];
-[PNPPairingView _pencilTransformForState:deviceState:];
-[PNPPairingView backgroundColorForWizardController:];
-[PNPPairingView chargingStatusView];
-[PNPPairingView controllerFlow];
-[PNPPairingView controllerFlowForWizard:];
-[PNPPairingView insetMainScreenSize];
-[PNPPairingView pencilView];
-[PNPPairingView prepareForTransitionToWizard];
-[PNPPairingView setChargingStatusView:];
-[PNPPairingView setControllerFlow:];
-[PNPPairingView setShowWizardContents:];
-[PNPPairingView setShowsChargingStatusView:];
-[PNPPairingView setWizardViewController:];
-[PNPPairingView shouldShowWhatsNewController];
-[PNPPairingView showWizardContents];
-[PNPPairingView showsChargingStatusView];
-[PNPPairingView transitionToWizard];
-[PNPPairingView unhideWizardIfNecessary];
-[PNPPairingView wizardDidRequestSaveOnboardingStatus:];
-[PNPPairingView wizardDidSelectPairNewPencil:wizardView:];
-[PNPPairingView wizardTransitionFinished];
-[PNPPairingView wizardViewController];
-[PNPPairingView wizardViewRequestsDismiss:];
```
