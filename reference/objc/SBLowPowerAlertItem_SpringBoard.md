# `SBLowPowerAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBLowPowerBaseAlertItem`
- 2 instance variables, 1 properties, 7 instance methods, 4 class methods

## Instance variables

```
I _talkLevel;
@"SPBeaconManager" _beaconManager;
```

## Properties

```
@property (T@"SPBeaconManager",&,N,V_beaconManager) beaconManager;
```

## Class methods

```
+[SBLowPowerAlertItem initialize];
+[SBLowPowerAlertItem setBatteryLevel:];
+[SBLowPowerAlertItem _shouldIgnoreChangeToBatteryLevel:];
+[SBLowPowerAlertItem _thresholdForLevel:];
```

## Instance methods

```
-[SBLowPowerAlertItem init];
-[SBLowPowerAlertItem alertMessage];
-[SBLowPowerAlertItem beaconManager];
-[SBLowPowerAlertItem _createSystemApertureElement];
-[SBLowPowerAlertItem setBeaconManager:];
-[SBLowPowerAlertItem initWithLevel:];
-[SBLowPowerAlertItem _batteryPercentageString];
```
