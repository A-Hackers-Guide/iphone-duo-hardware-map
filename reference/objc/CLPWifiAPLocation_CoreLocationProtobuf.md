# `CLPWifiAPLocation`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 14 properties, 38 instance methods, 0 class methods

## Instance variables

```
d _scanTimestamp;
@"NSString" _appBundleId;
i _channel;
i _hidden;
@"CLPLocation" _location;
@"NSString" _mac;
i _rssi;
i _scanType;
i _serverHash;
{?="scanTimestamp"b1"hidden"b1"scanType"b1"serverHash"b1} _has;
```

## Properties

```
@property (T@"NSString",&,N,V_mac) mac;
@property (Ti,N,V_channel) channel;
@property (TB,N) hasHidden;
@property (Ti,N,V_hidden) hidden;
@property (Ti,N,V_rssi) rssi;
@property (TB,N) hasScanTimestamp;
@property (Td,N,V_scanTimestamp) scanTimestamp;
@property (T@"CLPLocation",&,N,V_location) location;
@property (TB,R,N) hasAppBundleId;
@property (T@"NSString",&,N,V_appBundleId) appBundleId;
@property (TB,N) hasServerHash;
@property (Ti,N,V_serverHash) serverHash;
@property (TB,N) hasScanType;
@property (Ti,N,V_scanType) scanType;
```

## Instance methods

```
-[CLPWifiAPLocation rssi];
-[CLPWifiAPLocation setChannel:];
-[CLPWifiAPLocation channel];
-[CLPWifiAPLocation appBundleId];
-[CLPWifiAPLocation writeTo:];
-[CLPWifiAPLocation setHidden:];
-[CLPWifiAPLocation setAppBundleId:];
-[CLPWifiAPLocation location];
-[CLPWifiAPLocation mergeFrom:];
-[CLPWifiAPLocation hasAppBundleId];
-[CLPWifiAPLocation setServerHash:];
-[CLPWifiAPLocation setRssi:];
-[CLPWifiAPLocation serverHash];
-[CLPWifiAPLocation setHasServerHash:];
-[CLPWifiAPLocation scanType];
-[CLPWifiAPLocation hasServerHash];
-[CLPWifiAPLocation setLocation:];
-[CLPWifiAPLocation hash];
-[CLPWifiAPLocation copyTo:];
-[CLPWifiAPLocation description];
-[CLPWifiAPLocation setScanType:];
-[CLPWifiAPLocation readFrom:];
-[CLPWifiAPLocation copyWithZone:];
-[CLPWifiAPLocation isEqual:];
-[CLPWifiAPLocation dictionaryRepresentation];
-[CLPWifiAPLocation hidden];
-[CLPWifiAPLocation hasScanTimestamp];
-[CLPWifiAPLocation scanTimestamp];
-[CLPWifiAPLocation setHasScanTimestamp:];
-[CLPWifiAPLocation setScanTimestamp:];
-[CLPWifiAPLocation setMac:];
-[CLPWifiAPLocation mac];
-[CLPWifiAPLocation hasHidden];
-[CLPWifiAPLocation setHasHidden:];
-[CLPWifiAPLocation StringAsScanType:];
-[CLPWifiAPLocation setHasScanType:];
-[CLPWifiAPLocation hasScanType];
-[CLPWifiAPLocation scanTypeAsString:];
```
