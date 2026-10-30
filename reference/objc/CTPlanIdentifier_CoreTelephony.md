# `CTPlanIdentifier`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _iccid;
@"NSString" _carrierName;
@"NSString" _spn;
@"NSString" _phoneNumber;
@"NSString" _countryCode;
@"NSString" _label;
@"NSString" _mcc;
@"NSString" _mnc;
@"NSString" _gid1;
@"NSString" _gid2;
```

## Properties

```
@property (T@"NSString",&,N,V_iccid) iccid;
@property (T@"NSString",&,N,V_carrierName) carrierName;
@property (T@"NSString",&,N,V_spn) spn;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",&,N,V_countryCode) countryCode;
@property (T@"NSString",&,N,V_label) label;
@property (T@"NSString",&,N,V_mcc) mcc;
@property (T@"NSString",&,N,V_mnc) mnc;
@property (T@"NSString",&,N,V_gid1) gid1;
@property (T@"NSString",&,N,V_gid2) gid2;
```

## Class methods

```
+[CTPlanIdentifier supportsSecureCoding];
```

## Instance methods

```
-[CTPlanIdentifier phoneNumber];
-[CTPlanIdentifier carrierName];
-[CTPlanIdentifier setCarrierName:];
-[CTPlanIdentifier label];
-[CTPlanIdentifier setLabel:];
-[CTPlanIdentifier setPhoneNumber:];
-[CTPlanIdentifier iccid];
-[CTPlanIdentifier mnc];
-[CTPlanIdentifier countryCode];
-[CTPlanIdentifier encodeWithCoder:];
-[CTPlanIdentifier description];
-[CTPlanIdentifier initWithCoder:];
-[CTPlanIdentifier setMnc:];
-[CTPlanIdentifier mcc];
-[CTPlanIdentifier setIccid:];
-[CTPlanIdentifier isEqual:];
-[CTPlanIdentifier setCountryCode:];
-[CTPlanIdentifier setMcc:];
-[CTPlanIdentifier spn];
-[CTPlanIdentifier setSpn:];
-[CTPlanIdentifier gid1];
-[CTPlanIdentifier gid2];
-[CTPlanIdentifier initWithIccid:carrierName:phoneNumber:countryCode:label:mcc:mnc:gid1:gid2:];
-[CTPlanIdentifier setGid1:];
-[CTPlanIdentifier setGid2:];
```
