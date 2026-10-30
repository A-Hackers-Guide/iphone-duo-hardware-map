# `LAAuthenticationMethodResult`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"LAAuthenticationMethod" _authenticationMethod;
@"NSString" _authenticatedUser;
```

## Properties

```
@property (T@"LAAuthenticationMethod",R,N,V_authenticationMethod) authenticationMethod;
@property (T@"NSString",R,N,V_authenticatedUser) authenticatedUser;
```

## Instance methods

```
-[LAAuthenticationMethodResult authenticationMethod];
-[LAAuthenticationMethodResult authenticatedUser];
-[LAAuthenticationMethodResult initWithAuthenticatedUser:authenticationMethod:];
-[LAAuthenticationMethodResult unlockKeyBagWithError:];
```
