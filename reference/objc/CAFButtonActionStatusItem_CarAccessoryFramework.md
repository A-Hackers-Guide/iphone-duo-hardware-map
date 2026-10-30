# `CAFButtonActionStatusItem`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerStatusItem`
- 0 instance variables, 2 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (TC,N) buttonAction;
```

## Class methods

```
+[CAFButtonActionStatusItem serviceIdentifier];
+[CAFButtonActionStatusItem observerProtocol];
```

## Instance methods

```
-[CAFButtonActionStatusItem removeObserver:];
-[CAFButtonActionStatusItem addObserver:];
-[CAFButtonActionStatusItem registerObserver:];
-[CAFButtonActionStatusItem name];
-[CAFButtonActionStatusItem unregisterObserver:];
-[CAFButtonActionStatusItem buttonAction];
-[CAFButtonActionStatusItem setButtonAction:];
-[CAFButtonActionStatusItem registeredForButtonAction];
-[CAFButtonActionStatusItem _characteristicDidUpdate:fromGroupUpdate:];
-[CAFButtonActionStatusItem buttonActionCharacteristic];
```
