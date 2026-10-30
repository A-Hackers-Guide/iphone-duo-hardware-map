# `CTLazuliMessageEnvelope`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _secure;
q _type;
@"CTLazuliDestination" _from;
@"CTLazuliMessageID" _messageID;
@ _content;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"CTLazuliDestination",&,N,V_from) from;
@property (T@"CTLazuliMessageID",&,N,V_messageID) messageID;
@property (TB,N,V_secure) secure;
@property (T@,&,N,V_content) content;
```

## Class methods

```
+[CTLazuliMessageEnvelope supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageEnvelope setFrom:];
-[CTLazuliMessageEnvelope from];
-[CTLazuliMessageEnvelope setSecure:];
-[CTLazuliMessageEnvelope setContent:];
-[CTLazuliMessageEnvelope messageID];
-[CTLazuliMessageEnvelope content];
-[CTLazuliMessageEnvelope setType:];
-[CTLazuliMessageEnvelope type];
-[CTLazuliMessageEnvelope encodeWithCoder:];
-[CTLazuliMessageEnvelope setMessageID:];
-[CTLazuliMessageEnvelope description];
-[CTLazuliMessageEnvelope initWithCoder:];
-[CTLazuliMessageEnvelope copyWithZone:];
-[CTLazuliMessageEnvelope isEqual:];
-[CTLazuliMessageEnvelope secure];
-[CTLazuliMessageEnvelope initWithReflection:];
-[CTLazuliMessageEnvelope isEqualToCTLazuliMessageEnvelope:];
```
