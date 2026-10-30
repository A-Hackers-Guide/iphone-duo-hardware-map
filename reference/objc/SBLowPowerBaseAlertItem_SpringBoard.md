# `SBLowPowerBaseAlertItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAlertItem`
- 2 instance variables, 2 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _showFindMyAlert;
B _hasEnableLowPowerModeAction;
```

## Properties

```
@property (TB,N,V_showFindMyAlert) showFindMyAlert;
@property (TB,N,V_hasEnableLowPowerModeAction) hasEnableLowPowerModeAction;
```

## Instance methods

```
-[SBLowPowerBaseAlertItem alertMessage];
-[SBLowPowerBaseAlertItem didDeactivateForReason:];
-[SBLowPowerBaseAlertItem configure:requirePasscodeForActions:];
-[SBLowPowerBaseAlertItem shouldShowInLockScreen];
-[SBLowPowerBaseAlertItem wakeDisplay];
-[SBLowPowerBaseAlertItem shouldShowInEmergencyCall];
-[SBLowPowerBaseAlertItem setHasEnableLowPowerModeAction:];
-[SBLowPowerBaseAlertItem showFindMyAlert];
-[SBLowPowerBaseAlertItem _didDeactivateForDismissAction];
-[SBLowPowerBaseAlertItem _enableLowPowerMode];
-[SBLowPowerBaseAlertItem _enableLowPowerModeActionTitle];
-[SBLowPowerBaseAlertItem _enableLowPowerModeActionTriggered];
-[SBLowPowerBaseAlertItem _isLowPowerModeEnabled];
-[SBLowPowerBaseAlertItem _lowBatteryTitle];
-[SBLowPowerBaseAlertItem _setLowPowerMode:];
-[SBLowPowerBaseAlertItem _supportsLowPowerMode];
-[SBLowPowerBaseAlertItem _toggleLowPowerMode];
-[SBLowPowerBaseAlertItem hasEnableLowPowerModeAction];
-[SBLowPowerBaseAlertItem setShowFindMyAlert:];
```
