# `CAFVehicleUnits`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 4 properties, 8 instance methods, 2 class methods

## Properties

```
@property (T@"CAFDisplayUnits",R,N) displayUnitsService;
@property (T@"CAFLocale",R,N) localeService;
@property (T@"CAFDisplayUnits",R,N) displayUnits;
@property (T@"CAFLocale",R,N) locale;
```

## Class methods

```
+[CAFVehicleUnits accessoryIdentifier];
+[CAFVehicleUnits observerProtocol];
```

## Instance methods

```
-[CAFVehicleUnits removeObserver:];
-[CAFVehicleUnits addObserver:];
-[CAFVehicleUnits locale];
-[CAFVehicleUnits registerObserver:];
-[CAFVehicleUnits unregisterObserver:];
-[CAFVehicleUnits displayUnits];
-[CAFVehicleUnits displayUnitsService];
-[CAFVehicleUnits localeService];
```
