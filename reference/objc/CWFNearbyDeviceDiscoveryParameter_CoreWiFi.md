# `CWFNearbyDeviceDiscoveryParameter`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _filters;
q _channel;
q _band;
q _bandwidth;
q _type;
q _operation;
```

## Properties

```
@property (T@"NSArray",C,N,V_filters) filters;
@property (Tq,N,V_channel) channel;
@property (Tq,N,V_band) band;
@property (Tq,N,V_bandwidth) bandwidth;
@property (Tq,N,V_type) type;
@property (Tq,N,V_operation) operation;
```

## Class methods

```
+[CWFNearbyDeviceDiscoveryParameter supportsSecureCoding];
```

## Instance methods

```
-[CWFNearbyDeviceDiscoveryParameter setChannel:];
-[CWFNearbyDeviceDiscoveryParameter channel];
-[CWFNearbyDeviceDiscoveryParameter setOperation:];
-[CWFNearbyDeviceDiscoveryParameter operation];
-[CWFNearbyDeviceDiscoveryParameter init];
-[CWFNearbyDeviceDiscoveryParameter setFilters:];
-[CWFNearbyDeviceDiscoveryParameter band];
-[CWFNearbyDeviceDiscoveryParameter filters];
-[CWFNearbyDeviceDiscoveryParameter setType:];
-[CWFNearbyDeviceDiscoveryParameter type];
-[CWFNearbyDeviceDiscoveryParameter setBand:];
-[CWFNearbyDeviceDiscoveryParameter encodeWithCoder:];
-[CWFNearbyDeviceDiscoveryParameter setBandwidth:];
-[CWFNearbyDeviceDiscoveryParameter hash];
-[CWFNearbyDeviceDiscoveryParameter description];
-[CWFNearbyDeviceDiscoveryParameter initWithCoder:];
-[CWFNearbyDeviceDiscoveryParameter bandwidth];
-[CWFNearbyDeviceDiscoveryParameter copyWithZone:];
-[CWFNearbyDeviceDiscoveryParameter isEqual:];
-[CWFNearbyDeviceDiscoveryParameter isEqualToNDDParameters:];
```
