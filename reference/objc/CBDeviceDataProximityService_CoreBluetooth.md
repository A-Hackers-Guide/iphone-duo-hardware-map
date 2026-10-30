# `CBDeviceDataProximityService`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 21 instance variables, 25 properties, 54 instance methods, 1 class methods

## Instance variables

```
C _proximityServiceAccessoryCategory;
C _proximityServiceCategory;
C _proximityServiceColorCode;
C _proximityServiceFlags;
c _proximityServiceMeasuredPower;
c _proximityServiceMeasuredPowerImm;
c _proximityServiceMeasuredPowerVicinity;
C _proximityServiceSubType;
C _proximityServiceVersion;
S _proximityServicePSM;
S _proximityServiceVendorID;
I _proximityServiceProductID;
@"NSData" _proximityServiceClassicAddress;
@"NSData" _proximityServiceControlIdentifier;
@"NSData" _proximityServiceData;
@"NSData" _proximityServiceManufacturerID;
@"NSData" _proximityServiceModelID;
Q _proximityServicePairingCapabilities;
Q _proximityServiceProductKitBackoffTicks;
@"NSData" _proximityServiceSetupHash;
Q _proximityServiceSupportedFeatures;
```

## Properties

```
@property (TC,N,V_proximityServiceAccessoryCategory) proximityServiceAccessoryCategory;
@property (TC,N,V_proximityServiceCategory) proximityServiceCategory;
@property (T@"NSData",C,N,V_proximityServiceClassicAddress) proximityServiceClassicAddress;
@property (TC,N,V_proximityServiceColorCode) proximityServiceColorCode;
@property (T@"NSData",C,N,V_proximityServiceControlIdentifier) proximityServiceControlIdentifier;
@property (T@"NSData",C,N,V_proximityServiceData) proximityServiceData;
@property (TC,N,V_proximityServiceFlags) proximityServiceFlags;
@property (T@"NSData",C,N,V_proximityServiceManufacturerID) proximityServiceManufacturerID;
@property (Tc,N,V_proximityServiceMeasuredPower) proximityServiceMeasuredPower;
@property (Tc,N,V_proximityServiceMeasuredPowerImm) proximityServiceMeasuredPowerImm;
@property (Tc,N,V_proximityServiceMeasuredPowerVicinity) proximityServiceMeasuredPowerVicinity;
@property (T@"NSData",C,N,V_proximityServiceModelID) proximityServiceModelID;
@property (TQ,N,V_proximityServicePairingCapabilities) proximityServicePairingCapabilities;
@property (TI,N,V_proximityServiceProductID) proximityServiceProductID;
@property (TQ,N,V_proximityServiceProductKitBackoffTicks) proximityServiceProductKitBackoffTicks;
@property (TS,N,V_proximityServicePSM) proximityServicePSM;
@property (T@"NSData",C,N,V_proximityServiceSetupHash) proximityServiceSetupHash;
@property (TC,N,V_proximityServiceSubType) proximityServiceSubType;
@property (TQ,N,V_proximityServiceSupportedFeatures) proximityServiceSupportedFeatures;
@property (TS,N,V_proximityServiceVendorID) proximityServiceVendorID;
@property (TC,N,V_proximityServiceVersion) proximityServiceVersion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceDataProximityService supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceDataProximityService memoryFootprint];
-[CBDeviceDataProximityService encodeWithXPCObject:];
-[CBDeviceDataProximityService initWithDictionary:error:];
-[CBDeviceDataProximityService clear];
-[CBDeviceDataProximityService initWithXPCObject:error:];
-[CBDeviceDataProximityService descriptionWithLevel:];
-[CBDeviceDataProximityService setProximityServiceData:];
-[CBDeviceDataProximityService proximityServiceProductKitBackoffTicks];
-[CBDeviceDataProximityService proximityServiceMeasuredPower];
-[CBDeviceDataProximityService proximityServiceColorCode];
-[CBDeviceDataProximityService setProximityServiceMeasuredPowerImm:];
-[CBDeviceDataProximityService proximityServiceSubType];
-[CBDeviceDataProximityService proximityServiceSetupHash];
-[CBDeviceDataProximityService proximityServiceClassicAddress];
-[CBDeviceDataProximityService setProximityServiceMeasuredPowerVicinity:];
-[CBDeviceDataProximityService setProximityServiceColorCode:];
-[CBDeviceDataProximityService setProximityServiceSubType:];
-[CBDeviceDataProximityService setProximityServiceCategory:];
-[CBDeviceDataProximityService proximityServiceControlIdentifier];
-[CBDeviceDataProximityService setProximityServiceSupportedFeatures:];
-[CBDeviceDataProximityService proximityServicePairingCapabilities];
-[CBDeviceDataProximityService setProximityServiceManufacturerID:];
-[CBDeviceDataProximityService setProximityServicePairingCapabilities:];
-[CBDeviceDataProximityService proximityServiceProductID];
-[CBDeviceDataProximityService setProximityServiceClassicAddress:];
-[CBDeviceDataProximityService setProximityServiceVendorID:];
-[CBDeviceDataProximityService encodeWithCoder:];
-[CBDeviceDataProximityService proximityServiceFlags];
-[CBDeviceDataProximityService proximityServiceMeasuredPowerImm];
-[CBDeviceDataProximityService proximityServiceCategory];
-[CBDeviceDataProximityService proximityServiceMeasuredPowerVicinity];
-[CBDeviceDataProximityService proximityServiceSupportedFeatures];
-[CBDeviceDataProximityService setProximityServiceSetupHash:];
-[CBDeviceDataProximityService setProximityServiceModelID:];
-[CBDeviceDataProximityService description];
-[CBDeviceDataProximityService setProximityServiceVersion:];
-[CBDeviceDataProximityService proximityServiceManufacturerID];
-[CBDeviceDataProximityService setProximityServiceControlIdentifier:];
-[CBDeviceDataProximityService initWithCoder:];
-[CBDeviceDataProximityService proximityServicePSM];
-[CBDeviceDataProximityService hasAnyData];
-[CBDeviceDataProximityService proximityServiceAccessoryCategory];
-[CBDeviceDataProximityService proximityServiceVersion];
-[CBDeviceDataProximityService setProximityServiceProductID:];
-[CBDeviceDataProximityService proximityServiceData];
-[CBDeviceDataProximityService copyWithZone:];
-[CBDeviceDataProximityService proximityServiceModelID];
-[CBDeviceDataProximityService setProximityServiceAccessoryCategory:];
-[CBDeviceDataProximityService setProximityServiceMeasuredPower:];
-[CBDeviceDataProximityService proximityServiceVendorID];
-[CBDeviceDataProximityService setProximityServiceProductKitBackoffTicks:];
-[CBDeviceDataProximityService setProximityServicePSM:];
-[CBDeviceDataProximityService dictionaryRepresentation];
-[CBDeviceDataProximityService setProximityServiceFlags:];
```
