# `CAFGearRecommendation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 3 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFInt8Characteristic",R,N) gearShiftRecommendationCharacteristic;
@property (Tc,R,N) gearShiftRecommendation;
@property (T@"CAFInt8Range",R,N) gearShiftRecommendationRange;
```

## Class methods

```
+[CAFGearRecommendation serviceIdentifier];
+[CAFGearRecommendation observerProtocol];
```

## Instance methods

```
-[CAFGearRecommendation removeObserver:];
-[CAFGearRecommendation addObserver:];
-[CAFGearRecommendation registerObserver:];
-[CAFGearRecommendation name];
-[CAFGearRecommendation unregisterObserver:];
-[CAFGearRecommendation gearShiftRecommendation];
-[CAFGearRecommendation registeredForGearShiftRecommendation];
-[CAFGearRecommendation _characteristicDidUpdate:fromGroupUpdate:];
-[CAFGearRecommendation gearShiftRecommendationCharacteristic];
-[CAFGearRecommendation gearShiftRecommendationRange];
```
