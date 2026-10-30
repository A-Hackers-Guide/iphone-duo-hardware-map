# `LACSUnmanagedContext`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCredentialServices.framework__LocalAuthenticationCredentialServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACSContext`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSData" _externalizedContextRef;
^{__ACMHandle=} _contextRef;
B _ownsContextRef;
```

## Properties

```
@property (T@"NSData",R,N) contextRef;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACSUnmanagedContext dealloc];
-[LACSUnmanagedContext init:];
-[LACSUnmanagedContext contextRef];
-[LACSUnmanagedContext initWithContextRef:error:];
-[LACSUnmanagedContext _decryptData:seed:externalizedContext:error:];
-[LACSUnmanagedContext _encryptData:seed:externalizedContext:error:];
-[LACSUnmanagedContext _encryptionSeedForContext:error:];
-[LACSUnmanagedContext _withContext:error:];
-[LACSUnmanagedContext externalize];
-[LACSUnmanagedContext fetchCredentialData:];
-[LACSUnmanagedContext initWithACMContextRef:ownsContextRef:];
-[LACSUnmanagedContext storeCredentialData:securely:error:];
```
