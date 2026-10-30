# `CTSatelliteMessagingProvisioningReceipt`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _cfg_id;
@"NSError" _result;
@"NSString" _sps_environment;
```

## Properties

```
@property (T@"NSUUID",&,N,V_cfg_id) cfg_id;
@property (T@"NSError",&,N,V_result) result;
@property (T@"NSString",&,N,V_sps_environment) sps_environment;
```

## Class methods

```
+[CTSatelliteMessagingProvisioningReceipt supportsSecureCoding];
```

## Instance methods

```
-[CTSatelliteMessagingProvisioningReceipt setResult:];
-[CTSatelliteMessagingProvisioningReceipt cfg_id];
-[CTSatelliteMessagingProvisioningReceipt result];
-[CTSatelliteMessagingProvisioningReceipt encodeWithCoder:];
-[CTSatelliteMessagingProvisioningReceipt description];
-[CTSatelliteMessagingProvisioningReceipt initWithCoder:];
-[CTSatelliteMessagingProvisioningReceipt sps_environment];
-[CTSatelliteMessagingProvisioningReceipt copyWithZone:];
-[CTSatelliteMessagingProvisioningReceipt setSps_environment:];
-[CTSatelliteMessagingProvisioningReceipt setCfg_id:];
-[CTSatelliteMessagingProvisioningReceipt initWithID:result:sps:];
```
