# `LAAuthenticationBiometricMethodState`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LAAuthenticationMethodState`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isTouchID;
B _isFaceID;
B _isUserPresent;
Q _lockoutState;
```

## Properties

```
@property (TB,N,V_isTouchID) isTouchID;
@property (TB,N,V_isFaceID) isFaceID;
@property (TQ,N,V_lockoutState) lockoutState;
@property (TB,N,V_isUserPresent) isUserPresent;
```

## Instance methods

```
-[LAAuthenticationBiometricMethodState description];
-[LAAuthenticationBiometricMethodState lockoutState];
-[LAAuthenticationBiometricMethodState isFaceID];
-[LAAuthenticationBiometricMethodState isTouchID];
-[LAAuthenticationBiometricMethodState isUserPresent];
-[LAAuthenticationBiometricMethodState setIsFaceID:];
-[LAAuthenticationBiometricMethodState setIsTouchID:];
-[LAAuthenticationBiometricMethodState setIsUserPresent:];
-[LAAuthenticationBiometricMethodState setLockoutState:];
```
