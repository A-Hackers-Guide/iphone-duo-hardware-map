# `SBLowPowerFindMyAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertItem`
- 1 instance variables, 1 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"SPBeaconManager" _beaconManager;
```

## Properties

```
@property (T@"SPBeaconManager",&,N,V_beaconManager) beaconManager;
```

## Class methods

```
+[SBLowPowerFindMyAlertItem showFindMyAlert];
+[SBLowPowerFindMyAlertItem _readSupportsFindMy:];
```

## Instance methods

```
-[SBLowPowerFindMyAlertItem beaconManager];
-[SBLowPowerFindMyAlertItem configure:requirePasscodeForActions:];
-[SBLowPowerFindMyAlertItem shouldShowInLockScreen];
-[SBLowPowerFindMyAlertItem setBeaconManager:];
-[SBLowPowerFindMyAlertItem wakeDisplay];
```
