# `CAFEngineGaugeUI`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 4 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUIEmphasizedEngineGaugeCharacteristic",R,N) uiEmphasizedEngineGaugeCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) uiSecondaryEngineGaugeHiddenCharacteristic;
@property (TC,R,N) uiEmphasizedEngineGauge;
@property (TB,R,N) uiSecondaryEngineGaugeHidden;
```

## Class methods

```
+[CAFEngineGaugeUI serviceIdentifier];
+[CAFEngineGaugeUI observerProtocol];
```

## Instance methods

```
-[CAFEngineGaugeUI removeObserver:];
-[CAFEngineGaugeUI addObserver:];
-[CAFEngineGaugeUI registerObserver:];
-[CAFEngineGaugeUI name];
-[CAFEngineGaugeUI unregisterObserver:];
-[CAFEngineGaugeUI registeredForUIEmphasizedEngineGauge];
-[CAFEngineGaugeUI registeredForUISecondaryEngineGaugeHidden];
-[CAFEngineGaugeUI uiEmphasizedEngineGauge];
-[CAFEngineGaugeUI uiSecondaryEngineGaugeHidden];
-[CAFEngineGaugeUI _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEngineGaugeUI uiEmphasizedEngineGaugeCharacteristic];
-[CAFEngineGaugeUI uiSecondaryEngineGaugeHiddenCharacteristic];
```
