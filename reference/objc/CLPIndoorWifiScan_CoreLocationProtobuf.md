# `CLPIndoorWifiScan`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`](../userland/System__Library__PrivateFrameworks__CoreLocationProtobuf.framework__CoreLocationProtobuf.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 12 instance variables, 18 properties, 52 instance methods, 0 class methods

## Instance variables

```
d _age;
d _timestamp;
@"NSString" _bundleId;
i _channel;
i _hidden;
@"NSString" _mac;
i _rssi;
i _scanActivity;
i _scanCacheSource;
i _scanType;
i _wifiFrequencyBand;
{?="age"b1"hidden"b1"scanActivity"b1"scanCacheSource"b1"scanType"b1"wifiFrequencyBand"b1} _has;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (T@"NSString",&,N,V_mac) mac;
@property (Ti,N,V_channel) channel;
@property (TB,N) hasHidden;
@property (Ti,N,V_hidden) hidden;
@property (Ti,N,V_rssi) rssi;
@property (TB,N) hasAge;
@property (Td,N,V_age) age;
@property (TB,R,N) hasBundleId;
@property (T@"NSString",&,N,V_bundleId) bundleId;
@property (TB,N) hasScanType;
@property (Ti,N,V_scanType) scanType;
@property (TB,N) hasScanCacheSource;
@property (Ti,N,V_scanCacheSource) scanCacheSource;
@property (TB,N) hasWifiFrequencyBand;
@property (Ti,N,V_wifiFrequencyBand) wifiFrequencyBand;
@property (TB,N) hasScanActivity;
@property (Ti,N,V_scanActivity) scanActivity;
```

## Instance methods

```
-[CLPIndoorWifiScan rssi];
-[CLPIndoorWifiScan setChannel:];
-[CLPIndoorWifiScan channel];
-[CLPIndoorWifiScan setTimestamp:];
-[CLPIndoorWifiScan writeTo:];
-[CLPIndoorWifiScan hasBundleId];
-[CLPIndoorWifiScan setHidden:];
-[CLPIndoorWifiScan mergeFrom:];
-[CLPIndoorWifiScan age];
-[CLPIndoorWifiScan timestamp];
-[CLPIndoorWifiScan setRssi:];
-[CLPIndoorWifiScan setBundleId:];
-[CLPIndoorWifiScan hasScanActivity];
-[CLPIndoorWifiScan scanType];
-[CLPIndoorWifiScan bundleId];
-[CLPIndoorWifiScan hash];
-[CLPIndoorWifiScan copyTo:];
-[CLPIndoorWifiScan description];
-[CLPIndoorWifiScan setScanType:];
-[CLPIndoorWifiScan readFrom:];
-[CLPIndoorWifiScan copyWithZone:];
-[CLPIndoorWifiScan scanActivity];
-[CLPIndoorWifiScan setScanActivity:];
-[CLPIndoorWifiScan isEqual:];
-[CLPIndoorWifiScan dictionaryRepresentation];
-[CLPIndoorWifiScan hidden];
-[CLPIndoorWifiScan setAge:];
-[CLPIndoorWifiScan hasAge];
-[CLPIndoorWifiScan setHasAge:];
-[CLPIndoorWifiScan setMac:];
-[CLPIndoorWifiScan mac];
-[CLPIndoorWifiScan hasHidden];
-[CLPIndoorWifiScan setHasHidden:];
-[CLPIndoorWifiScan StringAsScanActivity:];
-[CLPIndoorWifiScan StringAsScanType:];
-[CLPIndoorWifiScan StringAsWifiFrequencyBand:];
-[CLPIndoorWifiScan setHasScanType:];
-[CLPIndoorWifiScan StringAsScanCacheSource:];
-[CLPIndoorWifiScan scanCacheSource];
-[CLPIndoorWifiScan hasScanCacheSource];
-[CLPIndoorWifiScan hasScanType];
-[CLPIndoorWifiScan hasWifiFrequencyBand];
-[CLPIndoorWifiScan scanActivityAsString:];
-[CLPIndoorWifiScan scanCacheSourceAsString:];
-[CLPIndoorWifiScan scanTypeAsString:];
-[CLPIndoorWifiScan setHasScanActivity:];
-[CLPIndoorWifiScan setHasScanCacheSource:];
-[CLPIndoorWifiScan setHasWifiFrequencyBand:];
-[CLPIndoorWifiScan setScanCacheSource:];
-[CLPIndoorWifiScan setWifiFrequencyBand:];
-[CLPIndoorWifiScan wifiFrequencyBand];
-[CLPIndoorWifiScan wifiFrequencyBandAsString:];
```
