# `CAFPairedDevices`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 4 properties, 8 instance methods, 2 class methods

## Properties

```
@property (T@"CAFPairedDevicesInformation",R,N) pairedDevicesInformationService;
@property (T@"CAFPairedDevicesAction",R,N) pairedDevicesActionService;
@property (T@"CAFPairedDevicesInformation",R,N) pairedDevicesInformation;
@property (T@"CAFPairedDevicesAction",R,N) pairedDevicesAction;
```

## Class methods

```
+[CAFPairedDevices accessoryIdentifier];
+[CAFPairedDevices observerProtocol];
```

## Instance methods

```
-[CAFPairedDevices removeObserver:];
-[CAFPairedDevices addObserver:];
-[CAFPairedDevices registerObserver:];
-[CAFPairedDevices unregisterObserver:];
-[CAFPairedDevices pairedDevicesAction];
-[CAFPairedDevices pairedDevicesInformation];
-[CAFPairedDevices pairedDevicesInformationService];
-[CAFPairedDevices pairedDevicesActionService];
```
