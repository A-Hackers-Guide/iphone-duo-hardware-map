# `CAFFuel`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 6 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFFuelLevel",R,N) fuelLevelService;
@property (T@"CAFFuelConsumption",R,N) fuelConsumptionService;
@property (T@"CAFFuelRemainingRange",R,N) fuelRemainingRangeService;
@property (T@"CAFFuelLevel",R,N) fuelLevel;
@property (T@"CAFFuelConsumption",R,N) fuelConsumption;
@property (T@"CAFFuelRemainingRange",R,N) fuelRemainingRange;
```

## Class methods

```
+[CAFFuel accessoryIdentifier];
+[CAFFuel observerProtocol];
```

## Instance methods

```
-[CAFFuel removeObserver:];
-[CAFFuel addObserver:];
-[CAFFuel registerObserver:];
-[CAFFuel unregisterObserver:];
-[CAFFuel fuelConsumption];
-[CAFFuel fuelLevel];
-[CAFFuel fuelConsumptionService];
-[CAFFuel fuelLevelService];
-[CAFFuel fuelRemainingRange];
-[CAFFuel fuelRemainingRangeService];
```
