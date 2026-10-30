# `CAFBatteryRemainingRange`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFDistanceDisplay`
- 0 instance variables, 3 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
```

## Class methods

```
+[CAFBatteryRemainingRange serviceIdentifier];
+[CAFBatteryRemainingRange observerProtocol];
```

## Instance methods

```
-[CAFBatteryRemainingRange removeObserver:];
-[CAFBatteryRemainingRange addObserver:];
-[CAFBatteryRemainingRange registerObserver:];
-[CAFBatteryRemainingRange name];
-[CAFBatteryRemainingRange unregisterObserver:];
-[CAFBatteryRemainingRange hidden];
-[CAFBatteryRemainingRange hasHidden];
-[CAFBatteryRemainingRange registeredForHidden];
-[CAFBatteryRemainingRange _characteristicDidUpdate:fromGroupUpdate:];
-[CAFBatteryRemainingRange hiddenCharacteristic];
```
