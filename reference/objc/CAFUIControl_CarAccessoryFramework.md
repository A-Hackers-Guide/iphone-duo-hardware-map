# `CAFUIControl`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 12 properties, 16 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUIState",R,N) uiStateService;
@property (T@"NSArray",R,N) uiInputDeviceButtonServices;
@property (T@"CAFUIAppearance",R,N) uiAppearanceService;
@property (T@"CAFEngineGaugeUI",R,N) engineGaugeUIService;
@property (T@"CAFEnergyGaugeUI",R,N) energyGaugeUIService;
@property (T@"CAFUIConfiguration",R,N) uiConfigurationService;
@property (T@"CAFUIState",R,N) uiState;
@property (T@"NSArray",R,N) uiInputDeviceButtons;
@property (T@"CAFUIAppearance",R,N) uiAppearance;
@property (T@"CAFEngineGaugeUI",R,N) engineGaugeUI;
@property (T@"CAFEnergyGaugeUI",R,N) energyGaugeUI;
@property (T@"CAFUIConfiguration",R,N) uiConfiguration;
```

## Class methods

```
+[CAFUIControl accessoryIdentifier];
+[CAFUIControl observerProtocol];
```

## Instance methods

```
-[CAFUIControl removeObserver:];
-[CAFUIControl addObserver:];
-[CAFUIControl registerObserver:];
-[CAFUIControl unregisterObserver:];
-[CAFUIControl uiConfiguration];
-[CAFUIControl uiState];
-[CAFUIControl energyGaugeUI];
-[CAFUIControl energyGaugeUIService];
-[CAFUIControl engineGaugeUI];
-[CAFUIControl engineGaugeUIService];
-[CAFUIControl uiAppearance];
-[CAFUIControl uiAppearanceService];
-[CAFUIControl uiConfigurationService];
-[CAFUIControl uiInputDeviceButtonServices];
-[CAFUIControl uiInputDeviceButtons];
-[CAFUIControl uiStateService];
```
