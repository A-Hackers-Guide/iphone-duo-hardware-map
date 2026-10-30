# `SBLockScreenBatteryChargingViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSCoverSheetViewControllerBase`
- Protocols: `BCBatteryDeviceObserving`
- 6 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _shouldDisplayBattery;
@"CSBatteryChargingView" _chargingView;
@"NSTimer" _visibilityTimer;
@"NSMutableArray" _connectedDevices;
@"BCBatteryDeviceController" _batteryDeviceController;
@"<SBLockScreenBatteryChargingViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBLockScreenBatteryChargingViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenBatteryChargingViewController dealloc];
-[SBLockScreenBatteryChargingViewController presentationStyle];
-[SBLockScreenBatteryChargingViewController setDelegate:];
-[SBLockScreenBatteryChargingViewController loadView];
-[SBLockScreenBatteryChargingViewController delegate];
-[SBLockScreenBatteryChargingViewController connectedDevicesDidChange:];
-[SBLockScreenBatteryChargingViewController chargingView];
-[SBLockScreenBatteryChargingViewController batteryVisible];
-[SBLockScreenBatteryChargingViewController _clearVisibilityTimer];
-[SBLockScreenBatteryChargingViewController _visibilityTimerFired:];
-[SBLockScreenBatteryChargingViewController initForDisplayOfBattery:];
-[SBLockScreenBatteryChargingViewController prepareForDismissalWithAnimation:];
-[SBLockScreenBatteryChargingViewController presentWithAnimation:];
-[SBLockScreenBatteryChargingViewController showChargeLevelWithBatteryVisible:];
```
