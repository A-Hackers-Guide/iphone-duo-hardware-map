# `ACCBLEPairingAccessory`

- Image: [`/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`](../userland/System__Library__PrivateFrameworks__AccessoryBLEPairing.framework__AccessoryBLEPairing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _desiredBLEPairingState;
B _blePairingFinished;
@"NSString" _accessoryUID;
@"NSDictionary" _accInfo;
@"NSData" _blePairingUUID;
@"NSData" _supportedPairTypes;
```

## Properties

```
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (TB,N,V_desiredBLEPairingState) desiredBLEPairingState;
@property (T@"NSDictionary",&,N,V_accInfo) accInfo;
@property (T@"NSData",&,N,V_blePairingUUID) blePairingUUID;
@property (T@"NSData",&,N,V_supportedPairTypes) supportedPairTypes;
@property (TB,N,V_blePairingFinished) blePairingFinished;
```

## Instance methods

```
-[ACCBLEPairingAccessory accessoryUID];
-[ACCBLEPairingAccessory setAccessoryUID:];
-[ACCBLEPairingAccessory accInfo];
-[ACCBLEPairingAccessory blePairingFinished];
-[ACCBLEPairingAccessory blePairingUUID];
-[ACCBLEPairingAccessory desiredBLEPairingState];
-[ACCBLEPairingAccessory initWithAccessoryUID:blePairingUUID:andAccInfo:supportedPairTypes:];
-[ACCBLEPairingAccessory setAccInfo:];
-[ACCBLEPairingAccessory setBlePairingFinished:];
-[ACCBLEPairingAccessory setBlePairingUUID:];
-[ACCBLEPairingAccessory setDesiredBLEPairingState:];
-[ACCBLEPairingAccessory setSupportedPairTypes:];
-[ACCBLEPairingAccessory supportedPairTypes];
```
