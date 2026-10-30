# `CWFDevice`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSString" _deviceRapportEffectiveIdentifier;
@"NSString" _macAddress;
@"NSString" _ipAddress;
@"NSString" _deviceName;
@"NSString" _productType;
@"NSString" _productColor;
@"NSString" _productMarketingName;
@"NSString" _model;
Q _retryCount;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceRapportEffectiveIdentifier) deviceRapportEffectiveIdentifier;
@property (T@"NSString",C,N,V_macAddress) macAddress;
@property (T@"NSString",C,N,V_ipAddress) ipAddress;
@property (T@"NSString",C,N,V_deviceName) deviceName;
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_productMarketingName) productMarketingName;
@property (T@"NSString",C,N,V_productType) productType;
@property (T@"NSString",C,N,V_productColor) productColor;
@property (TQ,N,V_retryCount) retryCount;
```

## Instance methods

```
-[CWFDevice model];
-[CWFDevice setModel:];
-[CWFDevice productColor];
-[CWFDevice macAddress];
-[CWFDevice userInfo];
-[CWFDevice setMacAddress:];
-[CWFDevice productType];
-[CWFDevice setProductType:];
-[CWFDevice setDeviceName:];
-[CWFDevice setRetryCount:];
-[CWFDevice ipAddress];
-[CWFDevice hash];
-[CWFDevice setIpAddress:];
-[CWFDevice isEqual:];
-[CWFDevice deviceName];
-[CWFDevice retryCount];
-[CWFDevice setProductColor:];
-[CWFDevice initWithUserInfo:];
-[CWFDevice deviceRapportEffectiveIdentifier];
-[CWFDevice hasFetchedDeviceInfo];
-[CWFDevice initWithRapportDevice:];
-[CWFDevice productMarketingName];
-[CWFDevice setDeviceRapportEffectiveIdentifier:];
-[CWFDevice setProductMarketingName:];
```
