# `CWFEAPCredentials`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
^v _TLSIdentityHandle;
@"NSString" _username;
@"NSString" _password;
```

## Properties

```
@property (T@"NSString",C,N,V_username) username;
@property (T@"NSString",C,N,V_password) password;
@property (T^{__SecIdentity=},C,D,N) TLSIdentity;
@property (T^v,C,D,N) TLSIdentityHandle;
```

## Class methods

```
+[CWFEAPCredentials supportsSecureCoding];
```

## Instance methods

```
-[CWFEAPCredentials dealloc];
-[CWFEAPCredentials username];
-[CWFEAPCredentials encodeWithCoder:];
-[CWFEAPCredentials hash];
-[CWFEAPCredentials description];
-[CWFEAPCredentials initWithCoder:];
-[CWFEAPCredentials setUsername:];
-[CWFEAPCredentials setPassword:];
-[CWFEAPCredentials copyWithZone:];
-[CWFEAPCredentials isEqual:];
-[CWFEAPCredentials password];
-[CWFEAPCredentials setTLSIdentity:];
-[CWFEAPCredentials TLSIdentity];
-[CWFEAPCredentials TLSIdentityHandle];
-[CWFEAPCredentials isEqualToEAPCredentials:];
-[CWFEAPCredentials setTLSIdentityHandle:];
```
