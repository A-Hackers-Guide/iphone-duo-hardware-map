# `_UIStatusBarDataBatteryEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarDataEntry`
- 5 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _saverModeActive;
B _prominentlyShowsDetailString;
q _capacity;
q _state;
@"NSString" _detailString;
```

## Properties

```
@property (Tq,N,V_capacity) capacity;
@property (Tq,N,V_state) state;
@property (TB,N,V_saverModeActive) saverModeActive;
@property (TB,N,V_prominentlyShowsDetailString) prominentlyShowsDetailString;
@property (T@"NSString",C,N,V_detailString) detailString;
```

## Class methods

```
+[_UIStatusBarDataBatteryEntry supportsSecureCoding];
```

## Instance methods

```
-[_UIStatusBarDataBatteryEntry setCapacity:];
-[_UIStatusBarDataBatteryEntry setState:];
-[_UIStatusBarDataBatteryEntry capacity];
-[_UIStatusBarDataBatteryEntry detailString];
-[_UIStatusBarDataBatteryEntry _ui_descriptionBuilder];
-[_UIStatusBarDataBatteryEntry prominentlyShowsDetailString];
-[_UIStatusBarDataBatteryEntry encodeWithCoder:];
-[_UIStatusBarDataBatteryEntry hash];
-[_UIStatusBarDataBatteryEntry saverModeActive];
-[_UIStatusBarDataBatteryEntry initWithCoder:];
-[_UIStatusBarDataBatteryEntry copyWithZone:];
-[_UIStatusBarDataBatteryEntry isEqual:];
-[_UIStatusBarDataBatteryEntry state];
-[_UIStatusBarDataBatteryEntry setDetailString:];
-[_UIStatusBarDataBatteryEntry setProminentlyShowsDetailString:];
-[_UIStatusBarDataBatteryEntry setSaverModeActive:];
```
