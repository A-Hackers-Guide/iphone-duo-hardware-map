# `LACCompanionAuthenticationProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `LACDomainStateProviding`
- 0 instance variables, 2 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"<LACCompanionAuthenticationProviderDelegate>",W,N) delegate;
@property (TB,R,N) isAvailable;
```

## Instance methods

```
-[LACCompanionAuthenticationProviding isAvailable];
-[LACCompanionAuthenticationProviding setDelegate:];
-[LACCompanionAuthenticationProviding delegate];
-[LACCompanionAuthenticationProviding authenticateWithRequest:];
-[LACCompanionAuthenticationProviding cancelAuthenticationWithID:];
```
