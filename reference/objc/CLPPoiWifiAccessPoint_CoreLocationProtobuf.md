# `CLPPoiWifiAccessPoint`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 7 properties, 23 instance methods, 0 class methods

## Instance variables

```
d _age;
d _scanTimestamp;
i _channel;
@"NSString" _mac;
i _rssi;
{?="age"b1"scanTimestamp"b1} _has;
```

## Properties

```
@property (T@"NSString",&,N,V_mac) mac;
@property (Ti,N,V_rssi) rssi;
@property (Ti,N,V_channel) channel;
@property (TB,N) hasAge;
@property (Td,N,V_age) age;
@property (TB,N) hasScanTimestamp;
@property (Td,N,V_scanTimestamp) scanTimestamp;
```

## Instance methods

```
-[CLPPoiWifiAccessPoint rssi];
-[CLPPoiWifiAccessPoint setChannel:];
-[CLPPoiWifiAccessPoint channel];
-[CLPPoiWifiAccessPoint writeTo:];
-[CLPPoiWifiAccessPoint mergeFrom:];
-[CLPPoiWifiAccessPoint age];
-[CLPPoiWifiAccessPoint setRssi:];
-[CLPPoiWifiAccessPoint hash];
-[CLPPoiWifiAccessPoint copyTo:];
-[CLPPoiWifiAccessPoint description];
-[CLPPoiWifiAccessPoint readFrom:];
-[CLPPoiWifiAccessPoint copyWithZone:];
-[CLPPoiWifiAccessPoint isEqual:];
-[CLPPoiWifiAccessPoint dictionaryRepresentation];
-[CLPPoiWifiAccessPoint setAge:];
-[CLPPoiWifiAccessPoint hasAge];
-[CLPPoiWifiAccessPoint setHasAge:];
-[CLPPoiWifiAccessPoint hasScanTimestamp];
-[CLPPoiWifiAccessPoint scanTimestamp];
-[CLPPoiWifiAccessPoint setHasScanTimestamp:];
-[CLPPoiWifiAccessPoint setScanTimestamp:];
-[CLPPoiWifiAccessPoint setMac:];
-[CLPPoiWifiAccessPoint mac];
```
