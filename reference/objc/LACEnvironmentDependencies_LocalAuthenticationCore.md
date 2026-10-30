# `LACEnvironmentDependencies`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"LACBiometryHelper" _biometryHelper;
@"<LACCompanionAuthenticationSessionMonitoring>" _phoneIntegrationSessionMonitor;
@"<LACCompanionAuthenticationSessionMonitoring>" _onenessSessionMonitor;
@"LACPasscodeHelper" _passcodeHelper;
```

## Properties

```
@property (T@"LACBiometryHelper",&,N,V_biometryHelper) biometryHelper;
@property (T@"<LACCompanionAuthenticationSessionMonitoring>",&,N,V_phoneIntegrationSessionMonitor) phoneIntegrationSessionMonitor;
@property (T@"<LACCompanionAuthenticationSessionMonitoring>",&,N,V_onenessSessionMonitor) onenessSessionMonitor;
@property (T@"LACPasscodeHelper",&,N,V_passcodeHelper) passcodeHelper;
```

## Instance methods

```
-[LACEnvironmentDependencies biometryHelper];
-[LACEnvironmentDependencies onenessSessionMonitor];
-[LACEnvironmentDependencies passcodeHelper];
-[LACEnvironmentDependencies phoneIntegrationSessionMonitor];
-[LACEnvironmentDependencies setBiometryHelper:];
-[LACEnvironmentDependencies setOnenessSessionMonitor:];
-[LACEnvironmentDependencies setPasscodeHelper:];
-[LACEnvironmentDependencies setPhoneIntegrationSessionMonitor:];
```
