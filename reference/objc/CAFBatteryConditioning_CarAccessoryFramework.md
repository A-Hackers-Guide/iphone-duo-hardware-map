# `CAFBatteryConditioning`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBatteryConditioningStateCharacteristic",R,N) batteryConditioningStateCharacteristic;
@property (TC,R,N) batteryConditioningState;
```

## Class methods

```
+[CAFBatteryConditioning serviceIdentifier];
+[CAFBatteryConditioning observerProtocol];
```

## Instance methods

```
-[CAFBatteryConditioning removeObserver:];
-[CAFBatteryConditioning addObserver:];
-[CAFBatteryConditioning registerObserver:];
-[CAFBatteryConditioning name];
-[CAFBatteryConditioning unregisterObserver:];
-[CAFBatteryConditioning batteryConditioningState];
-[CAFBatteryConditioning registeredForBatteryConditioningState];
-[CAFBatteryConditioning _characteristicDidUpdate:fromGroupUpdate:];
-[CAFBatteryConditioning batteryConditioningStateCharacteristic];
```
