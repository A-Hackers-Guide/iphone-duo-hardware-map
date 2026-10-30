# `WiFiAwarePairedDeviceInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
Q _deviceID;
@"NSString" _name;
@"NSString" _pairingName;
@"NSString" _vendorName;
@"NSString" _modelName;
@"NSDictionary" _attributes;
```

## Properties

```
@property (TQ,N,V_deviceID) deviceID;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSString",R,C,N,V_pairingName) pairingName;
@property (T@"NSString",R,C,N,V_vendorName) vendorName;
@property (T@"NSString",R,C,N,V_modelName) modelName;
@property (T@"NSDictionary",R,C,N,V_attributes) attributes;
```

## Class methods

```
+[WiFiAwarePairedDeviceInfo supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePairedDeviceInfo vendorName];
-[WiFiAwarePairedDeviceInfo deviceID];
-[WiFiAwarePairedDeviceInfo setDeviceID:];
-[WiFiAwarePairedDeviceInfo encodeWithCoder:];
-[WiFiAwarePairedDeviceInfo description];
-[WiFiAwarePairedDeviceInfo setName:];
-[WiFiAwarePairedDeviceInfo initWithCoder:];
-[WiFiAwarePairedDeviceInfo attributes];
-[WiFiAwarePairedDeviceInfo name];
-[WiFiAwarePairedDeviceInfo modelName];
-[WiFiAwarePairedDeviceInfo pairingName];
-[WiFiAwarePairedDeviceInfo initWithName:pairingName:vendorName:modelName:attributes:];
-[WiFiAwarePairedDeviceInfo initWithName:vendorID:modelName:attributes:];
```
