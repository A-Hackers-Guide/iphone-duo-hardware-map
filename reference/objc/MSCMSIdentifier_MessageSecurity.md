# `MSCMSIdentifier`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
i _type;
^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}} _issuerAndSerialNumber;
^{heim_base_data=Q^v} _subjectKeyId;
@"NSData" _skidData;
@"NSData" _serialNumberData;
@"NSData" _issuerNameData;
```

## Properties

```
@property (Ti,V_type) type;
@property (T^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}},V_issuerAndSerialNumber) issuerAndSerialNumber;
@property (T^{heim_base_data=Q^v},V_subjectKeyId) subjectKeyId;
@property (T@"NSData",&,V_skidData) skidData;
@property (T@"NSData",&,V_serialNumberData) serialNumberData;
@property (T@"NSData",&,V_issuerNameData) issuerNameData;
```

## Class methods

```
+[MSCMSIdentifier decodeIdentifier:error:];
```

## Instance methods

```
-[MSCMSIdentifier setSkidData:];
-[MSCMSIdentifier encodeMessageSecurityObject:];
-[MSCMSIdentifier initWithSkid:];
-[MSCMSIdentifier initWithIssuerName:serialNumber:];
-[MSCMSIdentifier setSubjectKeyId:];
-[MSCMSIdentifier dealloc];
-[MSCMSIdentifier setIssuerAndSerialNumber:];
-[MSCMSIdentifier issuerNameData];
-[MSCMSIdentifier issuerAndSerialNumber];
-[MSCMSIdentifier serialNumberData];
-[MSCMSIdentifier subjectKeyId];
-[MSCMSIdentifier setType:];
-[MSCMSIdentifier type];
-[MSCMSIdentifier initWithIssuerName:serialNumber:negativeNumber:];
-[MSCMSIdentifier setSerialNumberData:];
-[MSCMSIdentifier setIssuerNameData:];
-[MSCMSIdentifier skidData];
```
