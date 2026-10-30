# `LACSSecureCredential`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCredentialServices.framework__LocalAuthenticationCredentialServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
uuidBytes;
@"LACSSecurePassword" password;
```

## Properties

```
@property (T@"NSUUID",N,R) uuid;
@property (T@"LACSSecurePassword",N,R,Vpassword) password;
```

## Class methods

```
+[LACSSecureCredential supportsSecureCoding];
```

## Instance methods

```
-[LACSSecureCredential uuid];
-[LACSSecureCredential init];
-[LACSSecureCredential encodeWithCoder:];
-[LACSSecureCredential initWithCoder:];
-[LACSSecureCredential password];
-[LACSSecureCredential contextRef];
-[LACSSecureCredential initWithUUID:password:error:];
```
