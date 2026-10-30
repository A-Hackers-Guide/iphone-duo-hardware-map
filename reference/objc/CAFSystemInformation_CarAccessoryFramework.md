# `CAFSystemInformation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 15 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleVehicleBrandCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleNavigationSystemNameCharacteristic;
@property (T@"CAFRouteSourceCharacteristic",R,N) routeSourceCharacteristic;
@property (T@"NSString",R,N) userVisibleVehicleBrand;
@property (T@"NSString",R,N) userVisibleNavigationSystemName;
@property (TC,R,N) routeSource;
```

## Class methods

```
+[CAFSystemInformation serviceIdentifier];
+[CAFSystemInformation observerProtocol];
```

## Instance methods

```
-[CAFSystemInformation removeObserver:];
-[CAFSystemInformation addObserver:];
-[CAFSystemInformation registerObserver:];
-[CAFSystemInformation name];
-[CAFSystemInformation unregisterObserver:];
-[CAFSystemInformation userVisibleNavigationSystemName];
-[CAFSystemInformation routeSource];
-[CAFSystemInformation userVisibleVehicleBrand];
-[CAFSystemInformation registeredForRouteSource];
-[CAFSystemInformation registeredForUserVisibleNavigationSystemName];
-[CAFSystemInformation registeredForUserVisibleVehicleBrand];
-[CAFSystemInformation _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSystemInformation routeSourceCharacteristic];
-[CAFSystemInformation userVisibleNavigationSystemNameCharacteristic];
-[CAFSystemInformation userVisibleVehicleBrandCharacteristic];
```
