# `_UIBatteryView` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 11 properties, 22 instance methods, 0 class methods

## Properties

```
@property (Tq,N) sizeCategory;
@property (Td,N) chargePercent;
@property (Tq,N) chargingState;
@property (TB,N) saverModeActive;
@property (TB,N) showsPercentage;
@property (Tq,N) lowBatteryMode;
@property (Td,N) lowBatteryChargePercentThreshold;
@property (TB,R,N,GisLowBattery) lowBattery;
@property (TB,N) showsInlineChargingIndicator;
@property (T@"UIColor",C,N) fillColor;
@property (T@"UIColor",C,N) inactiveColor;
```

## Instance methods

```
-[_UIBatteryView setInactiveColor:];
-[_UIBatteryView setFillColor:];
-[_UIBatteryView fillColor];
-[_UIBatteryView sizeCategory];
-[_UIBatteryView inactiveColor];
-[_UIBatteryView saverModeActive];
-[_UIBatteryView setSizeCategory:];
-[_UIBatteryView setChargingState:];
-[_UIBatteryView chargingState];
-[_UIBatteryView showsPercentage];
-[_UIBatteryView chargePercent];
-[_UIBatteryView initWithSizeCategory:];
-[_UIBatteryView isLowBattery];
-[_UIBatteryView lowBatteryChargePercentThreshold];
-[_UIBatteryView lowBatteryMode];
-[_UIBatteryView setChargePercent:];
-[_UIBatteryView setLowBatteryChargePercentThreshold:];
-[_UIBatteryView setLowBatteryMode:];
-[_UIBatteryView setSaverModeActive:];
-[_UIBatteryView setShowsInlineChargingIndicator:];
-[_UIBatteryView setShowsPercentage:];
-[_UIBatteryView showsInlineChargingIndicator];
```
