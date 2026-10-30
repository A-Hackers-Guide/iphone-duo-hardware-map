# `CTPNRContextInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _isReady;
@"NSString" _plmn;
@"NSString" _imsi;
@"NSString" _phoneNumber;
@"NSString" _phoneNumberOnSIM;
```

## Properties

```
@property (TB,N,V_isReady) isReady;
@property (T@"NSString",&,N,V_plmn) plmn;
@property (T@"NSString",&,N,V_imsi) imsi;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",&,N,V_phoneNumberOnSIM) phoneNumberOnSIM;
```

## Class methods

```
+[CTPNRContextInfo supportsSecureCoding];
```

## Instance methods

```
-[CTPNRContextInfo phoneNumber];
-[CTPNRContextInfo isReady];
-[CTPNRContextInfo init];
-[CTPNRContextInfo phoneNumberOnSIM];
-[CTPNRContextInfo setIsReady:];
-[CTPNRContextInfo setPhoneNumber:];
-[CTPNRContextInfo setPlmn:];
-[CTPNRContextInfo imsi];
-[CTPNRContextInfo encodeWithCoder:];
-[CTPNRContextInfo setPhoneNumberOnSIM:];
-[CTPNRContextInfo description];
-[CTPNRContextInfo isEqualToPNRContextInfo:];
-[CTPNRContextInfo initWithCoder:];
-[CTPNRContextInfo setImsi:];
-[CTPNRContextInfo copyWithZone:];
-[CTPNRContextInfo isEqual:];
-[CTPNRContextInfo plmn];
```
