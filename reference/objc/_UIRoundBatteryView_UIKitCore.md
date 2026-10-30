# `_UIRoundBatteryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIBatteryView`
- 5 instance variables, 16 properties, 34 instance methods, 0 class methods

## Instance variables

```
model;
$__lazy_storage_$_contentView;
q sizeCategory;
@"UIColor" customFillColor;
@"UIColor" customInactiveColor;
```

## Properties

```
@property (Tq,N,VsizeCategory) sizeCategory;
@property (Td,N) chargePercent;
@property (Tq,N) chargingState;
@property (TB,N) saverModeActive;
@property (TB,N) showsPercentage;
@property (Tq,N) lowBatteryMode;
@property (Td,N) lowBatteryChargePercentThreshold;
@property (TB,N,R) lowBattery;
@property (TB,N) showsInlineChargingIndicator;
@property (T@"UIColor",N,&,VcustomFillColor) customFillColor;
@property (T@"UIColor",N,&) fillColor;
@property (T@"UIColor",N,&,VcustomInactiveColor) customInactiveColor;
@property (T@"UIColor",N,&) inactiveColor;
@property (Tq,N) style;
@property (T{CGSize=dd},N,R) intrinsicContentSize;
@property (T@"UIAccessibilityHUDItem",N,R) accessibilityHUDRepresentation;
```

## Instance methods

```
-[_UIRoundBatteryView _commonInit];
-[_UIRoundBatteryView accessibilityHUDRepresentation];
-[_UIRoundBatteryView intrinsicContentSize];
-[_UIRoundBatteryView setInactiveColor:];
-[_UIRoundBatteryView setFillColor:];
-[_UIRoundBatteryView fillColor];
-[_UIRoundBatteryView sizeCategory];
-[_UIRoundBatteryView inactiveColor];
-[_UIRoundBatteryView style];
-[_UIRoundBatteryView setStyle:];
-[_UIRoundBatteryView saverModeActive];
-[_UIRoundBatteryView setSizeCategory:];
-[_UIRoundBatteryView initWithCoder:];
-[_UIRoundBatteryView setChargingState:];
-[_UIRoundBatteryView initWithFrame:];
-[_UIRoundBatteryView chargingState];
-[_UIRoundBatteryView customFillColor];
-[_UIRoundBatteryView showsPercentage];
-[_UIRoundBatteryView chargePercent];
-[_UIRoundBatteryView customInactiveColor];
-[_UIRoundBatteryView initWithSizeCategory:];
-[_UIRoundBatteryView isLowBattery];
-[_UIRoundBatteryView lowBattery];
-[_UIRoundBatteryView lowBatteryChargePercentThreshold];
-[_UIRoundBatteryView lowBatteryMode];
-[_UIRoundBatteryView setChargePercent:];
-[_UIRoundBatteryView setCustomFillColor:];
-[_UIRoundBatteryView setCustomInactiveColor:];
-[_UIRoundBatteryView setLowBatteryChargePercentThreshold:];
-[_UIRoundBatteryView setLowBatteryMode:];
-[_UIRoundBatteryView setSaverModeActive:];
-[_UIRoundBatteryView setShowsInlineChargingIndicator:];
-[_UIRoundBatteryView setShowsPercentage:];
-[_UIRoundBatteryView showsInlineChargingIndicator];
```
