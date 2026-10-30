# `CWFRangingPeer`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 2 class methods

## Instance variables

```
B _useCoreRotation;
@"NSString" _MACAddress;
@"NSData" _identifier;
@"NSData" _PMK;
Q _numberOfMeasurements;
```

## Properties

```
@property (T@"NSString",C,N,V_MACAddress) MACAddress;
@property (T@"NSData",C,N,V_identifier) identifier;
@property (T@"NSData",C,N,V_PMK) PMK;
@property (TQ,N,V_numberOfMeasurements) numberOfMeasurements;
@property (TB,N,V_useCoreRotation) useCoreRotation;
```

## Class methods

```
+[CWFRangingPeer supportsSecureCoding];
+[CWFRangingPeer rangingPeerWithMACAddress:PMK:];
```

## Instance methods

```
-[CWFRangingPeer MACAddress];
-[CWFRangingPeer identifier];
-[CWFRangingPeer setIdentifier:];
-[CWFRangingPeer encodeWithCoder:];
-[CWFRangingPeer hash];
-[CWFRangingPeer description];
-[CWFRangingPeer initWithCoder:];
-[CWFRangingPeer copyWithZone:];
-[CWFRangingPeer isEqual:];
-[CWFRangingPeer PMK];
-[CWFRangingPeer setPMK:];
-[CWFRangingPeer useCoreRotation];
-[CWFRangingPeer isEqualToRangingPeer:];
-[CWFRangingPeer numberOfMeasurements];
-[CWFRangingPeer setMACAddress:];
-[CWFRangingPeer setNumberOfMeasurements:];
-[CWFRangingPeer setUseCoreRotation:];
```
