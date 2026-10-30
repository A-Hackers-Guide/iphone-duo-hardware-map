# `CTRoadsideProvider`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _supportsPayPerUse;
B _isActive;
B _isCarrierProvider;
q _providerId;
@"NSString" _providerName;
@"NSString" _bizId;
@"NSArray" _associatedPhoneNumbers;
```

## Properties

```
@property (Tq,N,V_providerId) providerId;
@property (T@"NSString",&,N,V_providerName) providerName;
@property (T@"NSString",&,N,V_bizId) bizId;
@property (TB,N,V_supportsPayPerUse) supportsPayPerUse;
@property (TB,N,V_isActive) isActive;
@property (TB,N,V_isCarrierProvider) isCarrierProvider;
@property (T@"NSArray",&,N,V_associatedPhoneNumbers) associatedPhoneNumbers;
```

## Class methods

```
+[CTRoadsideProvider supportsSecureCoding];
```

## Instance methods

```
-[CTRoadsideProvider setIsActive:];
-[CTRoadsideProvider encodeWithCoder:];
-[CTRoadsideProvider description];
-[CTRoadsideProvider providerName];
-[CTRoadsideProvider initWithCoder:];
-[CTRoadsideProvider isActive];
-[CTRoadsideProvider copyWithZone:];
-[CTRoadsideProvider isEqual:];
-[CTRoadsideProvider isEqualToProvider:];
-[CTRoadsideProvider providerId];
-[CTRoadsideProvider setProviderId:];
-[CTRoadsideProvider associatedPhoneNumbers];
-[CTRoadsideProvider bizId];
-[CTRoadsideProvider isCarrierProvider];
-[CTRoadsideProvider setAssociatedPhoneNumbers:];
-[CTRoadsideProvider setBizId:];
-[CTRoadsideProvider setIsCarrierProvider:];
-[CTRoadsideProvider setProviderName:];
-[CTRoadsideProvider setSupportsPayPerUse:];
-[CTRoadsideProvider supportsPayPerUse];
```
