# `CAFPairedDevicesInformation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFPairedDeviceListCharacteristic",R,N) pairedDeviceListCharacteristic;
@property (T@"CAFPairedDeviceList",R,N) pairedDeviceList;
```

## Class methods

```
+[CAFPairedDevicesInformation serviceIdentifier];
+[CAFPairedDevicesInformation observerProtocol];
```

## Instance methods

```
-[CAFPairedDevicesInformation removeObserver:];
-[CAFPairedDevicesInformation addObserver:];
-[CAFPairedDevicesInformation registerObserver:];
-[CAFPairedDevicesInformation name];
-[CAFPairedDevicesInformation unregisterObserver:];
-[CAFPairedDevicesInformation pairedDeviceList];
-[CAFPairedDevicesInformation registeredForPairedDeviceList];
-[CAFPairedDevicesInformation _characteristicDidUpdate:fromGroupUpdate:];
-[CAFPairedDevicesInformation pairedDeviceListCharacteristic];
```
