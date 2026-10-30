# `AWDLTrafficRegistrationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 9 instance variables, 9 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"NSString" _derivedLocalization;
B _legacyUpgradeRequired;
B _activeFlagOverride;
S _preferredChannel;
S _secondaryPreferredChannel;
@"NSString" _uniqueIdentifier;
@"WiFiMACAddress" _peerAddress;
q _options;
@? _invalidationHandler;
```

## Properties

```
@property (T@"NSString",R,N) localization;
@property (TB,N,V_activeFlagOverride) activeFlagOverride;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"WiFiMACAddress",C,N,V_peerAddress) peerAddress;
@property (Tq,N,V_options) options;
@property (TB,N,V_legacyUpgradeRequired) legacyUpgradeRequired;
@property (TS,N,V_preferredChannel) preferredChannel;
@property (TS,N,V_secondaryPreferredChannel) secondaryPreferredChannel;
```

## Class methods

```
+[AWDLTrafficRegistrationConfiguration supportsSecureCoding];
+[AWDLTrafficRegistrationConfiguration localizedErrorForConflictBetweenExistingService:withNewService:localDeviceName:localization:];
```

## Instance methods

```
-[AWDLTrafficRegistrationConfiguration setOptions:];
-[AWDLTrafficRegistrationConfiguration setInvalidationHandler:];
-[AWDLTrafficRegistrationConfiguration setUniqueIdentifier:];
-[AWDLTrafficRegistrationConfiguration peerAddress];
-[AWDLTrafficRegistrationConfiguration uniqueIdentifier];
-[AWDLTrafficRegistrationConfiguration localization];
-[AWDLTrafficRegistrationConfiguration encodeWithCoder:];
-[AWDLTrafficRegistrationConfiguration hash];
-[AWDLTrafficRegistrationConfiguration description];
-[AWDLTrafficRegistrationConfiguration initWithCoder:];
-[AWDLTrafficRegistrationConfiguration options];
-[AWDLTrafficRegistrationConfiguration invalidationHandler];
-[AWDLTrafficRegistrationConfiguration copyWithZone:];
-[AWDLTrafficRegistrationConfiguration isEqual:];
-[AWDLTrafficRegistrationConfiguration setPeerAddress:];
-[AWDLTrafficRegistrationConfiguration preferredChannel];
-[AWDLTrafficRegistrationConfiguration setPreferredChannel:];
-[AWDLTrafficRegistrationConfiguration initWithUniqueIdentifier:peerAddress:];
-[AWDLTrafficRegistrationConfiguration setLegacyUpgradeRequired:];
-[AWDLTrafficRegistrationConfiguration initWithDictionary:isActive:];
-[AWDLTrafficRegistrationConfiguration secondaryPreferredChannel];
-[AWDLTrafficRegistrationConfiguration setSecondaryPreferredChannel:];
-[AWDLTrafficRegistrationConfiguration initWithUniqueIdentifier:peerIPv6Address:];
-[AWDLTrafficRegistrationConfiguration activeFlagOverride];
-[AWDLTrafficRegistrationConfiguration hasSimilarOptionsTo:];
-[AWDLTrafficRegistrationConfiguration isKnownService];
-[AWDLTrafficRegistrationConfiguration legacyUpgradeRequired];
-[AWDLTrafficRegistrationConfiguration setActiveFlagOverride:];
```
