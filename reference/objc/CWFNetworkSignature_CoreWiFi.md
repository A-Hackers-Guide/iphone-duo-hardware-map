# `CWFNetworkSignature`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSString" _IPv4NetworkSignature;
@"NSString" _IPv6NetworkSignature;
```

## Properties

```
@property (T@"NSString",C,N,V_IPv4NetworkSignature) IPv4NetworkSignature;
@property (T@"NSString",C,N,V_IPv6NetworkSignature) IPv6NetworkSignature;
```

## Class methods

```
+[CWFNetworkSignature supportsSecureCoding];
+[CWFNetworkSignature createHexStringFromBytes:];
```

## Instance methods

```
-[CWFNetworkSignature IPv4NetworkSignature];
-[CWFNetworkSignature IPv6NetworkSignature];
-[CWFNetworkSignature encodeWithCoder:];
-[CWFNetworkSignature setIPv4NetworkSignature:];
-[CWFNetworkSignature description];
-[CWFNetworkSignature setIPv6NetworkSignature:];
-[CWFNetworkSignature initWithCoder:];
-[CWFNetworkSignature copyWithZone:];
-[CWFNetworkSignature initWithIPv4NetworkSignature:IPv6NetworkSignature:];
-[CWFNetworkSignature initWithIPv4NetworkSignature:];
-[CWFNetworkSignature initWithIPv4NetworkSignatureBytes:IPv6NetworkSignatureBytes:];
-[CWFNetworkSignature initWithIPv6NetworkSignature:];
-[CWFNetworkSignature initWithNetworkSignatureWithString:];
```
