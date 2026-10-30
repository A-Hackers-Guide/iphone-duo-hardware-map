# `_UIStatusBarBatteryItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- 6 instance variables, 6 properties, 19 instance methods, 4 class methods

## Instance variables

```
B _highlighted;
B _usesCondensedPercentageDisplay;
@"_UIStatusBarBatteryView" _batteryView;
@"_UIStatusBarStaticBatteryView" _staticBatteryView;
@"_UIStatusBarImageView" _chargingView;
@"_UIStatusBarStringView" _percentView;
```

## Properties

```
@property (T@"_UIStatusBarBatteryView",&,N,V_batteryView) batteryView;
@property (T@"_UIStatusBarStaticBatteryView",&,N,V_staticBatteryView) staticBatteryView;
@property (T@"_UIStatusBarImageView",&,N,V_chargingView) chargingView;
@property (T@"_UIStatusBarStringView",&,N,V_percentView) percentView;
@property (TB,N,V_highlighted) highlighted;
@property (TB,N,V_usesCondensedPercentageDisplay) usesCondensedPercentageDisplay;
```

## Class methods

```
+[_UIStatusBarBatteryItem chargingDisplayIdentifier];
+[_UIStatusBarBatteryItem iconDisplayIdentifier];
+[_UIStatusBarBatteryItem percentDisplayIdentifier];
+[_UIStatusBarBatteryItem staticIconDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarBatteryItem setChargingView:];
-[_UIStatusBarBatteryItem viewForIdentifier:];
-[_UIStatusBarBatteryItem _create_staticBatteryView];
-[_UIStatusBarBatteryItem percentView];
-[_UIStatusBarBatteryItem highlighted];
-[_UIStatusBarBatteryItem setStaticBatteryView:];
-[_UIStatusBarBatteryItem _create_percentView];
-[_UIStatusBarBatteryItem setBatteryView:];
-[_UIStatusBarBatteryItem setHighlighted:];
-[_UIStatusBarBatteryItem setPercentView:];
-[_UIStatusBarBatteryItem setUsesCondensedPercentageDisplay:];
-[_UIStatusBarBatteryItem _create_batteryView];
-[_UIStatusBarBatteryItem batteryView];
-[_UIStatusBarBatteryItem _create_chargingView];
-[_UIStatusBarBatteryItem dependentEntryKeys];
-[_UIStatusBarBatteryItem chargingView];
-[_UIStatusBarBatteryItem staticBatteryView];
-[_UIStatusBarBatteryItem applyUpdate:toDisplayItem:];
-[_UIStatusBarBatteryItem usesCondensedPercentageDisplay];
```
