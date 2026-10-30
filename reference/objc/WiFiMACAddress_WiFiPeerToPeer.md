# `WiFiMACAddress`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSData" _data;
@"NSData" _ipv6LinkLocalAddress;
```

## Properties

```
@property (T@"NSData",R,V_data) data;
@property (T@"NSData",R,V_ipv6LinkLocalAddress) ipv6LinkLocalAddress;
```

## Class methods

```
+[WiFiMACAddress supportsSecureCoding];
+[WiFiMACAddress zeroAddress];
```

## Instance methods

```
-[WiFiMACAddress data];
-[WiFiMACAddress initWithLinkLocalIPv6Address:];
-[WiFiMACAddress initWithMulticastIPv6Address:];
-[WiFiMACAddress encodeWithCoder:];
-[WiFiMACAddress hash];
-[WiFiMACAddress ipv6LinkLocalAddress];
-[WiFiMACAddress description];
-[WiFiMACAddress initWithAddress:ipv6Address:];
-[WiFiMACAddress initWithAddress:];
-[WiFiMACAddress initWithCoder:];
-[WiFiMACAddress copyWithZone:];
-[WiFiMACAddress isEqual:];
```
