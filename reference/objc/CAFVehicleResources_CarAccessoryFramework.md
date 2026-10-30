# `CAFVehicleResources`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 6 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFVehicleVariant",R,N) vehicleVariantService;
@property (T@"CAFVehicleInformation",R,N) vehicleInformationService;
@property (T@"CAFCustomImageArchive",R,N) customImageArchiveService;
@property (T@"CAFVehicleVariant",R,N) vehicleVariant;
@property (T@"CAFVehicleInformation",R,N) vehicleInformation;
@property (T@"CAFCustomImageArchive",R,N) customImageArchive;
```

## Class methods

```
+[CAFVehicleResources accessoryIdentifier];
+[CAFVehicleResources observerProtocol];
```

## Instance methods

```
-[CAFVehicleResources removeObserver:];
-[CAFVehicleResources addObserver:];
-[CAFVehicleResources registerObserver:];
-[CAFVehicleResources unregisterObserver:];
-[CAFVehicleResources vehicleInformation];
-[CAFVehicleResources customImageArchive];
-[CAFVehicleResources customImageArchiveService];
-[CAFVehicleResources vehicleInformationService];
-[CAFVehicleResources vehicleVariant];
-[CAFVehicleResources vehicleVariantService];
```
