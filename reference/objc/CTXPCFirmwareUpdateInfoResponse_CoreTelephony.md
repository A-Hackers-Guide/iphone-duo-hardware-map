# `CTXPCFirmwareUpdateInfoResponse`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCResponseMessage`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _firmwareInfo;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_firmwareInfo) firmwareInfo;
```

## Class methods

```
+[CTXPCFirmwareUpdateInfoResponse supportsSecureCoding];
```

## Instance methods

```
-[CTXPCFirmwareUpdateInfoResponse ct_shortName];
-[CTXPCFirmwareUpdateInfoResponse encodeWithCoder:];
-[CTXPCFirmwareUpdateInfoResponse initWithCoder:];
-[CTXPCFirmwareUpdateInfoResponse firmwareInfo];
-[CTXPCFirmwareUpdateInfoResponse initWithFimwareUpdateInfo:];
-[CTXPCFirmwareUpdateInfoResponse setFirmwareInfo:];
```
