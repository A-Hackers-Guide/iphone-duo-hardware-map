# `WiFiAwarePeerDevice`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
C _instanceID;
@"WiFiMACAddress" _macAddress;
```

## Properties

```
@property (TC,N,V_instanceID) instanceID;
@property (T@"WiFiMACAddress",&,N,V_macAddress) macAddress;
```

## Class methods

```
+[WiFiAwarePeerDevice supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePeerDevice macAddress];
-[WiFiAwarePeerDevice setMacAddress:];
-[WiFiAwarePeerDevice encodeWithCoder:];
-[WiFiAwarePeerDevice instanceID];
-[WiFiAwarePeerDevice description];
-[WiFiAwarePeerDevice initWithCoder:];
-[WiFiAwarePeerDevice setInstanceID:];
-[WiFiAwarePeerDevice initWithInstanceID:macAddress:];
```
