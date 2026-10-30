# `LACSExtractableCredential`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCredentialServices.framework__LocalAuthenticationCredentialServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
uuidBytes;
@"LACSExtractablePassword" password;
```

## Properties

```
@property (T@"NSUUID",N,R) uuid;
@property (T@"LACSExtractablePassword",N,R,Vpassword) password;
```

## Class methods

```
+[LACSExtractableCredential supportsSecureCoding];
```

## Instance methods

```
-[LACSExtractableCredential uuid];
-[LACSExtractableCredential init];
-[LACSExtractableCredential encodeWithCoder:];
-[LACSExtractableCredential initWithCoder:];
-[LACSExtractableCredential password];
-[LACSExtractableCredential contextRef];
-[LACSExtractableCredential initWithUUID:password:error:];
-[LACSExtractableCredential secureCopy];
```
