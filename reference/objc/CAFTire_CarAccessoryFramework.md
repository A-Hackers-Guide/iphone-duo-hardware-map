# `CAFTire`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 8 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) tirePressureServices;
@property (T@"NSArray",R,N) tireTemperatureServices;
@property (T@"CAFTirePressureMonitoringSystem",R,N) tirePressureMonitoringSystemService;
@property (T@"NSArray",R,N) tirePressures;
@property (T@"NSDictionary",R,N) tirePressuresIndexed;
@property (T@"NSArray",R,N) tireTemperatures;
@property (T@"NSDictionary",R,N) tireTemperaturesIndexed;
@property (T@"CAFTirePressureMonitoringSystem",R,N) tirePressureMonitoringSystem;
```

## Class methods

```
+[CAFTire accessoryIdentifier];
+[CAFTire observerProtocol];
```

## Instance methods

```
-[CAFTire removeObserver:];
-[CAFTire addObserver:];
-[CAFTire registerObserver:];
-[CAFTire unregisterObserver:];
-[CAFTire tirePressureMonitoringSystem];
-[CAFTire tirePressureMonitoringSystemService];
-[CAFTire tirePressureServices];
-[CAFTire tirePressures];
-[CAFTire tirePressuresIndexed];
-[CAFTire tireTemperatureServices];
-[CAFTire tireTemperatures];
-[CAFTire tireTemperaturesIndexed];
```
