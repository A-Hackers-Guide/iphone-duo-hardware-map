# `MSCMSSigningTimeAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 1 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _signingTime;
```

## Properties

```
@property (T@"NSDate",R,&,V_signingTime) signingTime;
@property (T@"MSOID",R,&) attributeType;
```

## Instance methods

```
-[MSCMSSigningTimeAttribute attributeType];
-[MSCMSSigningTimeAttribute initWithAttribute:error:];
-[MSCMSSigningTimeAttribute initWithSigningTime:];
-[MSCMSSigningTimeAttribute signingTime];
-[MSCMSSigningTimeAttribute encodeAttributeWithError:];
```
