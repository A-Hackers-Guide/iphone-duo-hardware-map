# `CAFPairedDevicesAction`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 6 properties, 17 instance methods, 2 class methods

## Properties

```
@property (T@"CAFConnectDeviceControl",R,N) connectDeviceControl;
@property (T@"CAFDisconnectDeviceControl",R,N) disconnectDeviceControl;
@property (T@"CAFForgetDeviceControl",R,N) forgetDeviceControl;
@property (TB,R,N) hasConnectDevice;
@property (TB,R,N) hasDisconnectDevice;
@property (TB,R,N) hasForgetDevice;
```

## Class methods

```
+[CAFPairedDevicesAction serviceIdentifier];
+[CAFPairedDevicesAction observerProtocol];
```

## Instance methods

```
-[CAFPairedDevicesAction removeObserver:];
-[CAFPairedDevicesAction addObserver:];
-[CAFPairedDevicesAction registerObserver:];
-[CAFPairedDevicesAction name];
-[CAFPairedDevicesAction unregisterObserver:];
-[CAFPairedDevicesAction hasForgetDevice];
-[CAFPairedDevicesAction hasConnectDevice];
-[CAFPairedDevicesAction hasDisconnectDevice];
-[CAFPairedDevicesAction connectDeviceControl];
-[CAFPairedDevicesAction connectDeviceWithIdentifier:completion:];
-[CAFPairedDevicesAction disconnectDeviceControl];
-[CAFPairedDevicesAction disconnectDeviceWithIdentifier:completion:];
-[CAFPairedDevicesAction forgetDeviceControl];
-[CAFPairedDevicesAction forgetDeviceWithIdentifier:completion:];
-[CAFPairedDevicesAction registeredForConnectDevice];
-[CAFPairedDevicesAction registeredForDisconnectDevice];
-[CAFPairedDevicesAction registeredForForgetDevice];
```
