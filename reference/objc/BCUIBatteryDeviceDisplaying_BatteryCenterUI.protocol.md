# `BCUIBatteryDeviceDisplaying` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 18 instance methods, 0 class methods

## Properties

```
@property (Tq,N) percentCharge;
@property (TB,N,GisCharging) charging;
@property (TB,N,GisLowCharge) lowCharge;
@property (TB,N,GisLowPowerModeEnabled) lowPowerModeEnabled;
@property (T@"UIImage",&,N) glyph;
@property (Td,N) scaleFactor;
@property (T@"NSString",?,C,N) name;
@property (TB,?,N,GisEmpty) empty;
@property (T@"<UIViewControllerTransitionCoordinator>",?,W,N) transitionCoordinator;
```

## Instance methods

```
-[BCUIBatteryDeviceDisplaying isCharging];
-[BCUIBatteryDeviceDisplaying isLowPowerModeEnabled];
-[BCUIBatteryDeviceDisplaying setGlyph:];
-[BCUIBatteryDeviceDisplaying glyph];
-[BCUIBatteryDeviceDisplaying setScaleFactor:];
-[BCUIBatteryDeviceDisplaying setLowPowerModeEnabled:];
-[BCUIBatteryDeviceDisplaying scaleFactor];
-[BCUIBatteryDeviceDisplaying setCharging:];
-[BCUIBatteryDeviceDisplaying setPercentCharge:];
-[BCUIBatteryDeviceDisplaying percentCharge];
-[BCUIBatteryDeviceDisplaying isLowCharge];
-[BCUIBatteryDeviceDisplaying setLowCharge:];
-[BCUIBatteryDeviceDisplaying transitionCoordinator];
-[BCUIBatteryDeviceDisplaying isEmpty];
-[BCUIBatteryDeviceDisplaying setName:];
-[BCUIBatteryDeviceDisplaying setEmpty:];
-[BCUIBatteryDeviceDisplaying name];
-[BCUIBatteryDeviceDisplaying setTransitionCoordinator:];
```
