# `CAFUIAppearance`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 4 properties, 13 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) nightModeCharacteristic;
@property (T@"CAFAppearanceModeCharacteristic",R,N) appearanceModeCharacteristic;
@property (TB,R,N) nightMode;
@property (TC,N) appearanceMode;
```

## Class methods

```
+[CAFUIAppearance serviceIdentifier];
+[CAFUIAppearance observerProtocol];
```

## Instance methods

```
-[CAFUIAppearance nightMode];
-[CAFUIAppearance removeObserver:];
-[CAFUIAppearance addObserver:];
-[CAFUIAppearance registerObserver:];
-[CAFUIAppearance name];
-[CAFUIAppearance unregisterObserver:];
-[CAFUIAppearance setAppearanceMode:];
-[CAFUIAppearance appearanceMode];
-[CAFUIAppearance registeredForAppearanceMode];
-[CAFUIAppearance registeredForNightMode];
-[CAFUIAppearance _characteristicDidUpdate:fromGroupUpdate:];
-[CAFUIAppearance appearanceModeCharacteristic];
-[CAFUIAppearance nightModeCharacteristic];
```
