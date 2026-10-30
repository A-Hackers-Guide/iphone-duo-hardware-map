# `MSMessageImprint`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"MSAlgorithmIdentifier" _algorithmIdentifier;
@"NSData" _hashedMessage;
```

## Properties

```
@property (T@"MSAlgorithmIdentifier",&,V_algorithmIdentifier) algorithmIdentifier;
@property (T@"NSData",&,V_hashedMessage) hashedMessage;
```

## Class methods

```
+[MSMessageImprint supportsSecureCoding];
```

## Instance methods

```
-[MSMessageImprint debugDescription];
-[MSMessageImprint encodeWithCoder:];
-[MSMessageImprint hash];
-[MSMessageImprint description];
-[MSMessageImprint initWithCoder:];
-[MSMessageImprint isEqual:];
-[MSMessageImprint init:hashedMessage:];
-[MSMessageImprint algorithmIdentifier];
-[MSMessageImprint expectedHashLength:];
-[MSMessageImprint hashedMessage];
-[MSMessageImprint initWithMessageImprint:];
-[MSMessageImprint isEqualToMessageImprint:error:];
-[MSMessageImprint isSupportedHashAlgorithm:];
-[MSMessageImprint setAlgorithmIdentifier:];
-[MSMessageImprint setHashedMessage:];
```
