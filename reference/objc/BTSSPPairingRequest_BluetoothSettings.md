# `BTSSPPairingRequest`

- Image: [`/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`](../userland/System__Library__PreferenceBundles__BluetoothSettings.bundle__BluetoothSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"BluetoothDevice" _device;
@"PSSpecifier" _specifier;
@"UIAlertController" _alert;
@ _delegate;
i _pairingStyle;
```

## Instance methods

```
-[BTSSPPairingRequest dismiss];
-[BTSSPPairingRequest dealloc];
-[BTSSPPairingRequest setDelegate:];
-[BTSSPPairingRequest show];
-[BTSSPPairingRequest acceptSSP:];
-[BTSSPPairingRequest hasLimitedSupportForHID];
-[BTSSPPairingRequest hidPairingResult:];
-[BTSSPPairingRequest initWithDevice:andSpecifier:];
-[BTSSPPairingRequest pairingStyle];
-[BTSSPPairingRequest sanitizeNameForAlert:];
-[BTSSPPairingRequest setPairingStyle:andPasskey:];
```
