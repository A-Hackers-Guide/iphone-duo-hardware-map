# `CAFEnergyGaugeUI`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUIEmphasizedEnergyLevelGaugeCharacteristic",R,N) uiEmphasizedEnergyLevelGaugeCharacteristic;
@property (T@"CAFUIEmphasizedConsumptionGaugeCharacteristic",R,N) uiEmphasizedConsumptionGaugeCharacteristic;
@property (TC,R,N) uiEmphasizedEnergyLevelGauge;
@property (TB,R,N) hasUiEmphasizedEnergyLevelGauge;
@property (TC,R,N) uiEmphasizedConsumptionGauge;
@property (TB,R,N) hasUiEmphasizedConsumptionGauge;
```

## Class methods

```
+[CAFEnergyGaugeUI serviceIdentifier];
+[CAFEnergyGaugeUI observerProtocol];
```

## Instance methods

```
-[CAFEnergyGaugeUI removeObserver:];
-[CAFEnergyGaugeUI addObserver:];
-[CAFEnergyGaugeUI registerObserver:];
-[CAFEnergyGaugeUI name];
-[CAFEnergyGaugeUI unregisterObserver:];
-[CAFEnergyGaugeUI hasUiEmphasizedConsumptionGauge];
-[CAFEnergyGaugeUI hasUiEmphasizedEnergyLevelGauge];
-[CAFEnergyGaugeUI registeredForUIEmphasizedConsumptionGauge];
-[CAFEnergyGaugeUI registeredForUIEmphasizedEnergyLevelGauge];
-[CAFEnergyGaugeUI uiEmphasizedConsumptionGauge];
-[CAFEnergyGaugeUI uiEmphasizedEnergyLevelGauge];
-[CAFEnergyGaugeUI _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEnergyGaugeUI uiEmphasizedConsumptionGaugeCharacteristic];
-[CAFEnergyGaugeUI uiEmphasizedEnergyLevelGaugeCharacteristic];
```
