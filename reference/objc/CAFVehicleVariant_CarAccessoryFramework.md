# `CAFVehicleVariant`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 13 properties, 24 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) exteriorStyleCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) interiorStyleCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) audioLogoCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLogoCharacteristic;
@property (T@"NSString",R,N) exteriorStyle;
@property (T@"NSString",R,N) interiorStyle;
@property (T@"NSString",R,N) vehicleLayout;
@property (TB,R,N) hasVehicleLayout;
@property (T@"NSString",R,N) audioLogo;
@property (TB,R,N) hasAudioLogo;
@property (T@"NSString",R,N) vehicleLogo;
@property (TB,R,N) hasVehicleLogo;
```

## Class methods

```
+[CAFVehicleVariant serviceIdentifier];
+[CAFVehicleVariant observerProtocol];
```

## Instance methods

```
-[CAFVehicleVariant removeObserver:];
-[CAFVehicleVariant addObserver:];
-[CAFVehicleVariant registerObserver:];
-[CAFVehicleVariant name];
-[CAFVehicleVariant unregisterObserver:];
-[CAFVehicleVariant audioLogo];
-[CAFVehicleVariant exteriorStyle];
-[CAFVehicleVariant interiorStyle];
-[CAFVehicleVariant registeredForAudioLogo];
-[CAFVehicleVariant registeredForExteriorStyle];
-[CAFVehicleVariant registeredForInteriorStyle];
-[CAFVehicleVariant registeredForVehicleLayout];
-[CAFVehicleVariant registeredForVehicleLogo];
-[CAFVehicleVariant vehicleLayout];
-[CAFVehicleVariant vehicleLogo];
-[CAFVehicleVariant _characteristicDidUpdate:fromGroupUpdate:];
-[CAFVehicleVariant audioLogoCharacteristic];
-[CAFVehicleVariant exteriorStyleCharacteristic];
-[CAFVehicleVariant hasAudioLogo];
-[CAFVehicleVariant hasVehicleLayout];
-[CAFVehicleVariant hasVehicleLogo];
-[CAFVehicleVariant interiorStyleCharacteristic];
-[CAFVehicleVariant vehicleLayoutCharacteristic];
-[CAFVehicleVariant vehicleLogoCharacteristic];
```
