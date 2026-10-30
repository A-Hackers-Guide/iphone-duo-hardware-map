# `THNetworkSignature`

- Image: [`/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread`](../userland/System__Library__PrivateFrameworks__CoreThread.framework__CoreThread.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSData" _ipv4NwSignature;
@"NSData" _ipv6NwSignature;
@"NSString" _wifiSSID;
@"NSString" _wifiPassword;
```

## Properties

```
@property (T@"NSData",R,N,V_ipv4NwSignature) ipv4NwSignature;
@property (T@"NSData",R,N,V_ipv6NwSignature) ipv6NwSignature;
@property (T@"NSString",R,N,V_wifiSSID) wifiSSID;
@property (T@"NSString",R,N,V_wifiPassword) wifiPassword;
```

## Class methods

```
+[THNetworkSignature supportsSecureCoding];
```

## Instance methods

```
-[THNetworkSignature encodeWithCoder:];
-[THNetworkSignature initWithCoder:];
-[THNetworkSignature wifiSSID];
-[THNetworkSignature ipv4NwSignature];
-[THNetworkSignature ipv6NwSignature];
-[THNetworkSignature initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:];
-[THNetworkSignature initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:];
-[THNetworkSignature wifiPassword];
```
