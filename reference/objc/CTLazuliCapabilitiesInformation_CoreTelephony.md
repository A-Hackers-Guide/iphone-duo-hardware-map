# `CTLazuliCapabilitiesInformation`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 17 instance variables, 17 properties, 41 instance methods, 1 class methods

## Instance variables

```
B _supportsVideoSharing;
B _supportsImageSharing;
B _supportsChat;
B _supportsFileTransfer;
B _supportsGeolocationCapabilities;
B _isBot;
B _supportsFeature;
B _supportsSecurity;
B _isExpired;
B _supportsExtendedMessagingReply;
B _supportsExtendedMessagingReaction;
B _supportsExtendedMessagingCustomReaction;
@"CTLazuliDestination" _recipient;
@"NSString" _supportedLazuliExtensions;
q _availibility;
@"CTLazuliAlternateIdentities" _alternateIdentities;
@"NSDate" _validUntil;
```

## Properties

```
@property (T@"CTLazuliDestination",&,N,V_recipient) recipient;
@property (TB,N,V_supportsVideoSharing) supportsVideoSharing;
@property (TB,N,V_supportsImageSharing) supportsImageSharing;
@property (TB,N,V_supportsChat) supportsChat;
@property (TB,N,V_supportsFileTransfer) supportsFileTransfer;
@property (TB,N,V_supportsGeolocationCapabilities) supportsGeolocationCapabilities;
@property (TB,N,V_isBot) isBot;
@property (T@"NSString",&,N,V_supportedLazuliExtensions) supportedLazuliExtensions;
@property (TB,N,V_supportsFeature) supportsFeature;
@property (Tq,N,V_availibility) availibility;
@property (T@"CTLazuliAlternateIdentities",&,N,V_alternateIdentities) alternateIdentities;
@property (T@"NSDate",&,N,V_validUntil) validUntil;
@property (TB,N,V_supportsSecurity) supportsSecurity;
@property (TB,N,V_isExpired) isExpired;
@property (TB,N,V_supportsExtendedMessagingReply) supportsExtendedMessagingReply;
@property (TB,N,V_supportsExtendedMessagingReaction) supportsExtendedMessagingReaction;
@property (TB,N,V_supportsExtendedMessagingCustomReaction) supportsExtendedMessagingCustomReaction;
```

## Class methods

```
+[CTLazuliCapabilitiesInformation supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliCapabilitiesInformation validUntil];
-[CTLazuliCapabilitiesInformation recipient];
-[CTLazuliCapabilitiesInformation setRecipient:];
-[CTLazuliCapabilitiesInformation isExpired];
-[CTLazuliCapabilitiesInformation encodeWithCoder:];
-[CTLazuliCapabilitiesInformation description];
-[CTLazuliCapabilitiesInformation initWithCoder:];
-[CTLazuliCapabilitiesInformation copyWithZone:];
-[CTLazuliCapabilitiesInformation isEqual:];
-[CTLazuliCapabilitiesInformation supportsFeature];
-[CTLazuliCapabilitiesInformation supportsGeolocationCapabilities];
-[CTLazuliCapabilitiesInformation alternateIdentities];
-[CTLazuliCapabilitiesInformation availibility];
-[CTLazuliCapabilitiesInformation initWithReflection:];
-[CTLazuliCapabilitiesInformation isBot];
-[CTLazuliCapabilitiesInformation isEqualToCTLazuliCapabilitiesInformation:];
-[CTLazuliCapabilitiesInformation setAlternateIdentities:];
-[CTLazuliCapabilitiesInformation setAvailibility:];
-[CTLazuliCapabilitiesInformation setIsBot:];
-[CTLazuliCapabilitiesInformation setIsExpired:];
-[CTLazuliCapabilitiesInformation setSupportedLazuliExtensions:];
-[CTLazuliCapabilitiesInformation setSupportsChat:];
-[CTLazuliCapabilitiesInformation setSupportsExtendedMessagingCustomReaction:];
-[CTLazuliCapabilitiesInformation setSupportsExtendedMessagingReaction:];
-[CTLazuliCapabilitiesInformation setSupportsExtendedMessagingReply:];
-[CTLazuliCapabilitiesInformation setSupportsFeature:];
-[CTLazuliCapabilitiesInformation setSupportsFileTransfer:];
-[CTLazuliCapabilitiesInformation setSupportsGeolocationCapabilities:];
-[CTLazuliCapabilitiesInformation setSupportsImageSharing:];
-[CTLazuliCapabilitiesInformation setSupportsSecurity:];
-[CTLazuliCapabilitiesInformation setSupportsVideoSharing:];
-[CTLazuliCapabilitiesInformation setValidUntil:];
-[CTLazuliCapabilitiesInformation supportedLazuliExtensions];
-[CTLazuliCapabilitiesInformation supportsChat];
-[CTLazuliCapabilitiesInformation supportsExtendedMessagingCustomReaction];
-[CTLazuliCapabilitiesInformation supportsExtendedMessagingReaction];
-[CTLazuliCapabilitiesInformation supportsExtendedMessagingReply];
-[CTLazuliCapabilitiesInformation supportsFileTransfer];
-[CTLazuliCapabilitiesInformation supportsImageSharing];
-[CTLazuliCapabilitiesInformation supportsSecurity];
-[CTLazuliCapabilitiesInformation supportsVideoSharing];
```
