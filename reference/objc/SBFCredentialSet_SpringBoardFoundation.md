# `SBFCredentialSet`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
^{__ACMHandle=} _acmContext;
B _ownsContext;
@"NSData" _cachedCredentials;
```

## Class methods

```
+[SBFCredentialSet supportsSecureCoding];
```

## Instance methods

```
-[SBFCredentialSet init];
-[SBFCredentialSet dealloc];
-[SBFCredentialSet encodeWithCoder:];
-[SBFCredentialSet initWithCoder:];
-[SBFCredentialSet serializedCredentialSet];
-[SBFCredentialSet initWithSerializedCredentialSet:];
```
