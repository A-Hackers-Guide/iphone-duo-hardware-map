# `LACPhoneIntegrationSessionProcessor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationRequestProcessor`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<LACCompanionAuthenticationEnvironmentProviding>" environmentProvider;
@"<LACCompanionAuthenticationSessionMonitoring>" monitor;
```

## Properties

```
@property (T@"<LACCompanionAuthenticationEnvironmentProviding>",N,R,VenvironmentProvider) environmentProvider;
@property (T@"<LACCompanionAuthenticationSessionMonitoring>",N,R,Vmonitor) monitor;
```

## Instance methods

```
-[LACPhoneIntegrationSessionProcessor monitor];
-[LACPhoneIntegrationSessionProcessor processRequest:configuration:completion:];
-[LACPhoneIntegrationSessionProcessor init];
-[LACPhoneIntegrationSessionProcessor canProcessRequest:];
-[LACPhoneIntegrationSessionProcessor environmentProvider];
-[LACPhoneIntegrationSessionProcessor initWithEnvironmentProvider:monitor:];
```
