# `LACCompanionAuthenticationSessionMonitoring` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 8 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) companion;
@property (TB,R,N) isMonitoring;
@property (TB,R,N) isSessionActive;
```

## Instance methods

```
-[LACCompanionAuthenticationSessionMonitoring startMonitoring];
-[LACCompanionAuthenticationSessionMonitoring isMonitoring];
-[LACCompanionAuthenticationSessionMonitoring companion];
-[LACCompanionAuthenticationSessionMonitoring isSessionActive];
-[LACCompanionAuthenticationSessionMonitoring removeObserver:];
-[LACCompanionAuthenticationSessionMonitoring stopMonitoring];
-[LACCompanionAuthenticationSessionMonitoring addObserver:];
-[LACCompanionAuthenticationSessionMonitoring refreshWithCompletion:];
```
