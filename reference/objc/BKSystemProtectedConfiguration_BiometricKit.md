# `BKSystemProtectedConfiguration`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _biometryEnabled;
@"NSNumber" _unlockEnabled;
@"NSNumber" _identificationEnabled;
@"NSNumber" _loginEnabled;
@"NSNumber" _unlockTokenMaxLifetime;
@"NSNumber" _bioMatchLifespan;
@"NSNumber" _passcodeInputLifespan;
@"NSNumber" _periocularFaceIDMatchEnabled;
```

## Properties

```
@property (T@"NSNumber",&,N,V_biometryEnabled) biometryEnabled;
@property (T@"NSNumber",&,N,V_unlockEnabled) unlockEnabled;
@property (T@"NSNumber",&,N,V_identificationEnabled) identificationEnabled;
@property (T@"NSNumber",&,N,V_loginEnabled) loginEnabled;
@property (T@"NSNumber",&,N,V_unlockTokenMaxLifetime) unlockTokenMaxLifetime;
@property (T@"NSNumber",&,N,V_bioMatchLifespan) bioMatchLifespan;
@property (T@"NSNumber",&,N,V_passcodeInputLifespan) passcodeInputLifespan;
@property (T@"NSNumber",&,N,V_periocularFaceIDMatchEnabled) periocularFaceIDMatchEnabled;
```

## Instance methods

```
-[BKSystemProtectedConfiguration initWithDictionary:];
-[BKSystemProtectedConfiguration dictionary];
-[BKSystemProtectedConfiguration description];
-[BKSystemProtectedConfiguration periocularFaceIDMatchEnabled];
-[BKSystemProtectedConfiguration setUnlockEnabled:];
-[BKSystemProtectedConfiguration unlockEnabled];
-[BKSystemProtectedConfiguration biometryEnabled];
-[BKSystemProtectedConfiguration bioMatchLifespan];
-[BKSystemProtectedConfiguration identificationEnabled];
-[BKSystemProtectedConfiguration loginEnabled];
-[BKSystemProtectedConfiguration passcodeInputLifespan];
-[BKSystemProtectedConfiguration setBioMatchLifespan:];
-[BKSystemProtectedConfiguration setBiometryEnabled:];
-[BKSystemProtectedConfiguration setIdentificationEnabled:];
-[BKSystemProtectedConfiguration setLoginEnabled:];
-[BKSystemProtectedConfiguration setPasscodeInputLifespan:];
-[BKSystemProtectedConfiguration setPeriocularFaceIDMatchEnabled:];
-[BKSystemProtectedConfiguration setUnlockTokenMaxLifetime:];
-[BKSystemProtectedConfiguration unlockTokenMaxLifetime];
```
