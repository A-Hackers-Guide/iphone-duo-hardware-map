# `CTXPCGetAuthenticationTokenResponse`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCResponseMessage`
- 0 instance variables, 1 properties, 3 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) tokens;
```

## Class methods

```
+[CTXPCGetAuthenticationTokenResponse allowedClassesForArguments];
+[CTXPCGetAuthenticationTokenResponse isSensitiveMessage];
```

## Instance methods

```
-[CTXPCGetAuthenticationTokenResponse ct_shortName];
-[CTXPCGetAuthenticationTokenResponse tokens];
-[CTXPCGetAuthenticationTokenResponse initWithTokens:];
```
