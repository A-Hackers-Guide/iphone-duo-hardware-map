# `CAFBluetoothStatus`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 8 properties, 18 instance methods, 2 class methods

## Properties

```
@property (T@"CAFModuleStatusCharacteristic",R,N) moduleStatusCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (TC,R,N) moduleStatus;
@property (T@"NSString",R,N) contentURLAction;
@property (TB,R,N) hasContentURLAction;
@property (TC,N) buttonAction;
@property (TB,R,N) hasButtonAction;
```

## Class methods

```
+[CAFBluetoothStatus serviceIdentifier];
+[CAFBluetoothStatus observerProtocol];
```

## Instance methods

```
-[CAFBluetoothStatus removeObserver:];
-[CAFBluetoothStatus addObserver:];
-[CAFBluetoothStatus registerObserver:];
-[CAFBluetoothStatus name];
-[CAFBluetoothStatus unregisterObserver:];
-[CAFBluetoothStatus buttonAction];
-[CAFBluetoothStatus setButtonAction:];
-[CAFBluetoothStatus hasButtonAction];
-[CAFBluetoothStatus contentURLAction];
-[CAFBluetoothStatus moduleStatus];
-[CAFBluetoothStatus registeredForButtonAction];
-[CAFBluetoothStatus registeredForContentURLAction];
-[CAFBluetoothStatus registeredForModuleStatus];
-[CAFBluetoothStatus _characteristicDidUpdate:fromGroupUpdate:];
-[CAFBluetoothStatus buttonActionCharacteristic];
-[CAFBluetoothStatus contentURLActionCharacteristic];
-[CAFBluetoothStatus hasContentURLAction];
-[CAFBluetoothStatus moduleStatusCharacteristic];
```
