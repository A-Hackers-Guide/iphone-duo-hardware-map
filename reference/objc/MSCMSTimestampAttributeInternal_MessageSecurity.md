# `MSCMSTimestampAttributeInternal`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"MSOID" attributeType;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 tstinfo;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 signedData;
```

## Properties

```
@property (T@"MSOID",N,&,VattributeType) attributeType;
```

## Instance methods

```
-[MSCMSTimestampAttributeInternal init];
-[MSCMSTimestampAttributeInternal setAttributeType:];
-[MSCMSTimestampAttributeInternal attributeType];
-[MSCMSTimestampAttributeInternal dealloc];
-[MSCMSTimestampAttributeInternal initWithAttribute:error:];
-[MSCMSTimestampAttributeInternal encodeAttributeWithError:];
-[MSCMSTimestampAttributeInternal initWithTimestampToken:error:];
-[MSCMSTimestampAttributeInternal timestampToken];
-[MSCMSTimestampAttributeInternal verifyTimestamp:error:];
```
