# `CBDeviceNearbyInfoV2Data`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDeviceDataComponent`, `CUXPCCodable`, `NSSecureCoding`, `NSCopying`
- 13 instance variables, 17 properties, 38 instance methods, 1 class methods

## Instance variables

```
C _nearbyInfoV2Flags;
C _nearbyInfoV2DecryptedFlags;
C _nearbyInfoV2EncryptedFlags;
C _nearbyInfoV2InvitationCounter;
C _nearbyInfoV2InvitationRouteType;
S _nearbyInfoV2CarrierOutageMobileCountryCode;
S _nearbyInfoV2CarrierOutageMobileNetworkCode;
S _nearbyInfoV2CarrierOutageResolutionTimeOffset;
@"NSData" _nearbyInfoV2AuthIntegrityTagData;
@"NSData" _nearbyInfoV2AuthTagData;
@"NSData" _nearbyInfoV2EncryptedData;
@"NSData" _nearbyInfoV2NearbyFaceTimeData;
@"NSData" _nearbyInfoV2NearbyFaceTimeEncryptedData;
```

## Properties

```
@property (TC,N,V_nearbyInfoV2Flags) nearbyInfoV2Flags;
@property (TC,N,V_nearbyInfoV2DecryptedFlags) nearbyInfoV2DecryptedFlags;
@property (TC,N,V_nearbyInfoV2EncryptedFlags) nearbyInfoV2EncryptedFlags;
@property (TC,N,V_nearbyInfoV2InvitationCounter) nearbyInfoV2InvitationCounter;
@property (TC,N,V_nearbyInfoV2InvitationRouteType) nearbyInfoV2InvitationRouteType;
@property (T@"NSData",C,N,V_nearbyInfoV2AuthIntegrityTagData) nearbyInfoV2AuthIntegrityTagData;
@property (T@"NSData",C,N,V_nearbyInfoV2AuthTagData) nearbyInfoV2AuthTagData;
@property (T@"NSData",C,N,V_nearbyInfoV2EncryptedData) nearbyInfoV2EncryptedData;
@property (T@"NSData",C,N,V_nearbyInfoV2NearbyFaceTimeData) nearbyInfoV2NearbyFaceTimeData;
@property (T@"NSData",C,N,V_nearbyInfoV2NearbyFaceTimeEncryptedData) nearbyInfoV2NearbyFaceTimeEncryptedData;
@property (TS,N,V_nearbyInfoV2CarrierOutageMobileCountryCode) nearbyInfoV2CarrierOutageMobileCountryCode;
@property (TS,N,V_nearbyInfoV2CarrierOutageMobileNetworkCode) nearbyInfoV2CarrierOutageMobileNetworkCode;
@property (TS,N,V_nearbyInfoV2CarrierOutageResolutionTimeOffset) nearbyInfoV2CarrierOutageResolutionTimeOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBDeviceNearbyInfoV2Data supportsSecureCoding];
```

## Instance methods

```
-[CBDeviceNearbyInfoV2Data memoryFootprint];
-[CBDeviceNearbyInfoV2Data encodeWithXPCObject:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2DecryptedFlags:];
-[CBDeviceNearbyInfoV2Data initWithDictionary:error:];
-[CBDeviceNearbyInfoV2Data clear];
-[CBDeviceNearbyInfoV2Data initWithXPCObject:error:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2InvitationRouteType:];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2CarrierOutageMobileCountryCode];
-[CBDeviceNearbyInfoV2Data descriptionWithLevel:];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2DecryptedFlags];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2Flags];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2AuthIntegrityTagData:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2AuthTagData:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2Flags:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2CarrierOutageResolutionTimeOffset:];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2AuthIntegrityTagData];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2NearbyFaceTimeData:];
-[CBDeviceNearbyInfoV2Data encodeWithCoder:];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2CarrierOutageMobileNetworkCode];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2AuthTagData];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2InvitationCounter];
-[CBDeviceNearbyInfoV2Data description];
-[CBDeviceNearbyInfoV2Data initWithCoder:];
-[CBDeviceNearbyInfoV2Data hasAnyData];
-[CBDeviceNearbyInfoV2Data copyWithZone:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2InvitationCounter:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2CarrierOutageMobileCountryCode:];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2NearbyFaceTimeData];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2InvitationRouteType];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2CarrierOutageMobileNetworkCode:];
-[CBDeviceNearbyInfoV2Data dictionaryRepresentation];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2CarrierOutageResolutionTimeOffset];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2EncryptedData];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2EncryptedFlags];
-[CBDeviceNearbyInfoV2Data nearbyInfoV2NearbyFaceTimeEncryptedData];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2EncryptedData:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2EncryptedFlags:];
-[CBDeviceNearbyInfoV2Data setNearbyInfoV2NearbyFaceTimeEncryptedData:];
```
