# `CAFVehicleInformation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) vehicleUserVisibleLabelCharacteristic;
@property (T@"NSString",R,N) vehicleUserVisibleLabel;
```

## Class methods

```
+[CAFVehicleInformation serviceIdentifier];
+[CAFVehicleInformation observerProtocol];
```

## Instance methods

```
-[CAFVehicleInformation removeObserver:];
-[CAFVehicleInformation addObserver:];
-[CAFVehicleInformation registerObserver:];
-[CAFVehicleInformation name];
-[CAFVehicleInformation unregisterObserver:];
-[CAFVehicleInformation registeredForVehicleUserVisibleLabel];
-[CAFVehicleInformation vehicleUserVisibleLabel];
-[CAFVehicleInformation _characteristicDidUpdate:fromGroupUpdate:];
-[CAFVehicleInformation vehicleUserVisibleLabelCharacteristic];
```
