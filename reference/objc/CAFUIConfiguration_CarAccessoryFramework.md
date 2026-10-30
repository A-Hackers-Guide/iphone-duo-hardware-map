# `CAFUIConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 2 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUIConfigurationOptionsCharacteristic",R,N) uiConfigurationOptionsCharacteristic;
@property (T@"CAFUIConfigurationOptions",C,N) uiConfigurationOptions;
```

## Class methods

```
+[CAFUIConfiguration serviceIdentifier];
+[CAFUIConfiguration observerProtocol];
```

## Instance methods

```
-[CAFUIConfiguration removeObserver:];
-[CAFUIConfiguration addObserver:];
-[CAFUIConfiguration registerObserver:];
-[CAFUIConfiguration name];
-[CAFUIConfiguration unregisterObserver:];
-[CAFUIConfiguration registeredForUIConfigurationOptions];
-[CAFUIConfiguration setUiConfigurationOptions:];
-[CAFUIConfiguration uiConfigurationOptions];
-[CAFUIConfiguration _characteristicDidUpdate:fromGroupUpdate:];
-[CAFUIConfiguration uiConfigurationOptionsCharacteristic];
```
