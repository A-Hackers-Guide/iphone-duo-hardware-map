# `CAFTripComputer`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 6 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFOdometer",R,N) odometerService;
@property (T@"CAFRemainingRange",R,N) remainingRangeService;
@property (T@"NSArray",R,N) tripServices;
@property (T@"CAFOdometer",R,N) odometer;
@property (T@"CAFRemainingRange",R,N) remainingRange;
@property (T@"NSArray",R,N) trips;
```

## Class methods

```
+[CAFTripComputer accessoryIdentifier];
+[CAFTripComputer observerProtocol];
```

## Instance methods

```
-[CAFTripComputer removeObserver:];
-[CAFTripComputer addObserver:];
-[CAFTripComputer odometer];
-[CAFTripComputer registerObserver:];
-[CAFTripComputer trips];
-[CAFTripComputer unregisterObserver:];
-[CAFTripComputer remainingRange];
-[CAFTripComputer odometerService];
-[CAFTripComputer remainingRangeService];
-[CAFTripComputer tripServices];
```
