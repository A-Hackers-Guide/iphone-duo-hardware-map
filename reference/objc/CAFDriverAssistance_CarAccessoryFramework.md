# `CAFDriverAssistance`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 4 properties, 8 instance methods, 2 class methods

## Properties

```
@property (T@"CAFDriverAssistanceSystem",R,N) driverAssistanceSystemService;
@property (T@"CAFTargetSpeed",R,N) targetSpeedService;
@property (T@"CAFDriverAssistanceSystem",R,N) driverAssistanceSystem;
@property (T@"CAFTargetSpeed",R,N) targetSpeed;
```

## Class methods

```
+[CAFDriverAssistance accessoryIdentifier];
+[CAFDriverAssistance observerProtocol];
```

## Instance methods

```
-[CAFDriverAssistance removeObserver:];
-[CAFDriverAssistance addObserver:];
-[CAFDriverAssistance registerObserver:];
-[CAFDriverAssistance unregisterObserver:];
-[CAFDriverAssistance targetSpeed];
-[CAFDriverAssistance driverAssistanceSystem];
-[CAFDriverAssistance driverAssistanceSystemService];
-[CAFDriverAssistance targetSpeedService];
```
