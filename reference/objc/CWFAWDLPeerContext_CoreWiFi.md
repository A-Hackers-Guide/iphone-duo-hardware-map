# `CWFAWDLPeerContext`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSString" _MACAddress;
@"NSString" _interfaceName;
```

## Properties

```
@property (T@"NSString",C,N,V_MACAddress) MACAddress;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
```

## Class methods

```
+[CWFAWDLPeerContext supportsSecureCoding];
+[CWFAWDLPeerContext AWDLPeerContextWithMACAddress:interfaceName:];
```

## Instance methods

```
-[CWFAWDLPeerContext MACAddress];
-[CWFAWDLPeerContext setInterfaceName:];
-[CWFAWDLPeerContext interfaceName];
-[CWFAWDLPeerContext encodeWithCoder:];
-[CWFAWDLPeerContext hash];
-[CWFAWDLPeerContext description];
-[CWFAWDLPeerContext initWithCoder:];
-[CWFAWDLPeerContext copyWithZone:];
-[CWFAWDLPeerContext isEqual:];
-[CWFAWDLPeerContext isEqualToAWDLPeerContext:];
-[CWFAWDLPeerContext setMACAddress:];
```
