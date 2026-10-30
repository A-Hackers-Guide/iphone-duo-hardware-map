# `CWFNearbyDeviceDiscoveryFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSString" _receiverMacAddress;
@"NSString" _transmitterMacAddress;
@"NSString" _bssid;
q _numReports;
q _frameType;
```

## Properties

```
@property (T@"NSString",C,N,V_receiverMacAddress) receiverMacAddress;
@property (T@"NSString",C,N,V_transmitterMacAddress) transmitterMacAddress;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (Tq,N,V_numReports) numReports;
@property (Tq,N,V_frameType) frameType;
```

## Class methods

```
+[CWFNearbyDeviceDiscoveryFilter supportsSecureCoding];
```

## Instance methods

```
-[CWFNearbyDeviceDiscoveryFilter init];
-[CWFNearbyDeviceDiscoveryFilter setBssid:];
-[CWFNearbyDeviceDiscoveryFilter encodeWithCoder:];
-[CWFNearbyDeviceDiscoveryFilter hash];
-[CWFNearbyDeviceDiscoveryFilter description];
-[CWFNearbyDeviceDiscoveryFilter bssid];
-[CWFNearbyDeviceDiscoveryFilter initWithCoder:];
-[CWFNearbyDeviceDiscoveryFilter copyWithZone:];
-[CWFNearbyDeviceDiscoveryFilter isEqual:];
-[CWFNearbyDeviceDiscoveryFilter frameType];
-[CWFNearbyDeviceDiscoveryFilter isEqualToNDDFilter:];
-[CWFNearbyDeviceDiscoveryFilter numReports];
-[CWFNearbyDeviceDiscoveryFilter receiverMacAddress];
-[CWFNearbyDeviceDiscoveryFilter setFrameType:];
-[CWFNearbyDeviceDiscoveryFilter setNumReports:];
-[CWFNearbyDeviceDiscoveryFilter setReceiverMacAddress:];
-[CWFNearbyDeviceDiscoveryFilter setTransmitterMacAddress:];
-[CWFNearbyDeviceDiscoveryFilter transmitterMacAddress];
```
