# `LAAuthenticationBiometricMethodConfiguration`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LAAuthenticationMethodConfiguration`
- 2 instance variables, 2 properties, 3 instance methods, 0 class methods

## Instance variables

```
B _autoRetry;
B _avoidUsingFaceIDCamera;
```

## Properties

```
@property (TB,R,N,V_autoRetry) autoRetry;
@property (TB,R,N,V_avoidUsingFaceIDCamera) avoidUsingFaceIDCamera;
```

## Instance methods

```
-[LAAuthenticationBiometricMethodConfiguration autoRetry];
-[LAAuthenticationBiometricMethodConfiguration avoidUsingFaceIDCamera];
-[LAAuthenticationBiometricMethodConfiguration initWithAutoRetry:avoidUsingFaceIDCamera:allowedUsers:authenticationContext:];
```
