# `CAFInternalCombustionEngine`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 4 properties, 8 instance methods, 2 class methods

## Properties

```
@property (T@"CAFEngineRPM",R,N) engineRPMService;
@property (T@"CAFEngineTemperature",R,N) engineTemperatureService;
@property (T@"CAFEngineRPM",R,N) engineRPM;
@property (T@"CAFEngineTemperature",R,N) engineTemperature;
```

## Class methods

```
+[CAFInternalCombustionEngine accessoryIdentifier];
+[CAFInternalCombustionEngine observerProtocol];
```

## Instance methods

```
-[CAFInternalCombustionEngine removeObserver:];
-[CAFInternalCombustionEngine addObserver:];
-[CAFInternalCombustionEngine registerObserver:];
-[CAFInternalCombustionEngine unregisterObserver:];
-[CAFInternalCombustionEngine engineRPM];
-[CAFInternalCombustionEngine engineRPMService];
-[CAFInternalCombustionEngine engineTemperature];
-[CAFInternalCombustionEngine engineTemperatureService];
```
