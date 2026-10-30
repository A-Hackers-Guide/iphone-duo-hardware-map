# `CAFTypeTestIndexByUnit`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 7 properties, 16 instance methods, 3 class methods

## Properties

```
@property (T@"CAFUnitTypeCharacteristic",R,N) distanceUnitRawValueCharacteristic;
@property (T@"CAFInt32Characteristic",R,N) testInt32Characteristic;
@property (TS,R,N) distanceUnitRawValue;
@property (T@"NSUnitLength",R,N) distanceUnit;
@property (Ti,N) testInt32;
@property (T@"CAFInt32Range",R,N) testInt32Range;
@property (TB,R,N) hasTestInt32;
```

## Class methods

```
+[CAFTypeTestIndexByUnit serviceIdentifier];
+[CAFTypeTestIndexByUnit indexBy];
+[CAFTypeTestIndexByUnit observerProtocol];
```

## Instance methods

```
-[CAFTypeTestIndexByUnit removeObserver:];
-[CAFTypeTestIndexByUnit addObserver:];
-[CAFTypeTestIndexByUnit registerObserver:];
-[CAFTypeTestIndexByUnit name];
-[CAFTypeTestIndexByUnit unregisterObserver:];
-[CAFTypeTestIndexByUnit distanceUnit];
-[CAFTypeTestIndexByUnit distanceUnitRawValue];
-[CAFTypeTestIndexByUnit hasTestInt32];
-[CAFTypeTestIndexByUnit registeredForDistanceUnit];
-[CAFTypeTestIndexByUnit registeredForTestInt32];
-[CAFTypeTestIndexByUnit setTestInt32:];
-[CAFTypeTestIndexByUnit testInt32];
-[CAFTypeTestIndexByUnit _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTypeTestIndexByUnit distanceUnitRawValueCharacteristic];
-[CAFTypeTestIndexByUnit testInt32Characteristic];
-[CAFTypeTestIndexByUnit testInt32Range];
```
