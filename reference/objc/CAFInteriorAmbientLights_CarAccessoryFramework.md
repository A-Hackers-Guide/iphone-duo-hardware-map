# `CAFInteriorAmbientLights`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 12 properties, 25 instance methods, 2 class methods

## Properties

```
@property (T@"CAFCurrentOwnerCharacteristic",R,N) currentOwnerCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) primaryColorCharacteristic;
@property (T@"CAFUInt32Characteristic",R,N) brightnessCharacteristic;
@property (T@"CAFSupportedColorsCharacteristic",R,N) supportedColorsCharacteristic;
@property (TC,N) currentOwner;
@property (TB,R,N) hasCurrentOwner;
@property (T@"NSString",C,N) primaryColor;
@property (TI,N) brightness;
@property (T@"CAFUInt32Range",R,N) brightnessRange;
@property (TB,R,N) hasBrightness;
@property (T@"CAFSupportedColors",R,N) supportedColors;
@property (TB,R,N) hasSupportedColors;
```

## Class methods

```
+[CAFInteriorAmbientLights serviceIdentifier];
+[CAFInteriorAmbientLights observerProtocol];
```

## Instance methods

```
-[CAFInteriorAmbientLights removeObserver:];
-[CAFInteriorAmbientLights setBrightness:];
-[CAFInteriorAmbientLights setPrimaryColor:];
-[CAFInteriorAmbientLights brightness];
-[CAFInteriorAmbientLights addObserver:];
-[CAFInteriorAmbientLights primaryColor];
-[CAFInteriorAmbientLights registerObserver:];
-[CAFInteriorAmbientLights name];
-[CAFInteriorAmbientLights unregisterObserver:];
-[CAFInteriorAmbientLights hasBrightness];
-[CAFInteriorAmbientLights brightnessCharacteristic];
-[CAFInteriorAmbientLights hasCurrentOwner];
-[CAFInteriorAmbientLights supportedColors];
-[CAFInteriorAmbientLights currentOwner];
-[CAFInteriorAmbientLights registeredForBrightness];
-[CAFInteriorAmbientLights registeredForCurrentOwner];
-[CAFInteriorAmbientLights registeredForPrimaryColor];
-[CAFInteriorAmbientLights registeredForSupportedColors];
-[CAFInteriorAmbientLights setCurrentOwner:];
-[CAFInteriorAmbientLights brightnessRange];
-[CAFInteriorAmbientLights _characteristicDidUpdate:fromGroupUpdate:];
-[CAFInteriorAmbientLights currentOwnerCharacteristic];
-[CAFInteriorAmbientLights hasSupportedColors];
-[CAFInteriorAmbientLights primaryColorCharacteristic];
-[CAFInteriorAmbientLights supportedColorsCharacteristic];
```
