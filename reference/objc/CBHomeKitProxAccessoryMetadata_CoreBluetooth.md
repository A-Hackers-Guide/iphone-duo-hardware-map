# `CBHomeKitProxAccessoryMetadata`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
C _accessoryCategory;
c _rssiOffsetProxPairing;
c _rssiOffsetImmediate;
c _rssiOffsetVicinity;
@"NSData" _manufacturerID;
@"NSData" _modelID;
Q _supportedFeatures;
Q _pairingCapabilities;
```

## Properties

```
@property (TC,N,V_accessoryCategory) accessoryCategory;
@property (T@"NSData",C,N,V_manufacturerID) manufacturerID;
@property (T@"NSData",C,N,V_modelID) modelID;
@property (Tc,N,V_rssiOffsetProxPairing) rssiOffsetProxPairing;
@property (Tc,N,V_rssiOffsetImmediate) rssiOffsetImmediate;
@property (Tc,N,V_rssiOffsetVicinity) rssiOffsetVicinity;
@property (TQ,N,V_supportedFeatures) supportedFeatures;
@property (TQ,N,V_pairingCapabilities) pairingCapabilities;
```

## Instance methods

```
-[CBHomeKitProxAccessoryMetadata setModelID:];
-[CBHomeKitProxAccessoryMetadata supportedFeatures];
-[CBHomeKitProxAccessoryMetadata setSupportedFeatures:];
-[CBHomeKitProxAccessoryMetadata modelID];
-[CBHomeKitProxAccessoryMetadata setAccessoryCategory:];
-[CBHomeKitProxAccessoryMetadata accessoryCategory];
-[CBHomeKitProxAccessoryMetadata manufacturerID];
-[CBHomeKitProxAccessoryMetadata pairingCapabilities];
-[CBHomeKitProxAccessoryMetadata rssiOffsetImmediate];
-[CBHomeKitProxAccessoryMetadata rssiOffsetProxPairing];
-[CBHomeKitProxAccessoryMetadata rssiOffsetVicinity];
-[CBHomeKitProxAccessoryMetadata setManufacturerID:];
-[CBHomeKitProxAccessoryMetadata setPairingCapabilities:];
-[CBHomeKitProxAccessoryMetadata setRssiOffsetImmediate:];
-[CBHomeKitProxAccessoryMetadata setRssiOffsetProxPairing:];
-[CBHomeKitProxAccessoryMetadata setRssiOffsetVicinity:];
```
