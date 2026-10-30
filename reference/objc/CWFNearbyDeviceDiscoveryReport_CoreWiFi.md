# `CWFNearbyDeviceDiscoveryReport`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 11 instance variables, 11 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _isLowConfidence;
@"NSDate" _timeStamp;
@"NSString" _receiver;
@"NSString" _transmitter;
@"NSString" _bssid;
@"NSArray" _rssi;
q _frameType;
q _bandwidth;
q _channel;
q _band;
q _rateMbps;
```

## Properties

```
@property (T@"NSDate",C,N,V_timeStamp) timeStamp;
@property (T@"NSString",C,N,V_receiver) receiver;
@property (T@"NSString",C,N,V_transmitter) transmitter;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (T@"NSArray",C,N,V_rssi) rssi;
@property (Tq,N,V_frameType) frameType;
@property (Tq,N,V_bandwidth) bandwidth;
@property (Tq,N,V_channel) channel;
@property (Tq,N,V_band) band;
@property (Tq,N,V_rateMbps) rateMbps;
@property (TB,N,V_isLowConfidence) isLowConfidence;
```

## Class methods

```
+[CWFNearbyDeviceDiscoveryReport supportsSecureCoding];
```

## Instance methods

```
-[CWFNearbyDeviceDiscoveryReport rssi];
-[CWFNearbyDeviceDiscoveryReport setChannel:];
-[CWFNearbyDeviceDiscoveryReport channel];
-[CWFNearbyDeviceDiscoveryReport setReceiver:];
-[CWFNearbyDeviceDiscoveryReport init];
-[CWFNearbyDeviceDiscoveryReport setRssi:];
-[CWFNearbyDeviceDiscoveryReport band];
-[CWFNearbyDeviceDiscoveryReport setBssid:];
-[CWFNearbyDeviceDiscoveryReport setBand:];
-[CWFNearbyDeviceDiscoveryReport encodeWithCoder:];
-[CWFNearbyDeviceDiscoveryReport receiver];
-[CWFNearbyDeviceDiscoveryReport setBandwidth:];
-[CWFNearbyDeviceDiscoveryReport hash];
-[CWFNearbyDeviceDiscoveryReport description];
-[CWFNearbyDeviceDiscoveryReport bssid];
-[CWFNearbyDeviceDiscoveryReport initWithCoder:];
-[CWFNearbyDeviceDiscoveryReport bandwidth];
-[CWFNearbyDeviceDiscoveryReport copyWithZone:];
-[CWFNearbyDeviceDiscoveryReport isEqual:];
-[CWFNearbyDeviceDiscoveryReport isLowConfidence];
-[CWFNearbyDeviceDiscoveryReport setTimeStamp:];
-[CWFNearbyDeviceDiscoveryReport timeStamp];
-[CWFNearbyDeviceDiscoveryReport setIsLowConfidence:];
-[CWFNearbyDeviceDiscoveryReport frameType];
-[CWFNearbyDeviceDiscoveryReport setTransmitter:];
-[CWFNearbyDeviceDiscoveryReport isEqualToNDDReport:];
-[CWFNearbyDeviceDiscoveryReport rateMbps];
-[CWFNearbyDeviceDiscoveryReport setFrameType:];
-[CWFNearbyDeviceDiscoveryReport setRateMbps:];
-[CWFNearbyDeviceDiscoveryReport transmitter];
```
