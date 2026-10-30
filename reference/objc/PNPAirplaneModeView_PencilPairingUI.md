# `PNPAirplaneModeView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PNPDeviceStateConfigurable`
- 7 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"PNPDeviceState" _deviceState;
@"UIView" _contentAreaView;
@"UILabel" _deviceNameLabel;
@"UIButton" _turnOnBluetoothButton;
@"NSString" _currentString;
@"NSString" _pencilStatusString;
@"<PNPAirplaneModeBluetoothViewDelegate>" _bluetoothDelegate;
```

## Properties

```
@property (T@"<PNPAirplaneModeBluetoothViewDelegate>",W,N,V_bluetoothDelegate) bluetoothDelegate;
@property (T@"PNPDeviceState",C,N) deviceState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PNPAirplaneModeView intrinsicContentSize];
-[PNPAirplaneModeView deviceState];
-[PNPAirplaneModeView layoutSubviews];
-[PNPAirplaneModeView setDeviceState:];
-[PNPAirplaneModeView initWithFrame:];
-[PNPAirplaneModeView _configureConstraints];
-[PNPAirplaneModeView _applePencilOff];
-[PNPAirplaneModeView _applePencilOn];
-[PNPAirplaneModeView _bluetoothOnString];
-[PNPAirplaneModeView _turnOnString];
-[PNPAirplaneModeView bluetoothDelegate];
-[PNPAirplaneModeView setBluetoothDelegate:];
-[PNPAirplaneModeView turnOnBluetooth:];
```
