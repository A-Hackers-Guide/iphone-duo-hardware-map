# `CAFUIState`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 8 properties, 17 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUISceneStateCharacteristic",R,N) uiSceneStateCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) uiSceneOptionsCharacteristic;
@property (T@"CAFDriverSideCharacteristic",R,N) driverSideCharacteristic;
@property (TC,R,N) uiSceneState;
@property (T@"NSArray",R,N) uiSceneOptions;
@property (TB,R,N) hasUiSceneOptions;
@property (TC,R,N) driverSide;
@property (TB,R,N) hasDriverSide;
```

## Class methods

```
+[CAFUIState serviceIdentifier];
+[CAFUIState observerProtocol];
```

## Instance methods

```
-[CAFUIState removeObserver:];
-[CAFUIState addObserver:];
-[CAFUIState registerObserver:];
-[CAFUIState name];
-[CAFUIState unregisterObserver:];
-[CAFUIState driverSide];
-[CAFUIState hasDriverSide];
-[CAFUIState registeredForDriverSide];
-[CAFUIState registeredForUISceneOptions];
-[CAFUIState registeredForUISceneState];
-[CAFUIState uiSceneOptions];
-[CAFUIState uiSceneState];
-[CAFUIState _characteristicDidUpdate:fromGroupUpdate:];
-[CAFUIState driverSideCharacteristic];
-[CAFUIState hasUiSceneOptions];
-[CAFUIState uiSceneOptionsCharacteristic];
-[CAFUIState uiSceneStateCharacteristic];
```
