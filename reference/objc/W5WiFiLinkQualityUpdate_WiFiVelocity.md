# `W5WiFiLinkQualityUpdate`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
f _cca;
q _rssi;
q _txRate;
d _timestamp;
```

## Properties

```
@property (Tq,N,V_rssi) rssi;
@property (Tq,N,V_txRate) txRate;
@property (Tf,N,V_cca) cca;
@property (Td,N,V_timestamp) timestamp;
```

## Class methods

```
+[W5WiFiLinkQualityUpdate supportsSecureCoding];
```

## Instance methods

```
-[W5WiFiLinkQualityUpdate rssi];
-[W5WiFiLinkQualityUpdate cca];
-[W5WiFiLinkQualityUpdate txRate];
-[W5WiFiLinkQualityUpdate setTimestamp:];
-[W5WiFiLinkQualityUpdate setTxRate:];
-[W5WiFiLinkQualityUpdate setCca:];
-[W5WiFiLinkQualityUpdate timestamp];
-[W5WiFiLinkQualityUpdate setRssi:];
-[W5WiFiLinkQualityUpdate encodeWithCoder:];
-[W5WiFiLinkQualityUpdate conformsToProtocol:];
-[W5WiFiLinkQualityUpdate description];
-[W5WiFiLinkQualityUpdate initWithCoder:];
-[W5WiFiLinkQualityUpdate copyWithZone:];
```
