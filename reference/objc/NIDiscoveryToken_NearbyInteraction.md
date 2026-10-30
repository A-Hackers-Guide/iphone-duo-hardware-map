# `NIDiscoveryToken`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 4 properties, 17 instance methods, 9 class methods

## Instance variables

```
@"NSData" _rawToken;
@"NSNumber" _shortDeviceAddress;
@"NSData" _identifyingSequence;
```

## Properties

```
@property (T@"NSData",R,C,V_rawToken) rawToken;
@property (T@"NSString",R) rawTokenAsString;
@property (Tq,R) tokenVariant;
@property (T@"<NIDeviceCapability>",R,C,N) deviceCapabilities;
```

## Class methods

```
+[NIDiscoveryToken supportsSecureCoding];
+[NIDiscoveryToken deserialize:];
+[NIDiscoveryToken serialize:];
+[NIDiscoveryToken _identifyingSequenceFromBytes:];
+[NIDiscoveryToken generateDiscoveryTokenFromBeaconIdentifier:];
+[NIDiscoveryToken generateFindingTokenWithIRK:];
+[NIDiscoveryToken generateFindingTokenWithIRK:forExternalUse:];
+[NIDiscoveryToken generateFindingTokenWithServiceID:deviceUUID:];
+[NIDiscoveryToken generateTokenWithUUID:];
```

## Instance methods

```
-[NIDiscoveryToken deviceCapabilities];
-[NIDiscoveryToken initWithBytes:];
-[NIDiscoveryToken shortDeviceAddress];
-[NIDiscoveryToken descriptionInternal];
-[NIDiscoveryToken tokenVariant];
-[NIDiscoveryToken rawToken];
-[NIDiscoveryToken getIRK];
-[NIDiscoveryToken encodeWithCoder:];
-[NIDiscoveryToken initWithDeviceAddress:];
-[NIDiscoveryToken objectInRawTokenOPACKDictForKey:];
-[NIDiscoveryToken rawTokenAsString];
-[NIDiscoveryToken hash];
-[NIDiscoveryToken description];
-[NIDiscoveryToken initWithCoder:];
-[NIDiscoveryToken getSessionIdentifier];
-[NIDiscoveryToken copyWithZone:];
-[NIDiscoveryToken isEqual:];
```
