# `MSCMSMessageDigestAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 1 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSData" _messageDigest;
```

## Properties

```
@property (T@"NSData",&,V_messageDigest) messageDigest;
@property (T@"MSOID",R,&) attributeType;
```

## Class methods

```
+[MSCMSMessageDigestAttribute messageDigestAttributeWithDigest:];
```

## Instance methods

```
-[MSCMSMessageDigestAttribute attributeType];
-[MSCMSMessageDigestAttribute initWithAttribute:error:];
-[MSCMSMessageDigestAttribute initWithDigest:];
-[MSCMSMessageDigestAttribute encodeAttributeWithError:];
-[MSCMSMessageDigestAttribute messageDigest];
-[MSCMSMessageDigestAttribute setMessageDigest:];
```
