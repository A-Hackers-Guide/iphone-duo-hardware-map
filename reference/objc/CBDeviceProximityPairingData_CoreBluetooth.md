# `CBDeviceProximityPairingData`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 16 instance variables, 20 properties, 44 instance methods, 2 class methods

## Instance variables

```
C _proximityPairingConnectionMethod;
C _proximityPairingSubType;
C _transmitPowerOne;
C _transmitPowerTwo;
C _transmitPowerThree;
C _peerStatusFlag;
C _accessoryStatusLidOpenCount;
I _proximityPairingOtherBudProductID;
I _proximityPairingProductID;
i _proximityPairingPrimaryPlacement;
i _proximityPairingSecondaryPlacement;
I _accessoryStatusFlags;
@"NSData" _proximityPairingClassicAddress;
@"NSData" _proximityPairingPayloadData;
d _accessoryStatusOBCTime;
@"CBDeviceObjectSetupData" _objectSetup;
```

## Properties

```
@property (TC,N,V_proximityPairingConnectionMethod) proximityPairingConnectionMethod;
@property (T@"NSData",C,N,V_proximityPairingClassicAddress) proximityPairingClassicAddress;
@property (TI,N,V_proximityPairingOtherBudProductID) proximityPairingOtherBudProductID;
@property (T@"NSData",C,N,V_proximityPairingPayloadData) proximityPairingPayloadData;
@property (TI,N,V_proximityPairingProductID) proximityPairingProductID;
@property (TC,N,V_proximityPairingSubType) proximityPairingSubType;
@property (Ti,N,V_proximityPairingPrimaryPlacement) proximityPairingPrimaryPlacement;
@property (Ti,N,V_proximityPairingSecondaryPlacement) proximityPairingSecondaryPlacement;
@property (TC,N,V_transmitPowerOne) transmitPowerOne;
@property (TC,N,V_transmitPowerTwo) transmitPowerTwo;
@property (TC,N,V_transmitPowerThree) transmitPowerThree;
@property (TC,N,V_peerStatusFlag) peerStatusFlag;
@property (TI,N,V_accessoryStatusFlags) accessoryStatusFlags;
@property (TC,N,V_accessoryStatusLidOpenCount) accessoryStatusLidOpenCount;
@property (Td,N,V_accessoryStatusOBCTime) accessoryStatusOBCTime;
@property (T@"CBDeviceObjectSetupData",&,N,V_objectSetup) objectSetup;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceProximityPairingData supportsSecureCoding];
+[CBDeviceProximityPairingData proxPairingPropertyMetadata];
```

## Instance methods

```
-[CBDeviceProximityPairingData memoryFootprint];
-[CBDeviceProximityPairingData encodeWithXPCObject:];
-[CBDeviceProximityPairingData initWithDictionary:error:];
-[CBDeviceProximityPairingData clear];
-[CBDeviceProximityPairingData initWithXPCObject:error:];
-[CBDeviceProximityPairingData descriptionWithLevel:];
-[CBDeviceProximityPairingData encodeWithCoder:];
-[CBDeviceProximityPairingData description];
-[CBDeviceProximityPairingData initWithCoder:];
-[CBDeviceProximityPairingData hasAnyData];
-[CBDeviceProximityPairingData copyWithZone:];
-[CBDeviceProximityPairingData dictionaryRepresentation];
-[CBDeviceProximityPairingData proximityPairingProductID];
-[CBDeviceProximityPairingData proximityPairingSubType];
-[CBDeviceProximityPairingData setObjectSetup:];
-[CBDeviceProximityPairingData setAccessoryStatusLidOpenCount:];
-[CBDeviceProximityPairingData setProximityPairingPayloadData:];
-[CBDeviceProximityPairingData accessoryStatusFlags];
-[CBDeviceProximityPairingData accessoryStatusLidOpenCount];
-[CBDeviceProximityPairingData accessoryStatusOBCTime];
-[CBDeviceProximityPairingData objectSetup];
-[CBDeviceProximityPairingData peerStatusFlag];
-[CBDeviceProximityPairingData proximityPairingClassicAddress];
-[CBDeviceProximityPairingData proximityPairingConnectionMethod];
-[CBDeviceProximityPairingData proximityPairingOtherBudProductID];
-[CBDeviceProximityPairingData proximityPairingPayloadData];
-[CBDeviceProximityPairingData proximityPairingPrimaryPlacement];
-[CBDeviceProximityPairingData proximityPairingSecondaryPlacement];
-[CBDeviceProximityPairingData setAccessoryStatusFlags:];
-[CBDeviceProximityPairingData setAccessoryStatusOBCTime:];
-[CBDeviceProximityPairingData setPeerStatusFlag:];
-[CBDeviceProximityPairingData setProximityPairingClassicAddress:];
-[CBDeviceProximityPairingData setProximityPairingConnectionMethod:];
-[CBDeviceProximityPairingData setProximityPairingOtherBudProductID:];
-[CBDeviceProximityPairingData setProximityPairingPrimaryPlacement:];
-[CBDeviceProximityPairingData setProximityPairingProductID:];
-[CBDeviceProximityPairingData setProximityPairingSecondaryPlacement:];
-[CBDeviceProximityPairingData setProximityPairingSubType:];
-[CBDeviceProximityPairingData setTransmitPowerOne:];
-[CBDeviceProximityPairingData setTransmitPowerThree:];
-[CBDeviceProximityPairingData setTransmitPowerTwo:];
-[CBDeviceProximityPairingData transmitPowerOne];
-[CBDeviceProximityPairingData transmitPowerThree];
-[CBDeviceProximityPairingData transmitPowerTwo];
```
