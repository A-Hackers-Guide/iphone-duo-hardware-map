# `CAFDriverAssistanceSystem`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) driverAssistanceModeIdentifierCharacteristic;
@property (T@"NSString",R,N) driverAssistanceModeIdentifier;
```

## Class methods

```
+[CAFDriverAssistanceSystem serviceIdentifier];
+[CAFDriverAssistanceSystem observerProtocol];
```

## Instance methods

```
-[CAFDriverAssistanceSystem removeObserver:];
-[CAFDriverAssistanceSystem addObserver:];
-[CAFDriverAssistanceSystem registerObserver:];
-[CAFDriverAssistanceSystem name];
-[CAFDriverAssistanceSystem unregisterObserver:];
-[CAFDriverAssistanceSystem driverAssistanceModeIdentifier];
-[CAFDriverAssistanceSystem registeredForDriverAssistanceModeIdentifier];
-[CAFDriverAssistanceSystem _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDriverAssistanceSystem driverAssistanceModeIdentifierCharacteristic];
```
