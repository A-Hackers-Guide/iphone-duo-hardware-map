# `CTTrafficDescriptor`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 12 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleId;
@"NSString" _appCategory;
@"NSString" _accountId;
@"NSString" _host;
@"NSString" _address;
@"NSNumber" _llphs;
@"NSNumber" _port;
@"NSNumber" _portRangeLow;
@"NSNumber" _portRangeUpper;
@"NSNumber" _ipProtocol;
@"NSNumber" _trafficClass;
@"NSString" _dnn;
```

## Properties

```
@property (T@"NSString",&,N,V_bundleId) bundleId;
@property (T@"NSString",&,N,V_appCategory) appCategory;
@property (T@"NSString",&,N,V_accountId) accountId;
@property (T@"NSString",&,N,V_host) host;
@property (T@"NSString",&,N,V_address) address;
@property (T@"NSNumber",&,N,V_llphs) llphs;
@property (T@"NSNumber",&,N,V_port) port;
@property (T@"NSNumber",&,N,V_portRangeLow) portRangeLow;
@property (T@"NSNumber",&,N,V_portRangeUpper) portRangeUpper;
@property (T@"NSNumber",&,N,V_ipProtocol) ipProtocol;
@property (T@"NSNumber",&,N,V_trafficClass) trafficClass;
@property (T@"NSString",&,N,V_dnn) dnn;
```

## Class methods

```
+[CTTrafficDescriptor supportsSecureCoding];
```

## Instance methods

```
-[CTTrafficDescriptor setHost:];
-[CTTrafficDescriptor setPort:];
-[CTTrafficDescriptor trafficClass];
-[CTTrafficDescriptor address];
-[CTTrafficDescriptor ipProtocol];
-[CTTrafficDescriptor setAddress:];
-[CTTrafficDescriptor accountId];
-[CTTrafficDescriptor setBundleId:];
-[CTTrafficDescriptor port];
-[CTTrafficDescriptor setTrafficClass:];
-[CTTrafficDescriptor bundleId];
-[CTTrafficDescriptor setAccountId:];
-[CTTrafficDescriptor encodeWithCoder:];
-[CTTrafficDescriptor description];
-[CTTrafficDescriptor initWithCoder:];
-[CTTrafficDescriptor copyWithZone:];
-[CTTrafficDescriptor host];
-[CTTrafficDescriptor dnn];
-[CTTrafficDescriptor setAppCategory:];
-[CTTrafficDescriptor setDnn:];
-[CTTrafficDescriptor appCategory];
-[CTTrafficDescriptor llphs];
-[CTTrafficDescriptor portRangeLow];
-[CTTrafficDescriptor portRangeUpper];
-[CTTrafficDescriptor setIpProtocol:];
-[CTTrafficDescriptor setLlphs:];
-[CTTrafficDescriptor setPortRangeLow:];
-[CTTrafficDescriptor setPortRangeUpper:];
```
