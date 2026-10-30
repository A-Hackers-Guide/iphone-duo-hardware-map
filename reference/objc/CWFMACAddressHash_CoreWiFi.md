# `CWFMACAddressHash`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 19 instance methods, 5 class methods

## Instance variables

```
@"NSData" _salt;
@"NSData" _hashData;
q _hashMethod;
```

## Properties

```
@property (T@"NSData",&,N,V_salt) salt;
@property (T@"NSData",&,N,V_hashData) hashData;
@property (Tq,N,V_hashMethod) hashMethod;
```

## Class methods

```
+[CWFMACAddressHash supportsSecureCoding];
+[CWFMACAddressHash hashMACAddressData:withSalt:];
+[CWFMACAddressHash hashMethodFromString:];
+[CWFMACAddressHash parseMACAddress:];
+[CWFMACAddressHash stringFromHashMethod:];
```

## Instance methods

```
-[CWFMACAddressHash salt];
-[CWFMACAddressHash setSalt:];
-[CWFMACAddressHash encodeWithCoder:];
-[CWFMACAddressHash hash];
-[CWFMACAddressHash description];
-[CWFMACAddressHash initWithCoder:];
-[CWFMACAddressHash copyWithZone:];
-[CWFMACAddressHash isEqual:];
-[CWFMACAddressHash hashData];
-[CWFMACAddressHash initWithMACAddressData:andSalt:];
-[CWFMACAddressHash hashMethod];
-[CWFMACAddressHash initWithHashData:andSalt:andHashMethod:];
-[CWFMACAddressHash initWithMACAddress:];
-[CWFMACAddressHash initWithMACAddress:andSalt:];
-[CWFMACAddressHash initWithMACAddressData:];
-[CWFMACAddressHash matchesMACAddress:];
-[CWFMACAddressHash matchesMACAddressData:];
-[CWFMACAddressHash setHashData:];
-[CWFMACAddressHash setHashMethod:];
```
