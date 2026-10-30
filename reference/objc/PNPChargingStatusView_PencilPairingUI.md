# `PNPChargingStatusView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PNPDeviceStateConfigurable`
- 20 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"PNPDeviceState" _deviceState;
@"UIView" _contentAreaView;
@"UIView" _batterySectionView;
@"UILabel" _deviceNameLabel;
@"_UIBatteryView" _batteryView;
@"UILabel" _percentageLabel;
@"PNPConnectButton" _tapToConnectButton;
@"NSLayoutConstraint" _alignDeviceNameToTopConstraint;
@"NSLayoutConstraint" _centerDeviceNameConstraint;
@"NSLayoutConstraint" _tapToConnectButtonWidthConstraint;
@"UIActivityIndicatorView" _spinnerView;
d _maxPillWidth;
B _didStartBatteryAnimation;
B _isFadingOutDeviceName;
B _showsCharging;
B _isTransitioningToBatteryUI;
B _didStartBatteryTransition;
B _alphaOutName;
@"<PNPChargingStatusViewDelegate>" _delegate;
q _chargingState;
```

## Properties

```
@property (T@"<PNPChargingStatusViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_showsCharging) showsCharging;
@property (TB,N,V_isTransitioningToBatteryUI) isTransitioningToBatteryUI;
@property (TB,N,V_didStartBatteryTransition) didStartBatteryTransition;
@property (Tq,N,V_chargingState) chargingState;
@property (TB,N,V_alphaOutName) alphaOutName;
@property (T@"PNPDeviceState",C,N) deviceState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PNPChargingStatusView intrinsicContentSize];
-[PNPChargingStatusView deviceState];
-[PNPChargingStatusView layoutSubviews];
-[PNPChargingStatusView setDeviceState:];
-[PNPChargingStatusView setDelegate:];
-[PNPChargingStatusView delegate];
-[PNPChargingStatusView updateConstraints];
-[PNPChargingStatusView setChargingState:];
-[PNPChargingStatusView initWithFrame:];
-[PNPChargingStatusView chargingState];
-[PNPChargingStatusView _performAnimations:completion:];
-[PNPChargingStatusView _setAndAnimateChargingStateToConnecting];
-[PNPChargingStatusView _showBatteryStatus];
-[PNPChargingStatusView alphaOutName];
-[PNPChargingStatusView beginPairing];
-[PNPChargingStatusView didStartBatteryTransition];
-[PNPChargingStatusView isTransitioningToBatteryUI];
-[PNPChargingStatusView setAlphaOutName:];
-[PNPChargingStatusView setDidStartBatteryTransition:];
-[PNPChargingStatusView setIsTransitioningToBatteryUI:];
-[PNPChargingStatusView setShowsCharging:];
-[PNPChargingStatusView showsCharging];
-[PNPChargingStatusView updateChargingState:];
```
