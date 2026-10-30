# `CAFEnvironmentalConditions`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 4 properties, 8 instance methods, 2 class methods

## Properties

```
@property (T@"CAFExteriorConditions",R,N) exteriorConditionsService;
@property (T@"CAFInteriorConditions",R,N) interiorConditionsService;
@property (T@"CAFExteriorConditions",R,N) exteriorConditions;
@property (T@"CAFInteriorConditions",R,N) interiorConditions;
```

## Class methods

```
+[CAFEnvironmentalConditions accessoryIdentifier];
+[CAFEnvironmentalConditions observerProtocol];
```

## Instance methods

```
-[CAFEnvironmentalConditions removeObserver:];
-[CAFEnvironmentalConditions addObserver:];
-[CAFEnvironmentalConditions registerObserver:];
-[CAFEnvironmentalConditions unregisterObserver:];
-[CAFEnvironmentalConditions exteriorConditions];
-[CAFEnvironmentalConditions exteriorConditionsService];
-[CAFEnvironmentalConditions interiorConditions];
-[CAFEnvironmentalConditions interiorConditionsService];
```
