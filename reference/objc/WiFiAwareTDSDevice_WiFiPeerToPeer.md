# `WiFiAwareTDSDevice`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _identifier;
@"NSData" _bluetoothAddress;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSData",R,N,V_bluetoothAddress) bluetoothAddress;
```

## Class methods

```
+[WiFiAwareTDSDevice supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareTDSDevice identifier];
-[WiFiAwareTDSDevice bluetoothAddress];
-[WiFiAwareTDSDevice encodeWithCoder:];
-[WiFiAwareTDSDevice description];
-[WiFiAwareTDSDevice initWithCoder:];
-[WiFiAwareTDSDevice copyWithZone:];
-[WiFiAwareTDSDevice name];
-[WiFiAwareTDSDevice initWithName:identifier:bluetoothAddress:];
```
