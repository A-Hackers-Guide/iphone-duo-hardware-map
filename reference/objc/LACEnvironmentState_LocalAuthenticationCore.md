# `LACEnvironmentState`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"LACEnvironmentMechanismBiometry" _biometry;
@"LACEnvironmentMechanismUserPassword" _userPassword;
@"NSArray" _companions;
```

## Properties

```
@property (T@"LACEnvironmentMechanismBiometry",&,N,V_biometry) biometry;
@property (T@"LACEnvironmentMechanismUserPassword",&,N,V_userPassword) userPassword;
@property (T@"NSArray",&,N,V_companions) companions;
```

## Class methods

```
+[LACEnvironmentState supportsSecureCoding];
+[LACEnvironmentState companionsForUser:];
+[LACEnvironmentState environmentStateForUser:auditToken:dependencies:error:];
```

## Instance methods

```
-[LACEnvironmentState biometry];
-[LACEnvironmentState setBiometry:];
-[LACEnvironmentState companions];
-[LACEnvironmentState initWithBiometry:userPassword:companions:];
-[LACEnvironmentState setCompanions:];
-[LACEnvironmentState userPassword];
-[LACEnvironmentState encodeWithCoder:];
-[LACEnvironmentState description];
-[LACEnvironmentState initWithCoder:];
-[LACEnvironmentState setUserPassword:];
-[LACEnvironmentState isEqual:];
```
