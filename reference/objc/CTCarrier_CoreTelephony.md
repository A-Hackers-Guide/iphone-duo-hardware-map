# `CTCarrier`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _carrierName;
@"NSString" _mobileCountryCode;
@"NSString" _mobileNetworkCode;
@"NSString" _isoCountryCode;
B _allowsVOIP;
```

## Properties

```
@property (T@"NSString",&,N,V_carrierName) carrierName;
@property (T@"NSString",&,N,V_mobileCountryCode) mobileCountryCode;
@property (T@"NSString",&,N,V_mobileNetworkCode) mobileNetworkCode;
@property (T@"NSString",&,N,V_isoCountryCode) isoCountryCode;
@property (TB,N,V_allowsVOIP) allowsVOIP;
```

## Instance methods

```
-[CTCarrier isoCountryCode];
-[CTCarrier setIsoCountryCode:];
-[CTCarrier carrierName];
-[CTCarrier setCarrierName:];
-[CTCarrier init];
-[CTCarrier description];
-[CTCarrier isEqual:];
-[CTCarrier mobileCountryCode];
-[CTCarrier mobileNetworkCode];
-[CTCarrier allowsVOIP];
-[CTCarrier setAllowsVOIP:];
-[CTCarrier setMobileCountryCode:];
-[CTCarrier setMobileNetworkCode:];
```
