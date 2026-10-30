# `LAEnvironmentState`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"LAEnvironmentMechanismBiometry" _biometry;
@"LAEnvironmentMechanismUserPassword" _userPassword;
@"NSArray" _companions;
@"LACEnvironmentState" _coreState;
```

## Properties

```
@property (T@"LACEnvironmentState",R,N,V_coreState) coreState;
@property (T@"LAEnvironmentMechanismBiometry",R,N,V_biometry) biometry;
@property (T@"LAEnvironmentMechanismUserPassword",R,N,V_userPassword) userPassword;
@property (T@"NSArray",R,N,V_companions) companions;
@property (T@"NSArray",R,N) allMechanisms;
```

## Instance methods

```
-[LAEnvironmentState biometry];
-[LAEnvironmentState companions];
-[LAEnvironmentState userPassword];
-[LAEnvironmentState description];
-[LAEnvironmentState copyWithZone:];
-[LAEnvironmentState isEqual:];
-[LAEnvironmentState allMechanisms];
-[LAEnvironmentState coreState];
-[LAEnvironmentState initWithCoreState:];
```
