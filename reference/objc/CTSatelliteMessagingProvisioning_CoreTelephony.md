# `CTSatelliteMessagingProvisioning`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _cfg_id;
@"NSData" _cfg;
@"NSString" _sps_environment;
```

## Properties

```
@property (T@"NSUUID",&,N,V_cfg_id) cfg_id;
@property (T@"NSData",&,N,V_cfg) cfg;
@property (T@"NSString",&,N,V_sps_environment) sps_environment;
```

## Class methods

```
+[CTSatelliteMessagingProvisioning supportsSecureCoding];
```

## Instance methods

```
-[CTSatelliteMessagingProvisioning cfg_id];
-[CTSatelliteMessagingProvisioning cfg];
-[CTSatelliteMessagingProvisioning initWithID:data:sps:];
-[CTSatelliteMessagingProvisioning encodeWithCoder:];
-[CTSatelliteMessagingProvisioning description];
-[CTSatelliteMessagingProvisioning initWithCoder:];
-[CTSatelliteMessagingProvisioning sps_environment];
-[CTSatelliteMessagingProvisioning setCfg:];
-[CTSatelliteMessagingProvisioning copyWithZone:];
-[CTSatelliteMessagingProvisioning setSps_environment:];
-[CTSatelliteMessagingProvisioning setCfg_id:];
```
