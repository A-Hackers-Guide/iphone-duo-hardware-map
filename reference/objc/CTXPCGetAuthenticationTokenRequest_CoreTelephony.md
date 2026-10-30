# `CTXPCGetAuthenticationTokenRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 0 properties, 10 instance methods, 2 class methods

## Class methods

```
+[CTXPCGetAuthenticationTokenRequest allowedClassesForArguments];
+[CTXPCGetAuthenticationTokenRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCGetAuthenticationTokenRequest requiredEntitlement];
-[CTXPCGetAuthenticationTokenRequest scope];
-[CTXPCGetAuthenticationTokenRequest ct_shortName];
-[CTXPCGetAuthenticationTokenRequest performRequestWithHandler:completionHandler:];
-[CTXPCGetAuthenticationTokenRequest correlationId];
-[CTXPCGetAuthenticationTokenRequest authSupportInfo];
-[CTXPCGetAuthenticationTokenRequest aggregatorTokenHash];
-[CTXPCGetAuthenticationTokenRequest aspIdentifier];
-[CTXPCGetAuthenticationTokenRequest embedded];
-[CTXPCGetAuthenticationTokenRequest initWithScope:aggregatorTokenHash:aspIdentifier:authSupportInfo:embedded:correlationId:];
```
