# `WiFiAwareMulticastConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _dynamicLinkRate;
@"WiFiMACAddress" _multicastAddress;
q _keyExchangeOverMedium;
@"NSData" _gtkKey;
@"NSData" _igtkKey;
@"NSData" _keyBlob;
```

## Properties

```
@property (T@"WiFiMACAddress",C,N,V_multicastAddress) multicastAddress;
@property (TB,N,V_dynamicLinkRate) dynamicLinkRate;
@property (Tq,N,V_keyExchangeOverMedium) keyExchangeOverMedium;
@property (T@"NSData",C,N,V_gtkKey) gtkKey;
@property (T@"NSData",C,N,V_igtkKey) igtkKey;
@property (T@"NSData",C,N,V_keyBlob) keyBlob;
```

## Class methods

```
+[WiFiAwareMulticastConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareMulticastConfiguration multicastAddressConfigurationEqual:];
-[WiFiAwareMulticastConfiguration init];
-[WiFiAwareMulticastConfiguration multicastAddress];
-[WiFiAwareMulticastConfiguration encodeWithCoder:];
-[WiFiAwareMulticastConfiguration description];
-[WiFiAwareMulticastConfiguration initWithCoder:];
-[WiFiAwareMulticastConfiguration copyWithZone:];
-[WiFiAwareMulticastConfiguration setMulticastAddress:];
-[WiFiAwareMulticastConfiguration isEqual:];
-[WiFiAwareMulticastConfiguration keyBlob];
-[WiFiAwareMulticastConfiguration setKeyBlob:];
-[WiFiAwareMulticastConfiguration setDynamicLinkRate:];
-[WiFiAwareMulticastConfiguration setKeyExchangeOverMedium:];
-[WiFiAwareMulticastConfiguration dynamicLinkRate];
-[WiFiAwareMulticastConfiguration igtkKey];
-[WiFiAwareMulticastConfiguration gtkKey];
-[WiFiAwareMulticastConfiguration keyExchangeOverMedium];
-[WiFiAwareMulticastConfiguration setGtkKey:];
-[WiFiAwareMulticastConfiguration setIgtkKey:];
```
