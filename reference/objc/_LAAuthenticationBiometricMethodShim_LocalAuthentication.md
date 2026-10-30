# `_LAAuthenticationBiometricMethodShim`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAAuthenticationBiometricMethodObserver`
- 3 instance variables, 7 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"LAAuthenticationBiometricMethod" _biometricMethod;
@"LAAuthenticationBiometricMethodState" _biometricMethodState;
@"LAAuthenticationMethodResult" _biometricMethodResult;
```

## Properties

```
@property (T@"LAAuthenticationBiometricMethod",R,N,V_biometricMethod) biometricMethod;
@property (T@"LAAuthenticationBiometricMethodState",R,V_biometricMethodState) biometricMethodState;
@property (T@"LAAuthenticationMethodResult",R,V_biometricMethodResult) biometricMethodResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_LAAuthenticationBiometricMethodShim sharedInstance];
```

## Instance methods

```
-[_LAAuthenticationBiometricMethodShim init];
-[_LAAuthenticationBiometricMethodShim biometricMethod];
-[_LAAuthenticationBiometricMethodShim authenticationMethod:didAuthenticateWithResult:];
-[_LAAuthenticationBiometricMethodShim authenticationMethod:didChangeState:];
-[_LAAuthenticationBiometricMethodShim authenticationMethod:didStartWithState:];
-[_LAAuthenticationBiometricMethodShim biometricMethodResult];
-[_LAAuthenticationBiometricMethodShim biometricMethodState];
```
