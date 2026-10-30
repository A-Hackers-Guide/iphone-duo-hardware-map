# `LACAuthenticatorHelper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"<LACADMUserProviding>" userProvider;
```

## Properties

```
@property (T@"<LACADMUserProviding>",N,R,VuserProvider) userProvider;
```

## Class methods

```
+[LACAuthenticatorHelper sharedInstance];
```

## Instance methods

```
-[LACAuthenticatorHelper init];
-[LACAuthenticatorHelper initWithUserProvider:];
-[LACAuthenticatorHelper isAdministratorRequiredForUserID:authenticator:];
-[LACAuthenticatorHelper isOwnerRequiredForUserID:authenticator:];
-[LACAuthenticatorHelper isRequirementMetForUserID:authenticator:];
-[LACAuthenticatorHelper userProvider];
```
